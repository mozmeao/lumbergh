/**
 * Google Analytics Event Tracking
 */
;(function($) {
    'use strict';

    var $root = $(':root');
    function trackClick(selector, trackEventArgs) {
        trackEventArgs.unshift('careersSnippetGA.send', 'event');
        $root.on('click', selector, function() {
            ga.apply(ga, trackEventArgs);
        });
    }

    // If window.location.hash is set on page load, and the hash matches an
    // element that's being tracked, we need to disable all scroll events until
    // that element is reached by the browser. Otherwise, scroll events will be
    // triggered for every element above the linked one.
    var ignoreScrollEvents = false;
    var trackedIds = [];
    function trackScroll(id, trackEvent) {
        trackedIds.push(id);
        trackEvent.unshift('careersSnippetGA.send', 'event');

        $(id).waypoint(function () {
            // Ignore events unless we have reached the correct element.
            if (ignoreScrollEvents) {
                if (window.location.hash === id) {
                    ignoreScrollEvents = false;
                }
                return;
            }

            // Only check for autoscrolling if Mozilla global exists.
            if (!window.Mozilla || !window.Mozilla.autoscrolling) {
                ga.apply(ga, trackEvent);
            }
        });
    }

    /* Nav
    ***************************************************************************/
    trackClick('.ga-nav-home', ['Top Navigation', 'Click', 'Home']);
    trackClick('.ga-nav-home-logo', ['Top Navigation', 'Click', 'Home Logo']);
    trackClick('.ga-nav-team', ['Top Navigation', 'Click', 'Teams & Roles']);
    trackClick('.ga-nav-life', ['Top Navigation', 'Click', 'Life At Mozilla']);
    trackClick('.ga-nav-locations', ['Top Navigation', 'Click', 'Locations']);
    trackClick('.ga-nav-university', ['Top Navigation', 'Click', 'University']);
    trackClick('.ga-nav-listing', ['Top Navigation', 'Click', 'Job Listing']);


    /* Careers
    ***************************************************************************/
    trackClick('.ga-career-banner-listings', ['Career Banner Interactions', 'Top Banner Click', 'Job Listing']);
    trackClick('.ga-career-banner-internship', ['Career Banner Interactions', 'Top Banner Click', 'University']);
    trackClick('.ga-career-banner-volunteer', ['Career Banner Interactions', 'Top Banner Click', 'Volunteer']);

    trackClick('.ga-career-banner-listings-bottom', ['Career Banner Interactions', 'Bottom Banner Click', 'Job Listing']);
    trackClick('.ga-career-banner-internship-bottom', ['Career Banner Interactions', 'Bottom Banner Click', 'University']);
    trackClick('.ga-career-banner-volunteer-bottom', ['Career Banner Interactions', 'Bottom Banner Click', 'Volunteer']);

    trackScroll('#teams', ['Careers Home', 'scroll', 'Teams & Roles']);
    trackScroll('#life', ['Careers Home', 'scroll', 'Life At Mozilla']);
    trackScroll('#community', ['Careers Home', 'scroll', 'Community & Culture']);
    trackScroll('#locations', ['Careers Home', 'scroll', 'Locations']);
    trackScroll('#next', ['Careers Home', 'scroll', 'Are You Ready To Join']);


    /* Careers > Teams & Roles
    ***************************************************************************/
    trackClick('.teams-volunteer', ['Teams & Roles Interactions', 'link click', 'Looking to Volunteer']);
    trackClick('.teams-back', ['Teams & Roles Interactions', 'Menu Back Button']);

    // Primary hex navigation
    $root.on('click', '#teams-intro .teams-nav a', function() {
        var name = $(this).find('strong').text();
        ga('careersSnippetGA.send', 'event', 'Teams & Roles Interactions', 'Primary Nav Click', name);
    });

    // Secondary hex navigation
    $root.on('click', '#teams-nav-second a', function() {
        var name = $(this).find('strong').text();
        ga('careersSnippetGA.send', 'event', 'Teams & Roles Interactions', 'Secondary Left Side Nav Click', name);
    });

    // View Open Position buttons
    $root.on('click', '.teams-team a.cta', function() {
        var name = $(this).siblings('.team-head').text();
        ga('careersSnippetGA.send', 'event', 'Teams & Roles Interactions', 'View Open Positions', name);
    });


    /* Careers > Community & Culture
    ***************************************************************************/
    $root.on('click', '.community-box a', function() {
        var href = $(this).attr('href');
        ga('careersSnippetGA.send', 'event', 'Community & Culture Interactions', 'Link Click', href);
    });


    /* Careers > Locations
    ***************************************************************************/
    $root.on('click', 'a.location-link', function() {
        var city = $(this).text();
        ga('careersSnippetGA.send', 'event', 'Mozilla Location Map Interactions', 'Click', city);
    });


    /* Careers > Life Gallery
    ***************************************************************************/
    trackClick('#life-blocks-prev', ['What Makes Us Interactions', 'Left Carousel Click']);
    trackClick('#life-blocks-next', ['What Makes Us Interactions', 'Right Carousel Click']);


    /* University
    ***************************************************************************/
    trackClick('.ga-apply-banner', ['/university/ Interactions', 'Apply Now Clicks', 'Apply Now: Once a Mozillian']);
    trackClick('.ga-want-to-know', ['/university/ Interactions', 'Apply Now Clicks', 'Apply Now: Things You\'ll Want to Know']);
    trackClick('.ga-apply-now', ['/university/ Interactions', 'Apply Now Clicks', 'Apply Now: Ready to Start']);
    trackClick('.meet-us-on-campus', ['/university/ Interactions', 'Clicks', 'Meet Us On Campus']);

    trackScroll('#different', ['University', 'scroll', 'Its Different']);
    trackScroll('#know-boxes', ['University', 'scroll', 'Things youll want to know']);
    trackScroll('#videos', ['University', 'scroll', 'Videos']);
    trackScroll('#testimonials', ['University', 'scroll', 'Testimonials']);
    trackScroll('#meetus', ['University', 'scroll', 'Meet Us']);
    trackScroll('#gallery', ['University', 'scroll', 'Gallery']);


    /* Listings
    ***************************************************************************/
    trackClick('.ga-job-listing', ['Job List', 'Click', 'Job Detail']);
    trackClick('.ga-job-listing-detail', ['Job Detail', 'Click', 'Job Detail']);

    // Apply for this job button
    $root.on('click', '.ga-job-listing-apply', function() {
        var jobName = $('.job-post-title').text();
        ga('careersSnippetGA.send', 'event', 'Job Description Page Interactions', 'Apply for this Job', jobName);
    });


    // Ignore scroll events if the anchor we want is currently being tracked.
    // Do not call trackScroll past this line.
    ignoreScrollEvents = trackedIds.indexOf(window.location.hash) !== -1;
})(jQuery);
