#!/usr/bin/env python3

import argparse
from concurrent.futures import ProcessPoolExecutor
from functools import partial
import json
import os
from os import path
from pprint import pprint
import sys

# this must be done before the first import of weasyprint
import logging

logger = logging.getLogger("weasyprint")
logger.handlers = []
logger.setLevel("DEBUG")
logger.addHandler(logging.FileHandler("./weasyprint.log"))


from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

# from weasyprint.fonts import FontConfiguration


def bail(msg: str):
    print(msg, file=sys.stderr)
    exit(1)


def jsonLoad(infile: str):
    with open(infile, encoding="utf-8") as fp:
        return json.load(fp)


parser = argparse.ArgumentParser(
    description="Generate PDF tickets from schools list with codes",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "input", metavar="INPUT", help="Input file, schools list with codes"
)
parser.add_argument(
    "-v",
    "--verbose",
    help="verbose verbose verbose verbose!!!",
    action="count",
    default=0,
)
parser.add_argument(
    "-o",
    "--out",
    metavar="FOLDER",
    required=True,
    help="output folder, one PDF will be generate for each school here",
)


def codeToPdf(code, outpath, verbose):
    html = template.render(context=code)
    image_cache = {}
    doc = HTML(string=html, base_url=SCRIPT_DIR)
    print("4> ", path.join(outpath, f"{code['school']}.pdf"))
    doc.write_pdf(path.join(outpath, f"{code['school']}.pdf"), image_cache=image_cache)
    print("5> ", path.join(outpath, f"{code['school']}.pdf"))

    # debugging
    if verbose > 3:
        with open(path.join(outpath, f"{code['school']}.html"), "w") as f:
            f.write(html)


args = parser.parse_args()
if args.verbose:
    print(args)
if not path.isfile(args.input):
    bail(f"[{args.input}] is not a file")

SCRIPT_DIR = path.realpath(path.dirname(__file__))
env = Environment(loader=FileSystemLoader(SCRIPT_DIR))
template = env.get_template("pdf_template.html")

os.makedirs(args.out, exist_ok=True)
codes = jsonLoad(args.input)
# if args.verbose > 1:
#     pprint(codes)

# for code in codes:
#    partial(codeToPdf, outpath=args.out, verbose=args.verbose)(code)

# this operation is RAM bound
with ProcessPoolExecutor(max_workers=8) as executor:
    try:
        executor.map(
            partial(codeToPdf, outpath=args.out, verbose=args.verbose),
            codes,
            chunksize=10,
        )
    except KeyboardInterrupt:
        executor.shutdown()
