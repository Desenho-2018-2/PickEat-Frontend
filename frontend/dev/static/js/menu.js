function incrementValue(number){
    $(number).on(onclick, function(){
    var i = $(number).data('data-badge');
    $(number).data('data-badge', i + 1);
    $(number).attr('data-size',i + 1)
});
}

