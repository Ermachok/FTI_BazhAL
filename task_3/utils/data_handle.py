import os
import numpy as np


def get_voltage_data(voltages=None):
    if voltages is None:
        voltages = ['-0.45', '-0.35', '-0.25', '-0.15', '-0.05', '0', '0.05', '0.15', '0.25', '0.35', '0.45']

    calibration_data = {}
    for voltage in voltages:
        drs_channels_number = 8
        calibration_data[voltage] = [[] for _ in range(drs_channels_number)]
        folder_path = f'DRS_data/{voltage}_volts'
        files = os.listdir(folder_path)
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as file_data:
                for line in file_data.readlines():
                    if len(line) > 10:  # check not empty or strange line?
                        for ch in range(drs_channels_number):
                            calibration_data[voltage][ch].append(float(line.split(' ')[ch + 1]))

    return calibration_data



def get_single_voltage(voltage) -> dict:
    calibration_data = {}
    drs_channels_number = 8
    adc_counts = 1024
    calibration_data[f'{voltage}_Volts'] = {ch+1: [] for ch in range(drs_channels_number)}
    folder_path = f'DRS_data/{voltage}_volts'
    files = os.listdir(folder_path)
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        stop_point = stop_point_determination(file_name)
        with open(file_path, 'r') as file_data:
            voltage_data = file_data.readlines()
            for ch in range(drs_channels_number):
                ch_data = []
                for line in voltage_data:
                    if len(line) > 10:  # check not empty or strange line ?
                        ch_data.append(float(line.split(' ')[ch+1]))
                right_order_data = ch_data[adc_counts - stop_point:] + ch_data[:adc_counts - stop_point]
                #right_order_data = ch_data

                calibration_data[f'{voltage}_Volts'][ch+1].append(right_order_data)
    return calibration_data


def stop_point_determination(file_name: str) -> int:
    pattern = 'sp'
    pattern_index = file_name.index(pattern)
    stop_point = ''
    for sym in file_name[pattern_index + len(pattern):]:
        if sym.isdigit():
            stop_point += sym

    return int(stop_point)




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


def get_whisker_data(y_data: list) -> tuple:
    # TODO change 5120 to the number of measured points (5120 = 1024 * 5)
    voltages = ['-0.45', '-0.35', '-0.25', '-0.15', '-0.05', '0', '0.05', '0.15', '0.25', '0.35', '0.45']
    x_data = [float(vol) for vol in voltages]
    all_q1 = []
    all_q3 = []
    whiskers = []
    for j in range(len(x_data)):
        q1 = np.percentile(y_data[5120 * j:5120 * (j + 1)], 25)
        q3 = np.percentile(y_data[5120 * j:5120 * (j + 1)], 75)
        whisker_length = 1.5 * (q3 - q1)

        all_q1.append(q1)
        all_q3.append(q3)
        whiskers.append(whisker_length)

    return x_data, all_q1, all_q3, whiskers


if __name__ == '__main__':
    data = get_voltage_data()
    print('data_handle.py')
