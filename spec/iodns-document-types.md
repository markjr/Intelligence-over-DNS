# IoDNS Document Types

IoDNS defines an extensible set of document types. Initial core types:

## `identity`

Canonical identity and contact information associated with a name.

## `services`

API endpoints, service locations, MCP servers, and other technical endpoints.

## `blockchain`

Canonical assertions about blockchain assets, names, and addresses.

Examples include:

- Bitcoin addresses
- Ethereum EOAs
- ENS names
- Stacks `.btc` names
- proof-of-control references

## `payments`

Operational payment and access-control mechanisms for services.

Examples include:

- x402 discovery
- L402 authentication/payment endpoints
- Lightning Address
- LNURL
- settlement asset references

## `keys`

Signing keys used for object-level signatures and key rollover.

## Relationship between `blockchain` and `payments`

`blockchain` is for asserting ownership or authoritative association with
an on-chain identity or asset.

`payments` is for advertising how a client or agent can pay for service
or gain access to paid resources.

A `payments` document MAY reference `blockchain` entries by ID.
