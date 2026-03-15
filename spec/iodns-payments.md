# IoDNS Payments

The `payments` document type describes machine-payment protocols and
payment-related discovery metadata.

## Scope

This document type is intended for:

- x402
- L402
- Lightning Address
- LNURL
- settlement asset references
- machine-readable paid API metadata

## Rationale

Payment methods should be distinct from canonical wallet or name
assertions. For that reason IoDNS separates:

- `blockchain`: what assets or on-chain identities are associated with a name
- `payments`: how services attached to that name are paid for

## Example

```json
{
  "iod_version": "1.0",
  "zone": "example.com",
  "payments": {
    "methods": [
      {
        "id": "x402-main",
        "protocol": "x402",
        "discovery": "_x402.example.com",
        "endpoint": "https://pay.example.com/.well-known/x402",
        "settlement_assets": ["btc-main", "ens-primary"]
      },
      {
        "id": "l402-api",
        "protocol": "l402",
        "auth_endpoint": "https://api.example.com/l402",
        "issuer": "example.com",
        "token_type": "macaroon",
        "settlement_assets": ["btc-main"]
      },
      {
        "id": "lightning-address",
        "protocol": "lightning",
        "lightning_address": "pay@example.com"
      }
    ]
  },
  "last_updated": "2026-03-15T18:30:00Z"
}
```

## x402 compatibility

IoDNS can reference the standalone `_x402` TXT discovery convention
directly. A client MAY use either:

- direct `_x402` TXT discovery
- IoDNS `payments` discovery

IoDNS is therefore compatible with the focused x402 DNS discovery model
while also allowing richer metadata publication under a common framework.
