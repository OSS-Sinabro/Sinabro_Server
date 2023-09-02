from flask import Flask, send_file, abort, render_template
import os
from config import N, CCTVS, BASE_IMAGE_PATH

# Flask 앱을 생성
app = Flask(__name__)

@app.route('/image/<topic>')
def get_image(topic):
    
    # 이미지 파일 경로
    image_path = os.path.join(BASE_IMAGE_PATH, topic, f"{topic}_flooded.jpg")
    print(image_path + " check")

    # 이미지 파일이 없는 경우 404 에러를 반환
    if not os.path.exists(image_path):
        abort(404)
    
    # 이미지 파일을 반환
    return send_file(image_path, mimetype='image/jpg')

@app.route('/')
def index():
    return render_template('cctv_control_tower.html', N=N, cctvs = CCTVS)


if __name__ == '__main__':
    app.run(debug=True) # 개발모드
    # app.run(debug=False) # 프로덕션모드
