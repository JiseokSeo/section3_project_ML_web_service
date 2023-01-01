import flask
from flask import Flask, request, render_template
import joblib
import fasttext
import numpy as np
from scipy import misc

app = Flask(__name__)


# 메인 페이지 라우팅
@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html')


# 데이터 예측 처리
@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method == 'POST':

        # input 받아오기
        file = request.form['str1']
        if not file: return render_template('index.html', label="입력 대기")

        # 예측 수행
        label = model.predict(file)

        # 결과 리턴
        return render_template('index.html', label=label)


if __name__ == '__main__':
    # 모델 로드
    # ml/model.py 선 실행 후 생성
    model = fasttext.load_model('./model/model.bin')
    # Flask 서비스 스타트
    app.run(host='0.0.0.0', port=8000, debug=True)
