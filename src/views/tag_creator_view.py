from src.views.htpp_types.http_request import HttRequest
from src.views.htpp_types.htpp_response import HttpResponse


class TagCreatorView:
    '''
        responsability for interacting with HTTP
    '''

    def validade_and_create(self, http_request: HttRequest) -> HttpResponse:
        boby = http_request.body
        product_code = boby["product_code"]

        # Logica de regra de negocio
        print("Na minha view")
        # retorno htpp
        return HttpResponse(status_code=200, body={"hello": "word"})
