from pfms.swagger.pfms_swagger_api_spec import FileUpload

from application.composer.composer.data.composer_enum import CardType
from application.composer.composer.model.card import Card
from marshmallow import fields
from pfms.common.enum_processor import EnumField
from pfms.pfapi.base.pfms_base_schema import PfDetailBaseSchema, common_exclude_append, update_exclude_append, \
    PfBaseSchema


class CardDropDownList(PfBaseSchema):

    class Meta:
        model = Card
        load_instance = True

    id = fields.Integer(required=True, error_messages={"required": "Please enter id"})
    name = fields.String(required=True, error_messages={"required": "Please enter name"})


class CardDetailsDto(PfDetailBaseSchema):

    class Meta:
        model = Card
        load_instance = True

    type = EnumField(CardType, required=True, error_messages={"required": "Please Enter Type"})
    name = fields.String(required=True, error_messages={"required": "Please Enter Name"})
    title = fields.String(required=True, error_messages={"required": "Please Enter Title"})
    description = fields.String(allow_none=True)
    target = fields.String(allow_none=True)
    targetType = fields.String(allow_none=True)



class CardCreateDto(CardDetailsDto):
    class Meta:
        model = Card
        load_instance = True
        exclude = common_exclude_append()


class CardUpdateDto(CardDetailsDto):
    class Meta:
        model = Card
        load_instance = True
        exclude = update_exclude_append()

    id = fields.Integer(required=True, error_messages={"required": "Please enter id"})


class CardFileUpload(PfBaseSchema):
    name = FileUpload(required=True, error_messages={"required": "Please upload file."})


class CardFileUploadResponse(PfBaseSchema):
    path = FileUpload(required=True, error_messages={"required": "Please upload file."})

