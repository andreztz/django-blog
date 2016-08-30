// $.noConflict();
// jQuery.(document).ready(function() {
//
// });


var main = function() {
    $(".btn-burguer").on('click', function() {
        $(this).toggleClass("active");
        $(".dropdown").toggleClass("dropdown-active");
    });
}

$(document).ready(main);
