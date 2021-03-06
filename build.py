#! /usr/bin/env python
"""
Usage:
    build.py pelican
    build.py --version
    build.py -h | --help

Options:
   -h, --help   Show this help text
   --version    Show Version
"""
from __future__ import print_function
import os

from docopt import docopt


def safe_call(args_list):
    from subprocess import call
    # Avoid output deadlock!
    # http://stackoverflow.com/questions/2561902/python-execute-process-block-till-it-exits-supress-output
    null_device = open(os.devnull, 'w')
    return call(args_list, bufsize=4096, stdout=null_device, stderr=null_device)


if __name__ == '__main__':
    args = docopt(__doc__, version='0.0.1')

    if args['pelican']:
        import build_pelican

        exit(build_pelican.run())
    else:
        exit(print(docopt(__doc__, argv='--help')))

