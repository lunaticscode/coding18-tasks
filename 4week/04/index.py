# 과제목표
# 1) Flask에서 route를 통해 url의 파라미터를 해석
# 2) 게시판에서 흔히 볼 수 있는 페이징 처리
# (* 페이징 처리를 간단히 설명하면, 1페이지 클릭 하면 1 ~ 10번 게시물, 2페이지 클릭하면 11 ~ 20번 게시물 출력하는 형태)

from flask import Flask, render_template, request, jsonify
from pymongo import errors as pymonogoError
from db_init import db
# ------------ 여기는 건드리지 마세요 ------------ #
# mongoDB 컴패스 내부에서 local -> test_paging_data 컬렉션을 확인해보세요.
collection_name = "test_paging_data"
# ------------ 여기는 건드리지 마세요 ------------ #

app = Flask(__name__)

@app.route("/test")
def get_param():
    try:
        # http://localhost:5000/test?title=fastcampus 로 요청을 보낼 경우,
        # request.args.get()을 통해 얻고자하는 파라미터의 값을 받을 수 있음.
        title = request.args.get("title") 
        print(title)
        return jsonify({"result": True, "title": title}) # jsonfy를 통해 html 템플릿이 아닌 json 형태의 데이터만 보낼 수 있음.
    except ValueError as Error:
        print('(!) Query Parsing Error\n', Error)
        return jsonify({"result": False})


@app.route("/")
def show_index_page():
    # ----------- 직접 코드 작성 ------------ #
    #
    # 클라이언트에서 요청한 api url 에서 'page' 라는 파라미터를 받고,
    # 이 'page' 파라미터를 이용하여 10개씩 데이터를 페이징 처리해서 출력하는 코드를 작성해주세요.
    # (* pymongo의 skip, limit을 이용)  
    # 
    # ----------- 직접 코드 작성 ------------ #
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
def insert_dummy_data(): # 페이징 테스트용 데이터 추가
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