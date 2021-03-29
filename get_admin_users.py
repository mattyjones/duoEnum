#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function
import sys
import pprint

import duo_client
from six.moves import input

argv_iter = iter(sys.argv[1:])


def get_next_arg(prompt):
    try:
        return next(argv_iter)
    except StopIteration:
        return input(prompt)


admin_api = duo_client.Admin(
    host="",
    ikey="",
    skey="",
)

all_info = True
admin_list = []
logs = admin_api.get_administrator_log()

if all_info:  # get all the log data
    pprint.pprint(logs)
else:
    for log in logs:  # just get a list of admin
        if log["action"] == "admin_login":
            if log["username"] not in admin_list:
                admin_list.append(log["username"])

if admin_list:
    print("This list is based on the 'admin_login' event")
    print("DUO Admin:s\n")
    for admin in admin_list:
        print(admin)
