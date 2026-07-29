# Capstone Proposal: Predictive Maintenance for Centrifugal Pumps

## Operational Problem Statement
Unplanned pump failures create production losses, emergency labor, and safety risk. The capstone will build a predictive maintenance workflow that identifies pumps likely to fail within seven days and estimates remaining useful life for prioritized maintenance scheduling.

## Source Data
- Synthetic IoT data in `data/pdm_synthetic_sensor_data.csv`
- 2,640 timestamped records across 24 pump assets
- Signals: vibration, temperature, pressure, acoustic level, motor current, error events, shift, depot, health status, fault type, and RUL
- Built-in teaching issues: missing values, outliers, and a constant sensor column with no predictive value

## Analytical Approach
- Clean missing values and flag outliers using the three-standard-deviation rule
- Use an independent t-test to compare day vs. night vibration behavior
- Engineer rolling mean, RMS, and peak-to-peak vibration features
- Train a bagged-tree classifier for seven-day failure risk
- Fit a baseline regression model for remaining useful life

## Success Metrics
- Reduce false alarms by 20% versus a simple threshold rule
- Catch at least 80% of near-failure events during the seven-day intervention window
- Keep RUL mean absolute error below 72 hours in the synthetic benchmark
- Translate model outputs into two stakeholder-ready briefs: one technical, one financial

## Pilot Result Baseline
- Classifier accuracy: 94.7%
- Sensitivity: 81.9%
- False alarm rate: 1.0%
- RUL MAE: 109.0 hours
