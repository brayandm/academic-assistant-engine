from apiflask import Schema

from apiflask.fields import String
from apiflask.validators import Length


class TextTranslated(Schema):
    taskId = String(required=True, validate=Length(0, 256))
    text = String(required=True, validate=Length(0, 10000))
