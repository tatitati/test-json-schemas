from jsonschema import validate

class TestValidateBasicSchemas():
	def test_can_validate_a_json_schema(self):

		schema = {
			"type" : "object",
			"properties" : {
				"price" : {"type" : "number"},
				"name" : {"type" : "string"},
			},
		}

		validate(instance={"name" : "Eggs", "price" : 34.99}, schema=schema)

	def test_whole_schema_definition(self):
		schema={
			"definitions": {},
			"$schema": "http://json-schema.org/draft-07/schema#",
			"$id": "https://example.com/object1667838199.json",
			"title": "Root",
			"type": "object",
			"required": [
				"name",
				"price"
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
				"price": {
					"$id": "#root/price",
					"title": "Price",
					"type": "number",
					"examples": [
						34.99
					],
					"default": 0.0
				}
			}
		}

		validate(instance={"name" : "Eggs", "price" : 34.99}, schema=schema)


