# IoDNS
### Agent-discoverable metadata published over DNS

IoDNS (Intelligence over DNS) is a framework for publishing structured,
machine-readable metadata inside the DNS namespace using TXT records and
DNSSEC authentication.

It allows a DNS name to act as an authoritative registry for information
beyond traditional address records, including:

- service endpoints
- agent APIs
- machine-payment protocols (x402, L402)
- blockchain identities
- cryptographic keys
- machine-readable policy

IoDNS effectively creates a lightweight semantic layer on top of DNS,
allowing applications, agents, and services to discover identity,
capabilities, and payment mechanisms directly from the global DNS
namespace.

---

## Background

DNS was originally designed to map human-readable names to network
addresses. Over time, it has increasingly been used to publish additional
metadata.

Back in 2018, I wrote in my book:

> "There is also another aspect of the DNS, which has emerged relatively
> recently, that takes it beyond a protocol simply for mapping names to
> IP addresses and back. The DNS is now, and will increasingly be, used
> to publish metadata.
>
> Because of its ubiquity and relatively light footprint, especially
> combined with DNSSEC to authenticate responses, the DNS lends itself
> well for publishing other data that applications and clients will be
> searching for. I am speaking specifically now of authentication,
> reputation, and encryption processes such as X.509 certificates,
> PGP/GPG keys, DNS-based Real-Time Blackhole Lists (RBLs), and response
> policy zones (RPZs). The relatively widespread adaptation of SPF and
> DKIM signal the early beginnings of these types of DNS applications."

Technologies such as SPF, DKIM, DMARC, DANE, and DNS-based service
discovery have already demonstrated that DNS can function as a
distributed metadata layer.

IoDNS builds on this pattern by defining a structured way to publish
JSON metadata in DNS records so that software systems and autonomous
agents can discover services and capabilities programmatically.

---

## Why DNS?

DNS has several properties that make it well suited for metadata
distribution:

- global reach and ubiquity
- hierarchical authority model
- built-in caching and replication
- extremely lightweight queries
- cryptographic authentication via DNSSEC

These properties allow DNS zones to act as authoritative registries for
machine-readable metadata with minimal additional infrastructure.

---

## Discovery for the Agentic Economy

As software agents become capable of autonomously discovering services,
negotiating access, and executing transactions, they require a globally
available signaling and discovery layer.

Any such layer must have several characteristics:

- global reach
- low latency
- decentralized authority
- cache-friendly distribution
- cryptographic authenticity

The Domain Name System already provides these properties.

Creating a new global discovery infrastructure for agents would largely
replicate mechanisms that DNS already implements: hierarchical authority,
distributed caching, and global resolution.

IoDNS therefore treats DNS not merely as a name-to-address mapping
system, but as the natural discovery substrate for machine-readable
metadata.

Rather than introducing a new network layer, IoDNS leverages the
existing DNS namespace to publish structured metadata that agents,
applications, and services can query using the infrastructure that
already exists everywhere on the Internet.

DNS already solves global discovery; IoDNS simply extends it to
machine-readable intelligence.

---

## How an Agent Uses IoDNS

IoDNS allows software agents to discover the capabilities and policies
associated with a domain using standard DNS queries.

A typical interaction might proceed as follows:

1. Discover IoDNS support

   `_iod.example.com TXT`

2. Retrieve the metadata index

   `_iod.index.example.com TXT`

   The index lists available documents such as:
   - identity
   - services
   - blockchain
   - payments

3. Fetch relevant metadata

   `_iod.doc.services.example.com TXT`

   TXT records contain chunked, encoded JSON describing service endpoints.

4. Determine payment requirements

   `_iod.doc.payments.example.com TXT`

   Supported payment protocols may include:
   - x402
   - L402
   - Lightning

5. Interact with the service

   Using the discovered endpoints and payment mechanisms, the agent can
   authenticate, pay for access, or interact with the service.

---

## Conceptual Model

```text
DNS
 └── IoDNS metadata
      ├── identity
      ├── services
      ├── blockchain
      └── payments
            ├── x402
            └── L402
```

DNS remains the root of authority for the namespace.
IoDNS provides a structured layer for publishing metadata associated
with that namespace.

---

## Relationship to Existing Work

IoDNS does not replace x402 or L402. It provides a discovery layer for
them.

The standalone x402 DNS discovery draft remains useful as a focused,
minimal mechanism for `_x402` TXT-based discovery. IoDNS incorporates
that use case into a broader metadata framework and may eventually
subsume it if the wider model proves useful in practice.

---

## Not to be confused with

Security vendors have used the phrase "Intelligence over DNS" to
describe threat-intelligence feeds distributed through DNS lookups.

IoDNS is unrelated to those systems.

Those products use DNS as a transport channel for security data.
IoDNS instead defines a structured framework for publishing metadata
inside DNS itself.

---

## Repository Structure

```text
spec/
    iodns-protocol.md
    iodns-dns-encoding.md
    iodns-document-types.md
    iodns-payments.md

drafts/
    draft-jeftovic-iodns-00.md

examples/
    example-zonefile.txt
    example-services.json
    example-blockchain.json
    example-payments.json

tools/
    encode_iodns.py
    resolve_iodns.py
```

---

## Status

IoDNS is currently an experimental specification.

The goal of this repository is to document the design, gather feedback,
and develop reference implementations. Future work may include formal
standardization through the IETF or related processes.

---

## References

- Jeftovic, M., "Simplifying Bitcoin Addresses with DNS", Bitcoin Magazine,
  May 7, 2024
- markjr/x402-dns-discovery
- lightninglabs/L402
