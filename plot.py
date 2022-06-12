import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("癌症發生統計數據.csv", encoding="big5")

filter = ( (df["性別"]=="全") & (df["縣市別"]=="全國") & (df["癌症別"]=="全癌症") )
data = df[filter]
print(data)

plt.figure(figsize=(12, 7))
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.plot(list(range(len(data))), data["平均年齡"], "o:", color="salmon")
plt.title("1979-2019癌症發生平均年齡")
plt.xlabel("西元年")
plt.ylabel("平均年齡")
plt.xticks(list(range(len(data))) ,data["癌症診斷年"], rotation=45 )
plt.ylim(40, 70)
plt.grid(True)
plt.show()

