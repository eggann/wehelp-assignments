let src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";

let content = document.createElement('div');
content.setAttribute("class", "content");

for(let i=1;i<9;i++){
    
    let content2 = document.createElement('div');
    document.body.appendChild(content);
    content.appendChild(content2);
    content2.setAttribute("class", "all");

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
        img.setAttribute("class", "img");

        name.textContent = myJson['result']['results'][i]['stitle'];
        name.setAttribute("class", "img_name");

    });
};
