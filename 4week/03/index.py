# 과제목표
# 1) Flask에서 route를 통한 mongodb CRUD(생성/조회/수정/삭제) 작업
# 2) 클라이언트(html) <--> 서버(Flask) <--> DB(mongoDB) 데이터 흐름 이해
# 참고 문서 https://pymongo.readthedocs.io/en/stable/tutorial.html

from flask import Flask, render_template, request, jsonify
from db_init import db

app = Flask(__name__)

@app.route("/")
def show_index_page():
    return render_template("index.html")

@app.route("/adduser")
def add_random_user():

    user_data = {
        "name": "taylor",
        "age": 30,
        "email": "testuser@email.com",
    }
    
    # try / except 는 api 통신이나 db 통신과 같이 의도하지 않은 에러가 일어날 수 있는 상황에서 자주 쓴다.
    # 만약 try / except로 감싸지 않은 상태에서 error가 발생된다면 프로세스가 멈춘다. 

    try: # try 내부에서 일어날 수 있는 에러들을 except 이하로 내려준다. 
        db['test_account'].insert_one(user_data) # 위의 user_data 를 test_account 컬렉션에 저장.
        return jsonify({"result": True}) # 데이터를 json 형태 {"key" : "value"} 로 변환해서 클라이언트에게 넘겨준다.
    except ValueError as error: # try 내부에서 일어난 error를 감지
        print('(!)DB Error', error)
        return jsonify({"result": False}) 

# methods 인자를 추가해서 어떤 방식의 http 통신을 받을건지 설정할 수 있다.
# 현재는 클라이언트로부터 'name' 이라는 데이터를 받아야 하므로 POST method를 명시해주어야 한다.
# (* templates/index.html 파일 참고해서 데이터를 어떻게 보내는지 확인해주세요.)
@app.route("/getuser", methods=["POST"])
def get_user():
    post_data = request.json # 클라이언트로부터 받은 데이터를 json 형태로 변환.
    username = post_data['name'] # json 형태로 변환된 데이터에서 'name'을 추출.
    try: 
        # mongodb의 test_account 컬렉션에서 'name'이 username
        user_data = db['test_account'].find_one({"name": username}, {"_id": False})
        return jsonify({"result": user_data})
    except ValueError as error:
        print('(!)DB Error', error)
        return jsonify({"result": False})

# ---------- 직접 작성 부분---------- #
#
# 클라이언트(브라우저)에서 ajax 통신을 통해 user 데이터를 받고(Flask에서 받음), 
# 이 데이터를 mongodb에 저장하는 코드를 작성해주세요.
#
# ----------직접 작성 부분---------- #    


# 1) 브라우저에서 '회원가입' 버튼 클릭하면, AJAX로 user데이터 넘김
# --- html 파일생성
# --- 회원가입 버튼 생성
# --- 회원가입 버튼을 눌렀을 때 발생하는 함수
# --------- $("#signUpButton").click(function() {
#   $.ajax( flask로 데이터를 전달해줌 )
# })

# 2) Flask에서 해당 데이터를 받아서 검증(일련의 데이터 유효성 검사)
# --- @app.route("/signup") 라우트를 생성
# --- 라우트에서 Ajax를 통해 날라온 데이터를 받음
# --- 데이터를 검증

# 3) 검증이 통과된 데이터를 pymongo를 통해서 user 데이터 삽입
# --- mongoDB.insert_one(user)




if __name__ == "__main__":
    app.run()