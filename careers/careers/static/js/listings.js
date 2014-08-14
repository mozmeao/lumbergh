(function(w, $) {
    'use strict';

    /*
    *  Listings
    */

    // updates spans that appear instead of select box or labels on larger secreens
    function filtersMaskUpdate(e) {
        var filterSelect = $(e.target);
        var filterName = filterSelect.siblings('label').text();
        var filterText = filterSelect.find('option:selected').text();
        var filterMask = filterSelect.siblings('.listings-filter-mask');
        filterMask.text(filterText);

        ga('careersSnippetGA.send', 'event', 'Listings Filter', filterName, filterText);
    }

    // hides or shows filters on mobile
    function filtersToggle() {
        var listingsFilters = $('#listings-filters');
        // if open...
        if(listingsFilters.hasClass('open')) {
            // close filters
            listingsFilters.removeClass('open');
            // scroll up if fiter heading is now out of sight
            var endOfVisible = listingsFilters.offset().top - 5;
            var paddingFromTop = $('.masthead').height();
            if (endOfVisible < $('body').scrollTop()) {
                $('body').animate({scrollTop: endOfVisible - paddingFromTop}, '500', 'swing');
            }
        } else {
            listingsFilters.addClass('open');
        }
    }

    // go to the position details page for the job position clicked
    function listingGoToPosition(e) {
        var listingsTarget = $(e.target);
        var listingsRow = listingsTarget.closest('.position');
        var listingsLocation = listingsRow.find('.title a').prop('href');
        window.location = listingsLocation;
    }

    // create elements and add event listners for listings page
    function listingsInit() {
        // turn filter heading into a button to hide and show filters on mobile
        var filterHeadButton = $('<button type="button">Filters</button>');
        filterHeadButton.click(filtersToggle);
        filterHeadButton.appendTo('.listings-filters-head');

        // add done button to filters to hide filters on mobile
        var filterDoneWraper = $('<div class="listings-done"></div>');
        var filterDoneButton = $('<button class="cta" type="button">Done</button>');
        filterDoneButton.click(filtersToggle);
        filterDoneButton.appendTo(filterDoneWraper);
        filterDoneWraper.appendTo('#listings-filters');

        // create spans to echo select contents - they appear instead of label on larger screens
        $('.listings-filter').each( function() {
            var filter = $(this);
            var filterSelect = filter.find('select');
            var filterLabelText = filterSelect.find('option:selected').text();

            // create filter mask
            var filterMask = $('<span class="listings-filter-mask">' + filterLabelText + '</span>');
            // update text when select changes
            filterSelect.on('change', filtersMaskUpdate);
            //attach filter mask
            filterMask.appendTo(filter);
        });

        // make valid listings in the table clickable
        $('#listings-positions tbody tr.position').on('click', listingGoToPosition);
    }

    // init listings
    $(function() {
        listingsInit();
    });

})(window, window.jQuery);
