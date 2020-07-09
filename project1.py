import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("911.csv")

print(df.info())
print(df.head())

print(df["zip"].value_counts().head(5))
print(df["twp"].value_counts().head(5))
print(df["title"].nunique())

def get_reason(x):
    return x.split(":")[0]
df["Reasons"]=df["title"].apply(lambda x:get_reason(x))
print(df["Reasons"].value_counts())

sns.set_style('whitegrid')
sns.countplot(df["Reasons"])
plt.show()

print(type(df["timeStamp"].loc[0]))
print((df["timeStamp"]).dtypes)

df["timeStamp"]=pd.to_datetime(df["timeStamp"])
print(type(df["timeStamp"].loc[0]))

'''time=df["timeStamp"].iloc[26942]
print(time.hour)
print(time.day)
print(time.month)
print(time.dayofweek)
'''
df["Hour"]=df["timeStamp"].apply(lambda x:x.hour)
df["Month"]=df["timeStamp"].apply(lambda x:x.month)
df["Day of Week"]=df["timeStamp"].apply(lambda x:x.dayofweek)
df["Day of Week"]=df["Day of Week"].map({0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'})
#print(df["Day of Week"])

sns.countplot(df["Day of Week"],hue=df["Reasons"])
plt.show()
sns.countplot(df["Month"],hue=df["Reasons"])
plt.show()

print(df['Month'].value_counts())

df1=df.groupby("Month").count()
plt.plot(df1["twp"])
plt.show()

df1.reset_index(inplace=True)
print(df1.head())
sns.lmplot(y="twp",x="Month",data=df1)
plt.show()

df["Date"]=df["timeStamp"].apply(lambda x:x.date())

print(df["Date"])

df2=df.groupby("Date").count()
#print(df2)
plt.plot(df2["twp"])
plt.show()

df2=df[df["Reasons"]=="Fire"].groupby("Date").count()
plt.plot(df2["twp"])
plt.show()

df2=df[df["Reasons"]=="Traffic"].groupby("Date").count()
plt.plot(df2["twp"])
plt.show()

df2=df[df["Reasons"]=="EMS"].groupby("Date").count()
plt.plot(df2["twp"])
plt.show()

df2=df.pivot_table(index="Day of Week",columns="Hour",values="Reasons",aggfunc="count")
print(df2)

sns.heatmap(df2,linecolor="black",lw="2",cmap="coolwarm",annot=True,fmt="d")
plt.show()
sns.clustermap(df2,linecolor="black",lw="2",cmap="coolwarm",annot=True,fmt="d")
plt.show()

df2=df.pivot_table(index="Day of Week",columns="Month",values="Reasons",aggfunc="count")
print(df2)

sns.heatmap(df2,linecolor="white",lw="2",cmap="magma",annot=True,fmt="d")
plt.show()
sns.clustermap(df2,linecolor="white",lw="2",cmap="magma",annot=True,fmt="d")
plt.show()

