let src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
fetch(src).then(function(response){
    return response.json();
}).then(function(result){
    console.log("最終資料", result['result']['results'][0]);
});
