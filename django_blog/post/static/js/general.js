$(document).ready(function () {
	$('#search_btn').click(function() {
		var text_input = $("#search__input").attr("value");
		location.hash.split('#')[0] = 'search-results/?q=' + text_input
	})
});