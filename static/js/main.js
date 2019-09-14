

$(document).ready(function() {
	$('div.uzb path').click(function() {
		let title = $(this).data('title')
		console.log(title)
		let title_top = $('span#title-top')
		let title_bottom = $('h5#title-bottom')

		title_top.text(title)
		title_bottom.text(title)
		$('div.uzb path').css({'fill':'#f2f2f2'})
		$(this).css({'fill':'#e8c570'})
	})
	$('#UZ-JI').css({'fill':'#e8c570'})
})


$(document).ready(function() {
	let slide_right = $('img#slide-right')
	let slide_left = $('img#slide-left')

	let win_slide_right = $('section.banner .carousel-control-next')
	let win_slide_left = $('section.banner .carousel-control-prev')

	win_slide_left.html(slide_left)
	win_slide_right.html(slide_right)
})


// $(document).ready(function() {

// 	let next_icon_us = $('img#next-icon')
// 	let prev_icon_us = $('img#prev-icon')

// 	let button_next_us = $('section.uslugi .owl-carousel .owl-nav button.owl-next')
// 	let button_prev_us = $('section.uslugi .owl-carousel .owl-nav button.owl-prev')

// 	button_next_us.html(next_icon_us)
// 	button_prev_us.html(prev_icon_us)

// 	$('section.uslugi .owl-carousel .owl-nav button.owl-next').html($('img#next-icon-us'))
// 	$('section.uslugi .owl-carousel .owl-nav button.owl-prev').html($('img#prev-icon-us'))
// })


// $(document).ready(function() {
// 	let next_icon = $('img#next-icon-po')
// 	let prev_icon = $('img#prev-icon-po')

// 	let button_next = $('section.polez .owl-carousel .owl-nav button.owl-next')
// 	let button_prev = $('section.polez .owl-carousel .owl-nav button.owl-prev')

// 	button_next.html(next_icon)
// 	button_prev.html(prev_icon)

// })


$(document).ready(function() {

	var owl = $('section.uslugi .owl-carousel');
	owl.owlCarousel({
	    loop:true,
	    margin:15,
	  
	    autoplay:false,
	    autoplayTimeout:2500,
	    autoplayHoverPause:true,
	    responsive:{
	        0:{
	            items:1
	        },
	        576:{
	            items:2
	        },
	        768:{
	            items:3
	        },
	        992:{
	            items:4
	        },
	        1200:{
	            items:5,
	            center:true,
	        }
	    }
	});

	$('.play').on('click',function(){
	    owl.trigger('play.owl.autoplay',[1000])
	})
	$('.stop').on('click',function(){
	    owl.trigger('stop.owl.autoplay')
	})
})

$(document).ready(function() {
	var owl = $('section.polez div.owl-carousel');
	owl.owlCarousel({
	    loop:true,
	    margin:15,
	    autoplay:true,
	    autoplayTimeout:1500,
	    autoplayHoverPause:true,
	    responsive:{
	        0:{
	            items:1
	        },
	        576:{
	            items:2
	        },
	        992:{
	            items:3
	        },
	        1200:{
	            items:4
	        },
	        1500:{
	            items:5
	        }
	    }
	});
	
	$('.play').on('click',function(){
	    owl.trigger('play.owl.autoplay',[1000])
	})
	$('.stop').on('click',function(){
	    owl.trigger('stop.owl.autoplay')
	})
})


$(document).ready(function() {

	document.addEventListener('keydown', function(event) {
	  if (event.code == 'Enter' && (event.ctrlKey || event.metaKey)) {
	    let text = "";
	    if (window.getSelection) {
	        text = window.getSelection().toString();
	    } else 
	    if (document.selection && document.selection.type != "Control") {
	        text = document.selection.createRange().text;
	    }
	    $('div.ctrl-enter').css({'display':'block'})
	    $('textarea#text-area-xato').val(text)
	  }
	});
})

$(document).ready(function() {
  $('button.btn-bekor').click(function() {
    $('div.ctrl-enter').css({'display':'none'})
  })
})

$(document).ready(function() {
	$('button.m-btn').click(function() {
		$('section.hmobil').fadeToggle()
	})
	$('button.header-btn').click(function() {
		$('section.full-menu').fadeToggle('fast')
	})
})

$(document).ready(function() {
	$('button.press-btn').click(function() {
		$('ul.press-ul').animate({
			height:'toggle'
		})

		$(this).children(".fa").toggleClass('arrow-reverse')

	})
})

$(document).ready(function() {
	$('[data-fancybox="images"]').fancybox({
	  afterLoad : function(instance, current) {
	    var pixelRatio = window.devicePixelRatio || 1;

	    if ( pixelRatio > 1.5 ) {
	      current.width  = current.width  / pixelRatio;
	      current.height = current.height / pixelRatio;
	    }
	  }
	});
})