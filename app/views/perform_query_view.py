from os import path
from flask import request, abort, current_app
from flask_restx import Namespace, Resource
from marshmallow import ValidationError

from app.classes.query_handler import QueryHandler
from app.schemas.query_schema import query_schema
from app.utils.functions import open_file

# ----------------------------------------------------------------------------------------------------------------------
# Create namespace
perform_query_ns = Namespace('perform_query')


# ----------------------------------------------------------------------------------------------------------------------
# Create route
@perform_query_ns.route('/')
class PerformQueryView(Resource):
    @perform_query_ns.doc(description="Get result",
                          params={"cmd1": "1st command", "value1": "1st value", "cmd2": "2nd command",
                                  "value2": "2nd value", "file_name": "name of file"},
                          responses={200: "OK", 400: "Bad Request"})
    def get(self):
        """
        Get result depending on input query \n
        :return: Text result with status code 200 or 400 if error
        """
        cmd1 = request.args.get("cmd1")
        value1 = request.args.get("value1")
        cmd2 = request.args.get("cmd2")
        value2 = request.args.get("value2")
        filename = request.args.get("file_name")

        if None in (cmd1, cmd2, value1, value2, filename):
            abort(400, "Wrong arguments")

        file_path = path.join(current_app.config.get('DATA_DIR'), filename)

        if not path.exists(file_path):
            abort(400, f"File {file_path} is not found")

        result = open_file(file_path)

        try:
            filter_1 = QueryHandler(cmd=cmd1, value=value1, data=result).build_query()
            filter_2 = QueryHandler(cmd=cmd2, value=value2, data=filter_1).build_query()
            return current_app.response_class('\n'.join(filter_2), content_type="text/plain")
        except (TypeError, ValueError, FileNotFoundError, IndexError) as e:
            abort(400, f"{e}")

    @perform_query_ns.doc(description="Get result",
                          responses={200: "OK", 400: "Bad Request"})
    def post(self):
        """
        Get result depending on input query \n
        :return: Text result with status code 200 or 400 if error
        """
        data = request.json

        try:
            checked_data = query_schema.load(data)
        except ValidationError:
            abort(400, "Wrong schema data")

        file_path = path.join(current_app.config.get('DATA_DIR'), checked_data['file_name'])

        if not path.exists(file_path):
            abort(400, f"File {file_path} is not found")

        result = open_file(file_path)

        try:
            filter_1 = QueryHandler(cmd=checked_data['cmd1'], value=checked_data['value1'], data=result).build_query()
            filter_2 = QueryHandler(cmd=checked_data['cmd2'], value=checked_data['value2'], data=filter_1).build_query()
            return current_app.response_class('\n'.join(filter_2), content_type="text/plain")
        except (TypeError, ValueError, FileNotFoundError, IndexError) as e:
            abort(400, f"{e}")
