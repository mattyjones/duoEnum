#! /usr/bin/env python
"""
    Duo Enumeration is a tool for checking if keys are valid
"""
import click
from duoenum import command
from duoenum.bin.version import __version__


@click.group()
@click.version_option(version=__version__)
def duoenum():
    """
    Duo Enumeration is a tool for checking if keys are valid
    """


duoenum.add_command(command.check_host.init_check_host)
# duoenum.add_command(command.write_policy.write_policy)
# duoenum.add_command(command.create_template.create_template)
# duoenum.add_command(command.query.query)


def main():
    """
    Duo Enumeration is a tool for checking if keys are valid
    """
    duoenum()


if __name__ == "__main__":
    main()
