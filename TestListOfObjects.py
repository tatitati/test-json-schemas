from jsonschema import validate

class TestListOfObjects():
	def test_can_validate_a_json_schema_with_list_of_elements(self):

		schema = {
			"definitions": {},
			"$schema": "http://json-schema.org/draft-07/schema#",
			"$id": "https://example.com/object1667838351.json",
			"title": "Root",
			"type": "object",
			"required": [
				"name",
				"prefered_cities"
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
				"prefered_cities": {
					"$id": "#root/prefered_cities",
					"title": "Prefered_cities",
					"type": "array",
					"default": [],
					"items":{
						"$id": "#root/prefered_cities/items",
						"title": "Items",
						"type": "object",
						"required": [
							"city"
						],
						"properties": {
							"city": {
								"$id": "#root/prefered_cities/items/city",
								"title": "City",
								"type": "string",
								"default": "",
								"examples": [
									"madrid"
								],
								"pattern": "^.*$"
							}
						}
					}

				}
			}
		}

		data = {
			"name" : "Eggs",
			"prefered_cities" : [
				{"city":"madrid"},
				{"city":"valencia"}
			]
		}

		validate(instance=data, schema=schema)

