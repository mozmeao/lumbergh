// All click based event tracking should go here 

$(function() {
    'use strict';

    function trackClick(className, trackEvent) {
        $(className).click(function() {
            _gaq.push(trackEvent);        
        }); 
    }

    /* Nav */
    trackClick('.ga-nav-listing', ['_trackEvent', 'Job Listing', 'Click', 'Nav Listing']);

    /* Careers Click Tracking */
    trackClick('.ga-career-banner-listings', ['_trackEvent', 'Job Listing', 'Click', 'Career Banner']);
    trackClick('.ga-career-banner-internship', ['_trackEvent', 'University', 'Click', 'Career Banner']);
    trackClick('.ga-career-banner-volunteer', ['_trackEvent', 'Volunteer', 'Click', 'Career Banner']);    

    trackClick('.ga-career-banner-listings-bottom', ['_trackEvent', 'Job Listing', 'Click', 'Career Banner Bottom']);
    trackClick('.ga-career-banner-internship-bottom', ['_trackEvent', 'University', 'Click', 'Career Banner Bottom']);
    trackClick('.ga-career-banner-volunteer-bottom', ['_trackEvent', 'Volunteer', 'Click', 'Career Banner Bottom']);      

    /* University Click Tracking */
    trackClick('.ga-apply-banner', ['_trackEvent', 'Apply Now', 'Click', 'University Banner']);
    trackClick('.ga-want-to-know', ['_trackEvent', 'Apply Now', 'Click', 'University Want To Know']);
    trackClick('.ga-apply-now', ['_trackEvent', 'Apply Now', 'Click', 'University Apply Now']);
    
    /* Listings Click Tracking */
    trackClick('.ga-job-listing', ['_trackEvent', 'Job Detail', 'Click', 'Job List']);
    trackClick('.ga-job-listing-detail', ['_trackEvent', 'Job Detail', 'Click', 'Job Detail']);
    trackClick('.ga-job-listing-apply', ['_trackEvent', 'Job Apply', 'Click', 'Jobvite Apply Now']);

});
