# -*- coding: utf-8 -*-

import sys
import subprocess
import re

def post_comment(issue_number, content_path, version):
    with open(content_path) as f2:
        issue_template = f2.read()
        subprocess.call(f'gh issue comment {issue_number} --body {issue_template}', shell=True)

print('Start')

# Argument check
arguments = sys.argv
if len(arguments) < 3:
    sys.exit('arguments is not found')

issue_number = arguments[1]
command, release_type, version = arguments[2].split(' ')
print(f'command = {command}, release_type = {release_type}, version = {version}')

if command != '/chatbot':
    sys.exit('invalid command. please set /chatbot.')

if release_type not in ['planned', 'hotfix']:
    sys.exit('invalid release type. please set planned or hotfix.')

if len(re.findall(r"([0-9]+)\.([0-9]+)\.([0-9]+)", version)) != 1:
    sys.exit('invalid version. please set like v1.2.3')

# Post comment
if release_type == 'planned':
    post_comment(issue_number, '.github/ISSUE_TEMPLATE/planned_release.md', version)
elif release_type == 'hotfix':
    post_comment(issue_number, '.github/ISSUE_TEMPLATE/hotfix_release.md', version)

print('Finish')