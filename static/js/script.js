function changemenubg(){
    let scrollvaue=window.scrollY;
    let nav=document.getElementById("navbar")
    if(scrollvaue < 100){
        nav.classList.remove("active")
    }
    else{
        nav.classList.add("active")
    }
}

window.addEventListener("scroll",changemenubg)