kill -9 $(ps -A | grep python | awk '{print $1}')
python3 serv.py