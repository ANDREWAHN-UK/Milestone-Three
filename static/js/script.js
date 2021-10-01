
// base page

const open = document.getElementById('open')
const close = document.getElementById('close')
const container = document.querySelector('.container-base')

open.addEventListener('click', () => container.classList.add('show-nav'))

close.addEventListener('click', () => container.classList.remove('show-nav'))


// registration page:

const signUpBtn = document.querySelector(".signup-btn");
const signInBtn = document.querySelector(".signin-btn");
const formsWrapper = document.querySelector(".forms-wrapper");


// when clicked, adds or removes the change class
signUpBtn.addEventListener("click", (e) => {
  e.preventDefault();
  formsWrapper.classList.add("change");
});

signInBtn.addEventListener("click", (e) => {
  e.preventDefault();
  formsWrapper.classList.remove("change");
});