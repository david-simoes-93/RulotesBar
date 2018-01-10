
// NIVO LIGHTBOX
$('.iso-box-section a').nivoLightbox({
        effect: 'fadeScale',
    });

// ISOTOPE FILTER
jQuery(document).ready(function($){

	if ( $('.iso-box-wrapper').length > 0 ) { 

	    var $container 	= $('.iso-box-wrapper'), 
	    	$imgs 		= $('.iso-box img');

	    $container.imagesLoaded(function () {

	    	$container.isotope({
				layoutMode: 'fitRows',
				itemSelector: '.iso-box'
	    	});

	    	$imgs.load(function(){
	    		$container.isotope('reLayout');
	    	})

	    });

	    //filter items on button click

	    $('.filter-wrapper li a').click(function(){

	        var $this = $(this), filterValue = $this.attr('data-filter');

			$container.isotope({ 
				filter: filterValue,
				animationOptions: { 
				    duration: 750, 
				    easing: 'linear', 
				    queue: false, 
				}              	 
			});	            

			// don't proceed if already selected 

			if ( $this.hasClass('selected') ) { 
				return false; 
			}

			var filter_wrapper = $this.closest('.filter-wrapper');
			filter_wrapper.find('.selected').removeClass('selected');
			$this.addClass('selected');

	      return false;
	    }); 

	}

});

jQuery(document).ready(function($){

    if ( $('.iso2-box-wrapper').length > 0 ) {

        var $container 	= $('.iso2-box-wrapper'),
            $imgs 		= $('.iso2-box img');



        $container.imagesLoaded(function () {

            $container.isotope({
                layoutMode: 'fitRows',
                itemSelector: '.iso2-box'
            });

            $imgs.load(function(){
                $container.isotope('reLayout');
            })

        });

        //filter items on button click

        $('.filter2-wrapper li a').click(function(){

            var $this = $(this), filterValue = $this.attr('data-filter');

            $container.isotope({
                filter: filterValue,
                animationOptions: {
                    duration: 750,
                    easing: 'linear',
                    queue: false,
                }
            });

            // don't proceed if already selected

            if ( $this.hasClass('selected') ) {
                return false;
            }

            var filter_wrapper = $this.closest('.filter2-wrapper');
            filter_wrapper.find('.selected').removeClass('selected');
            $this.addClass('selected');

            return false;
        });

    }

});


jQuery(document).ready(function($){
    document.getElementById('pfmain').click();
    document.getElementById('pf2main').click();
});

jQuery(document).ready(function($){
    $("#c1pano").pano({
        img: "static/images/cs4pano.jpg"
    });
    $("#c2pano").pano({
        img: "static/images/cs4pano.jpg"
    });
    $("#c3pano").pano({
        img: "static/images/cs4pano.jpg"
    });
    $("#c4pano").pano({
        img: "static/images/cs4pano.jpg"
    });
    $("#c5pano").pano({
        img: "static/images/cs4pano.jpg"
    });


    $("#r1pano").pano({
        img: "static/images/cs4pano.jpg"
    });
    $("#r2pano").pano({
        img: "static/images/cs4pano.jpg"
    });
    $("#r3pano").pano({
        img: "static/images/cs7pano.jpg"
    });
    $("#r4pano").pano({
        img: "static/images/cs7pano.jpg"
    });

    $("#r5pano").pano({
        img: "static/images/cs7pano.jpg"
    });
});


// HIDE MOBILE MENU AFTER CLIKING ON A LINK
   $('.navbar-collapse a').click(function(){
        $(".navbar-collapse").collapse('hide');
    });


// SCROLLTO THE TOP
$(document).ready(function() {
	// Show or hide the sticky footer button
		$(window).scroll(function() {
			if ($(this).scrollTop() > 200) {
				$('.go-top').fadeIn(200);
					} else {
						$('.go-top').fadeOut(200);
					}
				});		
				// Animate the scroll to top
				$('.go-top').click(function(event) {
					event.preventDefault();
				
					$('html, body').animate({scrollTop: 0}, 300);
				})
			});
