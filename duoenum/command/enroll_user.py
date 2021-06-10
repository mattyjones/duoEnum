#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function

import pprint
import sys

import click
import duo_client


# TODO read in from yaml file
# https://click.palletsprojects.com/en/7.x/parameters/
# https://click.palletsprojects.com/en/7.x/options/
@click.command(name="enroll_user", short_help="Enroll a new user")
@click.option(
    "--user",
    type=str,
    required=True,
    help="Enroll a user in a DUO account. Multiple users are seperated by a space \"user11 user2 user3\"",
)
@click.option(
    "--host",
    type=str,
    required=True,
    help="DUO host to use",
)
@click.option(
    "--integration_key", '-i',
    type=str,
    required=True,
    help="At this time a key pair associated with the AuthAPI is required. This is key is also know as the ikey",
)
@click.option(
    "--secret_key", '-s',
    type=str,
    required=True,
    help="At this time a key pair associated with the AuthAPI is required. This is key is also know as the skey",
)
@click.option(
    '--verbose', '-v',
    type=click.Choice(['critical', 'error', 'warning', 'info', 'debug'],
                      case_sensitive=False))
def init_enroll_user(user, host, integration_key, secret_key, verbose):
    """
        Perform any initialization functions necessary
    """
    # TODO implement verbose
    # TODO implement structured logging

    if user == "":  # TODO do something better here
        print("Please enter a user(s)")
        sys.exit(1)

    if host == "":  # TODO do something better here
        print("Please enter a host")
        sys.exit(1)

    if integration_key == "":  # TODO do something better here
        print("Please enter an integration key")
        sys.exit(1)

    if secret_key == "":  # TODO do something better here
        print("Please enter a secret_key")
        sys.exit(1)

    # TODO clean user input to prevent injection

    # remove quotes and split the string on spaces
    users = user.strip('\"').split()

    enrollment_config = {
        "ikey": integration_key,
        "skey": secret_key,
        "host": host,
        "users": users
    }

    # Entry point for the tool functionality
    enroll_user(enrollment_config)


def enroll_user(enrollment_config):
    """ Take a list of one or more users and enroll them in the given account.
    Care should be taken to not be overly noisy as DUO will surely notice quickly
    if a single IP is making lots of calls.
    """

    auth_api = duo_client.Auth(
        host=enrollment_config['host'],
        ikey=enrollment_config['ikey'],
        skey=enrollment_config['skey'],
    )

    for username in enrollment_config['users']:
        user_obj = {}

        try:
            user_obj = auth_api.enroll(username)  # enroll a new user

        except RuntimeError as e:
            if "Wrong integration type" in str(e):
                print(enrollment_config["ikey"], "Wrong integration type")

        # TODO CHECK THE RESULTS TO ENSURE THEY ARE VALID
        pprint.pprint(user_obj + "\n")

# user = None

# user = auth_api.enroll_status("DUTR0TSNEOL7TFXBO205", "duo://ucEVULS62a2TD21vfCIc-YXBpLTY5NjZkY2MzLmR1b3NlY3VyaXR5LmNvbQ")
#user = auth_api.preauth("DUTR0TSNEOL7TFXBO205")

# if user is not None:
#     pprint.pprint(user)
# else:
#     print("this sucks")
