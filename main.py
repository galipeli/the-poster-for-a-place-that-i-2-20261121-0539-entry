#!/usr/bin/env python3
"""Poster entry: copy the pre-rendered poster image to /output/entry.png.

The poster (a travel poster for VELMARA, a fictional lantern city
floating above a sea of clouds) is rendered at build time and shipped
as entry.png (JPEG bytes, 1024x1024, under 1 MiB). This program only
copies those bytes, using the Python standard library, so the sandboxed
run is deterministic and needs no network and no third-party packages.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"
MAX_BYTES = 1048576


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(SRC, "rb") as f:
        data = f.read()
    if len(data) > MAX_BYTES:
        print("error: entry.png is %d bytes, over the 1 MiB cap"
              % len(data), file=sys.stderr)
        return 1
    with open(DST, "wb") as f:
        f.write(data)
    print("wrote %s: %d bytes sha256=%s"
          % (DST, len(data), hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
