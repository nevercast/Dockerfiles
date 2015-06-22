#!/usr/bin/python
from sys import argv as args
from os import listdir as ls
from os.path import join, isfile
from subprocess import call
# Select developer name
devName = (len(args) > 1 and args[1]) or 'nevercast'
# Iterate one depth of folders looking for Dockerfiles
for file in ls('.'):
	if file[0] == '.' or isfile(file):
		continue
	if isfile(join(file, 'Dockerfile')):
		imageName = '{}/{}:latest'.format(devName, file)
		print 'Building ' + imageName
		call(['docker','build','-t',imageName, file])
