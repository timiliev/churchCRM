/*
function myFunction() {
  alert("Page is loaded");
};
*/


$( document ).ready(function() {
    //console.log("This is a test");
    $( ".bg-modal" ).hide();

    $( "#modal-plus-button-people-and-groups" ).click(function() {
        //alert("TEST TEST TEST");
        //$('#myFlexbox').css('display', 'flex');
        $( ".bg-modal" ).show();
    });

    $( "#modal-x-button-people-and-groups" ).click(function() {
        $( ".bg-modal" ).hide();
    });
});



