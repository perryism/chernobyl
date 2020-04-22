from flask import request

class Params:
    def __getattr__(self, key):
        if key == "json":
            return request.get_json()

    def __getitem__(self, key):
        value = request.args.get(key)

        if value is None:
            value = request.form.get(key)

        return value
