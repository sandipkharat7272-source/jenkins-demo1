import pandas as pd

print("extract data")
data = {
    'id' :[101,102,103],
    'name' :['sandip','kishan','ritik'],
    'age':[22,21,22]
}
df = pd.DataFrame(data)
print(df)