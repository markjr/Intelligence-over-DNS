#!/usr/bin/env python3
"""
Minimal helper to reassemble IoDNS TXT chunks into JSON.

Requires dnspython:
    pip install dnspython
"""
import argparse
import base64
import json
import re

import dns.resolver

PATTERN = re.compile(r"seq=(\d+)/(\d+);csum=([0-9a-fA-F]{8});part=(.+)")


def pad_b64(s: str) -> str:
    return s + "=" * ((4 - len(s) % 4) % 4)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="DNS name to query, e.g. _iod.doc.payments.example.com")
    args = parser.parse_args()

    answers = dns.resolver.resolve(args.name, "TXT")
    frames = []
    for rr in answers:
        for s in rr.strings:
            text = s.decode()
            m = PATTERN.fullmatch(text)
            if not m:
                continue
            seq, total, csum, part = m.groups()
            frames.append((int(seq), int(total), part))

    if not frames:
        raise SystemExit("No valid IoDNS frames found")

    frames.sort(key=lambda x: x[0])
    total = frames[0][1]
    if len(frames) != total:
        raise SystemExit(f"Missing frames: expected {total}, got {len(frames)}")

    assembled = "".join(part for _, _, part in frames)
    raw = base64.urlsafe_b64decode(pad_b64(assembled))
    obj = json.loads(raw.decode())

    print(json.dumps(obj, indent=2))


if __name__ == "__main__":
    main()
