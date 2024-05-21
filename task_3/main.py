from task_3.utils.diff_models import model_ols, model_ridge, model_lasso
from task_3.utils.plots import plot_violin, plot_all_models, plot_single_voltage, plot_intervals
from task_3.utils.data_handle import get_voltage_data, preparing_for_models, get_single_voltage

import matplotlib.pyplot as plt
from task_3.utils.jaccard_index import made_intervals, jaccard_index


#voltages_data = get_voltage_data()




channel = 6
voltages = ['-0.45', '-0.35', '-0.25', '-0.15', '-0.05', '0', '0.05', '0.15', '0.25', '0.35', '0.45']

for voltage in voltages:
    one_voltage_data = get_single_voltage(voltage)
    figure, ax = plt.subplots(5, 1)
    for index, measure in enumerate(one_voltage_data[f'{voltage}_Volts'][channel]):
        ax[index].plot([i for i in range(len(measure))], measure, 'o')
        ax[index].set_xlim(0, 1024)
    plt.show()

    max_difference = []
    for measure in range(1024):
        measure_values = [one_voltage_data[f'{voltage}_Volts'][channel][file_num][measure] for file_num in range(5)]
        max_difference.append(max(measure_values) - min(measure_values))
    plt.title(f'{voltage} Volts, {channel} channel')
    plt.plot([i for i in range(1024)], max_difference, 'o')
    plt.show()

#intervals = made_intervals(voltages_data[voltage][channel], radius_percent=10)
#print(jaccard_index(intervals))


#plot_intervals(intervals)
#
# plot_indicator = False
# if plot_indicator:
#     # plot_violin(voltages_data, channel=channel)
#     plot_single_voltage(voltages_data, voltage=voltage, channel=channel)
#
#     x_arr, y_arr = preparing_for_models(voltages_data, channel=channel)
#     x_extend, y_ols = model_ols(x_arr, y_arr)
#     _, y_ridge = model_ridge(x_arr, y_arr)
#     _, y_lasso = model_lasso(x_arr, y_arr)
#
#     plot_all_models(x_arr, y_arr,
#                     y_lasso=y_lasso,
#                     y_ridge=y_ridge,
#                     y_ols=y_ols,
#                     x_extend=x_extend)
