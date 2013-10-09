(function() {
    'use strict';

    window.onload = function() {

        var hannahVideo = document.getElementById('video-hannah');
        hannahVideo.setAttribute('poster', '/static/img/video-thumbs/hannah-700.jpg');
        var mikeVideo = document.getElementById('video-mike');
        mikeVideo.setAttribute('poster', '/static/img/video-thumbs/mike-700.jpg');
        var jamesVideo = document.getElementById('video-james');
        jamesVideo.setAttribute('poster', '/static/img/video-thumbs/james-700.jpg');

        videojs("video-hannah");
        videojs("video-mike");
        videojs("video-james");

    };


})();
