$(document).ready(function(){
    $("#post-create-formats").click(function(){
        const data = new FormData(document.getElementById('formdata'));
        postData('http://127.0.0.1:8000/api/v2/Report/Formats/', data)
        .then((data) => {"a"});
    })
})


async function postData(url = '',data = {}){
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return response.json();
}