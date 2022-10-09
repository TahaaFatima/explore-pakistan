$(document).ready(function(){


  // For Gilgit baltistan
//   $("#hideone").hide();
//   $(".btn1").click(function(){
//     $("#hideone").show(500);
//   });
//   $(".show").click(function(){
//     $("#hideone").hide(500);
//   });

// // For Balochistan
//   $("#hidetwo").hide();
//   $(".btn2").click(function(){
//     $("#hidetwo").show(500);
//   });
//   $(".show1").click(function(){
//     $("#hidetwo").hide(500);
//   });
// // For KPK
//   $("#hidethree").hide();
//   $(".btn3").click(function(){
//     $("#hidethree").show(500);
//   });
//   $(".show2").click(function(){
//     $("#hidethree").hide(500);
//   });
// // For Punjab
//   $("#hidefour").hide();
//   $(".btn4").click(function(){
//     $("#hidefour").show(500);
//   });
//   $(".show4").click(function(){
//     $("#hidefour").hide(500);
//   });
//   // For Shindh
//   $("#hidefive").hide();
//   $(".btn5").click(function(){
//     $("#hidefive").show(500);
//   });
//   $(".show5").click(function(){
//     $("#hidefive").hide(500);
//   });
// slick slider
  $('.second').slick({
    dots: true,
    infinite: true,
    speed: 500,
    fade: true,
    cssEase: 'linear',
    autoplay: true,
    autoplayspeed: 8000,
  });
  
});


var header = document.getElementById("nav");
var btns = header.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
  var current = document.getElementsByClassName("active");
  current[0].className = current[0].className.replace(" active", "");
  this.className += " active";
  });
}



// $(document).ready(function(){
    // $('.filter select').selectpicker();
    // $('#search-bar').keyup(function(){
    //     var value = $(this).val().toLowerCase();
    //     $('#list li').each(function(){
    //         var search = $(this).text().toLowerCase();
    //         if(search.indexOf(value)> -1){
    //             $(this).show();
    //         }
    //         else{
    //             $(this).hide();
    //         }
    //     });
    // });

// const searchWrapper =document.querySelector(".search-input");
// const inputBox = searchWrapper.querySelector("#search");
// const suggBox = searchWrapper.querySelector(".autocom-box");

// inputBox.onkeyup = (e)=>{
//     let userData = e.target.value;
//     let emptyArray = [];
//     if(userData){
//         emptyArray = sugestion.filter((data)=>{
//            return data = toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
//         });

//         emptyArray = emptyArray.map((data)=>{
//             return data = '<li>'+ data +'</li>';
//         });
//         console.log(emptyArray);
//         searchWrapper.classList.add("active");
//     }else{

//     }
//     showSuggestions(emptyArray)
// }
//   function showSuggestions(list){
//     let listData;
//     if(!list.length){

//     }
// else{
//     listData = list.join('');
// }
// suggBox.innerHtml = listData;
//   }  
// });
