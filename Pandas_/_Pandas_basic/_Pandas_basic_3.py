from matplotlib import pyplot as plt  # 데이터 시각화 라이브러리
import pandas as pd

# ################## 기초 통계량

plt.rc('font', family='Malgun Gothic')  # 폰트 설정
plt.rc('axes', unicode_minus=False)  # 한글 폰트를 사용하면 minus font가 깨지는 경우가 있어서 unicode_minus를 False로 설정합니다.

# low_memory = False 하면 전체 파일을 다 가져오는 것
df = pd.read_csv(r'C:/Users/82109/Desktop/Universtiey/2020-2/data/소상공인시장진흥공단_상가업소정보_의료기관_201909.csv', low_memory=False)

# 위도에 대한 평균값
print(df["위도"].mean())

# 위도의 중앙값
print(df["위도"].median())

# 위도 최댓값
print(df["위도"].max())

# 위도 최솟값
print(df["위도"].min())

# 위도 갯수 비어있는 값은 제외
print(df["위도"].count())

# 위에서 한 모든 값 + 사분위수까지 다 구해줌
print(df["위도"].describe())

# 두개의 컬럼을 비교해주는데 파이썬에서는 두 개 이상의 자료를 가져올 떈, list 형태로 가져와야 한다
print(df[["위도","경도"]].describe())

# 모든 수치형 데이터를 요약함 // 결측치는 제외하고 보여준다
print(df.describe())

# 모든 문자형 데이터를 요약함 // top 은 가장 많이 등장한 object freq 은 top 에 대한 빈도수 // unique 는 중복되는 애들이 몇개 인지 알려주는 것
print(df.describe(include="object"))