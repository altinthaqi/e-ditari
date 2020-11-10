document.addEventListener('DOMContentLoaded', function() {
   //Get the button:
mybutton = document.getElementById("top_button");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  //window.scroll({top: 0, behavior: "smooth"});
  window.scrollTo({top: 0, behavior: 'smooth'});

}
});

