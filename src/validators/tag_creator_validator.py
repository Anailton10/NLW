from cerberus import Validator
from src.errors.error_types.http_unprocessable_entipy import HttpUnprocessableEntityError


def tag_creator_validator(request) -> None:
    body_validator = Validator({
        "product_code": {"type": "string", "requerid": True, "empty": False}
    })

    response = body_validator.validate(request.json)
    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
