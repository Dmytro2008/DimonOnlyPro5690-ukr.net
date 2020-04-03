var url = 'http://127.0.0.1:8000/api/';

var btnn = document.getElementById("butt_id");
// var contt = document.getElementById("film_cl");



btnn.addEventListener("click", function(){
  var xhr = new XMLHttpRequest();
  xhr.open("GET", url);
  xhr.addEventListener('load', function(){
    var ourData = JSON.parse(xhr.responseText);
    renderHTML(ourData);
  })
  xhr.send();

})


function renderHTML(data) {
  var container = document.getElementById("comments_1");
  var htmlString = "";

  for (i=0; i < data.length; i++){
      htmlString += "<h2>"+data[i].title+"</h2>" +"<p>"+ data[i].description +"</p>" +"</br>" ;

    }
  container.insertAdjacentHTML('beforeend', htmlString);
}
