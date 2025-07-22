echo Starting camera server and websocket server.
/usr/bin/nohup /home/pi/dev/laser-turret/venv/bin/python camera.py &
/usr/bin/nohup /home/pi/dev/laser-turret/venv/bin/python main.py &

echo Started
