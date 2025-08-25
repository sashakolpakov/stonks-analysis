# Stonks Analysis

This project analyzes financial data using various dimensionality reduction techniques (UMAP, tSNE, PCA, and DiRE) to visualize relationships between different asset classes (stocks, crypto, index). We also compare different embedding methods performance on a variety of factors such as proper asset clustering and class identification. This can be useful for identifying possible similarities between assets and for trading strategies carry-over. 

## Jupyter Notebook
Open and run `stonks_analysis.ipynb` to see the complete analysis. You can modify the tickers and date range in the notebook to analyze different assets or time periods.

## Dependencies

The package automatically installs all required dependencies:
- yfinance - for downloading financial data
- pandas, numpy - data manipulation
- matplotlib - plotting
- scikit-learn - PCA, tSNE
- umap-learn - [UMAP](https://github.com/lmcinnes/umap) dimensionality reduction
- dire-jax - [DiRE](https://github.com/sashakolpakov/dire-jax) dimensionality reduction
- hdbscan - [HDBSCAN](https://github.com/scikit-learn-contrib/hdbscan) clustering algorithm
