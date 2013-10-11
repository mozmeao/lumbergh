(function(w, $) {
    'use strict';

    /*
    *   Pin position header
    */

    function positionPinInit() {
        // create container to hold place of pinned post header
        var positionHeadSpacer = $('<div />').attr('id', 'job-post-head-spacer');
        // set its height
        var positionHeadHeight = $('.job-post-head').height();
        positionHeadSpacer.height(positionHeadHeight);

        // attach
        positionHeadSpacer.prependTo('#job-post');

        // set waypoint to add and remove pin class
        var jobPost = $('#job-post');
        jobPost.waypoint( function(direction) {
             if (direction == 'down') {
                jobPost.addClass('pin');
            } else if (direction == 'up') {
                jobPost.removeClass('pin');
            }
        }, {
            offset: function() {
                return $('header.masthead').height();
            }
        });
    }

    $(function() {
        if(Mozilla.Test.isParallax) {
            positionPinInit();
        }
    });

})(window, window.jQuery);
