# 과제목표
# Flask에서 route를 통한 클라이언트 요청에 대한 응답 작성
# 참고 공식문서 https://flask.palletsprojects.com/en/2.2.x/patterns/viewdecorators/

from flask import Flask, render_template

# template_folder 를 통해서 html 파일을 관리
# template_folder 의 이름을 별도로 지정해주지 않으면 기본 값은 "templates"
app = Flask(__name__, template_folder="taylor_templates")
@app.route('/') # 브라우저에서 http://localhost:5000/ 경로로 들어왔을 때 
def hello_taylor(): # 함수는 아무 이름으로 가능
    return render_template('index.html') # render_template를 통해서 template 폴더에 있는 파일을 브라우저에 던져준다.

# ----------직접 작성 부분---------- #
# 
# @app.route("/me") 를 통해 본인의 이름을 html 파일에서 나타낼 수 있게 코드를 작성해주세요.
#  
# ----------직접 작성 부분---------- #
    

if __name__ == "__main__":
    app.run() # 별도로 port 를 적어주지 않으면 기본 값은 5000