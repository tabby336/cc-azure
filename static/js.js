function do_something() {
	var text = $('#something').val()
	console.log(text);
	$.ajax({
		url: "/do_something",
		type: "POST",
		data: {text: text},
		success: function(data) {
			console.log(data);
		}
	})
}