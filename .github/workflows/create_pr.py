# -*- coding: utf-8 -*-

import subprocess
import sys
import re

# Create master merge PR
print('\n------Create PR-------')
release_ver = '9.10.0'
pr_title = f'{release_ver}リリースブランチ'
pr_body = f'レビュー対象はBump version to {release_ver}のコミットからです。\n'
command = f'gh pr create --title "{pr_title}" --body "{pr_body}" --label release --draft'
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
