import cv2
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("img_dir", help="image directory path")
parser.add_argument("img_height", help="height of image")
args = parser.parse_args()

file = args.arg1
H = int(args.arg2)
dir_name = os.path.splitext(os.path.basename(file))[0] + "-H=" + str(H)

movie = cv2.VideoCapture(file)
nframe = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))
fps = movie.get(cv2.CAP_PROP_FPS)
time = nframe/fps
print(f"フレーム数：{nframe}")
print(f"フレームレート：{fps}")
print(f"動画時間：{time}")
if not os.path.exists(dir_name):
    os.makedirs(dir_name)   
print(dir_name)

for i in range(nframe):
    ret, frame = movie.read()
    h, w, _ = frame.shape
    W = int((H/h)*w)
    frame = cv2.resize(frame, dsize=(W, H))
    cv2.imwrite(dir_name + "/" + str(i).zfill(10) + ".png", frame)



