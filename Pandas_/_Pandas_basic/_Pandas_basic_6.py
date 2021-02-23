import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# ############################ scattaplot 으로 그리기
plt.rc('font', family='Malgun Gothic')  # 폰트 설정
plt.rc('axes', unicode_minus=False)

df = pd.read_csv(r'C:/Users/82109/Desktop/Universtiey/2020-2/data/소상공인시장진흥공단_상가업소정보_의료기관_201909.csv', low_memory=False)

df_seoul = df[df["시도명"] == "서울특별시"].copy()

print(df_seoul)

fig1, ax1 = plt.subplots()
# hue 는 색상을 나타내는 옵션, 시군구명 의 색상을 다르게 나타낸다
sns.scatterplot(ax=ax1, data=df_seoul, x="경도", y="위도", hue="시군구명")

fig2, ax2 = plt.subplots()
# 해당 데이터만 가져온다, x, y 축이 꼭 들어가야 함, 점으로 표시된다.
df_seoul[["경도", "위도", "시군구명"]].plot.scatter(ax=ax2, x="경도", y="위도", grid=True)


fig3, ax3 = plt.subplots()
# hue 는 색상을 나타내는 옵션, 시군구명 의 색상을 다르게 나타낸다
sns.scatterplot(ax=ax3, data=df, x="경도", y="위도", hue="시도명")


plt.show()