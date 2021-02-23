import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

# ###################### 카테고리형 데이터(스트링) 과 수치형 데이터 는 다루는 법이 다르다

plt.rc('font', family='Malgun Gothic')  # 폰트 설정
plt.rc('axes', unicode_minus=False)

df = pd.read_csv(r"C:\Users\82109\Desktop\Universtiey\2020-2\data\NHIS_OPEN_GJ_2017_v1.1.csv", encoding="cp949", low_memory=False)

# 성별코드 에 따라 가입자일련번호 를 셈
# df.groupby(["성별코드"])["가입자일련번호"].count()

# 성별코드와 음주여부 에 따른 가입자일련번호 의 갯수를 셈
# df.groupby(["성별코드","음주여부"])["가입자일련번호"].count()

# index 기준으로 values 는 컬럼으로 기능은 count 한다
# print(df.pivot_table(index="성별코드", values=["음주여부","가입자일련번호"], aggfunc=["count","mean"]))

# agg 를 사용하면 원하는 수치를 한번에 볼 수 있다
print(df.groupby(["성별코드","음주여부"])["가입자일련번호"].agg(["count","mean"]))

# 샘플 1000개만 가져온다. random_state 는 변환하지 않고 고정값을 가져온다.
df_sample = df.sample(1000, random_state=1)

# 성별 에 따라 음주여부 를 표시한다
fig, ax = plt.subplots()
sns.countplot(ax=ax, data=df_sample, x="음주여부", hue="성별코드")

# 연령대 별 음주여부 를 표시
fig, ax1 = plt.subplots()
sns.countplot(ax=ax1, data=df, x="연령대코드(5세단위)", hue="음주여부")

# fig, ax1 = plt.subplots()
# 슬라이싱을 이용해 12개(0-11) 의 컬럼을 히스토그램으로 출력, bins 는 막대의 갯수를 제어한다.
# df.iloc[:, :12].hist(ax=ax1, figsize=(12,12), bins=100)

plt.show()