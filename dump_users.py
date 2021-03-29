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


# Configuration and information about objects to create.
# TODO: You should also be able to read in from a file (REMOVE ME)
admin_api = duo_client.Admin(
    host="
    ikey="",
    skey="",  # TODO (REMOVE ME)
)

# Retrieve user info from API:
users = admin_api.get_users()
for user in users:
    pprint.pprint(user)
    # print(user["username"])
    # print(user["realname"]),
    # print(user["email"]),
    # for group in user["groups"]:
    #     print(group["name"]),
    # for p in user["phones"]:
    #     print(p["name"]),
    #     print(p["number"]),
    #     print(p["platform"]),
    #     print(p["model"]),
    #     print(p["type"]),
    # print(user["notes"]),
    # pprint.pprint(user["webauthncredentials"]),
    # print(user["tokens"]),
    print("\n")
