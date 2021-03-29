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


key_dicts = [{
    "host": "",
    "i_key": "",
    "s_key": "",
},
    {
        "host": "",
        "i_key": "",
        "s_key": "",
    }
]

for key in key_dicts:
    user = None
    username = "darkstar"

    auth_api = duo_client.Auth(
        host=str(key["host"]),
        ikey=str(key["i_key"]),
        skey=str(key["s_key"]),
    )

    try:
        user = auth_api.enroll(username)

    except RuntimeError as e:
        if "Wrong integration type" in str(e):
            print(key["i_key"], "Wrong integration type")

    if user is not None:
        pprint.pprint(user)

