from flask import jsonify
from .errors import ValidationError


class JsonResponse():

    def apiResponse(self, result, status=200):
        return jsonify({'result': result, 'status': status})

    def throwError(self, message):
        raise ValidationError(
            404,  # Http Status code
            error=message, code=404
        )

    def throwException(self, message):
        raise ValidationError(400, error=message, code=400)