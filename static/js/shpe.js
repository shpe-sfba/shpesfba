$(document).ready(function() {
    /* Enable tooltips */
    $('[data-toggle="tooltip"]').tooltip(); 

    /* Membership Accordion */ 
    $('.collapse.in').prev('.panel-heading').addClass('active');
    $('#accordion, #bs-collapse').on('show.bs.collapse', function(a) {
        $(a.target).prev('.panel-heading').addClass('active');
    }).on('hide.bs.collapse', function(a) {
        $(a.target).prev('.panel-heading').removeClass('active');
    });
});