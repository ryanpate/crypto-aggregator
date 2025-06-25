---
title: "Hardware Wallets & Cold Storage"
description: "Step-by-step guide to setting up and using hardware wallets and other cold-storage methods to secure your Bitcoin."
keywords:
  - "hardware wallets"
  - "cold storage"
  - "Ledger Nano"
  - "Trezor Model T"
  - "paper wallet"
  - "air-gapped wallet"
---

# Hardware Wallets & Cold Storage

Cold storage is the gold standard for long-term Bitcoin security.

## A. Hardware Wallets

### Popular Devices  
- **Ledger Nano S / X**  
- **Trezor One / Model T**  
- **Coldcard Mk. 4**

### Setup & Usage Steps  
1. **Unbox** and inspect the factory seal.  
2. **Install** the vendor’s companion app on a clean PC.  
3. **Generate** a new seed on the device (never on your computer).  
4. **Record** the 24-word seed on paper/metal backup.  
5. **Configure** a PIN and enable passphrase protection if offered.  
6. **Test** by sending a small “test” BTC transaction.

---

## B. Paper & Air-Gapped Wallets

### Creating a Paper Wallet  
1. Visit an **offline** seed generator (e.g. bitaddress.org) on an air-gapped machine.  
2. Print the public address + private key QR codes.  
3. Laminate or engrave on metal for durability.

### Air-Gapped USB Method  
1. Boot a **Live Linux** USB on an offline PC.  
2. Use `Electrum` or `Bitcoin Core` to generate keys.  
3. Export unsigned transactions via USB, sign offline, then broadcast on an online PC.

---

> _Continue to: [Software Wallets & Hot Storage](software-wallets-hot-storage.md)_