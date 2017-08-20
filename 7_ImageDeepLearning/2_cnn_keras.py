from PIL import Image
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import os
import numpy as np

#   카테고리 지정
from theano.gof.opt import optimizer

categories = ["chair", "camera", "butterfly", "elephant", "flamingo"]
nb_classes = len(categories)

#   이미지 크기
image_width = 64
image_height = 64

#   데이터 열기
X_train, X_test, y_train, y_test = np.load("./image/5obj.npy")
#   데이터 정규화
X_train = X_train.astype("float") / 256
X_test = X_test.astype("float") / 256
print('X_train shape :', X_train.shape)

#   모델 구축하기
model = Sequential()
model.add(Convolution2D(32, 3, 3, border_mode = 'same', input_shape=X_train.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, 3, 3, border_mode='same'))
model.add(Activation('relu'))
model.add(Convolution2D(64, 3, 3))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

#   모델 훈련
model.fit(X_train, y_train, batch_size=32, nb_epoch=50)

#   모델 평가
score = model.evaluate(X_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])

#############################################
#   예측하기
pre = model.predict(X_test)
#   예측 결과 테스트
for i, v in enumerate(pre) :
    pre_ans = v.argmax()    #   예측 레이블
    ans = y_test[i].argmax()    #   정답 레이블
    dat = X_test[i] #   이미지 데이터
    if ans == pre_ans : continue
    #   예측이 틀릴경우 출력
    print("[NG]", categories[pre_ans], "!=", categories[ans])
    print(v)
    #   이미지 출력
    fname = "image/error/" + str(i) + "-" + categories[pre_ans] + "-ne-" + categories[ans] + ".png"
    dat *= 256
    img = Image.fromarray(np.uint8(dat))
    os.makedirs(os.path.dirname(fname), exist_ok=True)
    img.save(fname)


#############################################
#   저장
hdf5_file = "/image/5obj-model.hdf5"
if os.path.exists(hdf5_file) :
    #   학습된 모델 읽기
    model.load_weights(hdf5_file)
    print("load ok")
else :
    #   파일로 저장
    model.fit(X_train, y_train, batch_size=32, epochs=50)
    os.makedirs(os.path.dirname(hdf5_file), exist_ok=True)
    model.save_weights(hdf5_file)
    print("save ok")