#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import shlex

command_line = 'ping -c 1 www.sohu.com'
args = shlex.split(command_line)
try:
    subprocess.check_call(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print('sohu web server is up')
except subprocess.CalledProcessError:
    print('Failed to get ping.')
