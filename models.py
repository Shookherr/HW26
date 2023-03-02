from marshmallow import Schema, fields, validates_schema, ValidationError
from typing import Dict, Any

VALID_CMD_COMMANDS = ('filter', 'unique', 'map', 'limit', 'sort', 'regex')


class RequestSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def check_all_cmd_valid(self, values: Dict[str, str], *args: Any, **kwargs: Any) -> None:
        if values['cmd'] not in VALID_CMD_COMMANDS:
            raise ValidationError(f'\'{values["cmd"]}\' is invalid command for \'cmd\' key')


class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many=True)
    file_name = fields.Str(requiered=True)
