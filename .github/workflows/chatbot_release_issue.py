# -*- coding: utf-8 -*-

import sys

print('Start')

# Argument check
arguments = sys.argv
if len(arguments) != 2:
    sys.exit('arguments is not found')
comment = arguments[1]

print(f'comment = {comment}')

print('Finish')