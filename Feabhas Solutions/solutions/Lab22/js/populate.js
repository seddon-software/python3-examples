// Gets Json data from /cgi-bin/get-data.py and populates html

$(document).ready(function() {
	$("#update").click(function() {
		reset_form();
		$.ajax({
			cache: false,
			url: '/cgi-bin/update.py',
			data: 'url='+$('#url').val(),
			dataType: 'json',
		success: populate_form
		});
    });
});

function reset_form() {
	$('#h1').text(0);
	$('#h2').text(0);
	$('#h3').text(0);
	$('#h4').text(0);
	$('#h5').text(0);
	$('#h6').text(0);
}

function populate_form(data) {
	$('#h1').text(data.h1);
	$('#h2').text(data.h2);
	$('#h3').text(data.h3);
	$('#h4').text(data.h4);
	$('#h5').text(data.h5);
	$('#h6').text(data.h6);
}
