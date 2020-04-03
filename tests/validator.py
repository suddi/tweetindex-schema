import json
import unittest

from jsonschema import validate

SCHEMAS = {
    'schema_directory': './schema/tweets',
    'fixture_directory': './tests/fixtures/tweets'
}

def load_json(filename):
    with open(filename) as data:
        json_data = json.load(data)
    return json_data

def validate_schema(payloads, schema):
    for payload in payloads:
        validate(payload, schema)

class SchemaTest(unittest.TestCase):
    request = {}
    response = {}
    fixture_request = []
    fixture_response = []

    def setUp(self):
        self.request = load_json(SCHEMAS['schema_directory'] + '/request.json')
        self.response = load_json(SCHEMAS['schema_directory'] + '/response.json')
        self.fixture_request = load_json(SCHEMAS['fixture_directory'] + '/request.json')
        self.fixture_response = load_json(SCHEMAS['fixture_directory'] + '/response.json')

    def test_request_schema(self):
        return validate_schema(self.fixture_request, self.request)

    def test_response_schema(self):
        return validate_schema(self.fixture_response, self.response)

if __name__ == '__main__':
    unittest.main()
