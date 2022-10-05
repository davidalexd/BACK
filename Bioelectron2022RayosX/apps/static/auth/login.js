const loginForm = document.getElementById("login-form")
const baseEndPoint = "http://127.0.0.1:8000/api"
if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event){
    event.preventDefault()
    const loginEndpoint = `${baseEndPoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData) 
    let bodyStr = JSON.stringify(loginObjectData)

    const options = {
        method:"POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body : bodyStr
    }
    fetch(loginEndpoint,options)
    .then(response=>{
        return response.json()
    })
    .then(data=>{
        console.log(data);
    })
    .catch(error=>{
        console.log(error);
    })
}