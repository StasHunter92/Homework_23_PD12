from marshmallow import Schema, fields


# ----------------------------------------------------------------------------------------------------------------------
# Create schema
class QuerySchema(Schema):
    """Schema for query"""
    cmd1 = fields.Str()
    value1 = fields.Str()
    cmd2 = fields.Str()
    value2 = fields.Str()
    file_name = fields.Str()


# ----------------------------------------------------------------------------------------------------------------------
# Create schema instance
query_schema = QuerySchema()
