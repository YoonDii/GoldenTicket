import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from articles.models import PlayDetail, LocationDetail

#################################################
# 필수 값
#################################################

# .env 파일의 api 불러옴
load_dotenv()
API_SECRET_KEY = os.environ.get("API_SECRET_KEY")

# 공연 시작일자
stdate = "&stdate=" + "20221115"
# 공연 종료일자
eddate = "&eddate=" + "20230630"
# 현재페이지
cpage = "&cpage=" + "2"
# 페이지당 목록 수
rows = "&rows=" + "1309"


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


def get_playIds_list():
    URL = (
        "http://www.kopis.or.kr/openApi/restful/pblprfr?service="
        + API_SECRET_KEY
        + stdate
        + eddate
        + cpage
        + rows
    )

    print(URL)

    response = requests.get(URL)
    # print(URL)
    # print(response.status_code)

    soup = BeautifulSoup(response.text, "xml")  # xml 문서라서
    playIds = soup.find_all("mt20id")  # mt20id : 목록 태그

    playIds_list = []
    for id in playIds:

        playIds_list.append(id.get_text())

    return playIds_list


def get_play_info():
    for playId in get_playIds_list():

        URL = (
            "http://www.kopis.or.kr/openApi/restful/pblprfr/"
            + playId
            + "?service="
            + API_SECRET_KEY
        )
        response = requests.get(URL)

        print(URL)
        soup = BeautifulSoup(response.text, "xml")
        _playid = soup.find("mt20id").get_text()
        _playname = soup.find("prfnm").get_text()
        _genrename = soup.find("genrenm").get_text()
        _playstate = soup.find("prfstate").get_text()
        _playstdate = soup.find("prfpdfrom").get_text()
        _playenddate = soup.find("prfpdto").get_text()
        _poster = soup.find("poster").get_text()
        _locationname = soup.find("fcltynm").get_text()
        _playcast = soup.find("prfcast").get_text()
        _runtime = soup.find("prfruntime").get_text()
        _age = soup.find("prfage").get_text()
        _locationid = soup.find("mt10id").get_text()
        d1 = date(int(_playstdate[0:4]), int(_playstdate[5:7]), int(_playstdate[8:]))
        d2 = date(int(_playenddate[0:4]), int(_playenddate[5:7]), int(_playenddate[8:]))
        # print(d1, d2, type(d1), type(d2))
        _image = soup.find_all("styurl")
        _image1 = None
        _image2 = None
        _image3 = None
        _image4 = None
        if len(_image) == 1:
            _image1 = _image[0].get_text()
        elif len(_image) == 2:
            _image1 = _image[0].get_text()
            _image2 = _image[1].get_text()
        elif len(_image) == 3:
            _image1 = _image[0].get_text()
            _image2 = _image[1].get_text()
            _image3 = _image[2].get_text()
        elif len(_image) == 4:
            _image1 = _image[0].get_text()
            _image2 = _image[1].get_text()
            _image3 = _image[2].get_text()
            _image4 = _image[3].get_text()
        # print(_image, len(_image))

        _ticketprice = soup.find("pcseguidance").get_text()
        _summary = soup.find("sty").get_text()
        _guidance = soup.find("dtguidance").get_text()

        play = PlayDetail(
            playid=_playid,
            playname=_playname,
            genrename=_genrename,
            playstate=_playstate,
            playstdate=d1,
            playenddate=d2,
            poster=_poster,
            locationname=_locationname,
            playcast=_playcast,
            runtime=_runtime,
            age=_age,
            locationid=_locationid,
            image1=_image1,
            image2=_image2,
            image3=_image3,
            image4=_image4,
            ticketprice=_ticketprice,
            summary=_summary,
            guidance=_guidance,
        )
        play.save()

        # playimage = PlayImage(
        #     image=_image,
        # )
        # playimage.playid = play.playid
        # playimage.save()


get_play_info()
