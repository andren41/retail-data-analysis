# How to Run: Retail Mini-Project

**Author:** André Nicolai Popadiuk | **Class:** T2 | **Course:** Data Analysis with Python

## Prerequisites

* Python 3.8 or higher installed
* pip

## Installing Dependencies

Open a terminal and run:

```
pip install pandas numpy
```

> **Note:** The `csv` and `datetime` libraries are part of Python's standard library, so they do not need to be installed.

## Dataset

The script needs the file `Base Varejo.csv` (a public Kaggle dataset, ~830,000 rows). It is **not included** in this repository due to its size.

Download it here: https://www.kaggle.com/datasets/namespaiva/base-varejo/data

## Running in VS Code (recommended)

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Confirm that `Base Varejo.csv` is in the same folder as `miniprojeto.py`.
4. Open the integrated terminal and run:

```
python miniprojeto.py
```

## Running in Google Colab

1. Go to [colab.research.google.com](https://colab.research.google.com).
2. Create a new notebook (**+ New notebook**).
3. In the first cell, upload the CSV by running the following code (then select `Base Varejo.csv`):

```python
from google.colab import files
files.upload()
```

4. Paste the contents of `miniprojeto.py` into the following cells.
5. Change the `CAMINHO_CSV` variable in the script to:

```python
CAMINHO_CSV = "/content/Base Varejo.csv"
```

6. Run all cells (`Ctrl + F9`).

## Expected Output

The script prints the following to the terminal:

* **Sprint 1** → Read confirmation (number of records and columns)
* **Sprint 2** → Data types before and after conversion
* **Sprint 3** → Data quality report (nulls, duplicates, inconsistencies)
* **Sprint 4** → Descriptive statistics table (`CL_FHL`)
* **Sprint 5** → 5 grouping tables (`groupby` and `pivot_table`)
* **Sprint 6** → 6 key insights from the analysis

**Estimated run time:** 1 to 3 minutes (dataset with approximately 830,000 rows).
