import cv2
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("video_path", help="video file path")
parser.add_argument("img_height", help="height of image")
parser.add_argument("fps", help="fps(int) that you want to convert to")
args = parser.parse_args()

conv_fps = int(args.fps)

file = args.video_path
H = int(args.img_height)
dir_name = os.path.splitext(os.path.basename(file))[0] + "-H=" + str(H) + "-fps=" + str(conv_fps)

movie = cv2.VideoCapture(file)
nframe = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))
video_fps = int(round(movie.get(cv2.CAP_PROP_FPS)))
time = nframe/video_fps
print(f"フレーム数：{nframe}")
print(f"フレームレート：{video_fps}")
print(f"動画時間：{time}")

if not os.path.exists(dir_name):
    os.makedirs(dir_name)   

step = int(video_fps/conv_fps)

frame_counter = 0

for i in range(nframe):
    ret, frame = movie.read()
    
    frame_counter += 1
    
    if(frame_counter >= step):
        h, w, _ = frame.shape
        W = int((H/h)*w)
        frame = cv2.resize(frame, dsize=(W, H))
        cv2.imwrite(dir_name + "/" + str(i).zfill(10) + ".png", frame)
        frame_counter = 0



