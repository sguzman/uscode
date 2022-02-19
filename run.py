#!/usr/bin/env python

import sys
import os
import tasks
import tasks.utils
import traceback
import pprint as pp

# name of the task comes first
task_name = sys.argv[1]

# parse any command line flags off
options = {}
args = sys.argv[2:]
for arg in args:
    if arg.startswith("--"):

        if "=" in arg:
            key, value = arg.split('=')
        else:
            key, value = arg, True

        key = key.split("--")[1]
        if value == 'True':
            value = True
        elif value == 'False':
            value = False

    options[key.lower()] = value

# store original raw args array after task name
options['argv'] = args


# depends on tasks/[task_name].py being present relative to this directory
sys.path.append("tasks")

try:
    __import__(task_name).run(options)
except Exception as exception:
    print(tasks.utils.format_exception(exception))
