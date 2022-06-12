import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("癌症發生統計數據.csv", encoding="big5")
# print(df)

filter = ( (df["癌症診斷年"]==2019) & (df["性別"]=="全") & (df["縣市別"]=="全國") )
data = df[filter]
data = data.sort_values(by=["平均年齡"])
print(data)

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.bar( data["癌症別"], data["平均年齡"] )
plt.title("2019各癌症發生平均年齡")
plt.xlabel("癌症種類")
plt.ylabel("平均年齡")
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.5)
plt.show()