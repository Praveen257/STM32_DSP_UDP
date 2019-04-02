#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from subprocess import *

path = 'C:/Program Files/Git/git-bash.exe'
cmd = 'make'
p = run([path,cmd],stdout=PIPE,input='make',encoding='ascii')
print(p.returncode)