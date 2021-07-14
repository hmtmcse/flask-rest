import os
from pf_file_dir.pf_fd_util import delete
from pfms.pfapi.rr.pfms_request_respons import PfRequestResponse
from werkzeug.utils import secure_filename
from application.composer.composer.dto.card_dto import CardCreateDto, CardUpdateDto, CardDetailsDto, CardDropDownList, \
    CardFileUpload, CardFileUploadResponse
from application.composer.composer.model.card import Card
from pf_sqlalchemy.crud.pfs_rest_helper_service import PfsRestHelperService
from sqlalchemy import and_
from application.config.path_manager import upload_path_concat

pfs_rest_helper_service = PfsRestHelperService(Card)


def clean_upload():
    path = upload_path_concat("card")
    if os.path.exists(path):
        delete(path)


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

    def concat(self, first, second):
        return os.path.join(str(first), str(second))

    def create_path(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def remove_file_if_exist(self, path):
        if os.path.exists(path):
            os.remove(path)

    def get_path(self):
        return upload_path_concat("card")

    def upload_file(self):
        schema = CardFileUpload()
        data = self.upload_request_preocess(schema)
        names = self.request().get_file_inputs(schema)
        files = self.request().file_data()
        self.create_path(self.get_path())
        if 'name' in names:
            name = names[0]
            file = files[name]
            filename = secure_filename(file.filename)
            file_upload_path = self.concat(self.get_path(), filename)
            self.remove_file_if_exist(file_upload_path)
            file.save(file_upload_path)
            response = CardFileUploadResponse()
            response.path = "/static/uploads/card/" + filename
            return self.response().data_response(response)
        return self.response().error_response("Unable to upload file")
