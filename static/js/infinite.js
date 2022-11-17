function YesScroll() {
  const pagination = document.querySelector('.pagination'); // 페이지네이션 정보획득
  const fullContent = document.querySelector('.infinite'); // 전체를 둘러싼 컨텐츠 정보획득
  const fullContentOld = document.querySelector('.infinite-old');
  const nextLink = pagination.querySelector('.nextPage');
  const nextURL = nextLink.getAttribute('href');
  const totalPage = document.querySelector('.totalpagenum');
  const isNewOn = document.querySelector('#tag-new');
  const isOldOn = document.querySelector('#tag-old');
  const screenHeight = screen.height; // 화면 크기
  let oneTime = false; // 일회용 글로벌 변수
  document.addEventListener('scroll', OnScroll, { passive: true }) // 스크롤 이벤트함수정의
  function OnScroll() { //스크롤 이벤트 함수
    const fullHeight = fullContent.clientHeight; // infinite 클래스의 높이   
    const scrollPosition = scrollY; // 스크롤 위치
    if (fullHeight - screenHeight / 2 <= scrollPosition && !oneTime && isNewOn.classList.contains('on')) { // 만약 전체높이-화면높이/2가 스크롤포지션보다 작아진다면, 그리고 oneTime 변수가 거짓이라면
      console.log(isNewOn.classList.contains('on'))
      console.log("됨")
      oneTime = true; // oneTime 변수를 true로 변경해주고,
      madeBox(); // 컨텐츠를 추가하는 함수를 불러온다.
    }
    const fullHeightOld = fullContentOld.clientHeight;
    if (fullHeightOld - screenHeight / 2 <= scrollPosition && !oneTime && isOldOn.classList.contains('on')) { // 만약 전체높이-화면높이/2가 스크롤포지션보다 작아진다면, 그리고 oneTime 변수가 거짓이라면
      console.log("됨2")
      oneTime = true; // oneTime 변수를 true로 변경해주고,
      madeBoxOld(); // 컨텐츠를 추가하는 함수를 불러온다.
    }
  }
  var pagenum = 2
  function madeBox() {
    const URL = nextURL.replace('&page=2', '&page=' + pagenum)
    axios.get(URL)
      .then(function (response) {
        const parser = new DOMParser;
        const doc = parser.parseFromString(response.data, "text/html");
        const infInput = doc.querySelector('.inflist');
        const totalPageNum = totalPage.textContent
        fullContent.appendChild(infInput);
        console.log(URL);
        console.log(totalPageNum)
        if (pagenum >= totalPageNum) {
          document.removeEventListener('scroll', OnScroll, { passive: true });
        }
        pagenum++;
        oneTime = false;
      })
      .catch(function (error) {
        console.log(error)
      })
  }
  function madeBoxOld() {
    const URLOld = nextURL.replace('&page=2', '&page=' + pagenum)
    axios.get(URLOld)
      .then(function (response) {
        const parserOld = new DOMParser;
        const docOld = parserOld.parseFromString(response.data, "text/html");
        const infInputOld = docOld.querySelector('.inflist-old');
        const totalPageNum = totalPage.textContent
        fullContentOld.appendChild(infInputOld);
        console.log(URLOld);
        console.log(totalPageNum)
        if (pagenum >= totalPageNum) {
          document.removeEventListener('scroll', OnScroll, { passive: true });
        }
        pagenum++;
        oneTime = false;
      })
      .catch(function (error) {
        console.log(error)
      })
  }
}
YesScroll()