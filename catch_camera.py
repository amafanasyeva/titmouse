import cv2, itertools, time

ip = "192.168.1.2"
user = "admin"
pwd  = "zyitJk2X3Kn!"

cands = [
    # MJPEG
    "http://{ip}/mjpeg",
    "http://{ip}/video.mjpg",
    "http://{ip}/mjpg/video.mjpg",
    "http://{ip}/cgi-bin/mjpeg",
    "http://{ip}/cgi-bin/video.cgi?type=mjpg",
    # HLS
    "http://{ip}/live.m3u8",
    "http://{ip}/hls/live.m3u8",
    "http://{ip}/stream.m3u8",
    # RTSP (универсальные/брендовые)
    "rtsp://{user}:{pwd}@{ip}:554/Streaming/Channels/101",
    "rtsp://{user}:{pwd}@{ip}:554/Streaming/Channels/102",
    "rtsp://{user}:{pwd}@{ip}:554/cam/realmonitor?channel=1&subtype=0",
    "rtsp://{user}:{pwd}@{ip}:554/h264Preview_01_main",
    "rtsp://{user}:{pwd}@{ip}:554/h264Preview_01_sub",
    "rtsp://{user}:{pwd}@{ip}:554/stream1",
    "rtsp://{user}:{pwd}@{ip}:554/stream2",
]

def try_open(url):
    cap = cv2.VideoCapture(url.format(ip=ip, user=user, pwd=pwd), cv2.CAP_FFMPEG)
    ok = cap.isOpened()
    if ok:
        ok, _ = cap.read()
    cap.release()
    return ok

for u in cands:
    url = u.format(ip=ip, user=user, pwd=pwd)
    print(f"Пробую: {url}")
    if try_open(u):
        print(f"✅ Работает: {url}")
        break
else:
    print("❌ Подходящий прямой поток не найден. Смотри варианты B/C ниже.")
