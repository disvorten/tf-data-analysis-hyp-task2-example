import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 1109095907


def solution(x: np.array, y: np.array):
    alpha = 0.1
    res = anderson_ksamp([x, y])
    if res.pvalue <= alpha:
        return True
    else:
        return False
