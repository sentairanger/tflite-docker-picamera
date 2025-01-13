# tflite-docker-picamera
This project deploys a PiCamera app using Flask and TFLite via Docker and Docker Compose.

## Getting Started

This has been tested on a Pi 4 so it should work on a Pi 5, CM5, CM4, and any other 64 bit Pi. However it's recommended to use a board with at least 2 GB of RAM. First install Docker on Raspberry Pi. Follow this [https://docs.docker.com/engine/install/debian/](link). Docker compose should already be included so all you need to do is to run `docker compose build` and then `docker compose up`. That's it. Then go to a browser and go to `ip-address-of-pi`:5000 and the app should appear. Take a picture first and then click to classify the image.

![image](https://github.com/sentairanger/tflite-docker-picamera/blob/main/screen.jpg)
