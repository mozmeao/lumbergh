(function($) {
    'use strict';

    /*
    *  let's get this party started
    *  check for touch support, load js libraries, and activate page interactions
    */

    function pageInit() {
        console.log('pageInit');
        Modernizr.load({
            test: Mozilla.Test.isParallax,
            complete : function () {
                animationInit();
            }
        });
    }

    pageInit();

    window.onresize = function() { pageInit() };

    function animationInit() {
        differentListInit();
    }


    /*
    *  It's different section
    */

    var different = document.getElementById("different");
    var bottomInView = $(window).height() - $('#different').outerHeight();

    // bring in coffee cup

    var cupFromTop = parseInt(window.getComputedStyle((different),':before').top)
    var cupFromBottom = $('#different').outerHeight() - cupFromTop;
    var seeSomeCup = 100;

    $('#different').waypoint(function(direction) {
        if(direction === 'down') {
            $('#different').addClass('different-cup');
        }
    }, { offset: bottomInView + cupFromBottom - seeSomeCup });

    // bring in phone

    var phoneFromBottom = parseInt(window.getComputedStyle((different),':after').height) - 60;
    var seeSomePhone = 200;


    $('#different').waypoint(function(direction) {
        if(direction === 'down') {
            $('#different').addClass('different-phone');
        }
    }, { offset: function() {return bottomInView + phoneFromBottom - seeSomePhone } });

    // overlaping list display functions

    function differentListSwitch(e) {
        // if it was a click or enter key
        if (e.type === 'click' || e.which === 13) {
            // remove the class from all lists
            $('.different-list').removeClass('different-list-current');
            // add it back to the parent of the heading that was clicked
            $(e.target).closest('.different-list').addClass('different-list-current');
        }
    }

    function differentListSwitchInit() {
        //console.log('differentListSwitchInit');
        // enable click on headings (including adding tab index)
        var differentListHeadings = $('.different-list h3');
        $(differentListHeadings).attr('tabindex', 0);
        // add listeners
        $(differentListHeadings).on('click keydown', differentListSwitch);
    }

    // scroll in place list display functions

    function differentListScrollInit() {
        // TODO: parallax functionality being left until other stuff is fixed
    }

    // init #different section

    function differentListInit() {
        if (Mozilla.Test.isParallax) {
            differentListScrollInit();
        } else {
            differentListSwitchInit();
        }
    }

})(jQuery);
