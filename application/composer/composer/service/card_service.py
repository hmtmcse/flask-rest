from pfms.pfapi.rr.pfms_request_respons import PfRequestResponse
from pfms.pfapi.rr.pfms_response_processor import PfResponseProcessor

from application.composer.composer.dto.card_dto import CardCreateDto, CardUpdateDto, CardDetailsDto, CardDropDownList
from application.composer.composer.model.card import Card
from pf_sqlalchemy.crud.pfs_rest_helper_service import PfsRestHelperService
from sqlalchemy import and_

pfs_rest_helper_service = PfsRestHelperService(Card)


class CardService(PfRequestResponse):

    def create(self):
        return pfs_rest_helper_service.rest_create(CardCreateDto())

    def update(self):
        return pfs_rest_helper_service.rest_update(CardUpdateDto())

    def details(self, model_id: int):
        return pfs_rest_helper_service.rest_details(model_id, CardDetailsDto())

    def delete(self, model_id: int):
        return pfs_rest_helper_service.rest_delete(model_id)

    def restore(self, model_id: int):
        return pfs_rest_helper_service.rest_restore(model_id)

    def list(self):
        search = ["name"]
        return pfs_rest_helper_service.rest_list(CardDetailsDto(), search=search)

    def drop_down_list(self):
        query = Card.query.with_entities(Card.name, Card.id)
        return pfs_rest_helper_service.rest_list(CardDropDownList(), model=query, pagination=False)

    def list_card_by_ids(self, ids):
        return Card.query.filter(and_(Card.id.in_(ids), Card.isDeleted == False)).all()

    def form_data(self):
        data = self.request().form_data()
        return self.response().data_response(data)
