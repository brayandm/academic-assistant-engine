from apiflask import Schema

from apiflask.fields import String
from apiflask.validators import Length


class TextToTranslate(Schema):
    original_language = String(required=True, validate=Length(0, 256))
    target_language = String(required=True, validate=Length(0, 256))
    text_type = String(required=True, validate=Length(0, 256))
    text = String(required=True, validate=Length(0, 5000))
    hook = String(required=False, validate=Length(0, 256))
