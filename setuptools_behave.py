#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2012-2014 Benno Rice, Richard Jones, Jens Engel and others, except where noted.
# All rights reserved.
# Copyright (c) 2015 Maciej Maciaszek
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
Setuptools command for behave.

Memee:
This version is authored on 16 Apr 2015. It will be incorporated into 1.2.6 of
Behave library.

.. code-block:: console

    python setup.py behave_test
    python setup.py behave_test --format=progress3
    python setup.py behave_test --args=features/one.feature
    python setup.py behave_test --tags=-xfail --args=features

.. seealso::

    * http://pypi.python.org/pypi/behave
    * http://github.com/behave/behave
"""

from setuptools import Command
from distutils import dir_util
from fnmatch import fnmatch
import os.path
import sys
import shlex
import subprocess


class behave_test(Command):
    """
    Simple test runner that runs 'behave' via a "setup.py" file.
    This ensures that all requirements are provided before the tests are run.
    """
    command_name = "behave_test"
    description = "Run feature tests with behave"
    default_format = "progress"
    default_args   = "features"
    local_egg_dir  = ".eggs"
    command_consumes_arguments = False
    user_options = [
        ("format=", "f", "Use formatter (default: %s)" % default_format),
        ("tags=",   "t", "Use tags to select/exclude features/scenarios"),
        ("dry-run", "d", "Use dry-run mode"),
        ("args=", None,
         "Features to run (default: %s)" % default_args),
        ]
    boolean_options = [ "dry-run" ]

    def initialize_options(self):
        self.format = self.default_format
        self.tags = None
        self.dry_run = None
        self.args = self._get_paths()

    def finalize_options(self):
        self.ensure_string("format", self.default_format)
        self.ensure_string_list_with_comma_words("tags")
        self.ensure_string_list("args")

    def ensure_string_list_with_comma_words(self, option):
        """Ensures that a string with whitespace separated words
        is converted into list of strings.
        Note that commas are allowed in words
        (compared :meth:`ensure_string_list()`).
        """
        value = getattr(self, option, None)
        if not value:
            return
        parts = shlex.split(value)
        setattr(self, option, parts)

    def _ensure_required_packages_are_installed(self, install_dir="."):
        # -- NOTE: Packages are downloaded and provided as local eggs.
        self.announce("ensure_required_packages_are_installed")
        initial_dir = os.getcwd()
        try:
            dir_util.mkpath(install_dir)
            # -- NO LONGER NEEDED: os.chdir(self.local_egg_dir)
            if self.distribution.install_requires:
                self.distribution.fetch_build_eggs(self.distribution.install_requires)
            if self.distribution.tests_require:
                self.distribution.fetch_build_eggs(self.distribution.tests_require)
        finally:
            os.chdir(initial_dir)

    def _get_paths(self):
        return self.default_args

    def _select_paths(self, path=".", pattern="*"):
        selected = [ os.path.join(path, f)
                     for f in os.listdir(path)  if fnmatch(f, pattern)]
        return selected

    def _setup_env_with_local_python_path(self, egg_install_dir):
        PYTHONPATH = os.environ.get("PYTHONPATH", "")
        pathsep = os.pathsep
        PPATH=[x for x in PYTHONPATH.split(pathsep) if x]
        PPATH.insert(0, os.getcwd())
        local_eggs = self._select_paths(egg_install_dir, "*.egg")
        if local_eggs:
            PPATH[1:1] = [ os.path.abspath(p) for p in local_eggs]
        os.environ["PYTHONPATH"] = pathsep.join(PPATH)
        self.announce("Use PYTHONPATH=%s" % os.environ["PYTHONPATH"], level=3)
        return PYTHONPATH

    def run(self):
        # -- UPDATE SEARCHPATH: Ensure that local dir and local eggs are used.
        egg_install_dir = self.local_egg_dir
        self._ensure_required_packages_are_installed(egg_install_dir)
        OLD_PYTHONPATH = self._setup_env_with_local_python_path(egg_install_dir)

        returncode = self.behave()

        if returncode:
            self.announce("FAILED", level=4)
            raise SystemExit(returncode)

        # -- FINALLY: Restore
        os.environ["PYTHONPATH"] = OLD_PYTHONPATH
        return returncode

    def behave(self, path=None):
        from behave import __main__ as behave_main

        behave = os.path.join("bin", "behave")
        if not os.path.exists(behave):
            # -- ALTERNATIVE: USE: behave script: behave = "behave"
            # -- USE: behave module (main)
            behave = "-m behave"
        cmd_options = ""
        if self.tags:
            cmd_options = "--tags=" + " --tags=".join(self.tags)
        if self.dry_run:
            cmd_options += " --dry-run"
        if path:
            cmd_options += " %s" % path
        self.announce("CMDLINE: %s %s" % (behave, cmd_options), level=3)

        return behave_main.main(args=cmd_options)
