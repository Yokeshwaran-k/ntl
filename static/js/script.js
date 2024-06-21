
    window.onscroll = function() {myFunction()};
    
    var header = document.getElementById("header");
    var sticky = header.offsetTop;
    
    function myFunction() {
      if (window.pageYOffset > sticky) {
        header.classList.add("sticky");
      } else {
        header.classList.remove("sticky");
      }
    }

    var owl = $('.owl-carousel');
owl.owlCarousel({
    items:1,
    loop:true,
    margin:10,
    autoplay:true,
    autoplayTimeout:5000,
    autoplayHoverPause:true
});

    $(document).ready(function(){
      $('.inner-text').hide().fadeIn(2000);
    });

const signUpButton = document.getElementById("signUp");
const signInButton = document.getElementById("signIn");
const container = document.getElementById("Login_form");

signUpButton.addEventListener("click", () => {
  container.classList.add("right-panel-active");
});

signInButton.addEventListener("click", () => {
  container.classList.remove("right-panel-active");
});
    