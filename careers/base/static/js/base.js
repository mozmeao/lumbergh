(function (Mzp) {
    'use strict';

    Mzp.Navigation.init();
    Mzp.Menu.init();

    // wire up modal when clicking "Internships" in nav (temporary)
    var content = document.getElementById('internships-modal');

    var link = document.getElementById('ga-nav-internships');

    link.addEventListener('click', function (e) {
        e.preventDefault();
        Mzp.Modal.createModal(e.target, content, {
            title: 'Please check back',
            closeText: 'Close modal'
        });
    }, false);

})(window.Mzp);
