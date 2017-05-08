import math
import random

dot_cnt = 100000
cnt_in = 0
for i in range(dot_cnt):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if math.pow(x, 2) + math.pow(y, 2) <= 1:
        cnt_in += 1
        print(cnt_in)

print('-------------------------------------------')
print(' 전체점의 개수: ', dot_cnt)
print(' 사분원에 찍힌 점의개수: ', cnt_in)
print(' 원주율 : ', (cnt_in/dot_cnt)*4)

