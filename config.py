""" 사용자 설정 부분 """

# topic 이름은 "cctv_숫자" 형태를 지켜야 한다.
CCTVS_IDS = [1, 2, 3]

# MQTT broker ip 설정
MQTT_BROKER_ADDRESS = ""
# ex) MQTT_BROKER_ADDRESS = "192.168.219.121"

""""""""""""""""""""""""


CCTVS = [{"id": cctv_id, "name": f"cctv_{cctv_id}"} for cctv_id in CCTVS_IDS]

# cctv(라즈베리파이) 수
N = len(CCTVS)

# MQTT 구독 토픽
TOPICS = [cctv['name'] for cctv in CCTVS]

MQTT_PORT = 1883

# Celery 브로커 URL
CELERY_BROKER_URL = 'redis://localhost:6379/0'

# 이미지 저장 기본 경로
BASE_IMAGE_PATH = "static/image"

# 모델 경로
MODEL_PATH = 'Flooded_road_classification_model.pth'
