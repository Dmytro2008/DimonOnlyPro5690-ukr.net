// Json - javascript object notation
// Ajax - asynchronous javascript and xml

var btn = document.getElementById("btn")
var container = document.getElementById("ourcontainer")
var url = 'http://127.0.0.1:8000/blogs/'


$.ajax({
	method: 'GET',
	url: url,
	success: function(data){
		console.log(data)
		console.log("Информация успешно загрузилась")
	},
	error: function(error_data){
		console.log("Ошибка")
	}
})




btn.addEventListener("click", function(){
	var ourRequest = new XMLHttpRequest();
	ourRequest.open("GET", url);
	ourRequest.onload = function() {
		var ourData = JSON.parse(ourRequest.responseText);
		renderHTML(ourData);
	}
	ourRequest.send();

})

function renderHTML(data) {
	var container = document.getElementById("ourcontainer")
	var htmlString = "";
	var htmlString1 = "";
	var htmlString2 = "";

	for (i=0; i < data.length; i++){
		htmlString += "<p>Post "  + data[i].pk + "</p>"+"<p>"+ data[i].description +"</p>" +"</br>";
		htmlString1 += "<p>Title is "  + data[i].title + "</p>";

	}

	container.insertAdjacentHTML('beforeend', htmlString);
	container.insertAdjacentHTML('beforeend', htmlString1);
	container.insertAdjacentHTML('beforeend', htmlString2);
}
