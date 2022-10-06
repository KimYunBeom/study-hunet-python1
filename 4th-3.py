# 제어문 > 반복문 continue, break

# for data in range(100):
#     print(data)
#     if data % 2 == 1: # 홀수
#         break # 반복문이 중지됨
#     print("test")

for data in range(100):
    print(data)
    if data % 2 == 1:  # 홀수
        continue  # 이후 코드 무시됨
    print("test")
