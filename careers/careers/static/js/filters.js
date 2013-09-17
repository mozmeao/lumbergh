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
            remote: ['Remote'],
            berlin: ['Berlin', 'Europe', 'Any Office'],
            boston: ['Boston', 'US', 'Any Office'],
            london: ['London', 'Europe', 'Any Office'],
            mountainview: ['Mountain View', 'Bay Area', 'US', 'Any Office'],
            newzealand: ['New Zealand', 'Any Office'],
            paris: ['Paris', 'Europe', 'Any Office'],
            portland: ['Portland', 'US', 'Any Office'],
            sanfrancisco: ['San Francisco', 'Bay Area', 'US', 'Any Office'],
            toronto: ['Toronto', 'Any Office'],
            vancouver: ['Vancouver', 'Any Office']
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
            // Hide table and show all positions.
            this.$positionTable.hide();
            this.$emptyFilterMessage.hide();
            this.$positionTable.find('.position').removeClass('hidden').show();

            // Hide positions that don't match the current filters.
            this.filterPositions('type', this.$typeInput.val());
            this.filterPositions('team', this.$teamInput.val());
            this.filterPositionsByLocation(this.$locationInput.val());

            // If there aren't any positions being shown, show the no-results message.
            if (this.$positionTable.find('.position:not(.hidden)').length < 1) {
                this.$emptyFilterMessage.show();
            }

            this.$positionTable.show();
        },

        /**
         * Hide any positions that do have the correct value for the given field.
         */
        filterPositions: function(field, value) {
            if (value !== 'all') {
                var selector = '.position:not([data-' + field + '="' + value + '"])';
                this.$positionTable.find(selector).addClass('hidden').hide();
            }
        },

        /**
         * Hide any positions that are not located in a location matching the given filter value.
         */
        filterPositionsByLocation: function(filterValue) {
            if (this.locationsFor.hasOwnProperty(filterValue)) {
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
        var inputs = document.getElementById('position-filters').elements;
        var filters = new PositionFilters(inputs.type, inputs.team, inputs.location,
                                          document.getElementById('positions'));
        filters.bindEvents();
    });
})(jQuery);
