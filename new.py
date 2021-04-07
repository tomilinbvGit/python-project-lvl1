#!/usr/bin/env python3

import argparse
import json


def create_parser():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Generate diff"
    )
    parser.add_argument("first_file", nargs="?")
    parser.add_argument("second_file", nargs="?")
    parser.add_argument("-f", "--format", help="set format of output")

    return parser


def gendiff(file_path1, file_path2):
    file_1 = json.load(open(file_path1))
    file_2 = json.load(open(file_path2))
    old_keys = list(file_1.keys())
    new_keys = list(file_2.keys())
    shared_keys = sorted(list(set(old_keys + new_keys)))
    result = "{\n"

    for key in shared_keys:
        if key not in file_2:
            result += "\t- {0}: {1}\n".format(key, str(file_1[key]))
        elif key not in file_1:
            result += "\t+ {0}: {1}\n".format(key, str(file_2[key]))
        elif file_1[key] == file_2[key]:
            result += "\t {0}: {1}\n".format(key, str(file_1[key]))
        else:
            result += "\t- {0}: {1}\n".format(key, str(file_1[key]))
            result += "\t+ {0}: {1}\n".format(key, str(file_2[key]))

    result += "}"
    return result
