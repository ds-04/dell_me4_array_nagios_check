#!/usr/bin/env python

#D Simpson 2021, ds-04

from check_me4_disks import *
from check_me4_fans import *
from check_me4_psu import *
from check_me4_system import *
import unittest
import ast

#RUN AS python -m unittest test

#test disks
#current test data 5 disks, one fault of each type status 1,2,3
class test_check_me4_disks(unittest.TestCase):
   def setUp(self):
       self.testfile = open('tests/disk_test_data')
       self.testdata=ast.literal_eval(self.testfile.read())

   def tearDown(self):
       self.testfile.close()

   def test_disks(self):
       check_disks_output=check_me4_disks(self.testdata)
       print(check_disks_output)

#test fans
class test_check_me4_fans(unittest.TestCase):
   def setUp(self):
       self.testfile = open('tests/fans_test_data')
       self.testdata=ast.literal_eval(self.testfile.read())

   def tearDown(self):
       self.testfile.close()

   def test_fans(self):
       check_fans_output=check_me4_fans(self.testdata)
       print(check_fans_output)

#test system
class test_check_me4_system(unittest.TestCase):
   def setUp(self):
       self.testfile = open('tests/system_test_data')
       self.testdata=ast.literal_eval(self.testfile.read())

   def tearDown(self):
       self.testfile.close()

   def test_system(self):
       check_system_output=check_me4_system(self.testdata)
       print(check_system_output)

#test psus
class test_check_me4_psu(unittest.TestCase):
   def setUp(self):
       self.testfile = open('tests/psu_test_data')
       self.testdata=ast.literal_eval(self.testfile.read())

   def tearDown(self):
       self.testfile.close()

   def test_psu(self):
       check_psu_output=check_me4_psu(self.testdata)
       print(check_psu_output)


#test controllers
#TODO
