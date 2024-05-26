from intervals_definition import IntervalAlgebra, Interval
from task_3.utils.plots import plot_intervals


if __name__ == '__main__':
    algebra = IntervalAlgebra()

    a = Interval([15113, 15320])
    b = Interval([7384, 8120])

    all_y = []
    x = 0
    for _ in range(0, 10):
        x += 1
        all_y.append(algebra.interval_addition(b, a.multiply_on_number(x)))
    plot_intervals(all_y)

    print(all_y[0].get_width(), all_y[-1].get_width())
