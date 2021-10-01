
// base page

// this targets the circle, top screenLeft, and when show-nav is activated, 
// it shows the navbar, and moves the page, which is referred to as container-base

const open = document.getElementById('open')
const close = document.getElementById('close')
const container = document.querySelector('.container-base')

open.addEventListener('click', () => container.classList.add('show-nav'))

close.addEventListener('click', () => container.classList.remove('show-nav'))


// registration page:

let id = (id) => document.getElementById(id);

let classes = (classes) => document.getElementsByClassName(classes);

// tells js what ids to target
let username = id("username"),
  email = id("email"),
  password = id("password"),
  form = id("form"),
  
  errorMsg = classes("error"),
  successIcon = classes("success-icon"),
  failureIcon = classes("failure-icon");

  // tells js to watch out for the submit action, and react accordingly
  form.addEventListener("submit", (e) => {
    e.preventDefault();

    registration(username, 0, "Username cannot be blank");
    registration(email, 1, "Email cannot be blank");
    registration(password, 2, "Password cannot be blank");
  });

// id refers to our ids 
// serial targets the classes 
// message prints a message
  let registration = (id, serial, message) => {
    // trim removes white space in the user input fields
    if (id.value.trim() === "") {
      errorMsg[serial].innerHTML = message;
    id.style.border = "2px solid red";
    
    // if no user input, displays failure icon
    failureIcon[serial].style.opacity = "1";
    successIcon[serial].style.opacity = "0";
    } 
    
    else {
      errorMsg[serial].innerHTML = "";
    id.style.border = "2px solid green";
    
    // if there is user input, displays correct icon
    failureIcon[serial].style.opacity = "0";
    successIcon[serial].style.opacity = "1";
    }
  }