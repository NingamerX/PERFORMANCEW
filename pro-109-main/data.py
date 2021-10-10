import pandas as pd
import statistics

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()
mean = sum(data) / len(data)
median = statistics.median(data)
mode = statistics.mode(data)
stddev = statistics.stdev(data)

first_std_deviation_start, first_std_deviation_end = mean-stddev, mean+stddev
second_std_deviation_start, second_std_deviation_end = mean-(2*stddev), mean+(2*stddev)
third_std_deviation_start, third_std_deviation_end = mean-(3*stddev), mean+(3*stddev)

list_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(stddev))

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))