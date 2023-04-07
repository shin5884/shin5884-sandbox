# -*- coding: utf-8 -*-

import os
import sys
import re

print('Start')

# Argument check
arguments = sys.argv
if len(arguments) != 2:
    sys.exit('arguments is not found')

command, release_type, version = arguments[1].split(' ')
print(f'command = {command}, release_type = {release_type}, version = {version}')

if command != '/chatbot':
    sys.exit('invalid command. please set /chatbot.')

if release_type not in ['planned', 'hotfix']:
    sys.exit('invalid release type. please set planned or hotfix.')

if len(re.findall(r"([0-9]+)\.([0-9]+)\.([0-9]+)", version)) != 1:
    sys.exit('invalid version. please set like v1.2.3')

# Post comment
with open(".github/ISSUE_TEMPLATE/planned_release.md") as f2:
    issue_template = f2.read()
    print(issue_template)

print('Finish')