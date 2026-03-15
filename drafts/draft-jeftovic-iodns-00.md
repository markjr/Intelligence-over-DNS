# Internet-Draft: IoDNS (Intelligence over DNS)
*(working draft for discussion prior to IETF submission)*

**Title:** IoDNS (Intelligence over DNS)  
**Author:** Mark E. Jeftovic  
**Intended status:** Experimental  

---

## Abstract

This document describes IoDNS, a lightweight metadata publication
framework embedded within the Domain Name System (DNS). IoDNS allows any
DNS owner name to publish structured, machine-readable information in a
discoverable, authenticated, and integrity-protected format. The system
primarily uses DNS TXT records to transport JSON-based payloads and
requires DNSSEC for authoritative authenticity.

IoDNS enables a semantic layer over DNS that can signal identity,
service endpoints, policies, blockchain resources, and payment
mechanisms including x402 and L402.

---

## 1. Introduction

DNS is the globally distributed, permissionless database that underpins
Internet addressing and service discovery. Its reach, ubiquity, and
caching behavior make it attractive for applications requiring low-cost
distribution of authoritative metadata.

As applications and autonomous agents increasingly need to discover
services, payment mechanisms, and machine-readable policy, DNS offers a
natural substrate for publishing such information without introducing a
new global discovery layer.

IoDNS defines a convention for publishing structured JSON metadata in DNS
TXT records protected by DNSSEC.

---

## 2. Discovery

An IoDNS-enabled name publishes:

```dns
_iod.<owner> TXT "v=1; idx=_iod.index; alg=jcs+jws; enc=zstd+b64url; dnssec=required"
```

The `idx` field identifies the metadata index.

---

## 3. Document Index

The metadata index is published at `_iod.index.<owner>`.

Each TXT record describes one logical document:

```dns
_iod.index.example.com. 300 IN TXT "id=payments;type=payments;hash=abc123...;ts=2026-03-15T18:30:00Z;ttl=3600"
```

---

## 4. Document Transport

Logical documents are published at `_iod.doc.<id>.<owner>`.

TXT strings are chunked as:

```text
seq=<n>/<total>; csum=<crc32c>; part=<base64url>
```

Clients reassemble, decode, decompress, and verify the canonical JSON.

---

## 5. Core Document Types

### 5.1. `identity`

Identity and contact metadata.

### 5.2. `services`

API endpoints, MCP servers, and related service metadata.

### 5.3. `blockchain`

Canonical assertions about blockchain addresses, names, and
proof-of-control links.

### 5.4. `payments`

Machine-payment protocols and discovery metadata including x402, L402,
Lightning Address, and settlement references.

---

## 6. Relationship to x402 and L402

IoDNS does not replace x402 or L402. It provides a structured discovery
framework for them.

IoDNS also incorporates the use case covered by the standalone x402 DNS
discovery draft by allowing a `payments` document to reference `_x402`
TXT discovery or directly publish x402 endpoints.

---

## 7. Security Considerations

IoDNS relies on DNSSEC for transport authenticity. Zones MUST protect
DNSSEC signing keys. Clients MUST validate DNSSEC on `_iod`, `_iod.index`,
and `_iod.doc.*` RRsets.

Optional object-level signatures MAY be used for detached verification.

---

## 8. References

### 8.1. Normative References

- RFC 4033, "DNS Security Introduction and Requirements"
- RFC 6763, "DNS-Based Service Discovery"
- RFC 8785, "JSON Canonicalization Scheme (JCS)"

### 8.2. Informative References

- Jeftovic, M., "Simplifying Bitcoin Addresses with DNS", Bitcoin Magazine,
  May 7, 2024
- Jeftovic, M., "x402 DNS Discovery", GitHub repository:
  `markjr/x402-dns-discovery`
- Lightning Labs, "L402", GitHub repository:
  `lightninglabs/L402`

---

## 9. Status

This file is included in the repository as a working Internet-Draft
candidate to invite contributor feedback before any formal IETF
submission.
