// $('.multiple-items').slick({
//   infinite: true,
//   slidesToShow: 4,
//   slidesToScroll: 1,
//   arrows:true,
//   dots: false
// });

 
// $('.responsive').slick({
//   dots: true,
//   infinite: true,
//   speed: 300,
//   slidesToShow: 4,
//   slidesToScroll: 1,
//   responsive: [
//     {
//       breakpoint: 1024,
//       settings: {
//         slidesToShow: 3,
//         slidesToScroll: 3,
//         infinite: true,
//         dots: true
//       }
//     },
//     {
//       breakpoint: 600,
//       settings: {
//         slidesToShow: 2,
//         slidesToScroll: 2
//       }
//     },
//     {
//       breakpoint: 480,
//       settings: {
//         slidesToShow: 1,
//         slidesToScroll: 1
//       }
//     }
//     {
//       breakpoint: 320,
//       settings: {
//         slidesToShow: 1,
//         slidesToScroll: 1
//       }
//     }
//     // You can unslick at a given breakpoint now by adding:
//     // settings: "unslick"
//     // instead of a settings object
//   ]
// });


jQuery(document).ready(function(){

	jQuery('.sliderbox').slick({
  		speed: 500,
  		fade: true,
  		slidesToShow: 1,
  		slidesToScroll: 1,
  		infinite: true,
  		dots:false
  	});
  	jQuery('.gallery-slider').slick({
  		speed: 500,
  		slidesToShow: 4,
  		slidesToScroll: 1,
  		infinite: false,
  		dots:false,
      responsive: [
        {
          breakpoint:1199,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1
          }
        },
        {
          breakpoint:768,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1
          }
        },
        {
          breakpoint:767,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
        {
          breakpoint:500,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            autoPlay: true
          }
        }
      ]
  	});
  	jQuery('.slider-big').slick({
	  slidesToShow: 1,
	  slidesToScroll: 1,
	  arrows: false,
	  fade: true,
	  asNavFor: '.slider-thumb'
	});
	jQuery('.slider-thumb').slick({
	  slidesToShow: 3,
	  slidesToScroll: 3,
	  dots: true,
	  centerMode: true,
	  focusOnSelect: true,
	  fade: false,
	  infinite: true,
	  asNavFor: '.slider-big'
	});
	
	jQuery('.onclick').click(function(){
		jQuery('.search-box').css("display","block");
    return false;
	});

  jQuery(document).ready(function(){
    jQuery(".toggle-menu").click(function(){
      jQuery(this).parent().children('ul').slideToggle('slow');
      jQuery('.navbar-collapse').collapse('hide');
    });
  });
  jQuery('.navbar-toggler:not(:disabled):not(.disabled)').click(function(){
    /*jQuery(".navbar-collapse").collapse('hide');*/
    jQuery(".mob-menu ul").slideUp();
    jQuery('.navbar-collapse').collapse('show');
  });
});

$(document).mouseup(function(e) 
{
    var container = $(".search-box");

    // if the target of the click isn't the container nor a descendant of the container
    if (!container.is(e.target) && container.has(e.target).length === 0) 
    {
        container.hide();
    }
});

equalheight = function(container){
    var currentTallest = 0,
        currentRowStart = 0,
        rowDivs = new Array(),
        jQueryel,
        topPosition = 0;
    jQuery(container).each(function() {

        jQueryel = jQuery(this);
        jQuery(jQueryel).height('auto');
        topPostion = jQueryel.position().top;

        if (currentRowStart != topPostion) {
            for (currentDiv = 0 ; currentDiv < rowDivs.length ; currentDiv++) {
                rowDivs[currentDiv].height(currentTallest);
            }
            rowDivs.length = 0; // empty the array
            currentRowStart = topPostion;
            currentTallest = jQueryel.height();
            rowDivs.push(jQueryel);
        } else {
            rowDivs.push(jQueryel);
            currentTallest = (currentTallest < jQueryel.height()) ? (jQueryel.height()) : (currentTallest);
        }
        for (currentDiv = 0 ; currentDiv < rowDivs.length ; currentDiv++) {
            rowDivs[currentDiv].height(currentTallest);
        }
    });
}

jQuery(window).load(function() {
    equalheight('.service-image');
    equalheight('.service-info .title');
});

jQuery(window).resize(function(){
	equalheight('.service-image');
	equalheight('.service-info .title');
});