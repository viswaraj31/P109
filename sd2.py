import csv
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

data = df["writing score"].tolist()

mean = statistics.mean(data)
sd = statistics.stdev(data)

sd1s,sd1e = mean-sd,mean+sd
sd2s,sd2e = mean-2*sd,mean+2*sd
sd3s,sd3e = mean-3*sd,mean+3*sd

fig = ff.create_distplot([data],["Chemistry & Social"],show_hist = False)
fig.add_trace(go.Scatter(x = [sd1s,sd1s], y = [0,0.17],mode="lines",name = "-std1"))
fig.add_trace(go.Scatter(x = [sd1e,sd1e], y = [0,0.17],mode="lines",name = "+std1"))

fig.add_trace(go.Scatter(x = [sd2s,sd2s], y = [0,0.17],mode="lines",name = "-std2"))
fig.add_trace(go.Scatter(x = [sd2e,sd2e], y = [0,0.17],mode="lines",name = "+std2"))
fig.show()

liststd1 = [result for result in data if result>sd1s and result<sd1e]
liststd2 = [result for result in data if result>sd2s and result<sd2e]
liststd3 = [result for result in data if result>sd3s and result<sd3e]

print("Mean : ",mean)
print("standard deviation : ",sd)

print("{}% of data lies within 1 standard deviation".format(len(liststd1)*100.0 / len(data)))
print("{}% of data lies within 2 standard deviation".format(len(liststd2)*100.0 / len(data)))
print("{}% of data lies within 3 standard deviation".format(len(liststd3)*100.0 / len(data)))