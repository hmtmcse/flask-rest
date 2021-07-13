from application.composer.composer.controller.card_controller import card_controller
from application.composer.composer.model.card import database as card_model


class ComposerRegistry:

    def register_model(self, flask_app):
        card_model.drop_all()
        card_model.create_all()

    def register_controller(self, flask_app):
        flask_app.register_blueprint(card_controller)



composer_registry = ComposerRegistry()
