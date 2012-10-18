#!/usr/bin/env python

"""This script loads the tasks from taskwarrior, and the list of tickets from asana. 
For each task in pending,
  if a ticket exists in asana
    pass
  else
    create one

For each task in completed,
  if a ticket exists in asana
    finish it
  else
    create one
    finish it

For tickets that exist in asana, but not task warrior,
 do shit all :-)"""

workspace_name="london"


try:
  import taskw
except:
  print "You need to pip install taskw to use this tool"
  exit(1)

try:
  import sh
except:
  print "You need to pip install sh to use this tool"
  exit(1)

try:
  asana_blobs=sh.asana(workspace_name)
except sh.CommandNotFound:
  print "asana not found: Did you install the asana command line tools from github?"
  exit(1)
except sh.ErrorReturnCode_1:
  print "Asana exited with error code 1. Edit this script to set the partial name of your workspace"
  exit(1)

print asana_blobs

asana_tasks=[task for task in asana_blobs.split("\n")]
print asana_tasks
