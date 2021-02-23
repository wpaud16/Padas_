import pandas as pd

# 데이터 프레임 만듦
df=pd.DataFrame({'a':[4,5,6],
                 'b':[7,8,9],
                 'c':[10,11,12]},
                index=[1,2,3])
# 행렬로 나온다
print(df)

# 인덱스 & 'a' 열에 해당하는 값만 나옴
print(df['a'])

# 인덱스 & 'a' 열 column이랑 값 나옴
print(df[['a']])

# boolean 값으로 반환 df['a'] & df[['a']] 도 가능
print(df > 4)

# 2개의 열을 가져올 수도 있음
print(df[['a','b']])

# 카운트도 가능
print(df['a'].value_counts())

# 값 기준으로 정렬함
print(df['a'].sort_values())

# 'a'를 기준으로 정렬함 ascending=False 는 역순임
print(df.sort_values('a'))

#  1행을 날려버림
print(df.drop(1))

# 'c' 'b' 에 해당하는 열 축을 날림 axis=0 은 행을 기준임
print(df.drop(['c', 'b'], axis=1))

