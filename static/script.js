const navbtns = document.querySelectorAll('li');
for(let nav in navbtns)
nav.addEventListener("click", () =>{
    nav.classList.add('active')
})