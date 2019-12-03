"""lambdata - a collection of data science helper functions"""
import pandas as pd
import numpy as np
from scipy import stats

#sample code
ones = pd.DataFrame(np.ones(10))
zeros = pd.DataFrame(np.zeros(50))

#sample functions
def increment(x):
    return (x + 1)

def mean(x):
    return (len(x) / 2)

def confidence_interval(data, confidence=0.95):
    data = np.array(data)
    mean = np.mean(data)
    n = len(data)
    stderr = stats.sem(data)
    margin = stderr * stats.t.ppf((1 + confidence) / 2.0, n - 1)
    return (mean, mean - margin, mean + margin)

def top_perc(df, cols):
    for col in cols:
        df = df[(df[col] >= np.percentile(df[col], 0.5)) &
            (df[col] <= np.percentile(df[col], 99.5))]
    return df
