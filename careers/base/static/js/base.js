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
        $('#tray-toggle').on('click touchend' , trayMenuOpen);

        // add tray and copy nav there
        $('body').prepend('<div id="nav-tray" tabindex="-1"></div>');
        $('#nav-main-menu').clone().attr('id', '').appendTo('#nav-tray');

        // add close button
        $('body').prepend('<button id="nav-tray-close" type="button">Close</button>');
        $('#nav-tray-close').on('click touchend', trayMenuClose);

        // capture touch on body while tray open
        document.ontouchstart = function trayMenuHandleTouch(e) {
            if ($('body.tray-open').length) {
                if ($(e.target).parents('#nav-tray').length === 1) {
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

        // add class to body to prevent scrolling
        $('body').addClass('freeze');

        /* add class to body to display menu
        *  FF bug #625289 prevents the transition from animating if we apply the change together,
           so this gets a small delay
        */
        window.setTimeout(function trayMenuClass() {
                $('body').addClass('tray-open');
        }, 100);

        // move focus to newly visible menu
        $('#nav-tray-close').focus();
    }

    function trayMenuClose() {
       // remove class from body which displays menu
       $('body').removeClass('tray-open');

       /* remove class from body that prevents scrolling
       *  FF bug #625289 prevents the transition from animating if we apply the change together,
          so this gets a small delay
       */
       window.setTimeout(function trayMenuClassRemove() {
            $('body').removeClass('freeze');
       }, 100);
       $('#tray-toggle').focus();
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
