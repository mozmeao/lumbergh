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
        testimonialsInit();
    }


    /*
    *  It's Different section
    */

    var different = document.getElementById('different');
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

    // fade in boxes
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

    // swipe boxes
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
        $('#know-boxes').carouFredSel({
            responsive: true,
            width: knowBoxWidth,
            height: 'auto',
            align: 'center',
            prev: '#know-boxes-prev',
            next: '#know-boxes-next',
            pagination: '#know-boxes-pager',
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
        if (Mozilla.Test.isSmallScreen) {
            knowBoxSwipe();
        } else if (Mozilla.Test.isParallax) {
            knowBoxFadeIn();
        }
    }

    /*
    *  Testimonials
    */

    function testimonialsSwipe() {

        // add next & prev & pagination
        $('<button id="testimonials-prev" class="carousel-button carousel-button-prev"></button>').insertBefore('.testimonials');
        $('<button id="testimonials-next" class="carousel-button carousel-button-next"></button>').insertBefore('.testimonials');

        // init carousel
        $('.testimonials').eq(0).carouFredSel({
            responsive : false,
            width: 320,
            height: 'auto',
            align: 'center',
            prev: '#testimonials-prev',
            next: '#testimonials-next',
            scroll: 1,
            swipe: {
                onTouch: true
            },
            items: {
                width: 320,
                visible: 1
            },
            auto: false
        });

        function testimonialsSwipeResize() {
            if ($(window).width() > 680) {
                $('.testimonials').trigger('destroy', true);
                testimonialsChooseInit();
                $(window).off('resize', testimonialsSwipeResize);
            }
        }

        $(window).resize(testimonialsSwipeResize);
    }

    function testimonialsMovePointer() {
        var testimonialsCurrentImg = $('.testimonial-current img');
        var windowWidth = $(window).width();
        var testimonialPointerLeft = testimonialsCurrentImg.offset().left + 50;
        var testimonialPointerLeftFromCenter = windowWidth / 2 - testimonialPointerLeft;

        var testimonialPointerNewLeft;
        testimonialPointerNewLeft = testimonialPointerLeftFromCenter * -1;
        testimonialPointerNewLeft = testimonialPointerNewLeft + 'px';

        if (Modernizr.csstransitions) {
            $('.testimonials-pointer').css({'margin-left' : testimonialPointerNewLeft});
        } else {
            $('.testimonials-pointer').animate({ 'margin-left': testimonialPointerNewLeft}, 800, 'linear');
        }
    }

    function testimonialsChoose(e) {
        if (e.type === 'click' || e.which === 13) {
            var target = e.target;

            // remove class from others
            $('.testimonial-current').removeClass('testimonial-current');

            // add class to this one
            $(target).closest('.testimonial').addClass('testimonial-current');

            testimonialsMovePointer();
        }
    }

    function testimonialsChooseInit() {
        var testimonials = $('#testimonials');
        var testimonialImages = testimonials.find('img');

        // add class to parent to remove default styling
        testimonials.addClass('testimonials-choose');
        // attach triggers to pictures
        testimonialImages.attr('tabindex', 0).on('click keydown', testimonialsChoose);
        // add pointer
        $('<div class="testimonials-pointer"></div>').appendTo(testimonials);
        // click on first image to move pointer into place
        testimonialImages.eq(0).click();

        $(window).on('resize', function() {
            clearTimeout(this.resizeTimeout);
            this.resizeTimeout = setTimeout(testimonialsMovePointer, 200);
        });
    }

    // init #testimonials section
    function testimonialsInit() {
        if (Mozilla.Test.isSmallScreen) {
            testimonialsSwipe();
        } else {
            testimonialsChooseInit();
        }
    }


    /*
    *  Events Section
    */

    function eventsToggle() {
        var transitionDelay = 0;
        if (Modernizr.csstransitions) {
            transitionDelay = 50;
        }

        if ($('.event-toggle-off').length) {
            // show - loop through with small offset for smooth open
            $('.event-toggle').each(function(index) {
                var delay = index * transitionDelay;
                var currentElement = $(this);
                window.setTimeout(function(){
                    currentElement.removeClass('event-toggle-off');
                }, delay);
            });
            // change text of button
            $('#event-toggle-button').text('Hide more');
        } else {
             // hide - loop through with small offset for smooth close
            $($('.event-toggle').get().reverse()).each( function (index) {
                var delay = index * transitionDelay;
                var currentElement = $(this);
                window.setTimeout(function() {
                    currentElement.addClass('event-toggle-off');
                }, delay);
            });
            // scroll up if list is now out of sight
            var endOfVisible = $('#meetus table tbody tr:eq(5)').offset().top;
            var paddingFromTop = $('.masthead').height();
            if (endOfVisible < $('body').scrollTop()) {
                $('body').animate({scrollTop: endOfVisible - paddingFromTop}, '500', 'swing');
            }
            // change text of button
            $('#event-toggle-button').text('Show more');
        }
    }


    function eventsLengthInit() {
        var eventRows = $('#meetus table tbody tr');
        if(eventRows.length > 4) {
            // go through list and hide any greater than 5
            eventRows.slice(4).addClass('event-toggle').addClass('event-toggle-off');

            // add show button & listener
            $('<button id="event-toggle-button">Show More</button>').appendTo('#meetus .contain');
            $('#event-toggle-button').on('click', eventsToggle);
        }
    }

    if(Mozilla.Test.isSmallScreen) {
        eventsLengthInit();
    }


})(window, jQuery);
