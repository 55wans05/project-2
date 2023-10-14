#/bin/bash
PORT=$((1000 + $RANDOM % 65535))
cp credentials.ini web/credentials.ini
cd web
sed -i "s/PORT=5000/PORT=$PORT/g" credentials.ini
podman build -t project2 .
podman run -p $PORT:5000 --rm -it project2