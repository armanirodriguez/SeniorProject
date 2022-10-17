$('.nav-link').click(function (e) {
    localStorage.setItem('active-menu-item', $(this).attr('href'));
});

$(document).ready(function () {
    const activeMenuItem = $('.nav-link[href="' + localStorage.getItem('active-menu-item') + '"]').first();
    activeMenuItem && setActiveLink(activeMenuItem);
});
    
function setActiveLink($el) {
    $el.addClass('active');
    $el.click();
}