import pandas as pd
import statistics
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go


df=pd.read_csv("Students.csv")
mark_list=df["math score"].tolist()

mean=statistics.mean(mark_list)

median = statistics.median(mark_list)

mode = statistics.mode(mark_list)


print("Mean, Median and Mode of math score is {}, {} and {} respectively".format(mean,median,mode))

#Standard deviation for height and weight
height_std_deviation = statistics.stdev(mark_list)
weight_std_deviation = statistics.stdev(mark_list)

first_std_deviation_start, first_std_deviation_end = mean-height_std_deviation, mean+height_std_deviation
second_std_deviation_start,second_std_deviation_end = mean-(2*height_std_deviation), mean+(2*height_std_deviation)
third_std_deviation_start,third_std_deviation_end = mean-(3*height_std_deviation), mean+(3*height_std_deviation)


list_of_data_within_1_std_deviation = [result for result in mark_list if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in mark_list if result > second_std_deviation_start and result <second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in mark_list if result > third_std_deviation_start and result < third_std_deviation_end]

#Printing data for height and weight (Standard Deviation)
print("{} % of data for math score lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(mark_list)))
print("{} % of data for math score lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(mark_list)))
print("{} % of data for math score lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(mark_list)))


fig=ff.create_distplot([mark_list],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="standard deviation 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="standard deviation 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()