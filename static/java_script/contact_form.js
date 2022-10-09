$(document).ready(function(){
    $('#contact_form').validate({
        rules : {
          fname:"required",
          lname:"required",
          emails:{
            required:true,
            email:true
          },
          phone:{
            required:true,
            minlength:10
          },
          msg:"required"
        },
        messages: {
          fname:"Please enter your Fisrt name",
          lname:"Please enter your Last name",
          emails:{
            required:"please enter your email address",
            email:"please enter a valid email"
          },
          phone:{
            required:"This field is required",
            minlength:"please enter a valid phone number"
          },
          msg:"write your messages and complains here"
    }
  })

})