import numpy as np
from scipy.stats import stats


chat_id = 461694118



def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:
    significance_level = 0.03
    control_conversion_rate = x_success / x_cnt
    test_conversion_rate = y_success / y_cnt
    p = (x_success + y_success) / (x_cnt + y_cnt)

    SE = np.sqrt(p * (1 - p) * (1 / x_cnt + 1 / y_cnt))
    z = (test_conversion_rate - control_conversion_rate) / SE

    if z < -1 * abs(stats.norm.ppf(significance_level / 2)):
        return True
    elif z > abs(stats.norm.ppf(significance_level / 2)):
        return True
    else:
        return False
