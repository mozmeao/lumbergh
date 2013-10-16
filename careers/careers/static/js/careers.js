(function($) {
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
})(jQuery);
