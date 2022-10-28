$('.community-link').click(function (e) {
    localStorage.setItem('active-community-item', $(this).attr('id'));
});

$(document).ready(function () {
    const activeCommunityItem = $('.community-link[id="' + localStorage.getItem('active-community-item') + '"]').first();
    activeCommunityItem.addClass('community-active');
    //activeCommunityItem && setActiveLink(activeCommunityItem);
});

/*
function removeCommunityActiveLink() {
    const activeCommunityItem = $('.community-link[id="' + localStorage.getItem('active-community-item') + '"]').first();
    activeCommunityItem.removeClass('community-active');
    localStorage.setItem('active-community-item', "");
}*/

/*$('.community-link-removal').click(function (e) {
    removeCommunityActiveLink();
});*/