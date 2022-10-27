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



function removeActiveLink() {
    const activeMenuItem = $('.nav-link[href="' + localStorage.getItem('active-menu-item') + '"]').first();
    activeMenuItem && setActiveLink(activeMenuItem);
    activeMenuItem.removeClass('active');
    localStorage.setItem('active-menu-item', "");
}

$('#profile-links').click(function (e) {
    removeActiveLink();
});