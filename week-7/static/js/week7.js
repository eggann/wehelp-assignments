function submit_entry(){
    let list = document.getElementById("list");
    let username = document.getElementById("username").value;
    let src = `/api/members?username=${username}`;
    fetch(src).then((response) => {
        return response.json();
    }).then((result) => {
        if(result.data != null) {
            list.innerHTML = result.data.name + ' ' + '(' +result.data.username + ')';
        }
        else {
            list.innerHTML = '無此帳戶';
        }
    });
};