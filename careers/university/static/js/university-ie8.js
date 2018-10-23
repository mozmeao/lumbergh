(function() {
    'use strict';

    window.onload = function() {

        var hannahVideo = document.getElementById('video-morgan');
        hannahVideo.setAttribute('poster', '/static/img/video-thumbs/morgan-700.jpg');
        var mikeVideo = document.getElementById('video-harry');
        mikeVideo.setAttribute('poster', '/static/img/video-thumbs/harry-700.jpg');
        var jamesVideo = document.getElementById('video-samantha');
        jamesVideo.setAttribute('poster', '/static/img/video-thumbs/samantha-700.jpg');

        videojs("video-morgan");
        videojs("video-harry");
        videojs("video-samantha");

    };


})();
