;(function($) {
    'use strict';

    /**
     * Monitors inputs and filters a list of positions when they change.
     */
    function PositionFilters(typeInput, teamInput, locationInput, positionTable) {
        this.$typeInput = $(typeInput);
        this.$teamInput = $(teamInput);
        this.$locationInput = $(locationInput);
        this.$positionTable = $(positionTable);
        this.$emptyFilterMessage = this.$positionTable.find('.empty-filter-message');
    }

    PositionFilters.prototype = {
        /**
         * Mapping of location filter value -> Locations it matches
         */
        locationsFor: {
            remote: ['Remote', 'All'],
            berlin: ['Berlin', 'Europe', 'Any Office', 'Remote', 'All'],
            boston: ['Boston', 'US', 'North America', 'Any Office', 'Remote', 'All'],
            london: ['London', 'Europe', 'Any Office', 'Remote', 'All'],
            mountainview: ['Mountain View', 'Bay Area', 'US', 'North America', 'Any Office', 'Remote', 'All'],
            newzealand: ['New Zealand', 'Any Office', 'Remote', 'All'],
            paris: ['Paris', 'Europe', 'Any Office', 'Remote', 'All'],
            portland: ['Portland', 'US', 'North America', 'Any Office', 'Remote', 'All'],
            sanfrancisco: ['San Francisco', 'Bay Area', 'US', 'North America', 'Any Office', 'Remote', 'All'],
            toronto: ['Toronto', 'North America', 'Any Office', 'Remote', 'All'],
            vancouver: ['Vancouver', 'North America', 'Any Office', 'Remote', 'All'],
            bayarea: ['Mountain View', 'San Francisco', 'Bay Area', 'US', 'North America', 'Any Office', 'Remote', 'All'],
            latinamerica: ['Latin America', 'Remote', 'All'],
            northamerica: ['Boston', 'Portland', 'Mountain View', 'San Francisco', 'Toronto', 'Vancouver', 'Bay Area', 'US', 'North America', 'Any Office', 'Remote', 'All'],
            europe: ['Berlin', 'London', 'Paris', 'Europe', 'Any Office', 'Remote', 'All', 'All']
        },

        /**
         * Bind onFilterChange to the change events for each input.
         */
        bindEvents: function() {
            var self = this;
            var callback = function() {
                self.onFilterChange();
            };

            this.$typeInput.change(callback);
            this.$teamInput.change(callback);
            this.$locationInput.change(callback);
        },

        /**
         * When a filter changes, refresh the position list.
         */
        onFilterChange: function() {
            var filters = {
                'position_type': this.$typeInput.val(),
                'team': this.$teamInput.val(),
                'location': this.$locationInput.val()
            }

            // Hide table and show all positions.
            this.$positionTable.hide();
            this.$emptyFilterMessage.hide();
            this.$positionTable.find('.position').removeClass('hidden').show();

            // Hide positions that don't match the current filters.
            this.filterPositions('type', filters['position_type']);
            this.filterPositions('team', filters['team']);
            this.filterPositionsByLocation(filters['location']);

            // If there aren't any positions being shown, show the no-results message.
            if (this.$positionTable.find('.position:not(.hidden)').length < 1) {
                this.$emptyFilterMessage.show();
            }

            // Save filter state in browser history.
            if (Modernizr.history) {

                // Get rid of unset filters.
                for (var k in filters) {
                    if (filters.hasOwnProperty(k) && !filters[k]) {
                        delete filters[k];
                    }
                }

                // Build a querystring from populated filters.
                var querystring = $.param(filters)
                if (!$.isEmptyObject(filters)) {
                    querystring = "?" + querystring;
                }

                // Replace history state with this filtered state.
                window.history.replaceState(filters, 'Filtered', location.pathname + querystring);
            }

            this.$positionTable.show();
        },

        /**
         * Hide any positions that do have the correct value for the given field.
         */
        filterPositions: function(field, value) {
            if (value !== '') {
                var selector = '.position:not([data-' + field + '="' + value + '"])';
                this.$positionTable.find(selector).addClass('hidden').hide();
            }
        },

        /**
         * Hide any positions that are not located in a location matching the given filter value.
         */
        filterPositionsByLocation: function(filterValue) {
            if (filterValue !== '' && this.locationsFor.hasOwnProperty(filterValue)) {
                var validLocations = this.locationsFor[filterValue];
                var positions = this.$positionTable.find('.position');
                for (var k = 0; k < validLocations.length; k++) {
                    positions = positions.not('[data-location*="' + validLocations[k] + '"]');
                }

                positions.addClass('hidden').hide();
            }
        }
    };

    $(function() {
        var inputs = document.getElementById('listings-filters').elements;
        var filters = new PositionFilters(inputs.position_type, inputs.team, inputs.location,
                                          document.getElementById('listings-positions'));
        filters.bindEvents();
        filters.onFilterChange(); // Trigger sorting on initial load for querystring arguments.
    });
})(jQuery);
