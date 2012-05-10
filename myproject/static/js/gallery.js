$(document).ready(function(){
	$('.image_thumb').live('click', function(e){
		 e.preventDefault();
		 $('.loading_place').html('<img src="/static/images/ajax-loader.gif">')
         var big_img = $(this).attr('original')
         var img_el = $('.image_big')
         img_el.fadeOut('fast',function(){img_el.attr('src', big_img)})
	});

	$('.image_big').load(function(){ $('.loading_place').html(''); $('.image_big').fadeIn('slow'); });

	$('.nav_dot').live('click',function(e){
		e.preventDefault()
		var img_list = $('.thumb_list')

		$('.nav_dot').attr('src','/static/images/page_dor_black.png')
		$(this).attr('src','/static/images/page_dor_white.png')


		img_list.html('')
		var page = $(this).attr('page')

		$.get('',{'page':page},function(resp){
          $(resp).each(function(index,item){
          var img_html = '<img class="image_thumb" src="'+item.thumb+'" width="60" height="60" original="'+item.image+'">'
           img_list.append(img_html)
          })
		})


	})
})