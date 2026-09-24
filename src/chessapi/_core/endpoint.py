from chessapi._core.client import AsyncBaseClient, BaseClient


class BaseEndpoint:
    def __init__(self, client: BaseClient) -> None:
        self._client = client


class AsyncBaseEndpoint:
    def __init__(self, client: AsyncBaseClient) -> None:
        self._client = client
