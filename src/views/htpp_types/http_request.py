from typing import Dict


class HttRequest:
    def __init__(self, header: Dict = {},
                 body: Dict = {},
                 query_params: Dict = {}):
        self.header = header
        self.body = body
        self.query_params = query_params
