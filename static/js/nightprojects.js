// (function() {}); is the same as document.ready();
(function() {
    function aboutToggle(event) {
        event.preventDefault();
        $('#about-menu-1').toggle();
    }
    function otherToggle(event) {
        event.preventDefault();
        $('#other-menu-1').toggle();
    }
    $('#about-menu').click(aboutToggle);
    $('#other-menu').click(otherToggle);
})();
