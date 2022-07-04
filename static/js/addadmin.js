const form = document.getElementById('form')
const errorElement = document.getElementById('emailerror')
const username = document.getElementById('username')
const password = document.getElementById('password')
const confirmpassword = document.getElementById('confirm_password')

form.addEventListener('submit' ,(e)  => {
    let messages =[]
    if(username.value.trim()==""){
        messages.push("Please enter username")
        username.style.border="solid 4px red"
    }
    else if(username.value.length<5){
        messages.push("Username too short.")
        password.style.border="solid 4px red"
    }
    else if(password.value.trim()==""){
        messages.push("Please enter a password.")
        password.style.border="solid 4px red"
    }
    else if(password.value.length<5){
        messages.push("Password too short.")
        password.style.border="solid 4px red"
    }
    else if(confirmpassword.value.trim()==""){
        messages.push("Please confirm your password.")
        password.style.border="solid 4px red"
    }
    else if(password.value!=confirmpassword.value){
        messages.push("Passwords don't match.")
        confirmpassword.style.border="solid 4px red"
    }
    if(messages.length >0){
        e.preventDefault()
        errorElement.innerHTML = messages.join(' , ' )
    }
    else{
        alert("Admin added successfully")
    }
})

