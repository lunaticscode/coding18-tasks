# 과제 목표
# Flask에서 return 하는 데이터를 통해 html에서 Template 문법을 적용.
# 참고 공식문서 https://flask.palletsprojects.com/en/2.2.x/templating/

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello_taylor():
    # render_template을 통해 보여줄 html 파일과, 해당 파일에서 쓸 파이썬 변수 'user_name'을 선언.
    return render_template('index.html', user_name="Taylor")

# 1)
# ---------- 직접 작성 부분---------- #
# 
# @app.route("/me") 를 통해 본인의 이름을 html에 출력할 수 있는 코드를 작성해주세요.
#  
# ----------직접 작성 부분---------- #    


# 2)
# ---------- 직접 작성 부분---------- #
#
# user_list = ["Jason", "Timber", "Lucas"]
# @app.route("/users") 를 통해 위 user_list에 있는 이름들을 html에 출력할 수 있는 코드를 작성해주세요.
# (단, html 파일에서 파이썬의 for 문법을 적용해야 함.)
#
# ----------직접 작성 부분---------- #    
    
if __name__ == "__main__":
    app.run() # 별도로 port 를 적어주지 않으면 기본 값은 5000