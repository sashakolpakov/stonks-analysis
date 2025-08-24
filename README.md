# Stonks Analysis

This project analyzes financial data using various dimensionality reduction techniques (UMAP, tSNE, PCA, and DiRE) to visualize relationships between different asset classes (stocks, crypto, index). We also compare different embedding methods performance on a variety of factors such as proper asset clustering and class identification. This can be useful for identifying possible similarities between assets and for trading strategies carry-over. 

## Installation

### Option 1: Direct pip install from GitHub (Recommended for Colab)
```python
%pip install -U "git+https://github.com/sashakolpakov/stonks-analysis.git@main"
```

### Option 2: Local development
1. Clone the repository:
   ```bash
   git clone https://github.com/sashakolpakov/stonks-analysis.git
   cd stonks-analysis
   ```
2. Install in development mode:
   ```bash
   pip install -e .
   ```

## Usage

### In a Jupyter Notebook or Colab:
```python
# Install the package
%pip install -U "git+https://github.com/sashakolpakov/stonks-analysis.git@main"

# Import functions
from stonks_analysis import download_data, compute_generic_features
# OR import the utils module
from stonks_analysis import utils

# Use the functions
data = download_data("AAPL", lookback_days=365)
features = compute_generic_features(data)
```

### Run the analysis notebook:
Open and run `stonks_analysis.ipynb` to see the complete analysis. You can modify the tickers and date range in the notebook to analyze different assets or time periods.

## Dependencies

The package automatically installs all required dependencies:
- yfinance - for downloading financial data
- pandas, numpy - data manipulation
- matplotlib - plotting
- scikit-learn - machine learning utilities
- umap-learn - UMAP dimensionality reduction
- dire-jax - DiRE dimensionality reduction
