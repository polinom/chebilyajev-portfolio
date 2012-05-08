$('.image_big').load(function(){
		console.log('Loading >>>>> finished')
});

$(document).ready(function(){
    console.log('HELLO')
	$('.image_thumb').click(function(e){
         var big_img = $(this).attr('original')
         var img_el = $('.image_big')
         img_el.attr('src', big_img)

         if (img_el.complete || img_el.readyState === 4) {
    				console.log('hello')
			} else {
		  $(img_el).bind('load', function(){	
			       console.log('hello 2')
			});
        }
	});

})