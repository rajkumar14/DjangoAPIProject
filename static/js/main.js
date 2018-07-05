$(document).ready(function () {
// rollover animation for main navig //
$('.navigation ul li').hover(function () {
	$('ul.submenu', $(this)).stop(true, true).slideDown(800);
},
function () {
$('ul.submenu', $(this)).fadeOut(600);
}
);
//expand close sitemap script
   $('#site_coll').css('display', 'none');
   		$('.site_map').click(function (e) {
                e.preventDefault();
                $('#site_coll', $(this).parent().parent()).slideToggle();
                if ($("#site_coll").is(':visible')) {
                    $("html, body").animate({
                        scrollTop: $("#site_coll").offset().top
                    });
                }
                $(this).toggleClass('sitemap-btn-act');
            });
});
