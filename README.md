# Billboard Hot 100 Analysis: One-Hit Wonders vs Superstars

## Project Overview

This repository contains a comprehensive analysis of the Billboard Hot 100 chart data from 1958-2017, exploring the patterns that distinguish **one-hit wonders** from **superstars** and identifying early career signals that predict superstar success.

## Repository Structure

```
billboard-repo/
├── Question_2/
│   ├── Q2-OneHitWonders-vs-Superstars.ipynb
│   └── README.md
├── Question_5/
│   ├── Q5-Predictive-Signals-Superstar-Success.ipynb
│   └── README.md
└── README.md (this file)
```

## Questions Answered

### Question 2: Chart Performance Comparison
**How do one-hit wonders perform compared to superstars on the Billboard Hot 100?**

**Key Finding**: Superstars achieve **6.4 positions higher** peak rankings and show statistically significant differences in chart performance.

- 📊 Side-by-side performance metrics (boxplots)
- 📈 Statistical testing (Mann-Whitney U test)
- 🎯 Longevity and peak position analysis

### Question 5: Predictive Signals
**What early signs predict whether an artist will build a superstar career?**

**Key Finding**: Debut peak position is the #1 predictor. Artists with **Top 10 debuts are 2.1× more likely** to become superstars.

- 🎯 Feature importance analysis
- 📊 Conversion rates by debut tier
- 💡 Actionable insights for the music industry

## Key Insights

### 📊 Chart Performance
- **One-Hit Wonders**: Average peak position 45.0, 9.7 weeks on chart
- **Superstars**: Average peak position 38.6, 9.0 weeks on chart
- **Statistical Significance**: p < 0.001 (highly significant)

### 🎯 Predictive Signals
- **Top 10 Debuts**: 26.8% become superstars
- **Outside Top 20**: 12.5% become superstars
- **Success Multiplier**: 2.1×

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/lealeaddison/billboardhot100.git
   cd billboard-repo
   ```

2. **Check out the Khandie-Branch**
   ```bash
   git checkout Khandie-Branch
   ```

3. **Install dependencies**
   ```bash
   pip install pandas numpy matplotlib seaborn scipy jupyter
   ```

4. **Run the analyses**
   - Open Jupyter Notebook
   - Navigate to Question_2 or Question_5
   - Run cells sequentially

## Data Requirements

The analysis requires a Billboard Hot 100 dataset with these columns:
- `WeekID` - Date of chart entry (datetime)
- `Song` - Song title (string)
- `Performer` - Artist name (string)
- `Peak Position` - Highest chart position (numeric)
- `Weeks on Chart` - Total weeks on chart (numeric)
- `Week Position` - Position in that specific week (numeric)

## Technologies Used

- **Python 3.9+**
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **matplotlib/seaborn** - Visualization
- **scipy.stats** - Statistical testing
- **Jupyter Notebook** - Interactive analysis

## Branch Information

**Branch**: Khandie-Branch  
This branch contains the organized analysis with:
- Question 2: One-Hit Wonders vs Superstars comparison
- Question 5: Predictive signals for superstar success

---

**Last Updated**: November 2024
