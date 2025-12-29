import pandas
from pandas.core.interchange.dataframe_protocol import DataFrame

data = pandas.read_csv('weather_data.csv')
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

sum = sum(temp_list)
print(sum / len(temp_list))

print(data["temp"].mean())
print(data["temp"].max())

print(data.condition)
print(data["condition"])
print("away")
print(data.loc[data["temp"].max() == data["temp"]])
print("antoher sre")
print(data[data.temp.max() == data.temp])
print("monday things")
monday = data[data.day == "Monday"]
print(monday.temp * 1000)
print(monday)


#create dataframes from scratch

data_dict2 = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76,56,65]
}

data2 = pandas.DataFrame(data_dict2)
print(data2)
data.to_csv("./next.csv")