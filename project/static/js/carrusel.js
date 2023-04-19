$(document).ready(function() {
  var carousel = $(".carousel");
  var images = carousel.find("img");
  var currentImage = 0;

  function showNextImage() {
    images.removeClass("active");
    images.eq(currentImage).addClass("active");
    currentImage++;
    if (currentImage >= images.length) {
      currentImage = 0;
    }
    setTimeout(showNextImage, 3000); // Cambiar imagen cada 3 segundos
  }

  showNextImage();
});
