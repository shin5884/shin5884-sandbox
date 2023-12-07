# -*- coding: utf-8 -*-

import subprocess
import sys
import re

# Create master merge PR
print('\n------Create PR-------')
pr_title = f'ghでPRを作成するテスト'
pr_body = f'PRを作成しました。\n'
command = f'gh pr create --title ${pr_title} --body R{pr_body}'
proc = subprocess.Popen(command,
                        shell=True,
                        stdin = subprocess.PIPE,
                        stdout = subprocess.PIPE,
                        stderr = subprocess.PIPE)
stdout, stderr = proc.communicate()
print(stdout.decode('utf-8'))
print(stderr.decode('utf-8'))
print('Done')
print('---------------------------')
