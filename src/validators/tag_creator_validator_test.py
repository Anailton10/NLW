from src.errors.error_types.http_unprocessable_entipy import HttpUnprocessableEntityError
from .tag_creator_validator import tag_creator_validator


class MockRequest:
    def __init__(self, json) -> None:
        self.json = json


def test_tag_creator_validator():
    request = MockRequest(json={"product_code": "12345"})
    response = tag_creator_validator(request=request)

    assert response == 3
    ...


def test_tag_creator_validator_with_error():
    request = MockRequest(json={"product_code": 12345})

    try:
        tag_creator_validator(request=request)
        assert False
    except Exception as exeption:
        assert isinstance(exeption, HttpUnprocessableEntityError)
