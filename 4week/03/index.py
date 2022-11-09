# 과제목표
# 1) html에서 ajax를 통한 Flask API 호출
# 2) Flask에서 route를 통한 mongodb 데이터 생성 및 조회 작업
# 참고 문서 https://pymongo.readthedocs.io/en/stable/tutorial.html

from flask import Flask, render_template, request, jsonify
from db_init import db

app = Flask(__name__)

@app.route("/")
def show_index_page():
    return render_template("index.html")


# methods 인자를 추가해서 어떤 방식의 http 통신을 받을건지 설정할 수 있다.
#  --- 아무것도 명시하지않으면 GET으로 인지
#  --- method 종류: GET / POST / PUT / PATCH / DELETE )
# (* templates/index.html 파일 참고해서 데이터를 어떻게 보내는지 확인해주세요.)
@app.route("/user")
def get_user():
    user_name = request.args.get("name") # url에서 name 파라미터에 해당 되는 값을 가져온다.
    # try / except 는 api 통신이나 db 통신과 같이 의도하지 않은 에러가 일어날 수 있는 상황에서 자주 쓴다.
    # 만약 try / except로 감싸지 않은 상태에서 error가 발생된다면 프로세스가 멈춘다. 
    # try 내부에서 일어날 수 있는 에러들은 except 이하로 내려준다.

    try: 
        # find_one()을 통해 조건을 걸 수 있다.
        # find_one() 조건에 {"_id": False}를 명시해주지 않으면 json 형태로 응답을 해줄 수 없음.
        user_data = db['test_account'].find_one({"name": user_name}, {"_id": False})
        return jsonify({"result": user_data})
    except ValueError as error:
        print('(!)DB Error', error)
        return jsonify({"result": False, "message": "Not found user."})


# ---------- 직접 작성 부분---------- #
#
# 클라이언트(브라우저)에서 ajax 통신을 통해 user 데이터를 받고, 
# 이 데이터를 mongodb에 저장하는 코드를 작성해주세요.
#
# ----------직접 작성 부분---------- #    

if __name__ == "__main__":
    app.run()