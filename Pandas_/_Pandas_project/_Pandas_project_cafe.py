import pandas as pd
from folium.plugins import MarkerCluster # 가까운 애들 하나로 표시하고 확대하면 나눠짐
import folium as fol

# plt.rc('font', family='Malgun Gothic')  # 폰트 설정
# plt.rc('axes', unicode_minus=False)

# 파일 인코딩 주의
df = pd.read_csv(r'C:/Users/82109/Desktop/Universtiey/2020-2/data/소상공인시장진흥공단_상가(상권)정보_강원.csv', encoding='cp949',
                 low_memory=False)

df_chun_cafe = df[(df["시군구명"] == "춘천시") & (df["상권업종소분류명"] == "커피전문점/카페/다방")]

# 위도
min_latitude = 37.841903
max_latitude = 37.901475

# 경도
min_longitude = 127.700890
max_longitude = 127.793560

# 지정한 위도, 경도 에 들어오지 않는 애들은 삭제한다.
for n in df_chun_cafe.index:
    if (min_latitude <= (df_chun_cafe.loc[n, "위도"]) <= max_latitude) & (
            min_longitude <= (df_chun_cafe.loc[n, "경도"]) <= max_longitude):
        pass
    else:
        df_chun_cafe = df_chun_cafe.drop([n], axis=0)

latitude = df_chun_cafe["위도"].mean()
longitude = df_chun_cafe["경도"].mean()

m = fol.Map(location=[latitude, longitude], zoom_start=14, max_zoom=19) ##.choropleth(max_zoom=True)

# 가까운 애들 하나로 표시하고 확대하면 나눠짐
marker_cluster = MarkerCluster().add_to(m)

for n in df_chun_cafe.index:
    name = df_chun_cafe.loc[n, "상호명"]
    address = df_chun_cafe.loc[n, "도로명주소"]
    location = [df_chun_cafe.loc[n, "위도"], df_chun_cafe.loc[n, "경도"]]

    popup_text = f"{name}\n{address}"
    iframe = fol.IFrame(popup_text, width=250, height=60)
    popup = fol.Popup(iframe)

    fol.Marker(location=location, popup=popup, tooltip=name).add_to(marker_cluster)
    m.save("Cafe-2.html")
