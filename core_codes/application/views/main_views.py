from flask import Blueprint, request, jsonify
from ..utils import width_height
bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def assignment():
    return 'chaeyeongyun''s assignment3'


@bp.route('/hello')
def hello_world():
    return 'hello world !'


# GET 은 클라이언트에서 서버로 어떠한 리소스로 부터 정보를 요청하기 위해 사용되는 메서드이다. 
# 예를들면 게시판의 게시물을 조회할 때 쓸 수 있다.'
# curl -X GET http://127.0.0.1:5000/echo
@bp.route('/echo', methods=["GET"])
def echo():
    if request.method == "GET":
        data = {"parameter": "value"}
    return jsonify(data)


# curl -F "file=@/Users/yunchaeyeong/Desktop/mlops/image/cat.jpeg" -X POST http://127.0.0.1:5000/upload_image
@bp.route('/upload_image', methods=["POST"])
def upload_image():
    if request.method == "POST":
        f = request.files['file']
        return jsonify(width_height(f))
