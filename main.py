import os
import argparse
from AutoDoc import AutoDoc

parser = argparse.ArgumentParser(
    description="AutoDoc is a console application for generating code documentation using ChatGPT. Currently supports 2 languages Python and TypeScript (including JavaScript). You can use an example file for any language using --example.")

parser.add_argument(
    '-token',
    type=str,
    help='The path to the file with the token ChatGPT.',
    required=True
)

parser.add_argument(
    "-file",
    type=str,
    help='Path to the code file.',
    required=True
)
parser.add_argument(
    '-example',
    type=str,
    help="Path to a file with an example of comments to it. Optional."
)

args = parser.parse_args()

if not os.path.exists(args.token):
    print("Token file does not exist")
    exit(1)
if not os.path.exists(args.file):
    print("Code file does not exist")
    exit(1)
if args.example and not os.path.exists(args.example):
    print("Example file does not exist")
    exit(1)
autodoc = AutoDoc(os.path.normpath(args.token))
autodoc.add_file(os.path.normpath(args.file))
if args.example:
    autodoc.add_example(os.path.normpath(args.example))
autodoc.start()
