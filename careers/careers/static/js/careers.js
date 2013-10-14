(function(w, $) {
    'use strict';


    Modernizr.load({
        test: Mozilla.Test.isSmallScreen,
        yep: ['/static/js/libs/jquery.carouFredSel-6.2.1-packed.js','/static/js/libs/jquery.touchSwipe.min.js'],
        complete: animationInit
    });


    function animationInit() {
        communityVideoInit(); // TODO: delay until page loaded
    }

    /*
    *  Community & Culture
    *  - only one modal with video right now, could easily be adapted for more modals with different videos
    *  - modal and video created and inserted dynamically
    *  - video auto plays on modal open, auto pauses on modal close
    *  - modal can be closed by close button or by escape key
    */

    function communityEscapeWatch(e) {
        // if escape key is pressed, hide all modals
        if (e.keyCode == 27) {
            communityVideoHide(null);
        }
    }

    function communityVideoHide() {
        // stop video
        videojs('#video-interns').pause();

        // hide modal
        $('#community-interns-modal').removeClass('community-current');

        // removeescape listener
        $(document).off('keyup', communityEscapeWatch);

    }

    function communityVideoShow() {
        // show modal
        $('#community-interns-modal').addClass('community-current');

        // start video
        videojs('#video-interns').play();

        // add listener for escape key
        $(document).on('keyup', communityEscapeWatch);
    }


    function communityVideoInit() {
        if(!Mozilla.Test.isSmallScreen) {

            // create modal
            var videoModal = $('<div id="community-interns-modal" class="community-modal"></div>');

            // create and attach close/stop button
            var videoModalClose = $('<button class="community-modal-close">&times;</button>');
            videoModalClose.on('click', communityVideoHide);
            videoModalClose.appendTo(videoModal);

            // create and attach video wrapper
            var videoWrapper = $('<div class="community-video-wrapper"></div>');
            videoWrapper.appendTo(videoModal);

            // create video sources
            var videoInternsSrcMp4 = '<source src="//videos-cdn.mozilla.net/serv/interns/Interns-It%20can%20be%20you-720p-MPEG-4%282%29.mp4" type="video/mp4" />';
            var videoInternsSrcWebm = '<source src="//videos-cdn.mozilla.net/serv/interns/Interns-It%20can%20be%20you-720p-MPEG-4.webm" type="video/webm" />';
            var videoInternsSrcOgv = '<source src="//videos-cdn.mozilla.net/serv/interns/Interns-It%20can%20be%20you-720p-MPEG-4.theora.ogv" type="video/ogg" />';

            // create and attach video element
            // IE9 had issues when I appended the source to the video
            var videoInterns = $('<video id="video-interns" class="video-js vjs-sandstone-skin" controls preload="none" width="auto" height="auto">' +
                                videoInternsSrcMp4 +
                                videoInternsSrcWebm +
                                videoInternsSrcOgv +
                                '</video>');
            videoInterns.appendTo(videoWrapper);

            // append modal
            videoModal.appendTo('#community');

            // initialize video
            videojs('#video-interns');

            // create button to open modal & begin playing video
            var videoModalOpen = $('<button class="community-modal-open"></button>');
            videoModalOpen.on('click', communityVideoShow);
            videoModalOpen.appendTo('.community-box.community-interns');

            // make link a trigger as well
            var videoModalLink = $('.community-box.community-interns a');
            videoModalLink.on('click', function(e){
                e.preventDefault();
                communityVideoShow();
            });

        }

    }


})(window, window.jQuery);
