$(document).ready(function(){
	$('.image_thumb').click(function(e){
         var big_img = $(this).attr('original')
         var img_el = $('.image_big')
         img_el.attr('src', big_img)
	});
	$('.image_big').load(function(){ console.log('Loading >>>>> finished'); });
})