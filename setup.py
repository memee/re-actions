import os

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import setuptools_behave


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()


class PyTestCommand(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        import sys

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


requires = [
    'pyramid',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'cornice',
]

setup_requires = [
    'behave',
    'Sphinx',
    'PasteScript',
    'WebTest',
    'PyHamcrest',
]

tests_require = [
    'pytest'
]

setup(name='reactions',
      version=0.1,
      description='reactions',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      keywords="web services",
      author='Maciej Maciaszek',
      author_email='maciej.maciaszek@gmail.com',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='reactions',
      install_requires=requires,
      setup_requires=setup_requires,
      tests_require=tests_require,
      extras_require={
          'postgresql': 'psycopg2'
      },
      cmdclass={
          'test': PyTestCommand,
          'behave_test': setuptools_behave.behave_test
      },
      entry_points="""\
      [paste.app_factory]
      main = reactions:main
      [console_scripts]
      initialize_reactions_db = reactions.scripts.initializedb:main
      """,
      paster_plugins=['pyramid'])
