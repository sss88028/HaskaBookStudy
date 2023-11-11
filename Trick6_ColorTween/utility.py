from typing import List
import numpy as np

def tween_value(current: List[float], target: List[float], rate: float, minimum: float) -> (List[float], bool):
    res = []
    isEnd = True
    for curr, tgt in zip(current, target):
        diff = tgt - curr
        delta = diff * rate
        if abs(delta) < minimum:
            if abs(diff) <= minimum:
                res.append(tgt)
            else:
                delta = np.sign(delta) * minimum
                res.append(curr + delta)
                isEnd = isEnd and False
        else:
            res.append(curr + delta)
            isEnd = isEnd and False

    return res, isEnd
