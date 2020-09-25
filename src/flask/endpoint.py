import json
from flask import request
from flask_restx import Api, Resource
from src.resources.business_sector_api import set_business_sector
from src.resources.validator import Validator
from itertools import groupby

api = Api(
    version="1.0",
    title="Talkdesk Challenge",
    description="Phone information aggregator API"
)


@api.route("/aggregate")
class Aggregator(Resource):

    def aggregate(self, phone_info: list):
        list_in_tuples = []
        response = {}
        body = []

        for i in phone_info:
            list_in_tuples.append((i.get_prefix(), i.get_sector()))
        # sort by prefix
        data = sorted(list_in_tuples, key=lambda x: x[0])
        # group by prefix
        for key, group in (groupby(data, key=lambda x: x[0])):
            response.update({key: None})
            # group by sector
            for k, g in (groupby(list(group), key=lambda x: x[1])):
                body.append("{" + k + ": " + str(len(list(g))) + "},")
            response[key] = ''.join(body)
            body.clear()
        return json.dumps(response)

    def post(self):
        """Aggregates phone numbers according to the respective business sector"""
        # array received from the post request's body
        numbers = request.json
        if not numbers:
            raise Exception("No numbers were passed")
        else:
            validator = Validator(numbers)
            all_phone_info = validator.validated_numbers()
            for phone_info in all_phone_info:
                set_business_sector(phone_info)
        return self.aggregate(all_phone_info)