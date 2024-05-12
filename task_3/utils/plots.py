import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

from intervals_definition import IntervalAlgebra, Interval
from task_3.utils.data_handle import get_whisker_data


def plot_single_voltage(all_data: dict, voltage: str, channel: int) -> None:
    """
    Plot of measurements for chosen voltage
    :param all_data: all data from measurements, dict: keys - voltages, values =[0,8], len(value) = 5120 (1024 * 5)
    :param voltage: key for dict
    :param channel: channel number (from 0 to 8)
    :return: Non
    """
    fig, axs = plt.subplots(6, 1, figsize=(8, 8), sharex=True)
    for measurements_number in range(5):   # exist 5 files with measurements
        counts = 1024
        indexes = [measurements_number * counts, measurements_number * counts + counts]

        x_data = [measurements_number for _ in range(counts)]
        y_data = all_data[voltage][channel-1][indexes[0]:indexes[1]]

        scatter_data = axs[0].scatter(y_data, x_data, s=2)
        axs[measurements_number + 1].hist(y_data, bins=50, color=scatter_data.get_facecolor()[0], edgecolor='black')

    axs[0].set_ylim(-0.2, 4.2)
    axs[0].set_yticks([x for x in range(0, 5)])
    axs[0].set_ylabel('Measure number')

    plt.tight_layout()
    plt.title(f'Voltage {voltage}, channel {channel+1}')
    plt.xlim(min(all_data[voltage][channel-1]) * 0.99,
             max(all_data[voltage][channel-1]) * 1.01)
    plt.show()


def plot_violin(all_data: dict, channel: int):
    """
    Plots violin plot
    :param all_data:
    :param channel:
    :return: none
    """
    for key, value in all_data.items():
        data = {'Voltage': [float(key) for _ in range(len(value[channel - 1]))], 'Counts': value[channel - 1]}
        df = pd.DataFrame(data)

        sns.violinplot(x='Voltage', y='Counts', data=df, inner='box', fill=False)

    plt.title(f'Channel {channel}')
    plt.grid()
    plt.show()


def plot_all_models(x_arr, y_arr, x_extend=None, y_ols=None, y_ridge=None, y_lasso=None) -> None:
    """
    :param x_arr: initial voltages
    :param y_arr: initial measurements
    :param x_extend: extended V
    :param y_ols: data from ordinary least square
    :param y_ridge: ridge opt.. data
    :param y_lasso: lasso opt.. data
    :return: shows plot
    """

    df = pd.DataFrame({'x': x_arr[0], 'y': y_arr[0]})

    x_whiskers, q1, q3, whiskers = get_whisker_data(y_arr)

    q1 = np.array(q1)
    q3 = np.array(q3)
    whiskers = np.array(whiskers)

    # TODO CHECK  DATA AVAILABILITY
    plt.plot(x_extend, y_ridge, color='red', label='Fit (Ridge)')
    plt.plot(x_extend, y_ols, color='blue', label='Fit (OLS)')
    plt.plot(x_extend, y_lasso, color='green', label='Fit (Lasso)')
    plt.scatter(x_arr, y_arr, s=2, zorder=5)

    sns.lineplot(data=df, x='x', y='y')

    plt.fill_between(x_whiskers, q3 + whiskers, q1 - whiskers)


    plt.xlim(-0.5, 0.5)
    plt.ylim(0, 16E3)
    plt.legend()
    plt.grid()
    plt.show()



def plot_intervals(interval_list: list[Interval]):
    for index, interval in enumerate(interval_list):
        plt.plot([index, index], interval.get_interval())

    plt.show()


if __name__ == '__main__':
    print('plots.py')
