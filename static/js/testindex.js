$(document).ready(function(){
    filter_data();
    function filter_data()
    {
        $('.filter_data').html('<div id="loading" style="" ></div>');
        var action = 'fetch_data';
        var pret_minim = $('#hidden_pret_minim').val();
        var pret_maxim = $('#hidden_pret_maxim').val();
        $.ajax({
            url:"/Drone",
            method:"POST",
            data:{action:action, pret_minim:pret_minim, pret_maxim:pret_maxim},
            success:function(data){
                $('.filter_data').html(data);
                $(".filter_data").append(data.htmlresponse);
            }
        });
    }
    $('#price_range').slider({
        range:true,
        min:50,
        max:5000,
        values:[50, 5000],
        step:50,
        stop:function(event, ui)
        {
            $('#price_show').html(ui.values[0] + ' - ' + ui.values[1]);
            $('#hidden_pret_minim').val(ui.values[0]);
            $('#hidden_pret_maxim').val(ui.values[1]);
            filter_data();
        }
    });
});