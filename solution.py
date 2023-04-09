import pandas as pd
import numpy as np
from scipy.stats import cramervonmises_2samp

chat_id = 1109095907 


def solution(x: np.array, y: np.array):
    alpha = 0.1
    res = cramervonmises_2samp(x, y, method='asymptotic')
    if res.pvalue <= alpha:
        return True
    else:
        return False
