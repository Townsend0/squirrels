import pandas
a=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")["Primary Fur Color"].tolist()
b = {
    "Colors": ["Gray", "Black", "Cinnamon"],
    "Count": [0, 0, 0]
}
for c in a:
    for d in range(len(b["Colors"])):
        b["Count"][d] += 1 if c == b["Colors"][d] else 0
pandas.DataFrame(b).to_csv("Big_Data.csv")
