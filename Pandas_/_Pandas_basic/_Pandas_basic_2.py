from matplotlib import pyplot as plt  # 데이터 시각화 라이브러리
import pandas as pd

# ####################### 결측치


plt.rc('font', family='Malgun Gothic')  # 폰트 설정
plt.rc('axes', unicode_minus=False)  # 한글 폰트를 사용하면 minus font가 깨지는 경우가 있어서 unicode_minus를 False로 설정합니다.

# low_memory = False 하면 전체 파일을 다 가져오는 것
df = pd.read_csv(r'C:/Users/82109/Desktop/Universtiey/2020-2/data/소상공인시장진흥공단_상가업소정보_의료기관_201909.csv', low_memory=False)

print(df.isnull())  # 결측치를 조사하는데 False면 값이 있음, Ture면 값이 없다.
print(df.isnull().sum())  # True==1이다. 그래서 sum을 하면 결측치가 몇개인지 알 수 있다
null_count = df.isnull().sum()  # 결측치를 변수에 저장
null_count.plot.bar(rot=30)  # 글자가 30도 돌아간다
null_count.plot.barh(figsize=(10, 10))  # barh는 x,y축을 바꿔서 표시하고 figsize는 가로 세로를 조절한다
plt.show()

print(null_count.reset_index())  # 데이터 타입으로 변환한다.
df_null_count = null_count.reset_index()  # 데이터 타입을 저장
df_null_count.columns = ['컬럼명', '결측치수']  # 컬럼명 바꾼다
print(df_null_count.sort_values(by='결측치수'))  # '결측치수'가 적은 수부터 정렬,
print(df_null_count.sort_values(by='결측치수', ascending=False))  # 역정렬
print(df_null_count.sort_values(by='결측치수', ascending=False).head(10))  # 결측치 상위 10개 출력
print(df['지점명'])  # 특정 컬럼만 불러온다. NaN== Not A Number

# 결측치 많은 놈들 제거하는 법
top_null_count = df_null_count.sort_values(by='결측치수', ascending=False).head(10)
drop_columns = top_null_count['컬럼명'].tolist()  # 제거할 놈들의 컬럼명을 리스트로 변환한다
df = df.drop(drop_columns, axis=1)  # 행 기준으로 하면 0 열을 기준으로 삭제하기 때문에 axis=1이다. 삭제한 애를 다시 df 에 저장해줘야 됨
print(df)

# 총 행, 열의 갯수 반환
print(df.shape)

# 위에 5개만 미리보기 tail은 마지막애들 볼 수 있음
print(df.head(3))

# 데이터의 요약본 열에 뭐가 있는지 보여줌 메모리, 데이터 타임, 결측치 등등을 보여준다.
print(df.info())

# 컬럼(열)명만 출력한다
print(df.columns)
