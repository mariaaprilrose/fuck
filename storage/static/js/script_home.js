$(document).ready(function() {
    $('#far_clouds').pan({fps: 30, speed: 0.7, dir: 'left', depth: 30});
    $('#near_clouds').pan({fps: 30, speed: 1, dir: 'left', depth: 70});
    $('#plane').pan({fps: 30, speed: 1, dir: 'right', depth: 50});
    move_upper_waves();
    move_middle_waves();
    //move_bottom_waves();
    $('#whale').animate({left: "+=2%"}, 5000, 'linear');
    $('#other_videos li:gt(3)').hide();
    counter = 0;
    $('#next').click(function() {
        if (counter < 4) {
            counter++;
        }

        if (counter == 1) {
            $('#other_videos li:nth-child(1)').hide();
            $('#other_videos li:nth-child(5)').show();
        } else if (counter == 2) {
            $('#other_videos li:nth-child(2)').hide();
            $('#other_videos li:nth-child(6)').show();
        } else if (counter == 3) {
            $('#other_videos li:nth-child(3)').hide();
            $('#other_videos li:nth-child(7)').show();
        } else if (counter == 4) {
            $('#other_videos li:nth-child(4)').hide();
            $('#other_videos li:nth-child(8)').show();
        }
    });
    $('#back').click(function() {
        if (counter > 0) {
            counter--;
        }

        if (counter == 3) {
            $('#other_videos li:nth-child(4)').show();
            $('#other_videos li:nth-child(8)').hide();
        } else if (counter == 2) {
            $('#other_videos li:nth-child(3)').show();
            $('#other_videos li:nth-child(7)').hide();
        } else if (counter == 1) {
            $('#other_videos li:nth-child(2)').show();
            $('#other_videos li:nth-child(6)').hide();
        } else if (counter == 0) {
            $('#other_videos li:nth-child(1)').show();
            $('#other_videos li:nth-child(5)').hide();
        }
    });
    $('#other_videos img').click(function() {
        $('#video').attr({
            'src': $(this).attr('alt'),
            'autoplay': 'autoplay'
        });
    });
});

function move_upper_waves() {
    $("#upper_wave").animate({right: "+=20px"}, 2000, 'linear', function () {
        $("#upper_wave").animate({right: "-=20px"}, 2000, 'linear', move_upper_waves);
    });
}

function move_middle_waves() {
    $("#middle_wave").animate({right: "+=50px"}, 3000, 'linear', function () {
        $("#middle_wave").animate({right: "-=50px"}, 3000, 'linear', move_middle_waves);
    });
}
    
function move_bottom_waves() {
    $("#bottom_wave").animate({right: "+=50px"}, 5000, 'linear', function () {
        $("#bottom_wave").animate({right: "-=50px"}, 5000, 'linear', move_bottom_waves);
    });
}
