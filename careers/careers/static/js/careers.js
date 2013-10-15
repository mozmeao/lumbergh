(function(w, $) {
    'use strict';

    $(function() {
        // Highlight correct link in the top navigation based on the url fragment id.
        var fragment = window.location.hash;
        if (fragment) {
            var matchedNavLink = $('#nav-main-menu a[href$="' + fragment + '"]');
            if (matchedNavLink.length > 0) {
                $('#nav-main-menu .current').removeClass('current');
                matchedNavLink.parent('li').addClass('current');
            }
        }
    });

    Modernizr.load({
        test: Mozilla.Test.isSmallScreen,
        yep: ['/static/js/libs/jquery.carouFredSel-6.2.1-packed.js','/static/js/libs/jquery.touchSwipe.min.js'],
        load: $('body').data('js-smallscreen'),
        complete: animationInit
    });


    function animationInit() {
        galleryInit();
        perksInit();
        communityVideoInit();
        locationsInit();
        nextInit();
    }
/*
    *  Gallery
    *  - gallery images are all sprites, loaded in phases
    *  - carousel is initilized at mobile tablet or desktop size
    *    then fixed at that height incase of resize by addition of a class
    */

    var gallerySpritesLoaded = 1;
    var gallerySpritesToLoad = 4;

    function galleryBlocksSpriteLoad() {
        // magic of media queries handles loading appropriate size
        if (gallerySpritesLoaded < gallerySpritesToLoad) {
            gallerySpritesLoaded ++;
            var galleryCarousel = $('#life-blocks');
            galleryCarousel.addClass('sprite-load-' + gallerySpritesLoaded);
        }
    }

    function galleryCarouselInit() {

        // determine small medium or large
        var galleryItemWidth = 360;
        var galleryItemHeight = 345;
        var galleryButtonMinWidth = 80;
        if (Mozilla.Test.isSmallScreen) {
            galleryItemWidth = 280 + 10; // mobile has padding
            galleryItemHeight = 225;
            galleryButtonMinWidth = 20;
        } else if (Mozilla.Test.isBigScreen) {
            galleryItemWidth = 480;
            galleryItemHeight = 460;
        }

        // how much space do we have?
        var galleryContainWidth = $(window).width();

        // measure how many items we can fit, minimum 1, leaving room for min wide buttons
        var galleryVisibleItems = Math.floor( (galleryContainWidth - (galleryButtonMinWidth * 2)) / galleryItemWidth);
        if (galleryVisibleItems < 1) { galleryVisibleItems = 1; }

        // set gallery width to be width of visible items
        var galleryWidth = galleryItemWidth * galleryVisibleItems;
        $('.life-blocks-contain').width(galleryWidth + 'px');

        // set button width to fill leftover space
        var galleryButtonWidth = ((galleryContainWidth - galleryWidth) / 2);
        $('#life-blocks .carousel-button').width(galleryButtonWidth);

        // initialize the carousel
        $('.life-blocks-contain').carouFredSel({
            responsive: false,
            width: galleryWidth,
            height: galleryItemHeight,
            align: 'center',
            prev: {
                button: '#life-blocks-prev',
                onBefore: galleryBlocksSpriteLoad
            },
            next: {
                button: '#life-blocks-next',
                onBefore: galleryBlocksSpriteLoad
            },
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
        var galleryNegativeMargin = (galleryItemWidth * -1) + galleryButtonWidth;
        $('.life-blocks-contain').css({'margin-left': galleryNegativeMargin + 'px'});

    }

    // create DOM elements later function is dependant on
    function galleryElements() {

        var frames = 14;
        var galleryClass = 'medium';
        if (Mozilla.Test.isSmallScreen) {
            frames = 35;
            galleryClass = 'small';
        } else if (Mozilla.Test.isBigScreen) {
            galleryClass = 'large';
        }

        // blocks container
        var galleryBlocks = $('<div id="life-blocks" class="life-blocks-' + galleryClass + '"></div>');
        var galleryBlocksContain = $('<div class="life-blocks-contain"></div>');

        // blocks buttons
        var galleryPrev = $('<button id="life-blocks-prev" class="carousel-button carousel-button-prev"></button>');
        var galleryNext = $('<button id="life-blocks-next" class="carousel-button carousel-button-next"></button>');

        // blocks frames
        for (var i = 0 ; i < frames; i++) {
            var frameNumber = i + 1;
            var galleryBlocksClasses = 'life-blocks-frame life-blocks-frame-' + frameNumber;
            var galleryBlocksFrame = $('<div class="' + galleryBlocksClasses + '"></div>');
            galleryBlocksFrame.appendTo(galleryBlocksContain);
        }

        // leg bone's connected to the hip bone...
        galleryPrev.appendTo(galleryBlocks);
        galleryNext.appendTo(galleryBlocks);
        galleryBlocksContain.appendTo(galleryBlocks);
        galleryBlocks.appendTo('#life-gallery-photos');

    }

    function galleryInit() {
        galleryElements();
        galleryCarouselInit();
    }

    /*
    *  Perks
    */

    // swipe boxes
    function perksSwipe() {

        // add next & prev & pagination
        $('<div id="life-perks-pager" class="carousel-pager"></div>').insertBefore('#life-perks-perks');
        $('<button id="life-perks-prev" class="carousel-button carousel-button-prev">').insertBefore('#life-perks-perks');
        $('<button id="life-perks-next" class="carousel-button carousel-button-next">').insertBefore('#life-perks-perks');

        // init carousel
        var perksWidth = $('.life-perks-head').width();
        $('.life-perk').width(perksWidth);
        $('#life-perks-perks').carouFredSel({
            responsive: true,
            width: perksWidth,
            height: 'auto',
            align: 'center',
            prev: '#life-perks-prev',
            next: '#life-perks-next',
            pagination: '#life-perks-pager',
            scroll: 1,
            swipe: {
                onTouch: true
            },
            items: {
                width: perksWidth,
                visible: 1
            },
            auto: false
        });

        // remove if we go past break point
        function perksSwipeResize() {
            if ($(window).width() > 680) {
                $('.life-perk').trigger('destroy', true);
                $('.life-perk').css('width', '');
                $(window).off('resize', perksSwipeResize);
            }
        }

        $(window).resize(perksSwipeResize);
    }

    // init perks section
    function perksInit() {
        if (Mozilla.Test.isSmallScreen) {
            perksSwipe();
        }
    }

    /*
    *  Community & Culture
    *  - only one modal with video right now, could easily be adapted for more modals with different videos
    *  - modal and video created and inserted dynamically
    *  - video auto plays on modal open, auto pauses on modal close
    *  - modal can be closed by close button or by escape key
    */

    function communityEscapeWatch(e) {
        // if escape key is pressed, hide all modals
        if (e.keyCode === 27) {
            communityVideoHide(null);
        }
    }

    function communityVideoHide() {
        // stop video
        videojs('#video-interns').pause();

        // hide modal
        $('#community-interns-modal').removeClass('community-current');

        // removeescape listener
        $(document).off('keyup', communityEscapeWatch);

    }

    function communityVideoShow() {
        // show modal
        $('#community-interns-modal').addClass('community-current');

        // start video
        videojs('#video-interns').play();

        // add listener for escape key
        $(document).on('keyup', communityEscapeWatch);
    }


    function communityVideoInit() {
        if(!Mozilla.Test.isSmallScreen) {

            // create modal
            var videoModal = $('<div id="community-interns-modal" class="community-modal"></div>');

            // create and attach close/stop button
            var videoModalClose = $('<button class="community-modal-close">&times;</button>');
            videoModalClose.on('click', communityVideoHide);
            videoModalClose.appendTo(videoModal);

            // create and attach video wrapper
            var videoWrapper = $('<div class="community-video-wrapper"></div>');
            videoWrapper.appendTo(videoModal);

            // create video sources
            var videoInternsSrcMp4 = '<source src="//videos-cdn.mozilla.net/serv/interns/Interns-It%20can%20be%20you-720p-MPEG-4%282%29.mp4" type="video/mp4" />';
            var videoInternsSrcWebm = '<source src="//videos-cdn.mozilla.net/serv/interns/Interns-It%20can%20be%20you-720p-MPEG-4.webm" type="video/webm" />';
            var videoInternsSrcOgv = '<source src="//videos-cdn.mozilla.net/serv/interns/Interns-It%20can%20be%20you-720p-MPEG-4.theora.ogv" type="video/ogg" />';

            // create and attach video element
            // IE9 had issues when I appended the source to the video
            var videoInterns = $('<video id="video-interns" class="video-js vjs-sandstone-skin" controls preload="none" width="auto" height="auto">' +
                                videoInternsSrcMp4 +
                                videoInternsSrcWebm +
                                videoInternsSrcOgv +
                                '</video>');
            videoInterns.appendTo(videoWrapper);

            // append modal
            videoModal.appendTo('#community');

            // initialize video
            videojs('#video-interns');

            // create button to open modal & begin playing video
            var videoModalOpen = $('<button class="community-modal-open"></button>');
            videoModalOpen.on('click', communityVideoShow);
            videoModalOpen.appendTo('.community-box.community-interns');

            // make link a trigger as well
            var videoModalLink = $('.community-box.community-interns a');
            videoModalLink.on('click', function(e){
                e.preventDefault();
                communityVideoShow();
            });

        }

    }


    /*
    *  Locations
    *  - two ways to show details:
    *    - on mobile a select box can be used to pick one
    *    - on desktop the user can click the link
    *  - both ways are initialized and the associated form controls are hidden by media queries
    *  - details can be hidden by:
    *    - selecting a new location details
    *    - pressing escape
    *    - on mobile: navgigating to the empty form option
    */

    function locationsEscapeWatch(e) {
        // if escape key is pressed, hide all modals
        if (e.keyCode === 27) {
            locationsHide(null);
        }
    }

    function locationsShow(locationId) {
        // remove class from any current one
        $('.location-current').removeClass('location-current');

        // add class to the one with matching ID
        $('#' + locationId).addClass('location-current');

        // add watcher for escape key
        $(document).on('keyup', locationsEscapeWatch);
    }

    function locationsHide() {
        // remove class from currently visible
        $('.location-current').removeClass('location-current');

        // remove watcher for escape key
        $(document).off('keyup', locationsEscapeWatch);
    }

    function locationsToggle(locationId) {
        if (locationId) {
            locationsShow(locationId);
        } else {
            locationsHide();
        }
    }

    function locationsModalInit() {
        var locations = $('.locations-location');

        // loop through locations links
        $(locations).each( function() {
            var location = $(this);

            // create close button
            var locationsModalClose = $('<button class="location-close">&times;</button>');
            locationsModalClose.on('click', locationsHide);

            // add close button
            var locationDetails = location.find('.location-details');
            locationDetails.prepend(locationsModalClose);

            // hijack links
            var locationLink = location.find('.location-link');
            var locationId = this.id;
            $(locationLink).on('click', function(e) {
                e.preventDefault();
                locationsToggle(locationId);
            });
        });

    }

    function locationsParallaxInit() {

        // waypoint to add/remove background pin
        var locations = $('#locations');

        locations.waypoint( function(direction) {
            if (direction === 'down'){
                locations.addClass('pin');
            } else if(direction === 'up') {
                locations.removeClass('pin');
            }
        }, {
            offset: -50
        });

        // waypoint to close locations modal
        $('#locations-list').waypoint(function(direction) {
            if (direction === 'down') {
                locationsHide();
            }
        }, {
            offset: function() {
                return $('header.masthead').height() - 50;
            }
        });
    }

    function locationsMenuInit() {
        // create container, select, and label
        var locationMenuContain = $('<div class="locations-menu"></div>');
        var locationsLabel = $('<label class="locations-label" for="locations-select">Select Location</label>');
        var locationsMenu = $('<select id="locations-select"></select>');
        var locationsDefaultOption = $('<option />');
        locationsDefaultOption.appendTo(locationsMenu);

        // get locations
        var locations = $('.locations-location');

        // create option tag for each location
        $(locations).each(function() {
            // get name
            var locationName = $(this).find('.location-link').text();

            // get id of location
            var locationId = this.id;

            // create option
            var locationOption = $('<option value="' + locationId + '">' + locationName + '</option>');

            // attach option
            locationOption.appendTo(locationsMenu);

        });

        // when contents of select change, change the visible location
        locationsMenu.on('change', function(e){
            var locationNew = $(e.target).val();
            locationsToggle(locationNew);
        });

        // attach menu to page
        locationsMenu.appendTo(locationMenuContain);
        locationsLabel.appendTo(locationMenuContain);
        locationMenuContain.insertBefore('#locations-list');
    }

    function locationsInit() {
        // create drop down for mobile
        locationsMenuInit();
        // create modal for larger
        locationsModalInit();

        if (Mozilla.Test.isParallax) {
            locationsParallaxInit();
        }
    }


    /*
    *  Next / ...and you?
    */

    function nextFadeBoxes() {
        var nextBoxes = $('.next-box');


        if (Modernizr.csstransitions) {
            $(nextBoxes).each( function (index) {
                var delay = index * 1000;
                var currentBox = $(this);
                window.setTimeout( function() {
                    currentBox.addClass('show');
                } , delay );
            });

            window.setTimeout( function() {
                $('.next-you').addClass('show');
            } , 5000 );

        } else {

            $(nextBoxes).each( function (index) {
                var delay = index * 1000;
                var currentBox = $(this);
                window.setTimeout( function() {
                    currentBox.fadeTo( 'slow', 1, function() {
                        currentBox.addClass('show').css('opacity', '');
                    });
                } , delay);
            });

            window.setTimeout( function() {
                $('.next-you').fadeTo( 'slow', 1, function() {
                    $(this).addClass('show').css('opacity', '');
                });
            } , 5000 );
        }


    }

    function nextInit() {
        if (Mozilla.Test.isParallax) {
            // waypoint to add/remove background pin
            var next = $('#next');
            next.waypoint(function(direction) {
                if (direction === 'down') {
                    next.addClass('pin');
                } else if (direction === 'up') {
                    next.removeClass('pin');
                }
            }, {
                offset: function() {
                    return $('header.masthead').height();
                }
            });

            // waypoint to fade in boxes
            var nextTeaser = $('#next-teaser');
            nextTeaser.waypoint( function(direction) {
                if (direction === 'down') {
                    // add class
                    nextFadeBoxes();
                }
            }, {
                offset: function() {
                    return $(window).height() - 100;
                },
                triggerOnce: true
            });
        } else {
            // add classes which display everything incase of resize
            $('.next-box').addClass('show');
            $('.next-you').addClass('show');
        }
    }



})(window, window.jQuery);
