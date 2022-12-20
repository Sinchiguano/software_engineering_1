import pandas as pd
data=pd.read_csv("iris_csv.csv")
#print(data.head)
#print(data.sample(10))
print(data.columns)
#print(data.shape)


print(data[10:20])

specifid_data=data[["class"]]
print(specifid_data.head(10))
#data.loc[data["class"]=="Iris-setosa"]
data.iloc[5]
print(data.loc[data["class"]=="Iris-setosa"])

print("#########################################")

counter=data["class"].value_counts()
print(counter)



min_data=data["sepallength"].min()
max_data=data["sepallength"].max()
print("Minimum:",min_data, "\nMaximum:", max_data)

print(data.isnull())
print("###########")
print(data.isnull().sum())