$(document).ready(function(){
    $('#booking_form').validate({
        rules : {
            name:"required",
            email:{
                required:true,
                email:true
            },
            phone:{
                required:true,
                minlength:10
            },
            checkin:"required",
            checkout:"required"
        },
        messages: {
            name:"Please enter your name",
            email:{
                required:"This field is required",
                email:"please enter a valid email "
            },
            phone:{
                required:"This field is required",
                minlength:"please enter a valid number"
            },
            checkin:"enter your checkin date here",
            checkout:"enter your checkout date here"            
        }
    });
})