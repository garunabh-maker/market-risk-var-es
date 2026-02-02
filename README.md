# Rolling VaR and Expected Shortfall (Market Risk)

## Objective
This project implements historical and rolling Value at Risk (VaR) and Expected Shortfall (ES) at the 97.5% confidence level to monitor tail risk for a trading portfolio, aligned with the FRTB market risk framework.

## Methodology
- Historical simulation approach
- Daily P&L as input
- 250-day rolling window
- Risk measures:
  - Historical VaR (97.5%)
  - Historical Expected Shortfall (97.5%)
  - Rolling Expected Shortfall
## Key Insights
- VaR provides a loss threshold but does not capture tail severity.
- Expected Shortfall measures average losses beyond the VaR threshold.
- Rolling ES highlights changes in tail risk across market regimes and is more informative during periods of stress.

## Regulatory Context
Under the Fundamental Review of the Trading Book (FRTB), Expected Shortfall at the 97.5% confidence level replaces VaR to better capture tail risk and market illiquidity. This project demonstrates the core building blocks of that framework.

## Project Structure
market-risk-var-es/
├── data/ # market data for Amazon Inc
├── src/ # Risk measure implementations
├── analysis.ipynb # Analysis and interpretation
└── README.md

## How to Run
1. Clone the repository
2. Install dependencies:
   - numpy
   - pandas
3. Run `analysis.ipynb` to compute and analyze risk measures.

## Notes
- Data used in this project is simulated for demonstration purposes.
- The focus is on methodology and interpretation rather than production optimization.



