#!/usr/bin/env python3
"""
Minimal helper to encode an IoDNS JSON document into chunked TXT strings.

This example keeps dependencies to the standard library. It uses base64url
encoding directly and skips zstd/JWS so it remains easy to run anywhere.
"""
import argparse
import base64
import json
import math
import zlib
from pathlib import Path


def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def chunk_string(s: str, size: int):
    for i in range(0, len(s), size):
        yield s[i:i + size]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file", type=Path)
    parser.add_argument("--owner", default="_iod.doc.example")
    parser.add_argument("--chunk-size", type=int, default=180)
    args = parser.parse_args()

    payload = json.loads(args.json_file.read_text())
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    encoded = b64url(canonical)
    parts = list(chunk_string(encoded, args.chunk_size))

    total = len(parts)
    for idx, part in enumerate(parts, start=1):
        crc = format(zlib.crc32(part.encode()) & 0xffffffff, "08x")
        print(f'{args.owner} TXT "seq={idx}/{total};csum={crc};part={part}"')


if __name__ == "__main__":
    main()
