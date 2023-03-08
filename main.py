import os
import argparse
from modules.autodoc import AutoDoc
from modules.file import File
from modules.settings import *
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

auth = {
    "email": config["ChatGPT"]["email"],
    "password": config["ChatGPT"]["password"],
    "session_token": config["ChatGPT"]["session_token"],
}


parser = argparse.ArgumentParser(
    description="AutoDoc is a console application for generating code documentation using ChatGPT. Currently supports 1 language: Python. You can use an example file for any language using -example."
)


parser.add_argument("-file", type=str, help="Path to the code file.", required=True)

args = parser.parse_args()


if not os.path.exists(args.file):
    exit(f"[{RED}Error{RESET}] Code file does not exist")


file = File(args.file)

autodoc = AutoDoc(
    auth,
    file.content(),
    file.language(),
)

result = autodoc.start()
file.create_commented_file(result)
