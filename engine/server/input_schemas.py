from apiflask import Schema

from apiflask.fields import String
from apiflask.validators import Length


class TextToTranslate(Schema):
    originalLanguage = String(required=True, validate=Length(0, 256))
    targetLanguage = String(required=True, validate=Length(0, 256))
    textType = String(required=True, validate=Length(0, 256))
    text = String(required=True, validate=Length(0, 5000))
    hook = String(required=False, validate=Length(0, 256))
