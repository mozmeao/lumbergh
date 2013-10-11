(function($) {
    'use strict';

    $(document).on('click', '.listings-link', function(e) {
        var openForApplications = $('body').data('openForApplications');
        if (!openForApplications) {
            e.preventDefault();
            window.location.hash = 'apply';
        }
    });
})(jQuery);
