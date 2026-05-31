# Data Analysis Tool

## Overview

Data Analysis Tool is an object-oriented Python package developed to simplify data preprocessing, exploratory data analysis, and interactive visualization tasks. The package provides a collection of utilities for data inspection, missing value treatment, duplicate removal, outlier detection, feature transformation, correlation analysis, and visualization. It is designed to help users efficiently prepare and explore tabular datasets within Python and Google Colab environments.

---

## Features

### Data Inspection

* Dataset loading and management
* Dataset summary generation
* Column information analysis
* Missing value identification

### Data Cleaning

* Missing value imputation using mean, median, mode, or constant values
* Duplicate row detection and removal
* Outlier detection using the Interquartile Range (IQR) method
* Row and column deletion utilities

### Data Visualization

* Histograms
* Bar charts
* Pie charts
* Scatter plots
* Violin plots
* Correlation heatmaps

### Feature Engineering

* Numerical data normalization

  * Min-Max Scaling
  * Standard Scaling
  * Robust Scaling
* Categorical data encoding

  * One-Hot Encoding
  * Ordinal Encoding

### Statistical Analysis

* Numerical correlation analysis
* Categorical correlation analysis using Cramer's V
* Unified association heatmaps

---

## Project Structure

```text
Data-Analysis-Tool/
│
├── data_analysis/
│   ├── __init__.py
│   └── core.py
│
├── pyproject.toml
├── README.md
├── .gitignore
└── data_analysis_notebook.ipynb
```

---

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/E23026/data-analysis-tool.git
```

---

## Usage

Import the package:

```python
from data_analysis import DataInspector, PlottingMethods
```

Create objects:

```python
inspector = DataInspector()
plotter = PlottingMethods()
```

Upload and inspect a dataset:

```python
inspector.upload_data()

inspector.get_summary()

inspector.column_details()
```

Handle missing values:

```python
inspector.handle_missing_values(
    strategy="median"
)
```

Remove duplicates:

```python
inspector.remove_duplicates()
```

Perform outlier detection:

```python
inspector.handle_outliers(
    columns=["Age", "Fare"],
    find_and_delete=True
)
```

Generate visualizations:

```python
inspector.plot_numerical(
    ["Age", "Fare"]
)

inspector.plot_categorical(
    ["Sex", "Embarked"]
)
```

Perform correlation analysis:

```python
inspector.plot_numerical_correlation()

inspector.plot_categorical_correlation()

inspector.plot_all_associations_heatmap()
```

---

## Dependencies

* NumPy
* Pandas
* Plotly
* SciPy
* Scikit-Learn

---

## Applications

This package can be used for:

* Exploratory Data Analysis (EDA)
* Data Cleaning and Preprocessing
* Statistical Analysis
* Academic Data Science Projects
* Machine Learning Data Preparation
* Educational Demonstrations in Python and Google Colab

---

## Author

E23026

GitHub Repository:
https://github.com/E23026/Statistical-Learning-e23026/Data-Analysis-Tool

