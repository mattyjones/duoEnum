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

user_bypass_code = None
user_bypass_code = admin_api.get_user_bypass_codes("")

if user_bypass_code is not None:
    for code in user_bypass_code:
        pprint.pprint(code)

print("\n")

all_bypass_codes = admin_api.get_bypass_codes()
for b in all_bypass_codes:
    pprint.pprint(b)
