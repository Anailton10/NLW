from src.views.htpp_types.http_request import HttRequest
from src.views.htpp_types.htpp_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController


class TagCreatorView:
    '''
        responsability for interacting with HTTP
    '''

    def validade_and_create(self, http_request: HttRequest) -> HttpResponse:
        tag_creator_controller = TagCreatorController()
        boby = http_request.body
        product_code = boby["product_code"]

        # Logica de regra de negocio
        formatted_response = tag_creator_controller.create(product_code)
        # retorno htpp
        return HttpResponse(status_code=200, body=formatted_response)
