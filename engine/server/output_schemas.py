from marshmallow import Schema, fields, validate


class TextTranslated(Schema):
    text = fields.String(required=True, validate=validate.Length(0, 10000))


class TranslationResult(Schema):
    taskId = fields.String(required=True, validate=validate.Length(0, 256))
    result = fields.Nested(TextTranslated, required=True)