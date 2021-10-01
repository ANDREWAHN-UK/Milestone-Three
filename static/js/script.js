
// base page

// this targets the circle, top screenLeft, and when show-nav is activated, 
// it shows the navbar, and moves the page, which is referred to as container-base

const open = document.getElementById('open')
const close = document.getElementById('close')
const container = document.querySelector('.container-base')

open.addEventListener('click', () => container.classList.add('show-nav'))

close.addEventListener('click', () => container.classList.remove('show-nav'))


