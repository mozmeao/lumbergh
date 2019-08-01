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
            };

            // Hide table and show all positions.
            this.$positionTable.hide();
            this.$emptyFilterMessage.hide();
            this.$positionTable.find('.position').removeClass('hidden').show();

            // Hide positions that don't match the current filters.
            this.filterPositions('type', filters['position_type']);
            this.filterPositions('team', filters['team']);
            this.filterLocations(filters['location']);


            // If there aren't any positions being shown, show the no-results message.
            if (this.$positionTable.find('.position:not(.hidden)').length < 1) {
                this.$emptyFilterMessage.show();
            }

            // Get rid of unset filters.
            for (var k in filters) {
                if (filters.hasOwnProperty(k) && !filters[k]) {
                    delete filters[k];
                }
            }

            // Build a querystring from populated filters.
            var querystring = $.param(filters);

            // Preserve Google Analytics parameters.
            var ga_parameters = window.location.search.substr(1).split('&').filter(
                function(parameter) {
                    return parameter.indexOf('utm_') === 0;
                }
            );
            if (querystring.length && ga_parameters.length) {
                querystring += '&';
            }
            querystring += ga_parameters.join('&');

            if (querystring.length) {
                querystring = '?' + querystring;
            }

            // Replace history state with this filtered state.
            window.history.replaceState(filters, 'Filtered', location.pathname + querystring);

            this.$positionTable.show();
        },

        /**
         * Hide any positions that do have the correct value for the given field.
         */
        filterPositions: function(field, value) {
            if (!value)
                return;

            this.$positionTable.find('tr.position').each(function(index, element) {
                var data = element.dataset[field];
                if (data.indexOf(value + ',') === -1) {
                    element.classList.add('hidden');
                }
            });
        },
        filterLocations: function(value) {
            if (!value)
                return;

            this.$positionTable.find('tr.position').each(function(index, element) {
                var data = element.dataset.location;

                // When user selects 'Remote' only list jobs explicitly marked
                // Remote otherwise list jobs matching value (which is a mozilla
                // office) and those marked as 'All Offices'
                if (value === 'Remote') {
                    if (data.indexOf(value + ',') === -1) {
                        element.classList.add('hidden');
                    }
                }
                else if (data.indexOf(value + ',') === -1 && data.indexOf('All Offices,') === -1) {
                    element.classList.add('hidden');
                }
            });
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
