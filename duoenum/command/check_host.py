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
@click.command(name="check_host", short_help="Check if an account host is valid")
@click.option(
    "--host",
    type=str,
    required=True,
    help="DUO account host to verify. Multiple hosts are seperated by a space \"host1 host2 host3\"",
)
@click.option(
    '--verbose', '-v',
    type=click.Choice(['critical', 'error', 'warning', 'info', 'debug'],
                      case_sensitive=False))
def init_check_host(host, verbose):
    """
        Perform any initialization functions necessary
    """
    # TODO implement verbose
    # TODO implement structured logging

    if host == "":  # TODO do something better here
        print("Please enter a host(s)")
        sys.exit(1)

    # TODO clean user input to prevent injection

    # remove quotes and split the string on spaces
    hosts = host.strip('\"').split()

    # Entry point for the tool functionality
    check_host(hosts)


def check_host(hosts):
    """ Take a list of one or more https hosts and confirm they are valid. Care should be taken to not be
    overly noisy as DUO will surely notice quickly if a single IP is making lots of calls.
    """
    for host in hosts:
        auth_api = duo_client.Auth(
            host=host,
            ikey="",
            skey=""
        )

        # TODO CHECK THE RESULTS TO ENSURE THEY ARE VALID
        # TODO check the timestamp to ensure it is within a given range
        ping_results = auth_api.ping()

        pprint.pprint(ping_results)
