from marshmallow import Schema, fields, validate


class TextTranslated(Schema):
    text = fields.String(required=True, validate=validate.Length(0, 10000))


class AiModel(Schema):
    name = fields.String(required=True, validate=validate.Length(0, 256))
    option = fields.String(required=True, validate=validate.Length(0, 256))
    usage_type = fields.String(required=True, validate=validate.Length(0, 256))
    usage = fields.Integer(required=True)


class TranslationResult(Schema):
    task_id = fields.String(required=True, validate=validate.Length(0, 256))
    task_name = fields.String(required=True, validate=validate.Length(0, 256))
    status = fields.String(required=True, validate=validate.Length(0, 256))
    result = fields.Nested(TextTranslated, required=True)
    ai_models = fields.List(fields.Nested(AiModel), required=True)
