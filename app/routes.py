from app import app
from flask import request
from flask import jsonify, make_response

from valideer import ValidationError

from .misc import RequestParser, BaseDispatcher, Custom1Dispatcher, Custom2Dispatcher, ResultResponse


@app.route("/")
def index():
    return "Hello mr and welcome"


@app.route("/base", methods=["POST"])
def base():
    try:
        value = RequestParser(request).parse_request()
        result = BaseDispatcher(value).dispatch()
        return ResultResponse(*result).json()
    except ValidationError as e:
        return make_response(jsonify({"message": e.msg}), 502)
    except ValueError as e:
        return make_response(jsonify({"message": e.args[0]}), 400)


@app.route("/custom1", methods=["POST"])
def custom1():
    try:
        value = RequestParser(request).parse_request()
        result = Custom1Dispatcher(value).dispatch()
        return ResultResponse(*result).json()
    except ValidationError as e:
        return make_response(jsonify({"message": e.msg}), 502)
    except ValueError as e:
        return make_response(jsonify({"message": e.args[0]}), 400)


@app.route("/custom2", methods=["POST"])
def custom2():
    try:
        value = RequestParser(request).parse_request()
        result = Custom2Dispatcher(value).dispatch()
        return ResultResponse(*result).json()
    except ValidationError as e:
        return make_response(jsonify({"message": e.msg}), 502)
    except ValueError as e:
        return make_response(jsonify({"message": e.args[0]}), 400)
