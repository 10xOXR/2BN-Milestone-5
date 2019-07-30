$(document).ready(function () {

    function initMaterialize() {
        $('.sidenav').sidenav({
            menuWidth: 500,
            edge: 'left',
            closeOnClick: true,
            draggable: true
        });

        $('.modal').modal();

        $('select').formSelect();
        $('.parallax').parallax();
    }

    initMaterialize();
});

$("#year").html(new Date().getFullYear());
