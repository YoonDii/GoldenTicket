# GOLDEN TICKET 🎫

> `골든티켓`은 예스24 티켓을 기반으로 한 `각종 문화공연 정보 제공 서비스` 입니다.

<br/>

<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=ffffff"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=ffffff"/>　<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=ffffff"/> <img src="https://img.shields.io/badge/javascript-yellow?style=flat-square&logo=javascript&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=ffffff"/>　<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=ffffff"/>　<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/>

<br/>

## **📅 일정**

- **2022.11.09 ~ 2022.11.21**
- 사이트 주소 : http://goldentiket.shop/
- http://kdtgoldenticketbean-env.eba-nsybrye9.ap-northeast-2.elasticbeanstalk.com/


<br />

## **🧑‍💻 개발팀**

<br />

<a href="https://github.com/YoonDii/GoldenTicket/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=YoonDii/GoldenTicket" />
</a>

<br/>
<br/>

| 이름   | 역할 |
| ------ | ---- |
| 조본희 | BE   |
| 조병진 | FE   |
| 김윤지 | FE   |
| 조수람 | BE   |
| 노은빈 | FE   |
|        |      |

---

## **🎮 주요 기능**

- **회원관리**
  - 회원가입
  - 로그인
  - **회원 프로필**
    - 회원 프로필 관리 / 수정
    - **회원간 팔로우 / 비동기 처리**
    - 찜한 상품 목록 확인
  - 로그아웃
  - 회원탈퇴

---

- **메인 페이지**

  - 전체보기
  - **배너 회전목마**
  - 랭킹 및 티저 영상
    - 장르별 TOP(1~3위) 랭킹
  - **장르 목록**
    - 목록에 마우스 올리면 사진 확대
  - UP BUTTON

- **장르 페이지**
  - 전체보기
  - **무한 스크롤**
  - **신상 / 종료순으로 정렬**
  - UP BUTTON
- **랭킹 페이지**
  - 랭킹 50위까지 좋아요 순으로 정렬
- **검색 페이지**
  - **상품 / 장르 / 장소 / 배우 이름으로 검색**
- **네브바**
  - 토글 버튼
  - 검색 기능
- **푸터**
  - 프로젝트 정보 및 팀 정보

---

- **상세 페이지**
  - 상품 제목
  - **상품 상세 정보**
    - 등급, 관람 시간, 장소, 가격 등
    - **KOPIS OPEN API**
  - **상품 좋아요 / 비동기 처리**
  - **예매하기**
    - 인터파크 상품으로 이동
  - **KAKAO MAP OPEN API**
  - **리뷰 목록 및 작성**
  - UP BUTTON
    - 지도 및 리뷰 링크 이동

---

- **리뷰 목록**
  - 리뷰 작성 시간 / 리뷰 내용 / 리뷰 평점 / 작성자 이름
  - 작성자 프로필 이동
- **리뷰 작성**
  - 리뷰 내용 / 평점 / 사진 추가
  - 모달 처리
- **리뷰 정보**
  - 리뷰 작성 시간 / 리뷰 내용 / 리뷰 평점 / 작성자 이름
  - 작성자 프로필 이동
  - 모달 처리
- **리뷰 수정 및 삭제**
  - 모달 처리

---

## **🧩 DB 설계**

![](./static/img/database.png)

<details>
<summary>접기/펼치기</summary>

![](./static/img/db-accounts.png)
![](./static/img/db-articles-01.png)
![](./static/img/db-articles-02.png)
![](./static/img/db-reviews.png)

</details>

---

## **🚀 View 설계**

![](./static/img/view-accounts.png)
![](./static/img/view-article.png)
![](./static/img/view-review.png)

---

## **🎫 서비스 소개**

<br/>

### **1. 메인 페이지**

- 메인 페이지에서는 페이지 간 이동이 자유롭게 `네비와 탑 버튼을 구성`하였습니다.
- `장르별 TOP 랭킹 / 장르별 목록을 나열`하고, `해당 공연 상세 페이지로 이동`이 가능합니다.

<br/>
<img width="100%" src="https://user-images.githubusercontent.com/108647861/203454134-5af780f5-a02f-4d51-a1cb-7cc92811c61f.gif"/>


---

<br />

### **2. 장르 페이지**

#### 2-1. `신상 / 종료순`으로 정렬

![](./static/img/service_photo/index.png)
![](./static/img/service_photo/index-end.png)

<br />

#### 2-2. `무한 스크롤`

- 스크롤을 내리면 `40개씩 공연이 노출`됩니다.

<img width="100%" src="https://user-images.githubusercontent.com/108647861/203453865-ba11e13f-cf8b-4619-8efc-7b451fd8e478.gif"/>


---

<br />

### **3. 랭킹 페이지**

- `좋아요 순으로 50위까지 랭킹을 선별` 하였습니다.
<img width="100%" src="https://user-images.githubusercontent.com/108647861/203454127-9fd29f7f-2c36-4eff-9801-76205e814e68.gif"/>


---

<br />

### **4. 검색 페이지**

- 검색은 `상품 / 장르 / 장소 / 배우 이름으로 검색이 가능`합니다.
- `추천 검색어 클릭`으로 추천 검색이 가능합니다.

<img width="100%" src="https://user-images.githubusercontent.com/108647861/203456228-f9d0ccf5-b656-4728-9d3c-0724e905dd96.gif"/>

---

<br />

### **5. 상세 페이지**

#### 5-1. 상품 정보

![](./static/img/service_photo/detail-info.png)
![](./static/img/service_photo/detail-reservation.png)

<br />

#### 5-2. 인터파크 상품으로 이동하여 예매 가능

![](./static/img/service_photo/detail-interpark.png)

#### 5-3. 상품 위치 확인

![](./static/img/service_photo/detail-map.png)

---

<br />

### **6. 리뷰 페이지**

![](./static/img/service_photo/review-index.png)

<br />

#### 6-1. 리뷰 작성

![](./static/img/service_photo/review-create.png)

<br />

#### 6-2. 리뷰 평점

![](./static/img/service_photo/review-average.png)

<br />

#### 6-3. 리뷰 목록

![](./static/img/service_photo/review-list.png)

<br />

#### 6-4. 리뷰 상세보기

![](./static/img/service_photo/review-detail.png)

<br />

#### 6-5. 리뷰 수정

![](./static/img/service_photo/review-update.png)
![](./static/img/service_photo/review-update-check.png)

---

<br />

### **7. 회원 관리**

#### 7-1. 회원 정보

- 회원 정보에서는 `회원이 찜한 공연 목록`와 `회원간 팔로우 수를 확인`할 수 있습니다.
- 찜한 공연 목록에 마우스를 올리면 ` 공연을 찜한 회원 수와 해당 공연의 리뷰 수를 확인`할 수 있습니다.
- `회원 정보 수정 및 삭제가 가능`합니다.

![](./static/img/service_photo/profile.png)
![](./static/img/service_photo/profile-option.png)

<br />

#### 7-2. 회원 간 팔로우

![](./static/img/service_photo/profile-follow.png)
![](./static/img/service_photo/profile-following.png)

---
