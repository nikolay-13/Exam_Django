let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}


let slideI = 0;
showS();

function showS() {
  let i;
  let slides = document.getElementsByClassName("mySlide");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideI++;
  if (slideI > slides.length) {slideI = 1}
  slides[slideI-1].style.display = "block";
  setTimeout(showS, 2000); // Change image every 2 seconds
}
