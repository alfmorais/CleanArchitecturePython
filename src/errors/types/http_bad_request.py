class HttpBadRequestError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        self.name = "BadRequest"
        self.status_code = 400
        super().__init__()
