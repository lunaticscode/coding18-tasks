from flask import Flask, render_template, jsonify
from pymongo import errors as pymonogoError
from db_init import db
collection_name = "test_paging_data"

app = Flask(__name__)

def get_page_data(page_number=0):
    try:
        page_data = db[collection_name].find({}, {"_id": False}).skip(page_number * 10).limit(10)
        print(list(page_data))
    except ValueError as error:
        print('(!)DB error \n', error)
    
@app.route("/")
def show_index_page():
    get_page_data()
    return render_template("index.html")







# --------------- 여기는 건드리지 마세요 ---------------- #
def is_exist_dummy_collection(): # 컬렉션 존재여부 화인
    try:
        db.validate_collection(collection_name)
        return True
    except pymonogoError.OperationFailure:
        return False
# --------------- 여기는 건드리지 마세요 ---------------- #


# --------------- 여기는 건드리지 마세요 ---------------- #
def insert_dummy_data(): # 테스트용 데이터 추가
    for idx in range(100):
        user_data = {
            "name": "usename-" + str(idx),
            "email": "user" + str(idx) + "@email.com"
        }
        try: 
            db[collection_name].insert_one(user_data)
        except ValueError as error:
            print(f'(!) DB Error occured ::\n{error}')
# --------------- 여기는 건드리지 마세요 ---------------- #

if __name__ == "__main__":
    # ------------ 여기는 건드리지 마세요 ------------- #
    if is_exist_dummy_collection() == False:
        insert_dummy_data()
    # ------------ 여기는 건드리지 마세요 ------------- #
    app.run()