(function(w, $) {
    'use strict';

    /*
    *  let's get this party started
    *  check for touch support, load js libraries, and activate page interactions
    */


    Modernizr.load({
        test: Mozilla.Test.isSmallScreen,
        yep: ['/static/js/libs/jquery.carouFredSel-6.2.1-packed.js','/static/js/libs/jquery.touchSwipe.min.js'],
        complete: animationInit
    });

    function animationInit() {
        differentListInit();
        knowBoxInit();
    }


    /*
    *  It's Different section
    */

    var different = document.getElementById("different");
    var bottomInView = $(window).height() - $('#different').outerHeight();

    // bring in coffee cup

    var cupFromTop = parseInt(window.getComputedStyle((different),':before').top, 10);
    var cupFromBottom = $('#different').outerHeight() - cupFromTop;
    var seeSomeCup = 100;

    $('#different').waypoint(function() {
        $('#different').addClass('different-cup');
    }, { offset: bottomInView + cupFromBottom - seeSomeCup });

    // bring in phone

    var phoneFromBottom = parseInt(window.getComputedStyle((different),':after').height, 10) - 60;
    var seeSomePhone = 200;

    $('#different').waypoint(function() {
        $('#different').addClass('different-phone');
        // if page loads and we are past phone cup doesn't load - load cup
        $('#different').addClass('different-cup');
        // we've got them both and can destroy this listener
        $('#different').waypoint('destroy');
    }, { offset: function() {return bottomInView + phoneFromBottom - seeSomePhone; } });

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


    /*
    *  Things You'll Want to Know section
    */

    function knowBoxFadeIn() {
        $('#know').waypoint(function() {
            var knowBoxes = $('.know-box');
            $(knowBoxes).eq(0).addClass('past');
            window.setTimeout(function () { $(knowBoxes).eq(1).addClass('past'); }, 800);
            window.setTimeout(function () { $(knowBoxes).eq(2).addClass('past'); }, 1600);
            window.setTimeout(function () { $(knowBoxes).eq(3).addClass('past'); }, 2200);
            $('#know').waypoint('destroy'); /* only need to fade them in once */
        }, { offset: '100%' });
    }

    function knowBoxSwipe() {

        // add class to fix this style in case of resize
        $('#know').addClass('caroufredsel');

        // add next & prev & pagination
        $('<div id="know-boxes-pager"></div>').insertBefore('#know-boxes');
        $('<button id="know-boxes-prev" class="carousel-button carousel-button-prev">').insertBefore('#know-boxes');
        $('<button id="know-boxes-next" class="carousel-button carousel-button-next">').insertBefore('#know-boxes');

        // init carousel
        var knowBoxWidth = $('#know-boxes-pager').width();
        $('.know-box').width(knowBoxWidth);
        $("#know-boxes").carouFredSel({
            responsive: true,
            width: knowBoxWidth,
            height: 'auto',
            align: 'center',
            prev: '#know-boxes-prev',
            next: '#know-boxes-next',
            pagination: "#know-boxes-pager",
            scroll: 1,
            swipe: {
                onTouch: true
            },
            items: {
                width: knowBoxWidth,
                visible: 1
            },
            auto: false
        });
    }

    // init #know section
    function knowBoxInit() {
        if(Mozilla.Test.isSmallScreen) {
            knowBoxSwipe();
        } else if (Mozilla.Test.isParallax) {
            knowBoxFadeIn();
        }
    }


})(window, window.jQuery);
