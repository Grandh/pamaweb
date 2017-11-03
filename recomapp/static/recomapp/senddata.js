$(document).ready(function(){
    $.ajaxSetup({
        data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
    });
});

function updateTags(){
    // 异步ajax，返回标签显示
    $.ajax({
        url:"/gettag/",
        data:{
            1:$('#gender').val(),
            2:$('#age').val(),
            3:$('#height').val(),
            4:$('#weight').val(),
            5:$('#education').val(),
            
            6:$('#marriage').val(),
            7:$('#occupation').val(),
            8:$('#surrounding').val(),
            9:$('#psychology').val(),
            10:$('#pregnant').val(),

            11:$('#diastolic').val(),
            12:$('#systolic').val(),
            13:$('#glucose').val(),
            14:$('#mouth').val(),
            15:$('#eye').val(),

            16:$('#disable').val(),
            17:$('#skin').val(),
            18:$('#heart').val(),
            19:$('#kidney').val(),
            20:$('#smoke').val(),

            21:$('#drink').val(),
            22:$('#diet').val(),
            23:$('#movement').val(),
            24:$('#diabetes').val(),
            25:$('#copd').val(),

            26:$('#treatment').val(),
            27:$('#heredopathia').val(),
            28:$('#exposure').val(),
            29:$('#imageology').val(),
            30:$('#medicine').val(),
            
        },
        dataType:'json',
        type:'POST',
        async:true,
        success: function(jsondata){
            $("#resultdiv").empty()
            var resulttext = ""
            for(key in jsondata){
                var output = key + " " + jsondata[key];
                // if(jsondata[key] == ""){continue}
                $("#resultdiv").append($("<p></p>").text(output));
            }
        },
        error:function(data){ alert('error')}
    })
}