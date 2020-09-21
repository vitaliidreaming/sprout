from flask import jsonify, make_response
import valideer


class RequestValue:
    def __init__(self, a: bool, b: bool, c: bool, d: float, e: int, f: int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    @classmethod
    def parse(cls, value):
        return cls(**valideer.parse({
            "+a": valideer.Boolean,
            "+b": valideer.Boolean,
            "+c": valideer.Boolean,
            "+d": valideer.AdaptTo(float),
            "+e": valideer.AdaptTo(int),
            "+f": valideer.AdaptTo(int),
        }).validate(value))

    def __repr__(self):
        return f"<Value {self.a} {self.b} {self.c} :: {self.d} {self.e} {self.f}>"


class RequestParser:
    def __init__(self, request):
        """
        Parse request to required form
        :type request: werkzeug.wrappers.request.Request
        """
        self.request = request

    def parse_request(self):
        if self.request.is_json:
            req = self.request.get_json()
            value = RequestValue.parse(req)
            return value


class BaseDispatcher:
    def __init__(self, value: RequestValue):
        self.value = value

    def dispatch(self):
        v = self.value
        if v.a and v.b and not v.c:
            return "M", self.res_m()
        if v.a and v.b and v.c:
            return "P", self.res_p()
        if not v.a and v.b and v.c:
            return "T", self.res_t()
        raise ValueError("Unacceptable input")

    def res_m(self):
        v = self.value
        return v.d + (v.d * v.e / 10)

    def res_p(self):
        v = self.value
        return v.d + (v.d * (v.e - v.f) / 25.5)

    def res_t(self):
        v = self.value
        return v.d - (v.d * v.f / 30)


class Custom1Dispatcher(BaseDispatcher):

    def res_p(self):
        v = self.value
        return 2 * v.d + (v.d * v.e / 100)


class Custom2Dispatcher(BaseDispatcher):
    def dispatch(self):
        v = self.value
        if v.a and v.b and not v.c:
            return "T", self.res_t()
        if v.a and v.b and v.c:
            return "P", self.res_p()
        if not v.a and v.b and v.c:
            return "T", self.res_t()
        if v.a and not v.b and v.c:
            return "M", self.res_m()
        raise ValueError("Unacceptable input")

    def res_m(self):
        v = self.value
        return v.f + v.d + (v.d * v.e / 100)


class ResultResponse:
    def __init__(self, variant: str, result: float):
        self.variant = variant
        self.result = result

    def json(self):
        return make_response(jsonify({
            "variant": self.variant,
            "result":  self.result
        }), 200)
