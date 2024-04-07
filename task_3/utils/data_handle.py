import os
import numpy as np


def get_voltage_data(voltages=None):
    if voltages is None:
        voltages = ['-0.45', '-0.35', '-0.25', '-0.15', '-0.05', '0', '0.15', '0.25', '0.35', '0.45']

    calibration_data = {}
    for voltage in voltages:
        calibration_data[voltage] = [[] for _ in range(8)]

        folder_path = f'DRS_data/{voltage}_volts'
        files = os.listdir(folder_path)

        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'r') as file_data:
                for line in file_data.readlines():
                    if len(line) > 10:
                        for ch in range(8):
                            calibration_data[voltage][ch].append(float(line.split(' ')[ch + 1]))

            # print(file_path)
    return calibration_data


def preparing_for_models(all_voltages: dict, channel: int):
    x_data = []
    y_data = []
    for key, value in all_voltages.items():
        x_data.append([float(key) for _ in range(len(value[0]))])
        for count in value[channel - 1]:
            y_data.append(count)

    x_arr = np.array(x_data).reshape(-1, 1)
    y_arr = np.array(y_data)

    return x_arr, y_arr


def get_whisker(all_data: dict, voltage: str, channel: int) -> list:

    whiskers = []
    for measurements_number in range(5):
        counts = 1024
        indexes = [measurements_number * counts, measurements_number * counts + counts]

        y_data = all_data[voltage][channel - 1][indexes[0]:indexes[1]]
        q1 = np.percentile(y_data, 25)
        q3 = np.percentile(y_data, 75)

        whisker_length = 1.5 * (q3 - q1)
        whiskers.append(whisker_length)

    return whiskers


if __name__ == '__main__':
    data = get_voltage_data()
    print('data_handle.py')
