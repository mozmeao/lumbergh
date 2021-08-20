/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

(function() {
    'use strict';
    var _gaAccountCode = document.documentElement.getAttribute('data-ga-code');

    // If doNotTrack is not enabled, it is ok to add GA
    // @see https://bugzilla.mozilla.org/show_bug.cgi?id=1217896 for more details
    if (typeof Mozilla.dntEnabled === 'function' && !Mozilla.dntEnabled() && _gaAccountCode) {
        // Hidden google isogram magic wooooooooooooo
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
        // ^^^ GHOSTS ^^^

        if (_gaAccountCode) {
            ga('create', _gaAccountCode, {'name': 'careersSnippetGA'});
            ga('careersSnippetGA.send', 'pageview');
        }
    }
})();
