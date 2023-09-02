call .\sina\Scripts\activate
cd .\

echo        Run MQTT Broker
pause
start cmd /k "mosquitto -v -c broker.conf"

echo        Run Flask Server
pause
start cmd /k "python flask_app.py"

echo        Run Image Classify
pause
start cmd /k "python image_classify.py"

echo        Run Celery Worker
pause
start cmd /k "celery -A image_processing worker --loglevel=INFO --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo --logfile=celery_deatail_logs.log"


    