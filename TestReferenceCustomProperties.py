from jsonschema import validate

class TestReferenceCustomProperties():

	def test_referenced_custom_properties(self):
		schema = {
			"definitions": {},
			"$schema": "http://json-schema.org/draft-07/schema#",
			"$id": "https://example.com/345345345.json",
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
					"$ref": "#/$defs/city"
				}
			},
			"$defs": {
				"city": {
					"type": "object",
					"properties": {
						"name": {
							"$id": "#root/capital/name",
							"title": "Name",
							"type": "string",
							"default": "",
							"examples": [
								"Eggs"
							],
							"pattern": "^.*$"
						},
						"population": {
							"$id": "#root/capital/population",
							"title": "population",
							"type": "number",
							"examples": [
								34.99
							],
							"default": 0.0
						}
					}
				}
			  }
		}

		data = {
			"name" : "Eggs",
			"capital" : {
				"name": "madrid",
				"population": 34
			}
		}

		validate(instance=data, schema=schema)