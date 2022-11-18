

// Ranking tag
const tagList = document.querySelectorAll(".ranking__tag__name");
const rankList = document.querySelectorAll(".ranking__list");
let activeList = ''; // 활성화된 리스트를 담을 변수

for (let i = 0; i < tagList.length; i++) {
  tagList[i].querySelector('.tag-btn').addEventListener('click', function(event) {
    event.preventDefault();
    for (let j = 0; j < tagList.length; j++) {
      tagList[j].classList.remove('on');
      rankList[j].style.display = 'none';
    }
    this.parentNode.classList.add('on');
    activeList = this.getAttribute('href');
    document.querySelector(activeList).style.display = 'flex';
  });
}

// slide banner
var index=0;
var i = 0;
var slider = document.getElementsByClassName("slider");
var line = document.getElementsByClassName("bnrline");

auto();

function show(n){
  for(i=0;i<slider.length;i++){
      slider[i].style.display="none";
  }
  for(i=0;i<line.length;i++){
    line[i].className=line[i].className.replace("active");
  }
  slider[n-1].style.display=("block");
  line[n-1].className += "active";
}

function auto(){
  index++;
  if(index>slider.length){
      index=1;
  }
  show(index);
  setTimeout(auto,3500); //3.5초마다 슬라이드바뀜
}

function plusSlide(n){
  index+=n;
  if(index>slider.length){
    index=1;
  }
  if(index<1){
    index = slider.length;
  }
  show(index);
}

function currentSlide(n){
  index=n;
  show(index);
}