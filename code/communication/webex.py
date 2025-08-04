import os
import requests

from log import get_logger

logger = get_logger(__name__)


class Webex:
    def __init__(self, api_key: str, email: str, message: str):
        self.api_key = api_key
        self.email = email
        self.message = message

    def _request(self, method, uri, **kwargs) -> requests.Response:
        return requests.request(
            method=method,
            url=f"https://webexapis.com{uri}",
            **kwargs
        )

    def message_user(self):
        response = self._request(
            method="POST",
            uri="/v1/messages",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
                "Accept": "application/json"
            },
            json={
                "toPersonEmail": f"{self.email}",
                "text": f"{self.message}",
            },
        )
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            msg: str = f"[{response.status_code}] {response.json()}"
            logger.error(msg)
            raise Exception(msg)

    def list_rooms(self):
        response = self._request(
            method="GET",
            uri="/v1/rooms",
            headers={
                "Authorization": f"Bearer {self.api_key}"
            }
        )
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            msg: str = f"[{response.status_code}] {response.json()}"
            logger.error(msg)
            raise Exception(msg)

    def list_people(self):
        response = self._request(
            method="GET",
            uri="/v1/people",
            headers={
                "Authorization": f"Bearer {self.api_key}"
            },
            params={
                "email": f"{self.email}"
            }
        )
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            msg: str = f"[{response.status_code}] {response.json()}"
            logger.error(msg)
            raise Exception(msg)
