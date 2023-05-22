import numpy as np
import cv2
import utils

FILE_NAME = "trained.npz"

# 각 글자의 데이터(trian)와 정답(train_labels) 업로드
with np.load(FILE_NAME) as data:
    train = data['train']
    train_labels = data['train_labels']
    knn = cv2.ml.kNearest_create()  # knn 알고리즘 객체 생성 (knn 알고리즘 초기화)
    knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)  # 행단위 샘플
"""
cv2.ml_KNearest.train (samples, layout, responses)
samples : 학습 데이터 행렬 (dtype = numpy.float32)
layout : 학습 데이터 배치 방법 (ROW > 한 행, COL > 한 열 구성)
responses : 각 학습 데이터에 대응되는 정답 행렬 (dtype = numpy.int32 또는 numpy.float32)
"""


# 특정 이미지를 받았을때, 학습 데이터들을 불러와 검사
def get_result(file_name):
    image = cv2.imread(file_name)
    chars = utils.extract_chars(image)  # 이미지들을 왼쪽에서부터 chars 함수에 담는다 (apple이라 적힌 이미지에서 알파벳들 추출) 함수 정확히 이해 X
    result_string = "" #결과 string들 담을 것
    # chars에서 train 데이터 속 어떤걸로 분류가 되는지 찾은 다음 matched에 넣는다
    for char in chars:
        # 가장 가까운 K개의 글자를 찾아, 어떤 숫자에 해당하는지 찾는다.
        # ret 예측 결과 데이터 result 예측 결과 neighbors k범위의 이웃 데이터 dist 이웃 데이터간 거리
        ret, result, neighbors, dist = knn.findNearest(utils.resize20(char[1]), k=9)
        matched = result
        result_string += str(matched)
        # result_string += matched (나동빈 코드)
    return result_string

f = open('run.txt', 'w')
f.write(get_result("input.png")) #파일 이름 미정, 인식하고 싶은 사진 파일 입력
f.close()