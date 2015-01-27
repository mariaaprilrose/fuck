$(document).ready(function() {
    $('#site_nav #contactus, #footer #contactus').click(function() {
        $('#contactus_box, #mask').fadeIn(300);
    });

    $('#contactus_box a img, #mask').click(function() {
        $('#contactus_box, #mask').fadeOut(300);
    });

    $('#auth_nav #login').click(function() {
        $('#login_box, #mask').fadeIn(300);
    });

    $('#login_box a img, #mask').click(function() {
        $('#login_box, #mask').fadeOut(300);
    });

    $('#login_box #signup').click(function() {
        $('#login_box').fadeOut(300);
        $('#signup_box').fadeIn(300);
        $('#signup_box #content').show();
        $('#signup_box form').hide();
    });

    $('#auth_nav #signup').click(function() {
        $('#signup_box, #mask').fadeIn(300);
        $('#signup_box #content').show();
        $('#signup_box form').hide();
    });

    $('#signup_box #content #facebook_signup').click(function() {
        $('#signup_box #content').hide();
        $('#signup_box form').show();
    });

    $('#signup_box form table tr td:nth-child(1)').css('border-right', '2px solid gray');
    $('#signup_box form table tr td:nth-child(2)').css('border-right', '2px solid gray');
    $('#signup_form form table tr td:nth-child(1)').css('border-right', '2px solid gray');
    $('#signup_form form table tr td:nth-child(2)').css('border-right', '2px solid gray');

    $('#signup_box a img, #mask').click(function() {
        $('#signup_box, #mask').fadeOut(300);
    });
});

$(document).keyup(function(e) {
    if (e.keyCode == 27) {
        $('#contactus_box, #mask').fadeOut(300);
        $('#login_box, #mask').fadeOut(300);
        $('#signup_box, #mask').fadeOut(300);
    }
});

function check_length(i) {
    if (i == 1) {
        password = $('#signup_box form #password').val();

        if (password.length < 7) {
            $('#signup_box form #password').css({
                'border':'1px solid red',
                'border-radius':'3px'
            });
        } else {
            $('#signup_box form #password').css({
                'border':'1px solid green',
                'border-radius':'3px'
            });
        }
    } else if (i == 2) {
        password = $('#signup_form form #password').val();

        if (password.length < 7) {
            $('#signup_form form #password').css({
                'border':'1px solid red',
                'border-radius':'3px'
            });
        } else {
            $('#signup_form form #password').css({
                'border':'1px solid green',
                'border-radius':'3px'
            });
        }
    }
}

function check_password(i) {
    if (i == 1) {
        password = $('#signup_box form #password').val();
        retype_password = $('#signup_box form #retype_password').val();

        if (password == retype_password) {
            $('#signup_box form #retype_password').css({
                'border':'1px solid green',
                'border-radius':'3px'});
        } else {
            $('#signup_box form #retype_password').css({
                'border':'1px solid red',
                'border-radius':'3px'});
        }
    } else if (i == 2) {
        password = $('#signup_form form #password').val();
        retype_password = $('#signup_form form #retype_password').val();

        if (password == retype_password) {
            $('#signup_form form #retype_password').css({
                'border':'1px solid green',
                'border-radius':'3px'
            });
        } else {
            $('#signup_form form #retype_password').css({
                'border':'1px solid red',
                'border-radius':'3px'
            });
        }
    }
}
