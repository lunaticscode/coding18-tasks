# 과제 목표
# localhost:5000 으로 접속하여, [파일 선택] 클릭 후 이미지 선택 -> [제출] 버튼 클릭 -> 제출한 이미지가 나오면 성공
# (* templates/index.html 파일은 그대로 사용해주세요.)
# (* 왜 굳이 Flask 서버 내부가 아닌, DB에 데이터를 저장하는 지에 대해서도 생각해보시면 좋습니다.)

from flask import Flask, render_template, request
from db_init import db
from gridfs import GridFS # install 필요 없음
import base64 # install 필요 없음

app = Flask(__name__)
fs = GridFS(db) # local 컬렉션에 GridFS를 통해 파일을 저장할 수 있는 공간을 만든다.


################## 여기는 건드리지 마세요 ##################
def get_image_file(saved_file_data):
    # binary -> base64 encoding -> utf-8 decoding 
    img_binary_data = fs.get(saved_file_data["_id"]).read()
    img_base64_data = base64.b64encode(img_binary_data)
    result_img_data = img_base64_data.decode('utf-8')
    return result_img_data
################## 여기는 건드리지 마세요 ##################    


@app.route("/upload", methods=["POST"])
def upload_file():
    
    # ------------ 직접 코드 작성 ------------ #
    # 
    # Flask 내장 라이브러리인 GridFS를 통해서 MongoDB에 이미지 파일을 저장해주세요.
    # (* filename 은 'test_image_file1' 으로 꼭 저장해주세요.)
    #
    # ------------ 직접 코드 작성 ------------ #


    ################## 이부분은 건드리지 마세요 ##################
    # DB에 저장된 이미지 데이터를 불러 온다.
    saved_file_data = db.fs.files.find_one({'filename': "test_image_file1"})
    # 불러온 이미지 데이터를 html 파일에서 사용할 수 있게 가공
    result_img_data = get_image_file(saved_file_data)
    return render_template("index.html", img_data = result_img_data)
    ################## 이부분은 건드리지 마세요 ##################
    

@app.route("/")
def show_index_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
