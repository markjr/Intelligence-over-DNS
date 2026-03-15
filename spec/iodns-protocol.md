# IoDNS Protocol Overview

IoDNS defines a convention for publishing structured metadata inside
DNS using TXT records protected by DNSSEC.

## Discovery

An IoDNS-enabled name publishes:

```dns
_iod.<owner>  TXT "v=1; idx=_iod.index; alg=jcs+jws; enc=zstd+b64url; dnssec=required"
```

## Index

The metadata index is published at:

```dns
_iod.index.<owner>
```

Each TXT entry identifies one logical document:

```dns
_iod.index.example.com. 300 IN TXT "id=payments;type=payments;hash=abc123...;ts=2026-03-15T18:30:00Z;ttl=3600"
```

## Documents

Each logical document is published under:

```dns
_iod.doc.<id>.<owner>
```

TXT strings are chunked using:

```text
seq=<n>/<total>; csum=<crc32c>; part=<base64url>
```

## Processing model

A client:

1. Resolves `_iod.<owner>`
2. Validates DNSSEC
3. Resolves `_iod.index.<owner>`
4. Selects one or more documents
5. Resolves `_iod.doc.<id>.<owner>`
6. Reassembles, decodes, decompresses, and verifies payloads
7. Consumes canonical JSON

## Design goals

- use only existing DNS infrastructure
- require DNSSEC for authenticity
- support independent subdomain deployment
- support object-level signatures
- support discovery for agents, APIs, and payments
