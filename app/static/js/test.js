$(document).on('ready',function(){
	var token;
$("#TestRegister").on('click',function(){
	alert()
	$.post('/users/Register',
	{
		"UserName":'test_user',
		'Password':'123456',
		'Email':'test@test.com',
		'Birthday':'1995-12-12',
		'NickName':'TestNick',
		'Gender':1,
		'Hometown':'testHomeTown',
		'MobilePhoneNumber':'10086',
		'Sentence':'testSentence'
	},function(data,status)
	{
		var d = $.parseJSON(data);
		alert(d['message'])
	})
})
$("#TestLogin").on('click',function(){
	alert()
	$.post('/users/Login',
	{
		"UserName":'test_user',
		'Password':'123456',
	},function(data,status)
	{
		var d = $.parseJSON(data);
		alert(d['message'])
		if(d['message']=='Login Success!')
		{
			alert(d['token'])
			token=d['token']
		}
	})
})
$("#TestFoodList").on('click',function(){
	$.post('/ym_dishes/getTodayFoodList',function(data,status)
		{
			alert('post')
			var d=$.parseJSON(data)
			if(d['message']!=undefined)
			{
				alert(d['message'])
				return 
			}
			$("#data").after('<p>PageNum'+ d['PageNum'] +'</p>')
			$("#data").after('<p>CurrentPage'+ d["CurrentPage"] +'</p>')
			var Dish_List=$.parseJSON(d["Dish_List"])
			for(var one=0; one< Dish_List.length;++one)
			{
				for(var key in Dish_List[one])
				{
					$("#data").after('<p>'+key+" : "+Dish_List[one][key]+'</p>')
				}
				$("#data").after('<p>food</p>')
			}
		})
})
$("#TestCommentList").on('click',function(){
	$.post('/ym_dish_comments/getCommentList',
	{
		'DishID':1,
		'page':2
		
	},function(data,status)
		{
			alert('post')
			var d=$.parseJSON(data)
			if(d['message']!=undefined)
			{
				alert(d['message'])
				return 
			}
			$("#data").after('<p>PageNum'+ d['PageNum'] +'</p>')
			$("#data").after('<p>CurrentPage'+ d["CurrentPage"] +'</p>')
			var Dish_List=$.parseJSON(d["comment_list"])
			for(var one=0; one< Dish_List.length;++one)
			{
				for(var key in Dish_List[one])
				{
					$("#data").after('<p>'+key+" : "+Dish_List[one][key]+'</p>')
				}
				$("#data").after('<p>food</p>')
			}
		})
})
$("#TestComment").on('click',function()
{
	$.post('/ym_dish_comments/createComment',
	{
		'DishID':1111,
		'Content':'122 push a comment on dish 1111 ',
		'token':token
		
	},function(data,status)
		{
			alert('post')
			var d = $.parseJSON(data);
			alert(d['message'])
		})
	
})
$("#TestLikeList").on('click',function()
{
	$.post('/like_dishes/getLikeDishes',
	{
		'token':token
		
	},function(data,status)
	{
		alert('post')
		var d=$.parseJSON(data)
		if(d['message']!=undefined)
		{
			alert(d['message'])
			return 
		}
		$("#data").after('<p>PageNum'+ d['PageNum'] +'</p>')
		$("#data").after('<p>CurrentPage'+ d["CurrentPage"] +'</p>')
		var Dish_List=$.parseJSON(d["Dish_List"])
		for(var one=0; one< Dish_List.length;++one)
		{
			for(var key in Dish_List[one])
			{
				$("#data").after('<p>'+key+" : "+Dish_List[one][key]+'</p>')
			}
			$("#data").after('<p>food</p>')
		}
	})
})
$("#TestLike").on('click',function(){
	$.post('/like_dishes/like',
	{
		'token':token,
		'DishID':4
		
	},function(data,status)
	{
		alert('post')
		var d=$.parseJSON(data)
		if(d['message']!=undefined)
		{
			alert(d['message'])
			return 
		}
	})
})
$("#TestDontLike").on('click',function(){
	$.post('/like_dishes/dont_like',
	{
		'token':token,
		'DishID':4
		
	},function(data,status)
	{
		alert('post')
		var d=$.parseJSON(data)
		if(d['message']!=undefined)
		{
			alert(d['message'])
			return 
		}
	})
})

$("#TestDontFavorite").on('click',function(){
	$.post('/favorite_dishes/dont_favorite',
	{
		'token':token,
		'DishID':4
		
	},function(data,status)
	{
		alert('post')
		var d=$.parseJSON(data)
		if(d['message']!=undefined)
		{
			alert(d['message'])
			return 
		}
	})
})

$("#TestFavorite").on('click',function(){
	$.post('/favorite_dishes/favorite',
	{
		'token':token,
		'DishID':4
		
	},function(data,status)
	{
		alert('post')
		var d=$.parseJSON(data)
		if(d['message']!=undefined)
		{
			alert(d['message'])
			return 
		}
	})
})
$("#TestFavoriteList").on('click',function(){
	$.post('/favorite_dishes/getFavoriteDishes',
	{
		'token':token,
		'DishID':4
		
	},function(data,status)
	{
		alert('post')
		var d=$.parseJSON(data)
		if(d['message']!=undefined)
		{
			alert(d['message'])
			return 
		}
		var Dish_List=$.parseJSON(d["Dish_List"])
		for(var one=0; one< Dish_List.length;++one)
		{
			for(var key in Dish_List[one])
			{
				$("#data").after('<p>'+key+" : "+Dish_List[one][key]+'</p>')
			}
			$("#data").after('<p>food</p>')
		}
	})
})

$("#TestUserInfo").on('click',function(){

	$.post('/users/getUserInfo',
	{
		'token':token
		
	},function(data,status)
	{
		alert('post')
		var d=$.parseJSON(data)
		if(d['message']!=undefined)
		{
			alert(d['message'])
			return 
		}
			for(var key in d)
			{
				$("#data").after('<p>'+key+" : "+d[key]+'</p>')
			}
			$("#data").after('<p>user</p>')
	})
})

$("#TestEditInfo").on('click',function(){

	$.post('/users/editUserInfo',
	{
		'token':token,
		'HeadImage':'head',
		'Email':'abc@qqq.com',
		'MobilePhoneNumber':'136000',
		'Hometown':'gz',
		'Gender':1,
		'Birthday':'2000-11-11',
		'Sentence':'sentence',
		'NickName':'sss'

		
	},function(data,status)
	{
		alert('post')
		var d=$.parseJSON(data)
		if(d['message']!=undefined)
		{
			alert(d['message'])
			return 
		}
	})
})
$("#TestEditPassword").on('click',function(){

	$.post('/users/changePassword',
	{
		'token':token,
		'old_password':'123456',
		'new_password':'123456'
	},function(data,status)
	{
		alert('post')
		var d=$.parseJSON(data)
		if(d['message']!=undefined)
		{
			alert(d['message'])
			return 
		}
	})
})
})