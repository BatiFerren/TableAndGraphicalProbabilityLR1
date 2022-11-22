import csv
import math

import matplotlib
import numpy as np
import matplotlib.pyplot as plt


def create_input_list(filename):
    data_str_list = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            for item in row:
                data_str_list.append(item.strip())
    data_list = [int(item) for item in data_str_list]
    return data_list


def count_failure_in_interval(intervals, main_list):
    begin = 0
    list_counters = []
    for i in intervals:
        end = i
        counter = 0
        for item in main_list:
            if begin < item <= end:
                counter += 1
        list_counters.append(counter)
        begin = i
    return list_counters


def calculate_probability_failures(densities, intervals):
    n = densities.__len__() + 1
    inter_probability_failures = []
    for i in range(n):
        sum_densities = sum(densities[:i])
        inter_probability_failures.append(sum_densities*intervals[0])
    probability_failures = inter_probability_failures[1:]
    return probability_failures


def main():
    dest_file = '2.csv'
    input_list = create_input_list(dest_file)
    print(input_list)
    sorted_input_list = sorted(input_list)
    print(sorted_input_list)
    interval = round((sorted_input_list[-1] - sorted_input_list[0]) / (1 + 3.3 * math.log10(sorted_input_list.__len__())))
    print(interval)
    half_interval = interval/2
    print(half_interval)
    number_of_intervals = math.ceil(sorted_input_list[-1] / interval)
    print(number_of_intervals)
    list_intervals = [interval * i for i in range(1, number_of_intervals + 1)]
    print(list_intervals)
    average_interval = [item-half_interval for item in list_intervals]
    print(average_interval)
    counter_failures = count_failure_in_interval(list_intervals, sorted_input_list)
    print(counter_failures)
    failure_density = [item/input_list.__len__() for item in counter_failures]
    print(failure_density)
    average_statistic_failure_density = [item/list_intervals[0] for item in failure_density]
    print(average_statistic_failure_density)
    probability_failures = calculate_probability_failures(average_statistic_failure_density, list_intervals)
    print(probability_failures)
    probability_without_failures = [1-item for item in probability_failures]
    print(probability_without_failures)

    x1 = np.array(average_interval)
    y1 = np.array(failure_density)
    plt.subplot(2,2,1)
    plt.plot(x1, y1, '-o')
    plt.grid()

    x2 = np.array(average_interval)
    y2 = np.array(average_statistic_failure_density)
    plt.subplot(2, 2, 2)
    plt.plot(x2, y2, '-o')
    plt.grid()

    x3 = np.array(average_interval)
    y3 = np.array(probability_failures)
    plt.subplot(2, 1, 2)
    plt.plot(x3, y3, '-o')

    x4 = np.array(average_interval)
    y4 = np.array(probability_without_failures)
    plt.subplot(2, 1, 2)
    plt.plot(x4, y4, '--o')
    plt.grid()

    plt.show()


if __name__ == '__main__':
    main()


