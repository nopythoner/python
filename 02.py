#! /usr/bin/env python
# coding:utf-8

from sys import argv

script,first,second,third = argv #需在终端进行python ex13.py first 2nd 3rd
script = raw_input("How old are you?")
first = raw_input("What's you name?")
second = raw_input("Where are you from?")
A = script
print "Your are %s script:". %script
print "Your name is:",first
print "Your youa are from :",second
print "Your third variable is :",third 

