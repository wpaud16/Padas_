import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
# ################## 중복 제거한 값

plt.rc('font', family='Malgun Gothic')  # 폰트 설정
plt.rc('axes', unicode_minus=False)

df= pd.read_csv(r'C:/Users/82109/Desktop/Universtiey/2020-2/data/소상공인시장진흥공단_상가업소정보_의료기관_201909.csv', low_memory=False)

# 상권업종 대분류명 에서 중복 되는 값을 출력해준다 // 값이 하나면 그 값을 출력해준다
print(df["상권업종대분류명"].unique())
print(df["상권업종중분류명"].unique())

# 상권업종 대분류명 에서 unique 한 값이 몇번 나오는지 알려준다 == len 도 사용 가능
print(df["상권업종대분류명"].nunique())
print(df["상권업종중분류명"].nunique())

# unique 값에 해당하는 데이터 갯수를 셀 수 있다
print(df["상권업종중분류명"].value_counts())

# 각각의 데이터가 차지하는 비율로 나타냄
print(df["시도명"].value_counts(normalize=True))

city = df["시도명"].value_counts()


# 가로바 형식으로 그려준다
fig1, ax1 = plt.subplots()
# ax 는 제일 마지막에 넣는 것이다
city.plot.barh(ax=ax1, figsize=(7,4), grid=True) # 크기를 크게 해서 글씨 겹침 방지
# ax1.grid()

# 색깔이 있고 좀 더 고급스러운 그림
fig1, ax2 = plt.subplots()
# y 축에 "시도명" 이름 붙고 x,y 반전해서 그려짐
sns.countplot(ax=ax2 ,data=df, y="시도명")

plt.show()