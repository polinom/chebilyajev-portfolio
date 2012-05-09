$(document).ready(function(){
	$('.image_thumb').click(function(e){
		 e.preventDefault();
		 $('.loading_place').html('<img src="/static/images/ajax-loader.gif">')
         var big_img = $(this).attr('original')
         var img_el = $('.image_big')
         img_el.fadeOut('fast',function(){img_el.fadeIn('slow'); img_el.attr('src', big_img)})
	});
	$('.image_big').load(function(){ $('.loading_place').html('') });

	$('.nav_dot').click(function(e){
		e.preventDefault()
		var page = $(this).attr('page')
		alert(page)


	})
})