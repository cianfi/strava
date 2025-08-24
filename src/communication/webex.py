import os
import requests

from utilities.log import get_logger

from communication.model import (
    webex_message_user, 
    webex_list_rooms,
    webex_list_people,
    )


logger = get_logger(__name__)


class Webex:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def _request(self, method, uri, **kwargs) -> requests.Response:
        return requests.request(
            method=method,
            url=f"https://webexapis.com{uri}",
            **kwargs
        )

    def message_user(self, email: str, message: str) -> webex_message_user:
        response = self._request(
            method="POST",
            uri="/v1/messages",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
                "Accept": "application/json"
            },
            json={
                "toPersonEmail": f"{email}",
                "text": f"{message}",
            },
        )
        if response.status_code == requests.codes.ok:
            logger.info(f"[{response.status_code}] Message has been successfully sent.")
            return webex_message_user.from_dict(response.json())
        else:
            msg: str = f"[{response.status_code}] {response.json()}"
            logger.error(msg)
            raise Exception(msg)

    def list_rooms(self) -> webex_list_rooms:
        response = self._request(
            method="GET",
            uri="/v1/rooms",
            headers={
                "Authorization": f"Bearer {self.api_key}"
            }
        )
        if response.status_code == requests.codes.ok:
            logger.info(f"[{response.status_code}] Message has been successfully sent.")
            return webex_list_rooms.from_dict(response.json())
        else:
            msg: str = f"[{response.status_code}] {response.json()}"
            logger.error(msg)
            raise Exception(msg)

    def list_people(self, email: str) -> webex_list_people:
        response = self._request(
            method="GET",
            uri="/v1/people",
            headers={
                "Authorization": f"Bearer {self.api_key}"
            },
            params={
                "email": f"{email}"
            }
        )
        if response.status_code == requests.codes.ok:
            logger.info(f"[{response.status_code}] Message has been successfully sent.")
            return webex_list_people.from_dict(response.json())
        else:
            msg: str = f"[{response.status_code}] {response.json()}"
            logger.error(msg)
            raise Exception(msg)
