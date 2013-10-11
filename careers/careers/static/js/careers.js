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
        // test: Mozilla.Test.isSmallScreen, this pages
        load: $('body').data('js-smallscreen'),
        complete: animationInit
    });


    function animationInit() {
        galleryInit();
        perksInit();
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

})(window, window.jQuery);
