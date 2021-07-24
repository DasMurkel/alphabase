#!/usr/bin/env python3

import alphabase
import datetime
import argparse as ap

WINDOWS_1252_ALPHABET = "0123456789!\"#$%&'()*+,-./:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
START = datetime.datetime(year=2019, month=1, day=1)
MAX_CHARACTERS = 3


def to_timedelta(v):
    return datetime.timedelta(minutes=v)


def minutes_since(start, end):
    delta = end - start
    return int(delta / datetime.timedelta(minutes=1))


def time_to_version(time=datetime.datetime.now()):
    ab = alphabase.alphabase(WINDOWS_1252_ALPHABET)
    minutes = minutes_since(START, time) % ab.max_value(MAX_CHARACTERS)
    version = ab.to_alphabet(minutes)
    return version.zfill(MAX_CHARACTERS)


def version_to_time(version):
    ab = alphabase.alphabase(WINDOWS_1252_ALPHABET)
    minutes = ab.to_int(version)
    # If we had a rollover, we want to add the max number of minutes to the
    # result because we want the result to be closer to today than rollover day.
    a, _ = divmod(minutes_since(START, datetime.datetime.now()),
                  ab.max_value(MAX_CHARACTERS))
    return to_timedelta(minutes) + START + to_timedelta(a * ab.max_value(MAX_CHARACTERS))


def parse_args():
    parser = ap.ArgumentParser(
        description="Converter for timestamp to alphabet and back")

    parser.add_argument("-b", "--back", default=False, action="store_true",
                        help="Takes three digit timestamp in alphabet. If provided, converted back to readable timestamp.")

    parser.add_argument(
        "value", nargs="*", help="Either a valid readable timestamp or the value in the alphabet to convert back to timestamp")

    return parser.parse_args()


if __name__ == "__main__":
    options = parse_args()

    if options.back:
        time = version_to_time(options.value[0])
        print(time)
    else:
        time = datetime.datetime.now()
        if options.value:
            time = datetime.datetime.fromisoformat(options.value[0])
        vers = time_to_version(time)
        print(vers)
