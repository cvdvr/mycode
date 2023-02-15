#!/usr/bin/env python3
import shutil
import os

#default path
os.chdir('/home/student/mycode/')

#moving files
shutil.move('raynor.obj', 'ceph_storage/')

xname = input('What is the new name for kerrigan.obj? ')

#rename
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

