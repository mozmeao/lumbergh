// All click based event tracking should go here 

$(function() {
    'use strict';

    function trackClick(className, trackEvent) {
        $(className).click(function() {
            _gaq.push(trackEvent);        
        }); 
    }

    /* Nav */
    trackClick('.ga-nav-home', ['_trackEvent', 'Top Navigation', 'Click', 'Home']);  
    trackClick('.ga-nav-home-logo', ['_trackEvent', 'Top Navigation', 'Click', 'Home Logo']);      
    trackClick('.ga-nav-team', ['_trackEvent', 'Top Navigation', 'Click', 'Teams Roles']); 
    trackClick('.ga-nav-life', ['_trackEvent', 'Top Navigation', 'Click', 'Life At Mozilla']);          
    trackClick('.ga-nav-locations', ['_trackEvent', 'Top Navigation', 'Click', 'Locations']);   
    trackClick('.ga-nav-university', ['_trackEvent', 'Top Navigation', 'Click', 'University']);                     
    trackClick('.ga-nav-listing', ['_trackEvent', 'Top Navigation', 'Click', 'Job Listing']);

    /* Careers Click Tracking */
    trackClick('.ga-career-banner-listings', ['_trackEvent', 'Career Banner', 'Click', 'Job Listing']);
    trackClick('.ga-career-banner-internship', ['_trackEvent', 'Career Banner', 'Click', 'University']);
    trackClick('.ga-career-banner-volunteer', ['_trackEvent', 'Career Banner', 'Click', 'Volunteer']);    

    trackClick('.ga-career-banner-listings-bottom', ['_trackEvent', 'Career Banner Bottom', 'Click', 'Job Listing']);
    trackClick('.ga-career-banner-internship-bottom', ['_trackEvent', 'Career Banner Bottom', 'Click', 'University']);
    trackClick('.ga-career-banner-volunteer-bottom', ['_trackEvent', 'Career Banner Bottom', 'Click', 'Volunteer']);      

    /* University Click Tracking */
    trackClick('.ga-apply-banner', ['_trackEvent', 'University Banner', 'Click', 'Apply Now']);
    trackClick('.ga-want-to-know', ['_trackEvent', 'University Want To Know', 'Click', 'Apply Now']);
    trackClick('.ga-apply-now', ['_trackEvent', 'University Apply Now', 'Click', 'Apply Now']);

    
    /* Listings Click Tracking */
    trackClick('.ga-job-listing', ['_trackEvent', 'Job List', 'Click', 'Job Detail']);
    trackClick('.ga-job-listing-detail', ['_trackEvent', 'Job Detail', 'Click', 'Job Detail']);
    trackClick('.ga-job-listing-apply', ['_trackEvent', 'Jobvite Apply Now', 'Click', 'Job Apply']);

});
