# IoDNS DNS Encoding

IoDNS documents are canonical JSON objects transported over TXT records.

## Canonicalization

Payloads SHOULD be normalized using JSON Canonicalization Scheme (JCS)
before hashing and optional signing.

## Compression

Payloads SHOULD be compressed using zstd.

## Encoding

Compressed payloads MUST be encoded using base64url.

## Chunking

Each TXT chunk carries:

```text
seq=<n>/<total>; csum=<crc32c>; part=<base64url>
```

Example:

```dns
_iod.doc.services.example.com. 300 IN TXT "seq=1/2;csum=1122aabb;part=KLUv..."
_iod.doc.services.example.com. 300 IN TXT "seq=2/2;csum=3344ccdd;part=EFGH..."
```

## Integrity

Clients validate:

- DNSSEC on `_iod`, `_iod.index`, and `_iod.doc.*`
- SHA-256 of canonical decoded payload against the index hash
- optional JWS/COSE signatures, if present
