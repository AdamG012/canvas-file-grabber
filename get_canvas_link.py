#!/usr/bin/env python3

import sys
import argparse
import requests
from os.path import exists

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description="""
                                 Canvas Link Extractor
                                 ---------------------
Takes a file number and optional course id and prints out the link to acccess the resource.""")

parser.add_argument('access_token', metavar="access_token", type=str,
                    help='The access token generated in canvas settings.')
parser.add_argument('--course_number', metavar="c", type=int,
                    help='The course number of the canvas link.', default=None)
parser.add_argument('-p', '--prefix', type=str,
                    help='The canvas infrastructure to use e.g. canvas.instructure.com.', default="canvas.instructure.com")
parser.add_argument('--files', metavar='files', action='store', type=int, nargs='+',
                    help='The file number(s) of the canvas link(s).')
args = parser.parse_args()

files           = args.files
access_token    = args.access_token
course_num      = str(args.course_number) + "/" if args.course_number is not None else ""
prefix          = args.prefix

if files is None or len(files) == 0:
    print(f"Invalid configuration, no files entered.")
    exit()


print("The link(s) will be generated below:\n")
for f in files:
        request = requests.get("https://{}/api/v1/{}files/{}?access_token={}".format(prefix, course_num, f, access_token))

        if request is None or 'url' not in request.json():
                print(f"Invalid configuration for {f}, check your arguments.")
                print(f"Generated request:\n{request}")
                continue

        data    = request.json()['url']
        print(data)
