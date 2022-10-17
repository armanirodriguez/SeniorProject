let scrollButton = document.getElementById("top-btn-wrap");
let overflow = document.getElementById("overflow-wrap");
let firstNav = document.getElementById("first-nav");

overflow.onscroll = function() {scrollFunction()};
function scrollFunction() {
  if (overflow.scrollTop > 40) {
    scrollButton.style.display = "block";
  } else {
    scrollButton.style.display = "none";
  }
}

function topFunction() {
  $("#overflow-wrap").animate({ scrollTop: 0 }, "fast");
}