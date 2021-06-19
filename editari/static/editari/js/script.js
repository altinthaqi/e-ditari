let sidenav = document.getElementById("side_nav");
let button = document.getElementById("hamburgerbutton");
function hamburgerButton() {
    button.style.transform += "rotate(180deg)";
    if(sidenav.style.width != 0 + "px") {
        sidenav.style.width = 0 + "px";
    } else {
        sidenav.style.width = 200 + "px";
    }
};


