from application.composer.composer.dto.card_dto import CardCreateDto, CardDetailsDto, CardUpdateDto, CardDropDownList
from application.composer.composer.service.card_service import CardService
from flask import Blueprint
from pfms.swagger.pfms_swagger_decorator import pfms_create, pfms_details, pfms_pagination_sort_search_list, \
    pfms_restore, pfms_delete, request_response_list

card_controller = Blueprint("card_controller", __name__, url_prefix="/api/v1/card")
card_service = CardService()


@card_controller.route("/create", methods=['POST'])
@pfms_create(request_body=CardCreateDto)
def create():
    return card_service.create()


@card_controller.route("/details/<int:id>", methods=['GET'])
@pfms_details(response_obj=CardDetailsDto)
def details(id: int):
    return card_service.details(id)


@card_controller.route("/update", methods=['POST'])
@pfms_create(request_body=CardUpdateDto)
def update():
    return card_service.update()


@card_controller.route("/delete/<int:id>", methods=['DELETE'])
@pfms_delete()
def delete(id: int):
    return card_service.delete(id)


@card_controller.route("/restore/<int:id>", methods=['GET'])
@pfms_restore()
def restore(id: int):
    return card_service.restore(id)


@card_controller.route("/list", methods=['GET'])
@pfms_pagination_sort_search_list(response_obj=CardDetailsDto)
def list():
    return card_service.list()


@card_controller.route("/drop-down-list", methods=['GET'])
@request_response_list(response_obj=CardDropDownList)
def drop_down_list():
    return card_service.drop_down_list()
