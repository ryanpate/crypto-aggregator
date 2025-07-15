---
title: "How Ethereum Works"
description: "An in-depth explanation of the Ethereum blockchain architecture: the EVM, gas mechanics, consensus model, and transaction flow."
keywords:
  - "How Ethereum works"
  - "Ethereum architecture"
  - "Ethereum Virtual Machine"
  - "EVM explained"
  - "Ethereum gas mechanics"
  - "Ethereum consensus"
  - "blockchain transaction flow"
  - "Ethereum PoW PoS"
---

# How Ethereum Works

Ethereum is powered by a combination of core components and processes that enable decentralized applications and smart contracts. This article covers:

## Table of Contents
1. [Ethereum Virtual Machine (EVM)](#ethereum-virtual-machine-evm)
2. [Gas & Transaction Lifecycle](#gas--transaction-lifecycle)
3. [Consensus Mechanisms: PoW to PoS](#consensus-mechanisms-pow-to-pos)
4. [Block Creation & Finality](#block-creation--finality)
5. [Smart Contract Execution](#smart-contract-execution)
6. [Networking & Nodes](#networking--nodes)
7. [Ethereum 2.0 & Sharding](#ethereum-20--sharding)

---

## Ethereum Virtual Machine (EVM)
The EVM is a sandboxed runtime environment where smart contracts execute. Every Ethereum node runs an instance of the EVM to ensure deterministic execution:
- **Bytecode execution:** Solidity/Vyper code compiled to EVM bytecode.
- **Determinism:** All nodes compute the same results for each transaction.
- **Isolation:** Smart contracts cannot access underlying system resources.

## Gas & Transaction Lifecycle
Gas is the fuel for Ethereum transactions:
1. **Nonce & Transaction Creation:** User signs a transaction with their private key.
2. **Gas Limit & Gas Price:** Maximum gas and price per unit of computational work.
3. **Inclusion in Mempool:** Nodes propagate pending transactions.
4. **Block Inclusion:** Miners/validators include transactions, consuming gas.
5. **Execution & State Changes:** EVM executes contract code, modifies state.
6. **Gas Accounting:** Unused gas refunded; fees paid to miner/validator.

## Consensus Mechanisms: PoW to PoS
- **Proof-of-Work (PoW):** Miners solve computational puzzles to propose blocks (pre-Merge).  
- **Proof-of-Stake (PoS):** Validators stake ETH to propose and attest blocks (post-Merge).  
- **Beacon Chain:** Coordinates PoS validators and shard chains.

## Block Creation & Finality
- **Block Time:** ~12 seconds per block.  
- **Finality:** PoS uses Casper FFG to finalize checkpoints every epoch.  
- **Reorgs:** Temporary chain forks resolved by longest chain or finality rules.

## Smart Contract Execution
- **State Trie:** Key-value store of account balances and contract storage.  
- **World State:** Updated by each transaction’s state changes.  
- **Intrinsic Gas:** Base gas cost per transaction plus computational costs.

## Networking & Nodes
- **Full Nodes:** Download and validate all blocks and state.  
- **Light Clients:** Fetch block headers and request state proofs.  
- **P2P Network:** DevP2P protocol for gossiping transactions and blocks.

## Ethereum 2.0 & Sharding
- **Phase 0 (Beacon Chain):** PoS consensus layer.  
- **Phase 1 (Shard Chains):** Parallel chains to increase throughput.  
- **Phase 1.5 (The Merge):** Integration of Ethereum mainnet into PoS.

---

_For foundational context, see [Understanding Ethereum: From Basics to NFTs](/ethereum/understanding-ethereum-basics-to-nfts/) and the cluster article [What Is Ethereum?](/ethereum/what-is-ethereum/)._