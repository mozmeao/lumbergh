/**
 * Google Analytics Event Tracking
 */
; (function() {
    'use strict';

    var noopfn = function () {};
    window.ga = window.ga || noopfn;

    var root = document.documentElement;
    function trackClick(selector, trackEventArgs) {
        trackEventArgs.unshift('careersSnippetGA.send', 'event');

        var target = document.querySelector(selector);

        root.addEventListener('click', function(e) {

        });
        /*
        $root.on('click', selector, function () {
            ga.apply(ga, trackEventArgs);
        });
        */
    }

    /* Nav
    ***************************************************************************/
    trackClick('#ga-nav-home-logo', ['Top Navigation', 'Click', 'Home Logo']);
    trackClick('#ga-nav-life', ['Top Navigation', 'Click', 'Life At Mozilla']);
    trackClick('#ga-nav-locations', ['Top Navigation', 'Click', 'Locations']);
    trackClick('#ga-nav-internships', ['Top Navigation', 'Click', 'Internships']);
    trackClick('#ga-nav-listing', ['Top Navigation', 'Click', 'Job Listing']);

    /* Listings
    ***************************************************************************/
    /*
    trackClick('.ga-job-listing', ['Job List', 'Click', 'Job Detail']);
    trackClick('.ga-job-listing-detail', ['Job Detail', 'Click', 'Job Detail']);

    // Apply for this job button
    $root.on('click', '.ga-job-listing-apply', function () {
        var jobName = $('.job-post-title').text();
        ga('careersSnippetGA.send', 'event', 'Job Description Page Interactions', 'Apply for this Job', jobName);
    });
    */
})();
