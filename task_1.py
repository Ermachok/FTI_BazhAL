from intervals_definition import Interval, IntervalAlgebra


if __name__ == '__main__':
    a = Interval([1.05, 1.05])
    b = Interval([1, 1])
    c = Interval([0.95, 0.95])
    d = Interval([1, 1])

    algebra = IntervalAlgebra()

    ans = algebra.interval_subtraction(algebra.interval_multiplication(a, d),
                                       algebra.interval_multiplication(b, c))

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
                                      a_1.get_interval(list_type=True),
                                      b_1.get_interval(list_type=True),
                                      c_1.get_interval(list_type=True),
                                      d_1.get_interval(list_type=True)))

        ans = algebra.interval_subtraction(algebra.interval_multiplication(a_1, d_1),
                                           algebra.interval_multiplication(b_1, c_1))
        print('a * d = {ad}'
              '\nc * b = {cb}'
              '\nad - cb = {ad_cb}'.format(ad=algebra.interval_multiplication(a_1, d_1).get_interval(list_type=True),
                                           cb=algebra.interval_multiplication(b_1, c_1).get_interval(list_type=True),
                                           ad_cb=ans.get_interval(list_type=True)))


    else:
        print('-' * 50)
        print(alpha, ans.get_interval(list_type=True))
