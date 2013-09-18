(function($) {
    'use strict';

    /*
    *  let's get this party started
    *  check for touch support, load js libraries, and activate page interactions
    */

    Modernizr.load({
        test: Modernizr.touch,
        complete : function () {
            animationInit();
        }
    });

    function animationInit() {
        differentListInit();
    }


    /*
    *  It's different section
    */

     // bring in coffee cup and phone

    $('#different').waypoint(function(direction) {
        if(direction === 'down') {
            $('#different').addClass('different-objects');
        }
    }, { offset: 350 });


    // overlaping list display functions

    function differentListSwitch(e) {
        // if it was a click or enter key
        if(e.type === 'click' || e.which === 13) {
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
        if(Mozilla.isParallax) {
            differentListScrollInit();
        } else {
            differentListSwitchInit();
        }
    }

})(jQuery);
