#!/usr/bin/env bash
initialize_reactions_db development.ini
python setup.py behave_test
rm reactions.sqlite
