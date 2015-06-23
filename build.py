#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from sys import argv
from os import listdir as ls
from os.path import join, isfile
from subprocess import call
from time import time
begin = time()

# Select developer name

developer_name = len(argv) > 1 and argv[1] or 'nevercast'

# Iterate one depth of folders looking for Dockerfiles

for file in ls('.'):
    if file[0] == '.' or isfile(file):
        continue
    if isfile(join(file, 'Dockerfile')):
        image_name = '{}/{}:latest'.format(developer_name, file)
        print('Building', image_name)
        call(['docker', 'build', '-t', image_name, file])

# Print operation completion message

print('Completed build in', time() - begin, 'seconds')
