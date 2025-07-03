---
title: "Multisignature Wallets"
description: "How to use multisig wallets (2-of-3, 3-of-5) for shared custody and extra protection of your Bitcoin."
keywords:
  - "multisig wallet"
  - "shared custody"
  - "Bitcoin multisignature"
  - "Electrum multisig"
  - "Casa wallet"
---

# Multisignature Wallets

Multisig requires **multiple approvals** before funds move—ideal for teams or high-value holdings.

## A. How Multisig Works  
- **M-of-N scheme:** Funds need at least M signatures out of N total keys.  
- Each key can reside on a separate device or with a different custodian.

## B. Common Configurations  
| Setup    | Use Case                                  |
|----------|-------------------------------------------|
| 2-of-3   | Personal+trusted friend backup            |
| 3-of-5   | Corporate treasury needing quorum         |
| 5-of-7   | DAO or community-governed fund            |

## C. Tools & Walkthroughs

### 1. Electrum Multisig  
1. Open Electrum → **File > New/Restore** wallet.  
2. Choose “Multi-signature wallet.”  
3. Define “N” co-signers and “M” required signatures.  
4. Each participant loads their own xpub.  
5. Export the multisig wallet file to each device.

### 2. Casa & Unchained Capital  
- **Casa:** Managed 2-of-3 multisig with social recovery.  
- **Unchained:** 2-of-3 multisig + integrated financing.

---

> _Proceed: [Seed Phrase & Key Management](./seed-phrase-key-management.md)_