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
        return (window.navigator.msMaxTouchPoints || window.navigator.maxTouchPoints || Modernizr.touch);
    }

    function _checkParallaxOkay() {
        return (_checkBigScreen() && !_checkTouch());
    }

    return {
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
    if (window.navigator.msMaxTouchPoints || window.navigator.maxTouchPoints || Modernizr.touch) {
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
        $('#tray-toggle').click(function trayMenuToggle() {
            if ($('body.tray-open').length) {
                trayMenuClose();
            } else {
                trayMenuOpen();
            }
        });

        // add tray and copy nav there
        $('body').prepend('<div id="nav-tray" tabindex="-1"></div>');
        $('#nav-main-menu').clone().appendTo('#nav-tray');

        // add close button
        $('body').prepend('<button id="nav-tray-close" type="button">Close</button>');
        $('#nav-tray-close').on('click', trayMenuClose);

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

    function trayMenuOpen() {
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
    *  smooth scrolling
    *  http://css-tricks.com/snippets/jquery/smooth-scrolling/
    */

    $(function() {
        $('a[href*=#]:not([href=#])').click(function() {
            if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') || location.hostname == this.hostname) {
                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
                if (target.length) {
                    $('html,body').animate({
                        scrollTop: target.offset().top - $('.masthead').height()
                    }, 1000);
                    return false;
                }
            }
        });
    });



})(jQuery);
