# Question 2: How do One-Hit Wonders perform compared to Superstars?

## Overview

This analysis examines the Billboard Hot 100 chart performance of **one-hit wonders** versus **superstars** across 60 years (1958-2017).

### Research Question
**How do one-hit wonders perform compared to superstars on the Billboard Hot 100 charts?**

## Definitions

- **One-Hit Wonder**: Artists with exactly **1 unique song** on the Hot 100
- **Superstar**: Artists with **5+ unique songs** on the Hot 100

## Key Findings

### Chart Longevity (Weeks on Chart)
- **One-Hit Wonders**: Average **9.7 weeks**
- **Superstars**: Average **9.0 weeks**
- **Ratio**: Superstars' hits stay on chart **0.93× longer** ⚠️ *Counterintuitive finding!*

### Peak Position (Lower is Better)
- **One-Hit Wonders**: Average peak position **45.0**
- **Superstars**: Average peak position **38.6**
- **Advantage**: Superstars achieve **6.4 positions higher** peak ranking

### Statistical Significance
✅ Both metrics show **p < 0.001** (highly significant differences)

## Important Insight

While superstars' individual hits don't necessarily stay longer on charts, they have the **ability to place 5+ songs** on the chart. This suggests:

1. Superstars have **better initial chart performance** (higher peaks)
2. Superstars have **established fanbases** that support multiple releases
3. The **portfolio effect** of multiple hits is what distinguishes superstars from one-hit wonders

## Files

- `Q2-OneHitWonders-vs-Superstars.ipynb` - Complete analysis with visualizations
- `README.md` - This file

## How to Use

1. Ensure you have the data file in the `data/` directory
2. Update the data path in the notebook if needed
3. Run the notebook cells sequentially
4. Review visualizations and statistics

## Data Requirements

The analysis requires the Billboard Hot 100 dataset with the following columns:
- `WeekID` - Date of chart entry
- `Song` - Song title
- `Performer` - Artist name
- `Peak Position` - Highest chart position reached
- `Weeks on Chart` - Total weeks on the chart
- `Week Position` - Position in the specific week

## Conclusion

Superstars demonstrate superior chart dominance through **consistent high peak positions** and **multi-hit success**, while one-hit wonders achieve temporary commercial success but cannot sustain follow-up releases.
