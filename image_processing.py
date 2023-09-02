from torchvision.models import resnet152
import torch.nn as nn
from PIL import Image
from torchvision import transforms
import torch.nn.functional as F
import torch
import os
import io
from collections import defaultdict
from celery import Celery
import logging
from config import CELERY_BROKER_URL, BASE_IMAGE_PATH, MODEL_PATH

## 로깅 설정
logging.basicConfig(filename='app.log', level=logging.INFO)

# Celery 앱 생성
app = Celery('image_processing', broker=CELERY_BROKER_URL)

# 모델 정의
model = resnet152()
num_features = model.fc.in_features
model.fc = nn.Sequential(
    nn.Dropout(0.3),
    nn.Linear(num_features, 3)
)

# 저장된 모델 가중치 로드
model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device('cpu')))
model.eval()

# 이미지 추론 함수
def infer_image(byte_im):
    transform = transforms.Compose([
        transforms.Resize((320, 320)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image = Image.open(io.BytesIO(byte_im)).convert("RGB")
    image_tensor = transform(image).unsqueeze(0)
    output = model(image_tensor)
    probabilities = F.softmax(output, dim=1)
    predicted_probability, predicted_class = torch.max(probabilities, 1)
    return predicted_class.item(), predicted_probability.item() * 100  #(추론 확률까지 반환)


# 연속적으로 감지된 클래스를 추적하는 딕셔너리
continuous_class = defaultdict(int)

# 이미지를 분류하는 작업
@app.task
def classify_image(topic, byte_im):
    # 이미지 추론 수행
    predicted_class, confidence = infer_image(byte_im)

    # 신뢰도 80 이하인 경우 일반도로 판단
    if predicted_class in [1, 2] and confidence < 80:
        predicted_class = 0
     
    if predicted_class == 0:
        print(topic, " > ", predicted_class, " : 일반\n")
    elif predicted_class in [1, 2]:
        print(topic, " > ", predicted_class, " : 침수\n")

    # 결과를 처리하는 작업을 큐에 추가
    logging.info("calling handle_result.delay") # log
    handle_result.delay(topic, predicted_class, byte_im)


# 분류 결과를 처리하는 작업
@app.task
def handle_result(topic, predicted_class, byte_im):
    logging.info("handle_result function called!") # log
    # 결과 처리 코드...
    if predicted_class in [1, 2]:
        logging.info("침수 count up") # log
        continuous_class[topic] += 1
    else:
        logging.info("count 초기화") # log
        continuous_class[topic] = 0

    # 연속적으로 감지된 클래스가 3회 이상인 경우
    if continuous_class[topic] >= 3:
        image_folder = os.path.join(BASE_IMAGE_PATH, topic)
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        image_path = os.path.join(image_folder, f"{topic}_flooded.jpg")
        logging.info(topic, " 침수패턴 검출") # log

        with open(image_path, "wb") as image_file:
            image_file.write(byte_im)
            logging.info(topic, " 이미지 저장") # log

