$(document).ready(function() {
    /*
    $('#profile #cover img, #profile #cover a').hover(
        function() {$('#profile #cover a').show();},
        function() {$('#profile #cover a').hide();}
    );*/ //the out function doesn't work. :(

    $('#profile #avatar img, #profile #avatar a').hover(
        function() {$('#profile #avatar a').show();},
        function() {$('#profile #avatar a').hide();}
    );

    $('#profile #avatar a').click(function() {
        $('#avatar_upload_form, #mask').fadeIn(300);
    });

    $('#avatar_upload_form a, #mask').click(function() {
        $('#avatar_upload_form, #mask').fadeOut(300);
    });

    $('#id_avatar').change(function() {
        input = this;
        if (input.files && input.files[0]) {
            reader = new FileReader();
            reader.onload = function (e) {
                $('#avatar_upload_form #avatar_img').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
    });

    $('#id_cover').change(function() {
        input = this;
        if (input.files && input.files[0]) {
            reader = new FileReader();
            reader.onload = function (e) {
                $('#cover_upload_form #cover_img').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
    });

    $('#profile #cover a').click(function() {
        $('#cover_upload_form, #mask').fadeIn(300);
    });

    $('#cover_upload_form a, #mask').click(function() {
        $('#cover_upload_form, #mask').fadeOut(300);
    });

    $('#profile #buttons #following').hover(
        function() {$('#profile #buttons #following').text('Unfollow Whale');},
        function() {$('#profile #buttons #following').text('Following Whale');}
    );
});

$(document).keyup(function(e) {
    if (e.keyCode == 27) {
        $('#avatar_upload_form, #mask').fadeOut(300);
        $('#cover_upload_form, #mask').fadeOut(300);
    }
});

function open_login_box() {
    $('#login_box, #mask').fadeIn(300);
}