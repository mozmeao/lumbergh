(function(w, $) {
    'use strict';


    Modernizr.load({
        test: Mozilla.Test.isSmallScreen,
        //yep: ['/static/js/libs/jquery.carouFredSel-6.2.1-packed.js','/static/js/libs/jquery.touchSwipe.min.js'],
        complete: animationInit
    });


    function animationInit() {
        locationsInit();
    }

    /*
    *  Locations
    *  - two ways to show details:
    *    - on mobile a select box can be used to pick one
    *    - on desktop the user can click the link
    *  - both ways are initialized and the associated form controls are hidden by media queries
    *  - details can be hidden by:
    *    - selecting a new location details
    *    - pressing escape
    *    - on mobile: navgigating to the empty form option
    */

    function locationsEscapeWatch(e) {
        // if escape key is pressed, hide all modals
        if (e.keyCode == 27) {
            locationsHide(null);
        }
    }

    function locationsShow(locationId) {
        // remove class from any current one
        $('.location-current').removeClass('location-current');

        // add class to the one with matching ID
        $('#' + locationId).addClass('location-current');

        // add watcher for escape key
        $(document).on('keyup', locationsEscapeWatch);
    }

    function locationsHide() {
        // remove class from currently visible
        $('.location-current').removeClass('location-current');

        // remove watcher for escape key
        $(document).off('keyup', locationsEscapeWatch);
    }

    function locationsToggle(locationId) {
        if(locationId){
            locationsShow(locationId);
        } else {
            locationsHide();
        }
    }

    function locationsModalInit() {
        var locations = $('.locations-location');

        // loop through locations links
        $(locations).each( function() {
            var location = $(this);

            // create close button
            var locationsModalClose = $('<button class="location-close">&times;</button>');
            locationsModalClose.on('click', locationsHide);

            // add close button
            var locationDetails = location.find('.location-details');
            locationDetails.prepend(locationsModalClose);

            // hijack links
            var locationLink = location.find('.location-link');
            var locationId = this.id;
            $(locationLink).on('click', function(e) {
                e.preventDefault();
                locationsToggle(locationId);
            });
        });

    }

    function locationsParallaxInit() {
        // TODO: parallax being left for last
    }

    function locationsMenuInit() {
        // create container, select, and label
        var locationMenuContain = $('<div class="locations-menu"></div>');
        var locationsLabel = $('<label class="locations-label" for="locations-select">Select Location</label>');
        var locationsMenu = $('<select id="locations-select"></select>');
        var locationsDefaultOption = $('<option />');
        locationsDefaultOption.appendTo(locationsMenu);

        // get locations
        var locations = $('.locations-location');

        // create option tag for each location
        $(locations).each(function() {
            // get name
            var locationName = $(this).find('.location-link').text();

            // get id of location
            var locationId = this.id;

            // create option
            var locationOption = $('<option value="' + locationId + '">' + locationName + '</option>');

            // attach option
            locationOption.appendTo(locationsMenu);

        });

        // when contents of select change, change the visible location
        locationsMenu.on('change', function(e){
            var locationNew = $(e.target).val();
            locationsToggle(locationNew);
        });

        // attach menu to page
        locationsMenu.appendTo(locationMenuContain);
        locationsLabel.appendTo(locationMenuContain);
        locationMenuContain.insertBefore('.locations-list');
    }

    function locationsInit() {
        // create drop down for mobile
        locationsMenuInit();
        // create modal for larger
        locationsModalInit();

        if(Mozilla.Test.isParallax){
            locationsParallaxInit();
        }
    }


})(window, window.jQuery);
