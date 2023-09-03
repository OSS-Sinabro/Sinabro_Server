<div align="center">
  <h1>Sinabro Server</h1>
<br/>
</div>

<br/>

## 🛠 시스템 구성도
><p align="center"><img src="https://github.com/OSS-Sinabro/Sinabro_Server/assets/90829718/5b7d8e34-79e5-4831-9091-6faea1e605cf" alt="시스템 구성도" width="600"></p>

<br/>

## ⚙ 서버 환경
><p align="center"><img src="https://github.com/OSS-Sinabro/Sinabro_Server/assets/90829718/6982fc1e-fdf6-4554-81c5-57f9be5a3ba1" alt="시스템 환경" width="600"></p>

<br/>

## 🖥 서버 구동화면

| **MQTT broker / Flask / Classification / Celery** | **관제센터 Webpage** |
| :--------: | :---------------------------: |
| <p align="center"><img src="https://github.com/OSS-Sinabro/Sinabro_Server/assets/90829718/0943afb7-930d-4bee-9010-e652704d2139" alt="구동화면 1" width="1000"></p> | <p align="center"><img src="https://github.com/OSS-Sinabro/Sinabro_Server/assets/90829718/f8a6bfbf-21d5-48a7-a98b-4d88f1b4522e" alt="구동화면 2" width="1200"></p> |

---
<br/>

## How to Build
<br/>

1. **Git clone**
```bash
> git clone https://github.com/OSS-Sinabro/Sinabro_Server.git
```
<br/>

2. **Virtual ENV Setting**<br/>
    - Python 3.10 이상 버전 설치 권장<br/>
    - 가상환경 이름은 <b>sina</b> 로 설정해 주세요

```bash
> python -m venv sina
> .\sina\Scripts\activate.bat
(sina) >
```
<br/>

3. **Install Package**<br/>

```bash
(sina) > pip install -r requirements.txt
```
<br/>

4. **Set config.py**<br/>
    - CCTVS_IDS 리스트는 정수 형태로 설정해 주세요<br/>
    - MQTT_BROKER_ADDRESS는 내부 IP 주소 형태로 설정해 주세요
```
# config.py

CCTVS_IDS = []
EX) CCTVS_IDS = [1, 2, 3]

MQTT_BROKER_ADDRESS = ""
EX) MQTT_BROKER_ADDRESS = "192.168.219.121"
```
<br/>

5. **Set Model file**<br/>
    - model download : <a href="https://drive.google.com/file/d/16JeA2ZvXkhJcd5dfkVBkT9tbOrz0xvyb/view?usp=sharing">Flooded_road_classification_model.pth</a>
    - 다운로드 받은 model을 project root path에 위치시켜 주세요
