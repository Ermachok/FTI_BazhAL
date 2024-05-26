from intervals_definition import IntervalAlgebra, Interval
import statistics


def made_intervals(voltage_list: list, radius_percent: float = None, radius_counts: int = None) -> list[Interval]:

    if not radius_percent:
        radius = radius_counts
    else:
        radius = statistics.mean(voltage_list) * radius_percent / 100

    result: list[Interval] = []
    for measurement in voltage_list:
        result.append(Interval(mid=measurement, rad=radius))

    return result


def jaccard_index(interval_list: list[Interval]) -> float:

    all_inf = []
    all_sup = []

    for interval in interval_list:
        inf, sup = interval.get_interval(set_type=True)
        all_inf.append(inf)
        all_sup.append(sup)

    jaccard = (min(all_sup) - max(all_inf)) / (max(all_sup) - min(all_inf))

    return jaccard


if __name__ == '__main__':
    print('jaccard_index.py worked')