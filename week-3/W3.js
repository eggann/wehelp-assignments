function main() {
    let src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";

    fetch(src)
    .then(function(response) {
        return response.json();
    })
    .then(function(result) {
        let content = document.createElement('div');
        document.body.appendChild(content);
        content.setAttribute("class", "content");
    
        Array.from(Array(8)).forEach((_, index) => {
            /**
             * all section
             */
            const all = document.createElement('div');
            content.appendChild(all);
            all.setAttribute("class", "all");
        
            /**
             * img section
             */
            const myString = result.result.results[index].file;
            const splits = myString.split(['https']);
            const src = `https${splits[1]}`;
            const img = document.createElement('img');
            all.appendChild(img);
            img.setAttribute("src", src);
            img.setAttribute("class", "img");
        
            /**
             * name section
             */
            const name = document.createElement('div');
            all.appendChild(name);
            name.textContent = result.result.results[index].stitle;
            name.setAttribute("class", "img_name");
        });
    });
};

main();