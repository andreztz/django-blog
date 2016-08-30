var main = function() {
    var menuState;

    $('.dropdown-content').css('visibility', 'hidden');

    menuState = $('.dropdown-content').css('visibility');


    $('.dropbtn').on('click', function(event) {
        event.preventDefault();
        /* Act on the event */
        
        if (menuState == 'hidden') {
            $('.dropdown-content').css('visibility', 'initial');
            menuState = $('.dropdown-content').css('visibility');
        }
        else {
            $('.dropdown-content').css('visibility', 'hidden');
            menuState = $('.dropdown-content').css('visibility');
            
        }
    });
}

$(document).ready(main);