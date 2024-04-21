from fastapi import FastAPI
import requests
from models import AbhaNumber

app = FastAPI(title="health information user")


class ABDM_HIU_AUTH:
    """
    Responsible for Authentication for the ABDM HIU API. Can authenticate ABDM as HIU.


    """

    def __init__(
        self,
        clientId: str,
        clientSecret: str,
    ):
        """
        :param clientId:
            API key used for identifying the application the user is authenticating with.
        :param client_secret:
             API secret used for making Auth requests.

        """
        self._clientId = clientId
        self._clientSecret = clientSecret

    @property
    def closed(self) -> bool:
        """True iff the auth object has been closed.

        When in the closed state, it can no longer request new tokens.
        """
        return self._closed
