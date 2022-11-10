import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from articles.models import PlayDetail, LocationDetail

#################################################
# 필수 값
#################################################

# .env 파일의 api 불러옴
load_dotenv()
API_SECRET_KEY = os.environ.get("API_SECRET_KEY")

# 현재페이지
cpage = "&cpage=" + "5"
# 페이지당 목록 수
rows = "&rows=" + "500"


#################################################
# 선택 값
#################################################
# 공연 상태 코드
prfstate = "&prfstate=" + "02"
# 지역코드 (시도)
signgucode = "&signgucode=" + "11"
# 지역코드 (구군)
signgucodesub = "&signgucodesub=" + "1111"
# 아동공연여부
kidstate = "&kidstate" + "Y"


def get_locationIds_list():
    URL = (
        "http://www.kopis.or.kr/openApi/restful/prfplc?service="
        + API_SECRET_KEY
        + cpage
        + rows
    )

    print(URL)

    response = requests.get(URL)
    # print(URL)
    # print(response.status_code)

    soup = BeautifulSoup(response.text, "xml")  # xml 문서라서
    locationIds = soup.find_all("mt10id")  # mt10id : 목록 태그

    locationIds_list = []
    for id in locationIds:

        locationIds_list.append(id.get_text())

    return locationIds_list


def get_location_info():
    for locationId in get_locationIds_list():

        URL = (
            "http://www.kopis.or.kr/openApi/restful/prfplc/"
            + locationId
            + "?service="
            + API_SECRET_KEY
        )
        response = requests.get(URL)

        print(URL)
        soup = BeautifulSoup(response.text, "xml")
        _locationid = soup.find("mt10id").get_text()
        _locationname = soup.find("fcltynm").get_text()
        _address = soup.find("adres").get_text()
        _phone = soup.find("telno").get_text()
        _relateurl = soup.find("relateurl").get_text()
        _lat = soup.find("la").get_text()
        _lgt = soup.find("lo").get_text()

        location = LocationDetail(
            locationid=_locationid,
            locationname=_locationname,
            address=_address,
            phone=_phone,
            relateurl=_relateurl,
            lat=_lat,
            lgt=_lgt,
        )
        location.save()


get_location_info()
