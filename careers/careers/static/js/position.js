(function(w, $) {
    'use strict';

    $(function() {
        // Create custom tracking vars for the current position being viewed.
        ga('careersSnippetGA.set', 'dimension1', $('.job-post-team').text());
        ga('careersSnippetGA.set', 'dimension2', $('#job-post').data('locationFilter'));
        ga('careersSnippetGA.send', 'event', 'CV Dummy', 'on load', undefined, undefined, true);
    });

})(window, window.jQuery);
