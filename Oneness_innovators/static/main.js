$(document).ready(function(){
$(window).scroll(function () {

 if($(window).scrollTop() > 100) {
    $('#sidebar').css('position','fixed');
    $('#sidebar').css('top','0');
 }
 else if ($(window).scrollTop() <= 1000) {
    $('#sidebar').css('position','');
    $('#sidebar').css('top','');
 }
    if ($('#sidebar').offset().top + $("#sidebar").height() > $("#footer").offset().top) {
        $('#sidebar').css('top',-($("#sidebar").offset().top + $("#sidebar").height() - $("#footer").offset().top));
    }
});
});
$('.nav-link').click(function() {
    var sectionTo = $(this).attr('href');
    $('html, body').animate({
      scrollTop: $(sectionTo).offset().top
    }, 1500);
});
