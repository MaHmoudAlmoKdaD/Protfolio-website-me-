//  JQuery
$(document).ready(function () {

    //effect to img hen hover
    $(".ul_links_my_media li a img").hover(function(e){
        $(this).css('border','2px solid #fff');
        },
        function(){
            $(this).css('border','2px solid rgba(46, 53, 54, 0.85)');
        });
    //efect when mouse down on icon
    $(".ul_links_my_media li a img").mousedown(function(e){
        let timeClick = $(this).css('border','2px solid #fff');
        // setTimeout( () => timeClick.remove(), 3000);
    });
    //efect when mouse up on icon
    $(".ul_links_my_media li a img").mouseup(function(e){
        let timeClick = $(this).css('border','2px solid rgba(46, 53, 54, 0.85)');
     // setTimeout( () => timeClick.remove(), 3000);
    });

    // effect for navigation right side
    $(".contact-portfolio li a").hover(function(e){
        $(this).css( {color: '#E5A5A2'} );
        },
        function(){
            $(this).css('color','#fff');
        });
});
// to save the pinl color on the anchor of page
window.onload = function () {
    let anchor = document.querySelectorAll('.contact-portfolio li a');
    let move = document.querySelector('.move1');
    if(move.value === 'move1'){
        anchor[0].style.color = '#E5A5A2' ;
    }
    else{
        anchor[0].style.color = '#fff' ;
    }
    if(move.value === 'move2'){
        anchor[1].style.color = '#E5A5A2' ;
    }
    else{
        anchor[1].style.color = '#fff' ;
    }
    if(move.value === 'move3'){
        anchor[2].style.color = '#E5A5A2' ;
    }
    else{
        anchor[2].style.color = '#fff' ;
    }
}
