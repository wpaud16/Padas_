import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import folium as fol

# #################### Folium 으로 시각화

plt.rc('font', family='Malgun Gothic')  # 폰트 설정
plt.rc('axes', unicode_minus=False)

df = pd.read_csv(r'C:/Users/82109/Desktop/Universtiey/2020-2/data/소상공인시장진흥공단_상가업소정보_의료기관_201909.csv', low_memory=False)

df_seoul_hospital = df[(df["상권업종소분류명"] == "종합병원") & (df["시도명"] == "서울특별시")]

lat = df_seoul_hospital["위도"].mean()
log = df_seoul_hospital["경도"].mean()

# folium 은 html 로 저장해서 열어야 한다 // zoom "1" d이면 세계 지도
map = fol.Map(location=[lat, log], zoom_start=12)

for n in df_seoul_hospital.index:
    # 서울에 있는 병원 번호 에 해당하는 상호명 출력
    name = df_seoul_hospital.loc[n, "상호명"]

    # 도로명 주소
    address = df_seoul_hospital.loc[n, "도로명주소"]

    # popup 창에 띄울 이름, 도로명 주소 합침
    popup = f"병원명: {name}\n도로명 주소: {address}"

    # 인덱스에 해당하는 위도, 경도 출력
    location = [df_seoul_hospital.loc[n, "위도"], df_seoul_hospital.loc[n, "경도"]]

    # 지점 표시는 Marker 로 하는데 하나씩 하고 map 에다가 저장하는 형식
    fol.Marker(location=location, popup=popup).add_to(map)

    # map 에 저장된 애들을 html 로 저장해서 저장
    map.save('maps.html')
