class Interval:
    def __init__(self, interval: list = None,
                 inf: float = None, sup: float = None,
                 mid: float = None, rad: float = None):
        if interval:
            self.__inf = interval[0]
            self.__sup = interval[1]
        elif mid and rad:
            self.__inf = mid + rad
            self.__sup = mid - rad
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

    def get_interval(self, accuracy: int = 12, list_type: bool = None, set_type: bool = None):
        if list_type:
            return [round(self.__inf, accuracy), round(self.__sup, accuracy)]
        elif set_type:
            return self.__inf, self.__sup
        else:
            raise Exception

    def get_middle(self):
        return round(self.__inf + (self.__sup - self.__inf) / 2, 5)

    def get_width(self):
        return self.__sup - self.__inf


class IntervalAlgebra:
    @staticmethod
    def interval_multiplication(interval_1: Interval, interval_2: Interval) -> Interval:
        interval_limits_1 = interval_1.get_interval()
        interval_limits_2 = interval_2.get_interval()

        multiplications = [elem_1 * elem_2
                           for elem_2 in interval_limits_2
                           for elem_1 in interval_limits_1]

        return Interval([min(multiplications), max(multiplications)])

    @staticmethod
    def interval_subtraction(interval_1: Interval, interval_2: Interval) -> Interval:
        return Interval([interval_1.get_interval()[0] - interval_2.get_interval()[1],
                         interval_1.get_interval()[1] - interval_2.get_interval()[0]])

    @staticmethod
    def interval_division(interval_1: Interval, interval_2: Interval) -> Interval:
        interval_limits_1 = interval_1.get_interval()
        interval_limits_2 = interval_2.get_interval()

        divisions = [elem_1 / elem_2
                     for elem_2 in interval_limits_2
                     for elem_1 in interval_limits_1]

        return Interval([min(divisions), max(divisions)])

