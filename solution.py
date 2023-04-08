import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 1109095907  # Ваш chat ID, не меняйте название переменной


def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.1
    a, b = ks_2samp(x, y)
    if b <= alpha:
        return True
    else:
        return False

