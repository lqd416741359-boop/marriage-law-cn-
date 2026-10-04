"""辅助计算器：仅做情景测算，不代表法院裁判结果。"""

def contribution_ratio(a, b):
    total = a + b
    if total <= 0:
        return (0.0, 0.0)
    return (a / total, b / total)


def scenario_split(net_value, ratio_a=0.5):
    """按用户指定情景比例测算净值分配。不得将默认50/50表述为法律必然。"""
    ratio_a = max(0.0, min(1.0, ratio_a))
    return {"A": net_value * ratio_a, "B": net_value * (1 - ratio_a)}
