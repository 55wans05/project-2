#/bin/bash
cd web
podman build -t project2 .
podman run -p 5000:5000 --rm -it project2