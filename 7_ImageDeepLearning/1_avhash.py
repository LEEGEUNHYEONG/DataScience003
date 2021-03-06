from PIL import Image
import numpy as np

#   이미지 데이터를 Average Hash로 변환
def average_hash(fname, size = 16) :
    img = Image.open(fname)
    img = img.convert('L')  #   그레이 스케일로 변환
    img = img.resize((size, size), Image.ANTIALIAS) #   리사이즈
    pixel_data = img.getdata()  #   픽셀 데이터 가져오기
    pixels = np.array(pixel_data)   #   Numpy 배열로 변환
    pixels = pixels.reshape((size, size))   # 2차원 배열로 변환
    avg = pixels.mean() #   평균 구하기
    diff = 1 * (pixels > avg)   #   평균보다 크면 1, 작으면 0
    return diff

#   이진 해시로 변환
def np2hash(n) :
    bhash = []
    for nl in ahash.tolist() :
        sl = [str(i) for i in nl]
        s2 = "".join(sl)
        i = int(s2, 2)  #   이진수를 정수로 변환
        bhash.append("%04x" % i)
    return "".join(bhash)

#   Average Hash 출력
ahash = average_hash('tower.jpg')
print(ahash)
print(np2hash(ahash))
