// Carousel
const buttons = document.querySelectorAll("[data-carousel-button]")

buttons.forEach(button => {
  button.addEventListener("click", () => {
    const offset = button.dataset.carouselButton === "next" ? 1 : -1
    const slides = button
      .closest("[data-carousel]")
      .querySelector("[data-slides]")

    const activeSlide = slides.querySelector("[data-active]")
    let newIndex = [...slides.children].indexOf(activeSlide) + offset
    if (newIndex < 0) newIndex = slides.children.length - 1
    if (newIndex >= slides.children.length) newIndex = 0

    slides.children[newIndex].dataset.active = true
    delete activeSlide.dataset.active
  })
})


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
var line = document.getElementsByClassName("line");

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

function curentSlide(n){
  index=n;
  show(index);
}