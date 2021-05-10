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
@click.command(name="check_endpoint", short_help="Check if an account endpoint is valid")
@click.option(
    "--endpoints",
    type=str,
    required=True,
    help="DUO account endpoint to verify. Multiple endpoints are seperated by a space \"endpoint1 endpoint2 endpoint3\"",
)
@click.option(
    '--verbose', '-v',
    type=click.Choice(['critical', 'error', 'warning', 'info', 'debug'],
                      case_sensitive=False))
def init_check_endpoint(endpoints, verbose):
    """
        Perform any initialization functions necessary
    """
    # TODO implement verbose
    # TODO implement logging

    if endpoints == "":  # TODO do something better here
        print("Please enter an endpoint(s)")
        sys.exit(1)

    # TODO clean user input to prevent injection

    # remove quotes and split the string on spaces
    endpoints = endpoints.strip('\"').split()

    # Entry point for the tool functionality
    check_endpoint(endpoints)


def check_endpoint(endpoints):
    """ Take a list of one or more https host endpoints and confirm they are valid. Care should be taken to not be
    overly noisy as DUO will surely notice quickly if a single IP is making lots of calls.
    """
    for endpoint in endpoints:
        auth_api = duo_client.Auth(
            host=endpoint,
            ikey="",
            skey=""
        )

        # TODO CHECK THE RESULTS TO ENSURE THEY ARE VALID
        # TODO check the timestamp to ensure it is within a given range
        ping_results = auth_api.ping()

        pprint.pprint(ping_results)
