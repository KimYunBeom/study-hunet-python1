# list 자료형

data = [
    "data1",
    "data2",
    1,
    2,
    3,
    [4, 5, 3],
]
"""
print(data[2])  # indexing : 값을 가리킴
print(data[:2])  # slicing : 값의 일부를 잘라냄
"""

"""
data2 = "Hello World"
print(data2[:5])
"""

# list 자료형의 값 변경
"""
data[0] = 1234
print(data)
"""

# list 자료형의 값 삭제
del data[0]
print(data)
