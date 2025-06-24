---
title: "Token Standards: ERC-20 & ERC-721"
description: "An overview of Ethereum’s token standards, covering the fungible ERC-20 and non-fungible ERC-721 specifications, use cases, and implementation details."
keywords:
  - "ERC-20 tokens"
  - "ERC-721 NFTs"
  - "Ethereum token standards"
  - "fungible tokens"
  - "non-fungible tokens"
  - "smart contract interfaces"
  - "token implementation"
---

# Token Standards: ERC-20 & ERC-721

Ethereum introduced standardized interfaces for tokens, enabling interoperability across wallets, exchanges, and dApps. The two foundational standards are **ERC-20** for fungible tokens and **ERC-721** for non-fungible tokens (NFTs).

## ERC-20: Fungible Tokens

### What Is ERC-20?
- A smart contract interface defining a common set of functions for interchangeable (fungible) tokens.
- Fungible tokens are identical and divisible (e.g., stablecoins, governance tokens).

### Core Functions
- `totalSupply()` — Returns total token supply.
- `balanceOf(address owner)` — Returns token balance of an address.
- `transfer(address to, uint256 amount)` — Transfers tokens.
- `approve(address spender, uint256 amount)` — Authorizes another address to spend tokens.
- `transferFrom(address from, address to, uint256 amount)` — Transfers on behalf of another.
- `allowance(address owner, address spender)` — Returns remaining approved amount.

### Events
- `Transfer(address indexed from, address indexed to, uint256 value)`
- `Approval(address indexed owner, address indexed spender, uint256 value)`

### Use Cases
- **Stablecoins:** USDC, DAI
- **Governance Tokens:** UNI, AAVE
- **Utility Tokens:** Gas tokens, reward tokens

*Cluster article: [Understanding Smart Contracts & the EVM](/ethereum/smart-contracts-and-evm/)*

## ERC-721: Non-Fungible Tokens (NFTs)

### What Is ERC-721?
- A standard for unique, indivisible tokens representing distinct digital assets.
- Each token has a unique `tokenId` and metadata URI.

### Core Functions
- `balanceOf(address owner)` — Number of NFTs owned by an address.
- `ownerOf(uint256 tokenId)` — Owner of a specific NFT.
- `safeTransferFrom(address from, address to, uint256 tokenId)` — Secure transfer with checks.
- `transferFrom(address from, address to, uint256 tokenId)` — Basic transfer without safety checks.
- `approve(address to, uint256 tokenId)` — Approve another address to transfer a specific NFT.
- `setApprovalForAll(address operator, bool approved)` — Approve or revoke operator for all NFTs.
- `getApproved(uint256 tokenId)` — Address approved for a specific NFT.
- `isApprovedForAll(address owner, address operator)` — Operator approval status.

### Events
- `Transfer(address indexed from, address indexed to, uint256 indexed tokenId)`
- `Approval(address indexed owner, address indexed approved, uint256 indexed tokenId)`
- `ApprovalForAll(address indexed owner, address indexed operator, bool approved)`

### Use Cases
- **Digital Art & Collectibles:** CryptoKitties, Bored Ape Yacht Club
- **Game Assets:** In-game items with provable scarcity
- **Real-World Tokenization:** Real estate deeds, event tickets

*Cluster article: [The NFT Revolution](/ethereum/understanding-ethereum-basics-to-nfts/)*

---

_Return to the pillar page: [Understanding Ethereum: From Basics to NFTs](/ethereum/understanding-ethereum-basics-to-nfts/)._
