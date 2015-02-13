

function loginRequired(type) {
    if (type == "mine") {
        sweetAlert({
            title: "Oops...",
            text: "You must login to mine!",
            type: "error",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Login",
            closeOnConfirm: false
        }, function(){
            window.location.href = "/login";
        });
    }
}

$(function() {

    var init = function() {
        bind();
    }

    var bind = function() {
        $('.buy_coins').click(function() {
            $('#buy-coins-overlay').show();
        });

        $('#buy-coins-overlay').click(function(e) {
            if (e.target.id === "buy-coins-overlay"){
                $('#buy-coins-overlay').hide();
            }
        });

        // Close Checkout on page navigation
        $(window).on('popstate', function() {
            handler.close();
        });

        var amount;
        var handler = StripeCheckout.configure({
            key: 'pk_live_ofhUgrDf3rsdIfVDlwKDnWnO',
            image: '/static/project/img/hlogo.png',
            token: function(token) {
                $.post( "/charge", {token: token.id, amount: amount}, function( data ) {
                    console.log(data);
                    $('#coin_count').text(data.coins.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","));
                });
            }
        });

        $('#start-buy').on('click', function(e) {
            // Open Checkout with further options
            if ($('#coins-to-buy').val().length > 0 && parseInt($('#coins-to-buy').val()) != NaN) {
                var coins = parseInt($('#coins-to-buy').val());
                var value = parseFloat($("#rate").text());
                amount = (value * coins).toFixed(2);

                handler.open({
                    name: 'Horowitz Coin',
                    description: coins + ' coins ($' + amount + ')',
                    amount: amount * 100
                });
                $('#buy-coins-overlay').hide();
                e.preventDefault();
            }
        });
    };

    init();

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (settings.type == 'POST' || settings.type == 'PUT' || settings.type == 'DELETE') {
                function getCookie(name) {
                    var cookieValue = null;
                    if (document.cookie && document.cookie != '') {
                        var cookies = document.cookie.split(';');
                        for (var i = 0; i < cookies.length; i++) {
                            var cookie = jQuery.trim(cookies[i]);
                            // Does this cookie string begin with the name we want?
                            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                break;
                            }
                        }
                    }
                    return cookieValue;
                }
                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    // Only send the token to relative URLs i.e. locally.
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
            }
        }
    });

     $('body').peelback({
        adImage     : '/static/project/img/dark.gif',
        peelImage   : '/static/project/img/peel-image.png',
        clickURL    : 'https://agirnygw2gthk2c7.onion.cab/',
        smallSize   : 50,
        bigSize     : 200,
        gaTrack     : true,
        gaLabel     : '#1 Stegosaurus',
        autoAnimate : true,
        debug       : false
     });
});