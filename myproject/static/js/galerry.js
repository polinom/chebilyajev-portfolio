$(document).ready(function(){

	$('.image_thumb').click(function(e){
         var big_img = $(this).attr('original')
         $('.image_big').attr('src', big_img)
	})
})