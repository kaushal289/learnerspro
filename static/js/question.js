const name = document.getElementById('name')
const form = document.getElementById('form')
const errorElement = document.getElementById('nameerror')
var intonumber = parseInt(document.getElementById('name'))
const question = document.getElementById('question')

form.addEventListener('submit' ,(e)  => {
    let messages =[]
    if( name.value.trim() ==""){
        messages.push("Please enter your name.")
        name.style.border= "solid 4px red"
    }
    else if(question.value.trim()==""){
        messages.push("This field shouldn't be.")
        question.style.border = "solid 4px red"
    }
    if(messages.length >0){
        e.preventDefault()
        errorElement.innerHTML = messages.join(' , ' )
    }
    else{
        alert("Question submitted successfully.")
    }
})
$(window).on('load',function(){
    $(".container").fadeIn(1000);
});
