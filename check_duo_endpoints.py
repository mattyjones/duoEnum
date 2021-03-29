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

duo_endpoints = [""]

for endpoint in duo_endpoints:
    auth_api = duo_client.Auth(
        host=endpoint,
        ikey="",
        skey="",
    )

    ping_results = auth_api.ping()

    pprint.pprint(ping_results)

