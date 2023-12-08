# -*- coding: utf-8 -*-

import subprocess
import sys

print('Start')

# Argument check
arguments = sys.argv
if len(arguments) != 2:
    sys.exit('Please set branch_prefix')
branch_prefix = arguments[1]

# Check [branch_prefix]/develop branch exists on remote
code = subprocess.call(f'git fetch origin {branch_prefix}/develop', shell=True)
if code != 0:
    sys.exit(f'{branch_prefix}/develop is not found')

# Checkout [branch_prefix]/qa branch
subprocess.call(f'git checkout -b {branch_prefix}/qa', shell=True)

# Merge [branch_prefix]/develop branch
code = subprocess.call(f'git merge origin/{branch_prefix}/develop', shell=True)
if code != 0:
    sys.exit(f'merge origin/{branch_prefix}/develop is failed')

# Push [branch_prefix]/qa branch
subprocess.call(f'git push -u origin {branch_prefix}/qa', shell=True)

print('Finish')
