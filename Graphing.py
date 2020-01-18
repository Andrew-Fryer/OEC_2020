import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df1 = pd.read_excel("./given-files/inputFile1.xlsx")
df2 = pd.read_excel("./given-files/inputFile2.xlsx")
df3 = pd.read_excel("./given-files/inputFile3.xlsx")
df4 = pd.read_csv("./given-files/test.csv")

print(df3)
print(df1.iloc[:, 2])
print(df4.loc)
for col in df4.columns:
    print(col)
df4.drop(df4.tail(1).index,inplace=True)
Total = plt.plot(df4.loc[:, 'Time'], df4.loc[:, 'Total'], label='Total')
Nuclear = plt.plot(df4.loc[:, 'Time'], df4.loc[:, 'Nuclear'], label='Nuclear')

Green = plt.plot(df4.loc[:, 'Time'], df4.loc[:, 'Green'], label='Green')
Bought = plt.plot(df4.loc[:, 'Time'], df4.loc[:, 'Neighbor'], label='Neighbor')
# ax.set_xticks(df4.loc[:, 'Time'], minor=True)A
plt.xticks(rotation=45)
plt.xlabel('Time')
plt.ylabel("MWH")
plt.legend()
plt.show()
