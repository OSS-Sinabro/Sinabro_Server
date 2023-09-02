$(document).ready(function(){
    setInterval(function(){
        // 각 라즈베리파이에 대해
        for (var i = 1; i <= N; i++) {  // N : 연결된 raspberry pi 수
            
            // IIFE를 사용하여 현재 i 값을 캡쳐
            (function(current_i) {
                // AJAX 요청을 사용하여 서버에 새 이미지를 요청
                $.get("/image/cctv_" + current_i)
                    .done(function() {
                        // 이미지 소스를 새 이미지의 URL로 업데이트
                        $("#image" + current_i).attr("src", "/image/cctv_" + current_i + "?" + new Date().getTime());
                        // 이미지 컨테이너를 보이게 합니다.
                        $("#imageContainer" + current_i).css("display", "block");
                    })
                    .fail(function() {
                        // 이미지 요소를 제거
                        $("#imageContainer" + current_i).remove();
                    });
            })(i);  // 즉시 실행 함수에 현재 i 값을 전달
        }
    }, 1500); // 1.5초마다 새 이미지를 요청
});
