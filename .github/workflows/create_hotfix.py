# -*- coding: utf-8 -*-

import subprocess
import sys
import re

print('Start')

# Argument check
arguments = sys.argv
if len(arguments) != 2:
    sys.exit('Please set release version like 1.2.3')
release_ver = arguments[1]
splited = re.findall(r"([0-9]+)\.([0-9]+)\.([0-9]+)", release_ver)
if len(splited) != 1:
    sys.exit('Version is invalid. Please set release version like 1.2.3')
new_major_version = int(splited[0][0])
new_minor_version = int(splited[0][1])
new_revision_version = int(splited[0][2])
print('New major version: ' + str(new_major_version))
print('New minor version: ' + str(new_minor_version))
print('New revision version: ' + str(new_revision_version))

# Create hotfix branch from master, and push it
print('\n------Push hotfix/v' + release_ver + ' branch-------')
subprocess.call('git checkout master', shell=True)
subprocess.call('git pull origin master', shell=True)
subprocess.call('git checkout -b hotfix/v' + release_ver, shell=True)
subprocess.call('git push origin `git rev-parse --abbrev-ref HEAD`', shell=True)
subprocess.call('git branch -u origin/hotfix/v' + release_ver, shell=True)
print('Done')
print('---------------------------')

# Create master merge PR
print('\n------Create PR-------')
pr_title = f'[Hotfix]{release_ver}リリース'
pr_body = f'hotfix/v{release_ver}ブランチを作成し、masterマージPRを作成しました。\n'
command = 'echo "v' + pr_title + '\n\n' + pr_body + '" | hub pull-request --draft -l release --base master -F -'
proc = subprocess.Popen(command,
                        shell=True,
                        stdin = subprocess.PIPE,
                        stdout = subprocess.PIPE,
                        stderr = subprocess.PIPE)
stdout, stderr = proc.communicate()
print(stdout.decode('utf-8'))
print('Done')
print('---------------------------')

print('Finish')
