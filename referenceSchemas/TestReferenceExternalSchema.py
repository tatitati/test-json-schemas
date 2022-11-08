from jsonschema import validate

class TestReferenceExternalSchema():
	def test_referenced_schema(self):
		schema = {
			"definitions": {},
			"$schema": "http://json-schema.org/draft-07/schema#",
			"$id": "https://example.com/country.json",
			"title": "Root",
			"type": "object",
			"required": [
				"name",
				"capital"
			],
			"properties": {
				"name": {
					"$id": "#root/name",
					"title": "Name",
					"type": "string",
					"default": "",
					"examples": [
						"Eggs"
					],
					"pattern": "^.*$"
				},
				"capital": {
					"$id": "#root/capital",
					"type": "object",
					"$ref": "file:city.json"
				}
			}
		}

		data = {
			"name" : "Eggs",
			"capital" : {
				"name": "madrid",
				"population": 34.4
			}
		}

		validate(instance=data, schema=schema)