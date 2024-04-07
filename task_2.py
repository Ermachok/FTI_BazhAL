from task_1 import Interval, interval_multiplication, interval_subtraction, interval_division


x_1 = [Interval([0.5, 1.5]), Interval([1.5, 2.5]), Interval([-0.5, 0.5])]
x_2 = [Interval([1.5, 2.5]), Interval([-1.5, -0.5]), Interval([0.5, 1.5])]
b = [Interval([2.5, 3.75]), Interval([0.35, 1.65]), Interval([0.475, 1.625])]



print('{} * x_1 + {} * x_2 = {b}'.format(x_1[0].get_middle(), x_2[0].get_middle(), b=b[0].get_middle()))
print('{} * x_1 + {} * x_2 = {b}'.format(x_1[1].get_middle(), x_2[1].get_middle(), b=b[1].get_middle()))
print('{} * x_1 + {} * x_2 = {b}'.format(x_1[2].get_middle(), x_2[2].get_middle(), b=b[2].get_middle()))


print(interval_division(b[0], x_1[0]).get_interval(accuracy=3), interval_division(x_2[0], x_1[0]).get_interval(accuracy=3))
