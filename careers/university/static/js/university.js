(function(w, $) {
    'use strict';

    /*
    *  let's get this party started
    *  check for touch support, load js libraries, and activate page interactions
    */

    Modernizr.load({
        test: Mozilla.Test.isSmallScreen,
        yep: $('body').data('js-smallscreen'),
        complete: animationInit
    });

    function animationInit() {
        differentListInit();
        knowBoxInit();
        testimonialsInit();
        galleryInit();
    }

    /*
    *  It's Different section
    *  - list switch (where user toggles visible list) capabilities are initalized at all sizes
    *  - parallax is loaded only isParallax on page load
    *    - spacer is made to take the place of the section head
    *    - section head is position fixed by .pin until there is 750px of section remaining
    *      - picked to keep bottom list from scrolling out of view
    *    - at that point section head is absolutely positioned by .pin-past in the section and beings
    *      to scroll
    *  - list heads are absolutely positioined to the top of the list container by .pin then position
    *    fixed until the bottom of the list reaches the bottom of the head and then they are
    *    absolutly positioned by .pin-past to the bottom of the list container (this involves much maths, which the js handles)
    */

    // switches between lists when they are in mobile/tablet display
    function differentListSwitch(e) {
        // if it was a click or enter key
        if (e.type === 'click' || e.which === 13) {
            // remove the class from all lists
            $('.different-list').removeClass('different-list-current');
            // add it back to the parent of the heading that was clicked
            $(e.target).closest('.different-list').addClass('different-list-current');
        }
    }

    // adds events to allow headings to trigger switch between lists
    function differentListSwitchInit() {
        // enable click on headings (including adding tab index)
        var differentListHeadings = $('.different-list h3');
        $(differentListHeadings).attr('tabindex', 0);
        // add listeners
        $(differentListHeadings).on('click keydown', differentListSwitch);
    }

    // elements and waypoints for cup and phone
    function differentListPinObjectInit () {
        var different = $('#different');

        // create and attach elements (becuse Safari doesn't do transitions on CSS content)
        var differentCup = $('<span class="different-object different-object-cup" />');
        var differentPhone =  $('<span class="different-object different-object-phone" />');
        different.addClass('different-objects');
        differentCup.appendTo(different);
        differentPhone.appendTo(different);

        var bottomInView = $(window).height() - different.outerHeight();

        // adds waypoints to slide cup into view

        var cupFromTop = parseInt(differentCup.position().top, 10);
        var cupFromBottom = different.outerHeight() - cupFromTop;
        var seeSomeCup = 100;

        different.waypoint(function() {
            different.addClass('different-cup-show');
        }, {
            offset: bottomInView + cupFromBottom - seeSomeCup,
            triggerOnce: true
        });

        // adds waypoints to slide phone into view

        var phoneFromBottom = parseInt(differentPhone.height(), 10) - 60;
        var seeSomePhone = 200;

        different.waypoint(function() {
            different.addClass('different-phone-show');
            // if page loads and we are past phone cup doesn't load - load cup
            different.addClass('different-cup-show');
        }, {
            offset: function() {return bottomInView + phoneFromBottom - seeSomePhone; },
            triggerOnce: true
        });
    }

    // waypoints to add/remove .pin and .pin-past classes to section head and list heads
    function differentListPinHeadInit () {
        var different = $('#different');
        var mastheadHeight = $('header.masthead').height();
        var differentListsHeadHeight = $('.different-lists-head').height();

        // create container to hold place of pinned list header
        var differentListHeadSpacer = $('<div />').attr('id', 'different-list-head-spacer');
        // set its height
        differentListHeadSpacer.height(differentListsHeadHeight);
        // attach
        differentListHeadSpacer.prependTo('#different');

        /* waypoint to pin and unpin section head and subhead */

        // waypoint toggle for scrolling past top of section
        different.waypoint( function(direction) {
            if (direction === 'down') {
                different.addClass('pin');
            } else if (direction === 'up') {
                different.removeClass('pin');
            }
        }, {
            offset: mastheadHeight
        });

        // waypoint toggle for scrolling to bottom of section
        // triggered when there is 750px of the section remaining
        different.waypoint( function(direction) {
            if (direction === 'down') {
                different.addClass('pin-past');
            } else if (direction === 'up') {
                different.removeClass('pin-past');
            }
        }, {
            offset: function() {
                return (different.height() - 700) * -1;
            }
        });

        /* waypoints to pin and unpin list heads */

        var differentWill = $('#different-will');

        // add/remove pin to will head
        differentWill.waypoint( function(direction) {
            if (direction === 'down') {
                differentWill.addClass('pin');
            } else if (direction === 'up') {
                differentWill.removeClass('pin');
            }
        }, {
            offset: function() {
                return mastheadHeight + differentListsHeadHeight ;
            }
        });

        // add/remove past-pin to will head
        differentWill.waypoint( function(direction) {
            if (direction === 'down') {
                differentWill.addClass('pin-past');
            } else if (direction === 'up') {
                differentWill.removeClass('pin-past');
            }
        }, {
            offset: function() {
                // down the height of all the fixed stuff
                // up the height of the list
                // down the bottom margin of the list (60px)
                return mastheadHeight + differentListsHeadHeight + differentWill.find('h3').height() - differentWill.height() + 60;
            }
        });

        var differentWillNot = $('#different-not');

        // add/remove pin to will not head
        differentWillNot.waypoint( function(direction) {
            if (direction === 'down') {
                differentWillNot.addClass('pin');
            } else if (direction === 'up') {
                differentWillNot.removeClass('pin');
            }
        }, {
            offset: function() {
                return mastheadHeight + differentListsHeadHeight ;
            }
        });

        // add/remove past-pin to will not head
        differentWillNot.waypoint( function(direction) {
            if (direction === 'down') {
                differentWillNot.addClass('pin-past');
            } else if (direction === 'up') {
                differentWillNot.removeClass('pin-past');
            }
        }, {
            offset: function() {
                return mastheadHeight + differentListsHeadHeight + differentWillNot.find('h3').height() - differentWillNot.height() + 60;
            }
        });
    }

    // init #different section
    function differentListInit() {
        if (Mozilla.Test.isParallax) {
            differentListPinObjectInit();
            differentListPinHeadInit();
        } else {
            $('#different').addClass('different-cup').addClass('different-phone');
        }
        differentListSwitchInit();
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
        $('<div id="know-boxes-pager" class="carousel-pager"></div>').insertBefore('#know-boxes');
        $('<button id="know-boxes-prev" class="carousel-button carousel-button-prev" type="button">Previous</button>').insertBefore('#know-boxes');
        $('<button id="know-boxes-next" class="carousel-button carousel-button-next" type="button">Next</button>').insertBefore('#know-boxes');

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
        } else {
            $('.know-box').addClass('past');
        }
    }


    /*
    *  Testimonials
    */

    function testimonialsSwipe() {

        // add next & prev & pagination
        $('<button id="testimonials-prev" class="carousel-button carousel-button-prev" type="button">Previous</button>').insertBefore('.testimonials');
        $('<button id="testimonials-next" class="carousel-button carousel-button-next" type="button">Next</button>').insertBefore('.testimonials');

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
        var target = e.target;

        // remove class from others
        $('.testimonial-current').removeClass('testimonial-current');

        // add class to this one
        $(target).closest('.testimonial').addClass('testimonial-current');

        testimonialsMovePointer();
    }

    function testimonialsChooseInit() {
        var testimonials = $('#testimonials');
        var testimonialImages = testimonials.find('img');

        // add class to parent to remove default styling
        testimonials.addClass('testimonials-choose');
        // attach triggers to pictures
        testimonialImages.attr('tabindex', 0).on('mouseenter focus', testimonialsChoose);
        // add pointer
        $('<div class="testimonials-pointer"></div>').appendTo(testimonials);
        // touch first image to move pointer into place
        testimonialImages.eq(0).trigger('mouseenter');

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
    *  Videos
    */

    // function to make sure video cues to play again when finished
    function videoEnded() {
        this.posterImage.show();
        this.bigPlayButton.show();
        this.currentTime(0);
        this.pause();
    }

    function videoEvent(videoName, state) {
        return function() {
            ga('careersSnippetGA.send', 'event', 'Intern Video Interactions', state, videoName);
        };
    }

    // change the video to the one matching the thumbnail that was clicked
    function videoFadeTo(e) {
        var videoTarget = $(e.target);
        if (e.type === 'click' || e.which === 13) {
            // get video user wants to see
            var videoNewID = videoTarget.attr('data-video-id');
            var videoOldID = $('.video-current .video-js').attr('id');

            // if it isn't what they're already watching
            if(videoNewID !== videoOldID) {
                // pause the current one
                videojs(videoOldID).pause();

                // move the current class on the videos
                var $newVideo = $('#' + videoNewID);
                $('.video-current').removeClass('video-current');
                $newVideo.closest('figure').addClass('video-current');

                // move the current class on the buttons
                $('.video-thumb-current').removeClass('video-thumb-current');
                videoTarget.addClass('video-thumb-current');

                // Track that a new video was opened.
                var videoName = $newVideo.siblings('figcaption').text();
                ga('careersSnippetGA.send', 'event', 'Intern Video Interactions', 'Open', videoName);
            }
        }
    }

    function videoInit() {
        $('.video-js').each( function(index) {
            var $video = $(this);
            var posterID = $video.attr('id');
            var videoName = $video.siblings('figcaption').text();

            // attach an appropriate poster image
            var windowWidth = $(window).width();
            var posterSize = 480;
            if (windowWidth < 321) {
                posterSize = 320;
            } else if (windowWidth > 481) {
                posterSize = 700;
            }
            var posterName = posterID.slice(6);
            $video.attr('poster','/static/img/video-thumbs/' + posterName + '-' + posterSize + '.jpg');

            // initialize video.js
            var thisVideo;
            if (!Mozilla.Test.isSmallScreen && index === 0) {
                thisVideo = videojs(posterID, { 'preload': 'auto' });
            } else {
                thisVideo = videojs(posterID);
            }

            // move current class on buttons incase they are in mobile and go to larger layout
            thisVideo.on('click', function() {
                $('.video-thumb[data-video-id='+posterID+']').trigger('click');
            });
            // make sure it ques to play again when it finishes
            thisVideo.on('ended', videoEnded);

            // Event tracking
            thisVideo.on('play', videoEvent(videoName, 'Play'));
            thisVideo.on('pause', videoEvent(videoName, 'Pause'));
            thisVideo.on('ended', videoEvent(videoName, 'Finish'));
        });

        // wire buttons up
        $('.video-thumb').on('click keydown', videoFadeTo);
    }

    $(function() {
        videoInit();
    });


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
            $('<button id="event-toggle-button" type="button">Show More</button>').appendTo('#meetus .contain');
            $('#event-toggle-button').on('click', eventsToggle);
        }
    }

    if(Mozilla.Test.isSmallScreen) {
        eventsLengthInit();
    }

    /*
    *  Gallery section
    *  - loads large gallery image after window.onload
    *  - smaller screens get a single height image gallery they can click or swipe through
    *  - larger screens get a double height band that is static
    */

    // setup the carousel
    function gallerySwipe() {

        // add the carousel class so styling stayes even if window resizes
        $('.gallery-wrapper').addClass('gallery-carousel');

        // add buttons
        $('<button id="gallery-prev" class="carousel-button carousel-button-prev" type="button">Previous</button>').insertBefore('.gallery-carousel');
        $('<button id="gallery-next" class="carousel-button carousel-button-next" type="button">Next</button>').insertBefore('.gallery-carousel');

        // add div that can act as fallback if user increases window size
        $('<div id="gallery-band"></div>').insertBefore('.gallery-carousel');
        $('#gallery-band').css({'background-image': 'url(/static/img/gallery-1100.jpg)'});


        // gallery items are 230px wide = 220px wide + 5px padding on each side
        var galleryItemWidth = 230;

        // how much space do we have?
        var galleryContainWidth = $(window).width();

        // measure how many items we can fit, minimum 1, leaving room for min 45px wide buttons
        var galleryVisibleItems = Math.floor( (galleryContainWidth - (45 * 2)) / galleryItemWidth);
        if (galleryVisibleItems < 1) { galleryVisibleItems = 1; }

        // set gallery width to be width of visible items
        var galleryWidth = galleryItemWidth * galleryVisibleItems;
        $('.gallery-carousel').width(galleryWidth + 'px');

        // set button width to fill leftover space
        var galleryButtonWidth = ((galleryContainWidth - galleryWidth) / 2) - 5;
        $('#gallery .carousel-button').width(galleryButtonWidth);

        // initialize the carousel
        $(".gallery-carousel").carouFredSel({
            responsive: false,
            width: galleryWidth,
            height: 220,
            align: 'center',
            prev: '#gallery-prev',
            next: '#gallery-next',
            scroll: galleryVisibleItems,
            swipe: {
                onTouch: true
            },
            items: {
                width: galleryItemWidth,
                visible: galleryVisibleItems
            },
            auto: false
        });

        // add negative margin to move first item in gallery off to left
        var galleryNegativeMargin = galleryItemWidth * -1;
        $('.gallery-carousel').css({'margin-left': galleryNegativeMargin+ 'px'});
    }

    // init #gallery section
    function galleryInit() {

        if(Mozilla.Test.isSmallScreen) {
            gallerySwipe();
        }

    }


})(window, jQuery);
