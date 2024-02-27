from matplotlib import pyplot


class Interval:
    def __init__(self, interval: list = None, inf=None, sup=None):
        if interval:
            self.__inf = interval[0]
            self.__sup = interval[1]
        else:
            self.__inf = inf
            self.__sup = sup

    def change_limits(self, inf_addition=None, sup_addition=None, both_change=None):
        if both_change:
            return Interval([self.__inf - both_change, self.__sup + both_change])
        else:
            return Interval([self.__inf + inf_addition, self.__sup - sup_addition])

    def multiply_on_number(self, number=None):
        if number:
            return Interval([self.__inf * number, self.__sup * number])

    def check_zero(self):
        if self.__inf <= 0 <= self.__sup:
            return True
        else:
            return False

    def get_interval(self, accuracy: int = 12, list_type=True):
        if list_type:
            return [round(self.__inf, accuracy), round(self.__sup, accuracy)]

    def get_width(self):
        return self.__sup - self.__inf


def interval_multiplication(interval_1: Interval, interval_2: Interval) -> Interval:
    interval_limits_1 = interval_1.get_interval()
    interval_limits_2 = interval_2.get_interval()

    multiplications = [elem_1 * elem_2
                       for elem_2 in interval_limits_2
                       for elem_1 in interval_limits_1]

    return Interval([min(multiplications), max(multiplications)])



def interval_subtraction(interval_1: Interval, interval_2: Interval) -> Interval:
    return Interval([interval_1.get_interval()[0] - interval_2.get_interval()[1],
                     interval_1.get_interval()[1] - interval_2.get_interval()[0]])



a = Interval([1.05, 1.05])
b = Interval([1, 1])
c = Interval([0.95, 0.95])
d = Interval([1, 1])

ans = interval_subtraction(interval_multiplication(a, d), interval_multiplication(b, c))

step = 1E-4
alpha = 0


while not ans.check_zero():
    alpha += step
    a_1 = a.change_limits(both_change=alpha)
    b_1 = b.change_limits(both_change=alpha)
    c_1 = c.change_limits(both_change=alpha)
    d_1 = d.change_limits(both_change=alpha)

    print('\nalpha = {}\n'
          'a = {}, b = {}\n'
          'c = {}, d = {}'.format(alpha,
                                  a_1.get_interval(),
                                  b_1.get_interval(),
                                  c_1.get_interval(),
                                  d_1.get_interval()))

    ans = interval_subtraction(interval_multiplication(a_1, d_1), interval_multiplication(b_1, c_1))
    print('a * d = {ad}'
          '\nc * b = {cb}'
          '\nad - cb = {ad_cb}'.format(ad=interval_multiplication(a_1, d_1).get_interval(),
                                       cb=interval_multiplication(b_1, c_1).get_interval(),
                                       ad_cb=ans.get_interval()))


else:
    print('-' * 50)
    print(alpha, ans.get_interval())

