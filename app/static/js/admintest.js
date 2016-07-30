$(document).on('ready',function(){
	var token;
	//var fail='1'// for testing failing token

	$("#adminTestLogin").on('click',function  () {
		$.post('/users/adminLogin',{
			"AdminName":"test_admin",
			'Password':'123456',
		},function(data,status){
			var d= $.parseJSON(data);
			alert(d['message']);
			if (d['message']=='Login Success!') {
				token=d['token']
				$("#data").text(d['token']);
			};
		})
	})

	$("#TestAllDish").on('click',function  (argument) {
		// body...
		$.post('/ym_dishes/adminGetFoodList',{
			'token':token,
			'page':2,
		},function  (data,status) {
			// body...
			var d=$.parseJSON(data)
			if(d['message']!=undefined){
				alert(d['message'])
				return
			}
			$("#data").after('<p>PageNum'+d['PageNum']+'</p>')
			$("#data").after('<p>CurrentPage'+d['CurrentPage']+'</p>')
			var Dish_List=$.parseJSON(d["Dish_List"])
			for (var i = 0; i < Dish_List.length; i++) {
				for(var key in Dish_List[i]){
					$("#data").after('<p>'+key+":"+Dish_List[i][key]+'</p>')
				}
				$("#data").after('<p>food</p>')
			};
		})
	})

	$("#TestEditDish").on('click',function  (argument) {
		// body...
		$.post('/ym_dishes/adminModifyDish',{
			'token':token,
			'DishID':'t-1',
			'DishType':'sss',
			'DishSmallImage':'lll1',
			'DishLargeImage':'ppp',
			'DishName':'nnn',
			'Taste':'hot',
			'RawStuff':'lajiao',
			'Location':'yifan',
			'Description':'hot!',
			'Price':19,
		},function  (data,status) {
			// body...
			var d=$.parseJSON(data);
			alert(d['message']);
			
		})
	})

	$("#TestAddDish").on('click',function  (argument) {
		// body...
		$.post('/ym_dishes/adminAddDish',{
			'token':token,
			'DishID':'t-3',
			'DishType':'sss',
			'DishSmallImage':'lll1',
			'DishLargeImage':'ppp',
			'DishName':'nnn',
			'Taste':'hot',
			'RawStuff':'lajiao',
			'Location':'yifan',
			'Description':'hot!',
			'Price':19,
		},function  (data,status) {
			// body...
			var d=$.parseJSON(data)
			alert(d['message']);
		})
	})

	$("#TestDelDish").on('click',function  (argument) {
		// body...
		$.post('/ym_dishes/adminDelDish',{
			'token':token,
			'DishID':'t-2',
		},function  (data,status) {
			// body...
			var d=$.parseJSON(data)
			alert(d['message']);
		})
	})

	$("#TestTodayDish").on('click',function(){
	
		$.post('/ym_dishes/getTodayFoodList',{
			//'page':2,
		},function(data,status)
		{
			var d=$.parseJSON(data)
			if(d['message']!=undefined)
			{
				alert(d['message']);
				return ;
			}
			$("#data").after('<p>PageNum'+ d['PageNum'] +'</p>')
			$("#data").after('<p>CurrentPage'+ d["CurrentPage"] +'</p>')
			var Dish_List=$.parseJSON(d["Dish_List"])
			for(var one=0; one< Dish_List.length;++one)
			{
				for(var key in Dish_List[one])
				{
					$("#data").after('<p>'+key+" : "+Dish_List[one][key]+'</p>');
				}
				$("#data").after('<p>food</p>');
			}
		});
	})

	$("#TestAddToday").on('click',function  (argument) {
		// body...
		$.post('/ym_dishes/adminOperateTodayDish/add',{
			'token':token,
			'DishID':'t-2',
		},function  (data,status) {
			// body...
			var d=$.parseJSON(data);
			
			alert(d['message']);
			return ;
			
		})
	});

	$("#TestDelToday").on('click',function  (argument) {
		$.post('/ym_dishes/adminOperateTodayDish/del',{
			'token':token,
			'DishID':'t-2',
		},function  (data,status) {
			// body...
			var d=$.parseJSON(data);
			
			alert(d['message']);
			return ;
		})
	});

	$("#TestComment").on('click',function  (argument) {
		// body...
		$.post('/ym_dish_comments/getCommentList',{
			'DishID':'t-1',
			//'page':2,
		}
			,function  (data,status) {
			// body...
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

	$("#TestDelComment").on('click',function  (argument) {
		// body...
		$.post('/ym_dish_comments/adminDeleteComment',{
			'token':token,
			'DishID':'t-1',
			'UserName':'t_u2',
		},function  (data,status) {
			// body...
			var d=$.parseJSON(data)
			alert(d['message'])
		})
	})
})