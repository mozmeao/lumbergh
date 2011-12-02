$(function() {
    $('#sections li a').click(function(ev) {
        ev.preventDefault();
        var self = $(this);

        self.parent().parent().find('a').removeClass('active');
        self.addClass('active');

        $('.role-group li a').addClass('disabled');
        if(self.data('jobtype') == 'all') {
            $('.role-group li a').removeClass('disabled');   
        } else {
            $('.role-group li a[data-jobtype="' + self.data('jobtype') + '"]').removeClass('disabled');
        }
    });

    $('body').on('click', '.role-group li a.disabled, .secondary li a.active', function(ev) {
        ev.preventDefault();
    });
});
