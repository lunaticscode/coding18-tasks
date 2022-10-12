from db_init import db
from faker import Faker
from faker.providers import internet
from uuid import uuid4
fake = Faker()
fake.add_provider(internet)

# dummy 유저 정보 생성
def create_dummy_user():
    uid = str(uuid4())
    name = fake.name()
    email = fake.email()
    user_data = {
        "_id": uid,
        "uid": uid,
        "name": name,
        "email": email,
    }
    return user_data



# ===== 1) 유저 정보 DB에 저장하기 ===== #
def insert_user():
    user_data = create_dummy_user()
    try:
        db["dummy_user"].insert_one(user_data)
    except ValueError as err:
        print(f'(!)DB Error {err}')
        return False
    return True
    
# insert_user()
# ==================================#



# ===== 2) 저장된 유저 목록 가져오기 ===== #
def get_users():
    try:
        user_list = db["dummy_user"].find()
        return list(user_list)
    except ValueError as err:
        print(f'(!)DB Error {err}')
        return False

user_list = get_users()
print(user_list)
# ==================================#



# ===== 3) 저장된 유저 이름 변경하기 ===== #
def modify_user_name(uid, after_name):
    if uid == None or uid == "":
        return False
    if after_name == None or after_name == "":
        return False
    try:
        db["dummy_user"].update_one({"uid": uid}, {"$set": {"name": after_name}})
        return True
    except ValueError as err:
        print(f'(!)DB Error {err}')

# modify_user_name("저장된 유저의 uid", "변경할 이름")
# ============================================#



# ===== 4) 저장된 유저 정보 삭제 ====== #
def delete_user(uid):
    if uid == None or uid == "":
        return False
    try:
        db["dummy_user"].delete_one({"uid": uid})
    except ValueError as err:
        print(f'(!)DB Error {err}')

# delete_user("삭제할 유저의 uid")
# ==================================#
