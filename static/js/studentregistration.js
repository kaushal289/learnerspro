const name = document.getElementById('name')
const lname = document.getElementById('lname')
const form = document.getElementById('form')
const errorElement = document.getElementById('nameerror')
var intonumber = parseInt(document.getElementById('name'))
const phnumber = document.getElementById('number')
const username = document.getElementById('username')
const email = document.getElementById('email')
const password = document.querySelector("#password")
const confirmpassword = document.querySelector("#confirmpassword")


form.addEventListener('submit' ,(e)  => {
    let messages =[]
    if( name.value.trim() ==""){
        messages.push("Non of the field should be empty.")
        name.style.border= "solid 4px red"
    }
    else if(lname.value.trim()==""){
        messages.push("Non of the field should be empty.")
        lname.style.border = "solid 4px red"
    }
    else if(username.value.trim()==""){
        messages.push("Non of the field should be empty.")
        username.style.border = "solid 4px red"
    }
    else if(email.value.trim()==""){
        messages.push("Please enter your email address.")
        email.style.border="solid 4px red"
    }
    else if(number.value.trim()==""){
        messages.push("Please enter your number.")
        number.style.border="solid 4px red"
    }
    else if(number.value.length<10 || number.value.length>10){
        messages.push("The number should be 10 digits.")
        number.style.border="solid 4px red"
    }
    else if(password.value.trim()==""){
        messages.push("The password fiels should not be empty.")
        password.style.border="solid 4px red"
    }
    else if(password.value.length<=8){
        messages.push("Password too short.")
        password.style.border="solid 4px red"
    }
    else if(confirmpassword.value.trim()==""){
        messages.push("Please confirm your password.")
        confirmpassword.style.border+"solid 4px red"
    }
    else if(password.value!=confirmpassword.value){
        messages.push("Passwords don't match.")
        confirmpassword.style.border="solid 4px red"
    }
    if(messages.length >0){
        e.preventDefault()
        errorElement.innerHTML = messages.join(' , ' )
    }

})
$(window).on('load',function(){
    $(".container").fadeIn(1000);
});
