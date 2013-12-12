// create namespace
if (typeof Mozilla === 'undefined') {
    var Mozilla = {};
}

Mozilla.Test = (function(w, $) {
    'use strict';

    function _checkBigScreen() {
        if($(window).width() > 920) {
            return true;
        } else {
            return false;
        }
    }

    function _checkSmallScreen() {
        if($(window).width() <= 680) {
            return true;
        } else {
            return false;
        }
    }

    function _checkTouch() {
        // add check for pointer events to the modernizer check for touch events
        return (window.navigator.msMaxTouchPoints || window.navigator.maxTouchPoints || Modernizr.touch);
    }

    function _checkParallaxOkay() {
        return (_checkBigScreen() && !_checkTouch());
    }

    return {
        isTouch: _checkTouch(),
        isBigScreen: _checkBigScreen(),
        isSmallScreen: _checkSmallScreen(),
        isParallax: _checkParallaxOkay(),
    };

})(window, window.jQuery); // Mozilla.Test

(function($) {
    'use strict';

    /*
    *   add class to HTML if we detect support for pointer events AKA microsoft touch screen
    */
    if (Mozilla.Test.isTouch) {
        $('html').addClass('moz-touch');
    } else {
        $('html').addClass('moz-no-touch');
    }

    /*
    *   move tabzilla into the header so it plays nice with our sticky menu
    */

    function moveTabzilla() {
        // check if tabzilla has been initlialized
        if ($('#tabzilla-panel').length) {
            // move into .masthead
            $('.masthead').prepend($('#tabzilla-panel'));
            // remove link from tab so that iOS doesn't pull down address bar when link is clicked, can't remove href altogether or keyboard loses access
            $('#tabzilla').attr('href', '#');
        } else {
            // try again in 1/10th of a second
             window.setTimeout(moveTabzilla, 100);
        }
    }

    $(function() {
        moveTabzilla();
    });


    /*
    *  tray/mobile menu
    */

    function trayMenuInit() {
        // add toggle button
        $('#nav-main').append('<button id="tray-toggle" aria-controls="nav-tray" tabindex="0" type="button">Menu</button>');
        $('#tray-toggle').on('click', trayMenuOpen);

        // add tray and copy nav there
        $('body').prepend('<div id="nav-tray" tabindex="-1"></div>');
        $('#nav-main-menu').clone().attr({
            'id': 'nav-mobile-menu',
            'role': 'navigation'
        }).appendTo('#nav-tray');

        // add close button
        $('#wrapper').prepend('<button id="nav-tray-close" type="button">Close</button>');
        $('#nav-tray-close').on('click', trayMenuClose);

        // capture touch on body while tray open
        document.ontouchstart = function trayMenuHandleTouch(e) {
            if ($('body').hasClass('tray-open')) {
                if ($(e.target).parents('#nav-mobile-menu').length === 1) {
                    // do nothing - allow interaction with tray
                } else if ($(e.target).attr('id') === 'nav-tray-close') {
                    // close tray if button touched or swiped
                    e.preventDefault();
                    trayMenuClose();
                } else {
                    // don't allow scrolling or interation anywhere else
                    e.preventDefault();
                }
            }
        };
    }

    function trayMenuOpen(e) {
        // iPhone starts to get jumpy when we add touchend, stop the click and the page refresh
        if(e){
            e.stopPropagation();
            e.preventDefault();
        }
        // open menu and add class to body to prevent scrolling
        $('body').addClass('tray-open freeze');
        // make the nav menu visible
        $('#nav-tray').addClass('open');
        // remove tray open listener on toggle menu icon
        $('#tray-toggle').off('click', trayMenuOpen);
        // move focus to newly visible menu
        $('#nav-main-menu').focus();
    }

    function trayMenuClose() {
        // remove class from body which displays menu
        $('body').removeClass('tray-open freeze');
        $('#nav-tray').removeClass('open');
        $('#tray-toggle').on('click', trayMenuOpen);
    }

    // trigger menu
    $(function() {
        trayMenuInit();
    });


    /*
    *  Compensate for header height when direct linking
    */

    $(function() {
        var pageHref = window.location.hash;
        if (pageHref) {
            if($(pageHref).length > 0) {
                // scroll a bit to avoid sticky header covering things
                $('html,body').animate({
                    scrollTop: $(pageHref).offset().top - $('.masthead').height() + 1
                }, 1000);
            }
        }
    });

    /*
    *  smooth scrolling
    *  http://css-tricks.com/snippets/jquery/smooth-scrolling/
    */

    $(function() {
        $('a[href*=#]:not([href=#])').not('.nosmoothscroll').click(function(e) {
            if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') || location.hostname == this.hostname) {
                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
                if (target.length) {
                    Mozilla.autoscrolling = true;

                    // animated scroll to target (+1 to make sure waypoint for anchor is triggered)
                    $('html,body').animate({
                        scrollTop: target.offset().top - $('.masthead').height() + 1
                    }, 1000, function() {
                        Mozilla.autoscrolling = false;
                    });
                    // give target keyboard focus
                    target.attr('tabindex', -1);
                    target.focus();
                    e.preventDefault();
                }
            }
        });
    });


})(jQuery);
