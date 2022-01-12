let src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
// fetch(src).then(function(response){
//     return response.json();
// }).then(function(result){
//     console.log("最終資料", result['result']['results'][0]);
// });

let content = document.createElement('div');
content.setAttribute("class", "content");

for(let i=1;i<9;i++){
  console.log(i);
    
    let content2 = document.createElement('div');
    document.body.appendChild(content);
    content.appendChild(content2);

    let img = document.createElement('img');
    document.body.appendChild(content);
    content2.appendChild(img);

    let name = document.createElement('div');
    document.body.appendChild(content);
    content2.appendChild(name);


    fetch(src).then(function(response) {
        return response.json();
        })
        .then(function(myJson) {
        console.log(myJson['result']['results']['0']);
        const myString = myJson['result']['results'][i]['file'];
        const splits = myString.split(['https']);
        console.log(String("https")+splits[1]);
        img.setAttribute("src",String("https")+splits[1]);
    });

    fetch(src).then(function(response) {
        return response.json();
        })
        .then(function(myJson) {
        console.log(myJson['result']['results']['0']);
        const myString_2 = myJson['result']['results'][i]['stitle'];
        console.log(myString_2);
        name.setAttribute("class", "img_name");
    });


}
