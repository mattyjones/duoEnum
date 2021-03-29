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


intergration_list = [{
    "integration_key": "",
    "secret_key": "",
    "host": ""
}]

for intergration in intergration_list:
    out = None
    admin_api = duo_client.Admin(
        host=str(intergration["host"]),
        ikey=str(intergration["i_key"]),
        skey=str(intergration["s_key"]),
    )

    try:
        out = admin_api.get_integration(intergration["i_key"])

    except RuntimeError as e:
        if "Wrong integration type" in str(e):
            print(intergration["i_key"], "does not have admin privileges")
    if out is not None:
        pprint.pprint(out)
        print("\n")
