(function(w, $) {
    'use strict';

    $(function() {
        // Create custom tracking vars for the current position being viewed.
        _gaq.push(['_setCustomVar', 1, 'Team', $('.job-post-team').text(), 3]);
        _gaq.push(['_setCustomVar', 2, 'Location of Job', $('#job-post').data('locationFilter'), 3]);
        _gaq.push(['_trackEvent', 'CV Dummy', 'on load', undefined, undefined, true]);
    });

})(window, window.jQuery);
