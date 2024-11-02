import pandas as pd
import numpy as np

def random_sampling(df, num_samples):
    return df.sample(n = num_samples, replace=False)

def monte_carlo_sampling(df, column_name, sample_size, num_samples):
    samples = []
    for i in range(num_samples):
        l = df[column_name].sample(n = sample_size, replace=True)
        samples.append(l.mean())
    return samples

#propotional sampling
def stratified_sampling(df, column_name, num_samples):
    return df.groupby(column_name, group_keys=False).apply(lambda x: x.sample(n = num_samples, replace=False))