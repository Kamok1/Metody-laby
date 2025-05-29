
# Predict Students' Dropout and Academic Success

## Setting up the virtual environment

1. Create a virtual environment:  
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:  
   - On Windows:  
     ```
     venv\Scripts\activate
     ```
   - On Linux/Mac:  
     ```
     source venv/bin/activate
     ```

3. Install required libraries:  
   ```
   pip install -r requirements.txt
   ```

## Running the full project

Note:
The second part of the project is located in the folder /part2.

To execute the full analysis and generate all visualizations and summaries, run:

```
python data_analysis_main.py
```

## Running individual functions


### Data processing

File: `data_process.py`  
Contains functions for mapping, encoding, and preprocessing the dataset.

Example usage:
```python
from data_process import process_data
df_cleaned = process_data(df)
```

### Data summary

File: `data_summary.py`
```python
from data_summary import save_statistics_to_csv
save_statistics_to_csv(df_cleaned)
```

### Bar plots

File: `generate_barplots.py`

```python
from plot_generators.generate_barplots import generate_barplots

generate_barplots(df_cleaned)
```

### Box plots

File: `generate_boxplots.py`

```python
from plot_generators.generate_boxplots import generate_boxplots

generate_boxplots(df_cleaned)
```

### Count plots

File: `generate_countplots.py`

```python
from plot_generators.generate_countplots import generate_countplots

generate_countplots(df_cleaned)
```

### Histogram plots

File: `generate_histogram_plots.py`

```python
from plot_generators.generate_histogram_plots import generate_hist_plots

generate_hist_plots(df_cleaned)
```

### Regression plots

File: `generate_regression_plots.py`

```python
from plot_generators.generate_regression_plots import generate_regression_plots

generate_regression_plots(df_cleaned)
```

### Violin plots

File: `generate_violinplots.py`

```python
from plot_generators.generate_violinplots import generate_violinplots

generate_violinplots(df_cleaned)
```

### Correlation heatmaps

File: `generate_corelations.py`

```python
from plot_generators.generate_corelations import generate_heatmaps

generate_heatmaps(df_cleaned)
```

### PCA plots

File: `generate_pca.py`

Replace the list of attributes with the relevant numerical columns:

```python
from plot_generators.generate_pca import plot_pca

plot_pca(df_cleaned, attributes=["attribute1", "attribute2", "attribute3"])
```

## Project output structure

After running scripts, plots and outputs will be saved in the following directories:

```
plots/
├── barplots/
├── boxplots/
├── countplots/
├── heatmaps/
├── histograms/
├── pca/
├── regressions/
├── violinplots/

output/
├── numeric_statistics.csv
├── categorical_statistics.csv
```
