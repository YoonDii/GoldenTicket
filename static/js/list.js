

$(function () {
    /*장르리스트*/
    //2뎁스 메뉴 보여주는 가짜 셀렉트박스 & 다른데 클릭해도 셀렉트박스 닫히도록
    $(".li-sec-tit2").on('click', function (e) {
        if ($(this).is(".on")) {
            e.preventDefault();
            $(this).removeClass("on");
            $(".li-sec-select").slideUp();

        } else {
            e.preventDefault();
            $(this).addClass("on");
            $(".li-sec-select").slideDown();
        }
    });
    $(document).mouseup(function (e) {
        var container = $(".li-sec-tit2");
        if (!container.is(e.target) && container.has(e.target).length === 0) {
            $(".li-sec-select").slideUp();
            $(".li-sec-tit2").removeClass("on");
        }
    });
});


$(document).ready(function () {
    jsf_genre_GetGenreList('15456', '1', '3');

    $('.li-sec-tag a').each(function () {
        $(this).unbind('click.btnGenreListTab').bind('click.btnGenreListTab', function (e) {
            e.preventDefault();
            $("#pCurPage").val(1);
            jsf_genre_GetGenreList('15456', '1', $(this).attr('token'));
        });

    });

});

//Scroll Event
var asyncType = false;
var didScroll;
var lastScrollTop;

$(window).scroll(function (event) {
    didScroll = true;
});

setInterval(function () {
    if (didScroll) {
        hasScrolled();
        didScroll = false;
    }
}, 1);

function hasScrolled() {
    var scrollT = $(this).scrollTop();
    var scrollH = $(this).height();
    var list_secH = $(".list-sec").height();
    
    if (scrollT > lastScrollTop) {
        //Scroll Down
        if (scrollT + scrollH + 150 >= list_secH) {
            var curPage = parseInt($("#pCurPage").val());
            var lastPage = Math.ceil($("#ListTotalCnt").val() / $("#pPageSize").val());
            if (curPage < lastPage) {
                if(asyncType){
                    return;
                }
                $("#pCurPage").val(curPage + 1);
                jsf_genre_GetGenreList('15456', '1', $('.li-sec-tag').find('a[class*="on"]').attr('token') );
                asyncType = true;
            }
        }
    }

    lastScrollTop = scrollT
}

    
