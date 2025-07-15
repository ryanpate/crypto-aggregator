---
title: "Impermanent Loss Explained"
description: "A detailed guide to understanding impermanent loss in DeFi liquidity pools: what it is, how it occurs, and strategies to mitigate its impact."
keywords:
  - "impermanent loss"
  - "liquidity pool risks"
  - "DeFi impermanent loss"
  - "impermanent loss mitigation"
  - "liquidity provider strategies"
  - "impermanent loss calculator"
---

# Impermanent Loss Explained

Impermanent loss occurs when you provide liquidity to an automated market maker (AMM) pool and the relative price of the pooled tokens changes. The value of your share in the pool can be less than if you simply held the tokens separately.

## What Causes Impermanent Loss

1. **Price Divergence:** When Token A and Token B in the pool move at different rates, the AMM rebalances your share, leading to a potential loss compared to HODLing.
2. **Pool Dynamics:** The constant product formula (x * y = k) forces the pool to adjust reserves as trades occur, impacting your share value.

## Calculating Impermanent Loss

The formula for impermanent loss (IL) when a token’s price changes by r% is:

```
IL = (2 * √(1 + r) / (2 + r)) - 1
```

- **r:** ratio of price change (e.g., 0.5 for a 50% increase)
- **Result:** percentage loss relative to HODLing

## Strategies to Mitigate Impermanent Loss

- **Stablecoin Pools:** Use pools with assets that have minimal volatility (e.g., USDC/DAI).
- **Diversify:** Spread liquidity across multiple pools and protocols.
- **Fee Farming:** Choose pools with high trading fees to offset IL.
- **Harvest & Rebalance:** Monitor and withdraw or rebalance when IL exceeds earned fees.

## Tools & Calculators

- [Impermanent Loss Calculator](https://www.zapper.fi/il) (Zapper.fi)
- **DeFi Dashboard Plugins:** Many wallets offer built-in IL estimators.

## Conclusion

Impermanent loss is a core risk of providing liquidity. By understanding its mechanics and employing mitigation strategies—like stablecoin pools and fee farming—you can optimize your DeFi earnings.

---

_Return to the [Pillar Page: The Ultimate Guide to DeFi](/defi/) or see our in-depth [Yield Farming & Liquidity Mining](/defi/yield-farming-liquidity-mining/) article for more strategies._