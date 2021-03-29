#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function

import pprint
import sys

from six.moves import input

import duo_client

argv_iter = iter(sys.argv[1:])


def get_next_arg(prompt):
    try:
        return next(argv_iter)
    except StopIteration:
        return input(prompt)


# Configuration and information about objects to create.
# TODO: You should also be able to read in from a file (REMOVE ME)
admin_api = duo_client.Admin(
    host="",
    ikey="",
    skey="",
)

logs = admin_api.get_authentication_log()

print_complete_logs = True
print_user_list = False

dirty_user_list = []
clean_log_list = []
clean_user_list = []

for log in logs:
    if "on trusted network" or "bypass" in log["reason"]:
        clean_entry = {
            "username": log["username"],
            "email": log["email"],
            "location": log["location"],
            "ip": log["ip"],
            "reason": log["reason"],
            "integration": log["integration"],
        }
        dirty_user_list.append(clean_entry)

for item in dirty_user_list:
    if item not in clean_log_list:
        clean_log_list.append(item)

for log in clean_log_list:
    if log["username"] not in clean_user_list:
        clean_user_list.append(log["username"])

if print_complete_logs:
    for item in clean_log_list:
        pprint.pprint(item)

if print_user_list:
    for item in clean_user_list:
        print(item)
