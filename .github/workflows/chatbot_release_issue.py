# -*- coding: utf-8 -*-

import sys
import re
import json
import os
import urllib.request

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')

def create_request(url, data=None):
    req = urllib.request.Request(url, data)
    req.add_header('Authorization', f'token {GITHUB_TOKEN}')
    return req

def post_comment(issue_number, body):
    print(f'post_comment body = {body}')
    url = f"https://api.github.com/repos/shin5884/shin5884-sandbox/issues/{issue_number}/comments"
    data = {
        "body": body
    }
    req = create_request(url, json.dumps(data).encode())
    urllib.request.urlopen(req)

def get_next_versions(version):
    splited = re.findall(r"([0-9]+)\.([0-9]+)\.([0-9]+)", version)
    current_major_version = int(splited[0][0])
    current_minor_version = int(splited[0][1])
    current_revision_version = int(splited[0][2])

    next_version = str(current_major_version) + "." + str(current_minor_version) + "." + str(current_revision_version + 1)
    next_versionCode = str(current_major_version * 100000 + current_minor_version * 1000 + (current_revision_version + 1) * 10)

    next_next_version = str(current_major_version) + "." + str(current_minor_version) + "." + str(current_revision_version + 2)
    next_next_versionCode = str(current_major_version * 100000 + current_minor_version * 1000 + (current_revision_version + 2) * 10)

    return next_version, next_versionCode, next_next_version, next_next_versionCode

def post_planned_release_comment(issue_number, version):
    next_version, next_versionCode, next_next_version, next_next_versionCode = get_next_versions(version)

    with open('.github/ISSUE_TEMPLATE/planned_release.md') as f2:
        template = f2.read()
        body = template.format(next_next_version, next_version, next_next_versionCode, next_versionCode)
        post_comment(issue_number, body)

def post_hotfix_release_comment(issue_number, version):
    next_version, next_versionCode, next_next_version, next_next_versionCode = get_next_versions(version)

    with open('.github/ISSUE_TEMPLATE/hotfix_release.md') as f2:
        template = f2.read()
        body = template.format(next_next_version, next_version, next_next_versionCode, next_versionCode)
        post_comment(issue_number, body)

print('Start')

# Argument check
arguments = sys.argv
if len(arguments) < 3:
    sys.exit('arguments is not found')

issue_number = arguments[1]
command, release_type, version = arguments[2].split(' ')
print(f'command = {command}, release_type = {release_type}, version = {version}')

if command != '/show-release-flow':
    sys.exit('invalid command. please set /action comment release flow.')

if release_type not in ['planned', 'hotfix']:
    sys.exit('invalid release type. please set planned or hotfix.')

if len(re.findall(r"([0-9]+)\.([0-9]+)\.([0-9]+)", version)) != 1:
    sys.exit('invalid version. please set like v1.2.3')

# Post comment
if release_type == 'planned':
    post_planned_release_comment(issue_number, version)
elif release_type == 'hotfix':
    post_hotfix_release_comment(issue_number, version)

print('Finish')