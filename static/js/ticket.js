const form = document.getElementById('form')
const errorElement = document.getElementById('nameerror')
const summary = document.getElementById('summary')

form.addEventListener('submit' ,(e)  => {
    let messages =[]
    if(summary.value.trim()==""){
        messages.push("This field shouldn't be.")
        summary.style.border = "solid 4px red"
    }
    if(messages.length >0){
        e.preventDefault()
        errorElement.innerHTML = messages.join(' , ' )
    }
    else{
        alert("Ticket raised successfully.")
    }
})
$(window).on('load',function(){
    $(".container").fadeIn(1000);
});
