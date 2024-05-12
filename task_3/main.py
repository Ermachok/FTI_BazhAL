from task_3.utils.diff_models import model_ols, model_ridge, model_lasso
from task_3.utils.plots import plot_violin, plot_all_models, plot_single_voltage, plot_intervals
from task_3.utils.data_handle import get_voltage_data, preparing_for_models

from task_3.utils.jaccard_index import made_intervals, jaccard_index

voltages_data = get_voltage_data()

voltage = '0'
channel = 1

intervals = made_intervals(voltages_data['-0.45'][channel], radius_percent=40)
print(jaccard_index(intervals))


#plot_intervals(intervals)

plot_indicator = False
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
