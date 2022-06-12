import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("癌症發生統計數據.csv", encoding="big5")

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 

fliter1 = ( (df["性別"] == "男") & (df["縣市別"] == "全國") & (df["癌症別"] == "全癌症") )
man = df[fliter1]
fliter2 = ( (df["性別"] == "女") & (df["縣市別"] == "全國") & (df["癌症別"] == "全癌症") )
woman = df[fliter2]


plt.plot(list(range(len(man))), man["平均年齡"] , "o-",label="全國男性", color='slateblue')
plt.plot(list(range(len(woman))), woman["平均年齡"] , "o-",label="全國女性", color='salmon')
plt.ylim(45, 70)
plt.xticks( list(range(len(man))), man["癌症診斷年"], rotation=45 )
plt.title('全國男性VS女性癌症發生平均年齡',fontsize=24, loc='center')
plt.xlabel('診斷年', fontsize=15)
plt.ylabel('平均年齡', fontsize=15)
plt.legend()
plt.show()