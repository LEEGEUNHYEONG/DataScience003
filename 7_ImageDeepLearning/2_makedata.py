import os, glob

import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split

#   분류대상 카테고리 선택
caltech_dir = "./image/101_ObjectCategories"
categories = ["chair", "camera", "butterfly", "elephant", "flamingo"]
nb_classes = len(categories)

#   이미지 크기 지정
image_width = 64
image_height = 64
pixels = image_width * image_height

#   이미지 읽기
X = []
Y = []
for idx, cat in enumerate(categories) :
    #   레이블 지정
    label = [0 for i in range(nb_classes)]
    label[idx] = 1
    #   이미지
    image_dir = caltech_dir + "/" + cat
    files = glob.glob(image_dir + "/*.jpg")

    print(image_dir)
    for i, f in enumerate(files) :
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_width, image_height))
        data = np.asarray(img)
        X.append(data)
        Y.append(label)
        if i % 10 == 0 :
            print(i, "\n", data)

X = np.array(X)
Y = np.array(Y)

#   학습 & 테스트 데이터 구분
X_train , X_test, y_train, y_test = \
    train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save("./image/5obj.npy", xy)

print("ok", len(Y))