# 자료형 > tuple

# list와 달리 수정, 삭제가 불가능. list 보다 속도가 빠르다.

data = (1, 2, 4)
print(data)

"""
print(data[0])
print(data[:2])

data[0] = "123"
print(data)
"""

del data[0]
print(data)
