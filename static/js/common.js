$(function(){
    $(".t-title").on('click',function () {
        var num=$(this).attr("value");
        $(this).parent("h3").siblings(".title1").toggle();
    })
})