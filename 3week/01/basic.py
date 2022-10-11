###### 1. List 자료형 다루기 ######
# [List] 자료형 선언
test_list = [1, "two", "3", 4, "five"]
print(test_list)

# [List] 특정 index의 value 가져오기
value_0 = test_list[0]
print(value_0)

# [List] value 추가
test_list.append("six") # 제일 마지막에 추가
print(test_list)  

test_list.insert(2, 3) # 현재 리스트의 문자열 순서대로 추가
print(test_list)

# [List] value 변경
test_list[1] = 2
print(test_list)

# [List] value 삭제
del test_list[0] # 0번 인덱스 삭제
print(test_list)

# [List] List의 길이 가져오기
print(len(test_list))

# [List] For문 (1) value 가져오기
for val in test_list:
    print(val)

# [List] For문 (2) index, value 가져오기
for index, val in enumerate(test_list):
    print(f'index: {index}, value: {val}') # f-string : 내부에 변수를 삽입할 수 있음.



###### 2. Dict 자료형 다루기 ######
#2 [Dict] 자료형 선언
user_info = {
    "name": "Jason",
    "email": "example@fastcampus.com",
    "birth": "1993-11-23",
    "auth_level": 5,
    "skill_list": ['html', 'css', 'javascript', 'python']
}
print(user_info)

# [Dict] 해당 key의 value 가져오기
user_name = user_info.get("name")
print(user_name)
user_email = user_info["email"]
print(user_email)

# [Dict] key, value 추가
user_info['addr'] = "korea"
print(user_info)

# [Dict] value 변경
user_info["auth_level"] = 3
print(user_info)

# [Dict] key, value 삭제
del user_info["addr"]
print(user_info)
