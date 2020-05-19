from flask import jsonify
from flask_restful import Api
from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import HTTPException


class ExtendedAPI(Api):
    """This class overrides 'handle_error' method of 'Api' class ,
    to extend global exception handing functionality of 'flask-restful'.
    """

    def handle_error(self, err):
        """It helps preventing writing unnecessary
        try/except block though out the application
        """
        print(err)

        # Handle HTTPExceptions
        if isinstance(err, HTTPException):
            return jsonify({
                'message': getattr(
                    err, 'description', HTTP_STATUS_CODES.get(err.code, '')
                )
            }), err.code
        # If msg attribute is not set,
        # consider it as Python core exception and
        # hide sensitive error info from end user
        #if not getattr(err, 'message', None):
        #    return jsonify({
        #        'message': 'has encountered some error'
        #    }), err.code
        # Handle application specific custom exceptions
        return jsonify(**err.kwargs), err.http_status_code
