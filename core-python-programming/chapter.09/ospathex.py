#!/usr/bin/env python
# --coding: utf-8 --
import os
__author__ = 'lovexiaov'

for tmpdir in ('/tmp', r'c:\tmp'):
    if os.path.isdir(tmpdir):
        break
else:
    print 'no temp directory available'
    tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print cwd

    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print cwd
