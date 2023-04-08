$(document).ready(function() {
  $('.logo-carousel').slick({
    slidesToShow: 8,
    slidesToScroll: 2,
    autoplay: true,
    autoplaySpeed: 1000,
    arrows: false,
    dots: false,
    pauseOnHover: true,
    responsive: [{
      breakpoint: 768,
      settings: {
        slidesToShow: 4,
        arrows: false,
      }
    }, {
      breakpoint: 520,
      settings: {
        slidesToShow: 3,
        arrows: false,
      }
    }]
  });
});