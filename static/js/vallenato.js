

$(document).ready(function()
{
	//Add Inactive Class To All Accordion Headers
	$('.accordion-header').toggleClass('inactive-header');
	
	//Set The Accordion Content Width
	var contentwidth = $('.accordion-header').width();
	
//	//Open The First Accordion Section When Page Loads
//	$('.accordion-header').first().toggleClass('active-header').toggleClass('inactive-header');
//	$('.accordion-content').first().slideDown().toggleClass('open-content');
	
	// The Accordion Effect
	$('.accordion-header').click(function () {
		if($(this).is('.inactive-header')) {
			// comment below line if you want to open all items  -- pradeep
			$('.active-header').toggleClass('active-header').toggleClass('inactive-header').next().slideToggle().toggleClass('open-content');
			$(this).toggleClass('active-header').toggleClass('inactive-header');
			$(this).next().slideToggle().toggleClass('open-content');
		}
		
		else {
			$(this).toggleClass('active-header').toggleClass('inactive-header');
			$(this).next().slideToggle().toggleClass('open-content');
		}
	});
	
    //Add Inactive Class To All Accordion Headers
	$('.accordion-header1').toggleClass('inactive-header1');
	
	//Set The Accordion Content Width
	var contentwidth = $('.accordion-header1').width();
	
	/*//Open The First Accordion Section When Page Loads
	$('.accordion-header').first().toggleClass('active-header').toggleClass('inactive-header');
	$('.accordion-content').first().slideDown().toggleClass('open-content');*/
	
	// The Accordion Effect
	$('.accordion-header1').click(function () {
		if($(this).is('.inactive-header1')) {
			// comment below line if you want to open all items  -- pradeep
			$('.active-header1').toggleClass('active-header1').toggleClass('inactive-header1').next().slideToggle().toggleClass('open-content');
			$(this).toggleClass('active-header1').toggleClass('inactive-header1');
			$(this).next().slideToggle().toggleClass('open-content');
		}
		
		else {
			$(this).toggleClass('active-header1').toggleClass('inactive-header1');
			$(this).next().slideToggle().toggleClass('open-content');
		}
	});
    
    //Add Inactive Class To All Accordion Headers
	$('.accordion-header2').toggleClass('inactive-header2');
	
	//Set The Accordion Content Width
	var contentwidth = $('.accordion-header2').width();
	
	/*//Open The First Accordion Section When Page Loads
	$('.accordion-header').first().toggleClass('active-header').toggleClass('inactive-header');
	$('.accordion-content').first().slideDown().toggleClass('open-content');*/
	
	// The Accordion Effect
	$('.accordion-header2').click(function () {
		if($(this).is('.inactive-header2')) {
			// comment below line if you want to open all items  -- pradeep
			$('.active-header2').toggleClass('active-header2').toggleClass('inactive-header2').next().slideToggle().toggleClass('open-content');
			$(this).toggleClass('active-header2').toggleClass('inactive-header2');
			$(this).next().slideToggle().toggleClass('open-content');
		}
		
		else {
			$(this).toggleClass('active-header2').toggleClass('inactive-header2');
			$(this).next().slideToggle().toggleClass('open-content');
		}
	});
	
	return false;
});

