import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics as st

df = pd.read_csv("medium_articles.csv")
list = df["claps"].tolist()

mean = st.mean(list)
std = st.stdev(list)

print(mean)
print(std)

def randommeans(counter):
    dataset = []
    for x in range(0,counter):
        randomindex = random.randint(0,len(list)-1)
        value = list[randomindex]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

listofmeans =[]
for i in range(0,1000):
    setofmeans = randommeans(100)
    listofmeans.append(setofmeans)

stdofmeans = st.stdev(listofmeans)
meanofmeans = st.mean(listofmeans)

print(stdofmeans)
print(meanofmeans)

fstdst,fstdend = meanofmeans-stdofmeans, meanofmeans + stdofmeans
sstdst,sstdend = meanofmeans-(2*stdofmeans), meanofmeans + (2*stdofmeans)
tstdst,tstdend = meanofmeans-(3*stdofmeans), meanofmeans + (3*stdofmeans)

fig = ff.create_distplot([listofmeans], ["No of Claps"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.20], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [fstdst,fstdst], y = [0,0.20], mode = "lines", name = "Stdev1 start"))
fig.add_trace(go.Scatter(x = [fstdend,fstdend], y = [0,0.20], mode = "lines", name = "Stdev1 end"))
fig.add_trace(go.Scatter(x = [sstdst,sstdst], y = [0,0.20], mode = "lines", name = "Stdev2 start"))
fig.add_trace(go.Scatter(x = [sstdend,sstdend], y = [0,0.20], mode = "lines", name = "Stdev2 end"))
fig.add_trace(go.Scatter(x = [tstdst,tstdst], y = [0,0.20], mode = "lines", name = "Stdev3 start"))
fig.add_trace(go.Scatter(x = [tstdend,tstdend], y = [0,0.20], mode = "lines", name = "Stdev3 end"))
fig.show()