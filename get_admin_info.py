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

admin_name_list = []
admin_info_list = []
logs = admin_api.get_administrator_log()

for log in logs:  # just get a list of admin
        if log["action"] == "admin_login":
            if log["username"] not in admin_name_list:
                admin_name_list.append(log["username"])

users = admin_api.get_users()
for user in users:
    if user["realname"] in admin_name_list:
        admin_info_list.append(user)

for admin in admin_info_list:
    print(admin["username"])
    print(admin["realname"]),
    print(admin["email"]),
    print("Groups:")
    for group in admin["groups"]:
        print("    ",group["name"]),
    print("Phones:")
    for p in admin["phones"]:
        print("    ",p["name"]),
        print("    ",p["number"]),
        print("    ",p["platform"]),
        print("    ",p["model"]),
        print("    ",p["type"]),
    print(admin["notes"]),

