import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# ##################데이터 색인하기

plt.rc('font', family='Malgun Gothic')  # 폰트 설정
plt.rc('axes', unicode_minus=False)

df = pd.read_csv(r'C:/Users/82109/Desktop/Universtiey/2020-2/data/소상공인시장진흥공단_상가업소정보_의료기관_201909.csv', low_memory=False)

# 상권업종중분류명 에서 약국/한약방 인 애들 boolean 으로 표시 된다
print(df["상권업종중분류명"] == "약국/한약방")

# 상권업종중분류명 에서 약국/한약방 인 애들만 출력
print(df[df["상권업종중분류명"] == "약국/한약방"])

# copy 해서 저장해야 원본에 영향을 주지 않는다
df_medical_data = df[df["상권업종중분류명"] == "약국/한약방"].copy()

# 상권업종중분류명 에서 유사의료업 인 애들만 출력
similar_medical = df["상권업종중분류명"] == "유사의료업"

# 상권업종중분류명 에서 유사의료업 인 애들 중에서 상권업종소분류명 뽑아서 unique 값 출력
print(df.loc[similar_medical, "상권업종소분류명"].value_counts())

# 상권업종중분류명 에서 유사의료업 인 애들 중에 시도명 이 서울특별시 인 애들 == 서울특별시에 있는 유사의료업 // pandas 에서는 and 대신 기호를 사용
print(df[(df["상권업종중분류명"] == "유사의료업") & (df["시도명"] == "서울특별시")])

# 데이터 프레임 형태로 만드는 것에 유의!
df_seoul_drug = df[(df["상권업종소분류명"] == "약국") & (df["시도명"] == "서울특별시")].copy()
print(df_seoul_drug["시군구명"].value_counts())

# 서울 에 약국 의 시군구명을 갯수 & 비율화 한 것
df_seoul_drug_counts = df_seoul_drug["시군구명"].value_counts()
df_seoul_drug_normalize = df_seoul_drug["시군구명"].value_counts(normalize=True)

df_seoul_hospital = df[(df["상권업종소분류명"] == "종합병원") & (df["시도명"] == "서울특별시")].copy()

# 서울 에 종합병원이라 분류 돼 있는 애들 중 상호명 에 의료기 이라는 텍스트가 들어가 있는 애들만 출력
print(df_seoul_hospital[df_seoul_hospital["상호명"].str.contains("의료기")])

# 서울 에 종합병원이라 분류 돼 있는 애들 중 상호명 에 의료기 | 꽃배달 | 상담소 | 장례식장 이라는 텍스트가 들어가 있는 애들만 출력
print(df_seoul_hospital[df_seoul_hospital["상호명"].str.contains("의료기|꽃배달|상담소|장례식장")])

# 저런 애들은 종합병원 이라 볼 수 없으니 따로 index 로 모으고 지우려면 리스트 형태로 만들어야 하니까 list 로 저장한다.
drop_elements = df_seoul_hospital[df_seoul_hospital["상호명"].str.contains("의료기|꽃배달|상담소|장례식장")].index.tolist()
print(drop_elements)

# 근데 생각해보니 의원 이라는 애들도 종합병원이라 할 수 없다 그래서 따로 만들어 준다
drop_elements2 = df_seoul_hospital[df_seoul_hospital["상호명"].str.endswith("의원")].index.tolist()

# 리스트끼리 더해준다 "drop_elements.append(drop_elements2)" 이렇게 하면 리스트 안에 리스트가 들어가서 안된다
print(drop_elements+drop_elements2)
drop_elements = drop_elements+drop_elements2

# 삭제 전
print("삭제 전 ",df_seoul_hospital.shape)

# 삭제 후 axis 는 "0" 이면 행 기준 , "1" 이면 열 기준 우리는 index 기준이니까 0
df_seoul_hospital = df_seoul_hospital.drop(drop_elements, axis=0)
print("삭제 후 ",df_seoul_hospital.shape)