
// base page

// this targets the circle, top screenLeft, and when show-nav is activated, 
// it shows the navbar, and moves the page, which is referred to as container-base

const open = document.getElementById('open')
const close = document.getElementById('close')
const container = document.querySelector('.container-base')

open.addEventListener('click', () => container.classList.add('show-nav'))

close.addEventListener('click', () => container.classList.remove('show-nav'))


const swiper = new Swiper('.swiper', {
    
    direction: 'horizontal',
    loop: true,
  
    // pagination
    pagination: {
      el: '.swiper-pagination',
    },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  
    //  scrollbar
    scrollbar: {
      el: '.swiper-scrollbar',
    },
  });