import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from collections import defaultdic

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

def get_counts2(sequence):
    counts = defaultdic(int)
    for x in sequence:
        counts[x] += 1
    return counts

