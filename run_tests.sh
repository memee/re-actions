#!/usr/bin/env bash
python setup.py behave_test
if [ -f reactions.sqlite ]; then
    rm reactions.sqlite
fi
