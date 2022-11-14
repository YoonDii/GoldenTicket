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
