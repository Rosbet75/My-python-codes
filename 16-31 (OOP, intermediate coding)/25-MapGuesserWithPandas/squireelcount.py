#challenge 1 create new dataframe that only contains fur color, count

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251229.csv")

print(data["Primary Fur Color"].value_counts()) #el modo chido

#el modo dificil

black_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_count  = len(data[data["Primary Fur Color"] == "Gray"])

data_dict = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count": [black_count, cinnamon_count, gray_count]
}

new_frame = pandas.DataFrame(data_dict)
print(new_frame)