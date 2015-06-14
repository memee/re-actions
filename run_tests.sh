#!/usr/bin/env bash
initialize_reactions_db development.ini
python setup.py behave_test
if [ -f reactions.sqlite ]; then
    rm reactions.sqlite
fi
