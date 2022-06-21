const form = document.getElementById('form')
const errorElement = document.getElementById('emailerror')
const newpassword = document.getElementById('new_password')
const confirmpassword = document.getElementById('confirm_password')

form.addEventListener('submit' ,(e)  => {
    let messages =[]
    if(newpassword.value.trim()==""){
        messages.push("Please enter a password.")
        newpassword.style.border="solid 4px red"
    }
    else if(newpassword.value.length<=8){
        messages.push("Password too short.")
        newpassword.style.border="solid 4px red"
    }
    else if(confirmpassword.value.trim()==""){
        messages.push("Please confirm your password.")
        newpassword.style.border="solid 4px red"
    }
    else if(newpassword.value!=confirmpassword.value){
        messages.push("Passwords don't match.")
        confirmpassword.style.border="solid 4px red"
    }
    if(messages.length >0){
        e.preventDefault()
        errorElement.innerHTML = messages.join(' , ' )
    }
    else{
        alert("Password changed successfully")
    }
})

