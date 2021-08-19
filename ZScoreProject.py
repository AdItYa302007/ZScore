import csv
import pandas as pd 
import plotly.graph_objects as go 
import plotly.figure_factory as ff 
import statistics
import random

df = pd.read_csv("ZScoreProject.csv")
data = df["reading_time"].to_list()

dataMean = statistics.mean(data)
dataStdDev = statistics.stdev(data)
print("Mean of the data is ",dataMean)
print("Standard Deviation of the data is ",dataStdDev)

def randomMean(any):
    dataSet=[]
    for i in range(0,any):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

meanlist=[]
for i in range(0,1000):
    SetOfMean = randomMean(100)
    meanlist.append(SetOfMean)

stdDev = statistics.stdev(meanlist)
mean = statistics.mean(meanlist)

firststdDevStart, firststdDevEnd = mean - stdDev, mean + stdDev
secondstdDevStart, secondstdDevEnd = mean - (2*stdDev), mean + (2*stdDev)
thirdstdDevStart, thirdstdDevEnd = mean - (3*stdDev), mean + (3*stdDev)

df = pd.read_csv("ZScoreProject.csv")
data = df["reading_time"].to_list()

meanOfSample = statistics.mean(data)
print("Mean of Sampling Distribution", meanOfSample)

fig = ff.create_distplot([meanlist],["Population Mean"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,2],mode = "lines",name = "Mean"))
fig.add_trace(go.Scatter(x=[meanOfSample, meanOfSample], y=[0,2],mode = "lines",name = "Mean of Sample"))
fig.add_trace(go.Scatter(x=[firststdDevEnd,firststdDevEnd], y=[0,2],mode = "lines",name = "Standard Deviation 1 end"))
fig.show()

zScore = (meanOfSample - mean)/stdDev
print("Z-Score:", zScore)