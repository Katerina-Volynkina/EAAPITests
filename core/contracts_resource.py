RESOURCE_DATA_SCHEMA = {
    "type" : "object",
    "properties": {
        "id" : {"type": "number"},
        "name" : {"type": "string"},
        "year" : {"type": "integer"},
        "color" : {"type": "string"},
        "pantone_value" : {"type": "string"}
    },
    "required": ["id", "name", "year", "color", "pantone_value"],
}

