import matplotlib.pyplot as plt
import statistics


from task_3.utils.diff_models import model_ols, model_ridge, model_lasso
from task_3.utils.plots import plot_violin, plot_all_models, plot_single_voltage, plot_intervals, plot_Qplot
from task_3.utils.data_handle import get_voltage_data, preparing_for_models, get_single_voltage

from task_3.utils.jaccard_index import made_intervals, jaccard_index


voltages_data = get_voltage_data()


channel = 7
voltages = ['-0.45', '-0.35', '-0.25', '-0.15', '-0.05', '0', '0.05', '0.15', '0.25', '0.35', '0.45']

# for voltage in voltages:
#     one_voltage_data = get_single_voltage(voltage)
#     figure, ax = plt.subplots(6, 1)
#     for index, measure in enumerate(one_voltage_data[f'{voltage}_Volts'][channel]):
#         ax[index].plot([i for i in range(len(measure))], measure, '.')
#         ax[index].set_xlim(0, 1024)
#         ax[index].get_xaxis().set_visible(False)
#
#     ax[0].set_title(f'{voltage} Volts, {channel} channel')
#
#
#     max_difference = []
#     for measure in range(1024):
#         measure_values = [one_voltage_data[f'{voltage}_Volts'][channel][file_num][measure] for file_num in range(5)]
#         max_difference.append(max(measure_values) - min(measure_values))
#
#     percent_above = 0.95
#     percent_95 = sorted(max_difference)[int(1024*percent_above)]
#     #print(percent_95)
#     ax[5].set_xlim(0, 1024)
#     ax[5].plot([i for i in range(1024)], max_difference, '.', color='red')
#     #plt.show()


voltage = '-0.45'
one_voltage_data = get_single_voltage(voltage)

max_difference = []
percent_above = 0.95
jaccards = []
for measure in range(1024):

    measure_values = [one_voltage_data[f'{voltage}_Volts'][channel][file_num][measure] for file_num in range(5)]
    intervals = made_intervals(measure_values, radius_counts=60)

    jaccards.append(jaccard_index(intervals))

    #plot_intervals(intervals)
#print(statistics.median(jaccards))
#plt.plot([i for i in range(1024)], jaccards)
#plt.hist(jaccards, bins=40, edgecolor='black')
#plt.show()


plot_indicator = True
if plot_indicator:
    plot_violin(voltages_data, channel=channel)
    plot_single_voltage(voltages_data, voltage=voltage, channel=channel)

    x_arr, y_arr = preparing_for_models(voltages_data, channel=channel)
    x_extend, y_ols = model_ols(x_arr, y_arr)
    _, y_ridge = model_ridge(x_arr, y_arr)
    _, y_lasso = model_lasso(x_arr, y_arr)

    plot_all_models(x_arr, y_arr,
                    y_lasso=y_lasso,
                    y_ridge=y_ridge,
                    y_ols=y_ols,
                    x_extend=x_extend)
