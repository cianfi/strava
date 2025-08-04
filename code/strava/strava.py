import requests
import os
import datetime

from strava.model import (
    Authorization, 
    Refresh, 
    GetAthlete, 
    AthleteActivities, 
    AthleteActivity, 
    DetailedRun
    )

from log import get_logger

from dotenv import set_key

logger = get_logger(__name__)

class Strava:
    def __init__(self, auth_token, client_id, client_secret, refresh_token, access_token, expires_at) -> None:
        self.access_token = access_token
        self.auth_token = auth_token
        self.client_id = client_id
        self.client_secret = client_secret  
        self.refresh_token = refresh_token
        self.expires_at = expires_at
        self.base_url = "https://www.strava.com"
        self._validate_access_token()

    def _request(self, method: str, uri: str, **kwargs) -> requests.Response:
        return requests.request(
            method=f"{method}",
            url=f"{self.base_url}{uri}",
            **kwargs
        )
    
    def _validate_access_token(self) -> None:
        if self.expires_at is None:
            logger.warning("Refreshing access token because no expiration date has been set.")
            self.refresh()
            
        elif datetime.datetime.now().timestamp() > int(self.expires_at):
            logger.warning("Refreshing access token because access token has expired.")
            self.refresh()
        else: 
            logger.info("Access token is valid.")
    
    def authentication(self) -> None: 
        response = self._request(
            method="POST", 
            uri="/oauth/token",
            params={
                "client_id": f"{self.client_id}",
                "client_secret": f"{self.client_secret}",
                "code": "dbbacd83a7b10c2bb6999123d42bbfea5c22c257",
                "grant_type": "authorization_code"
            }
        )

        if response.status_code == requests.codes.ok: 
            response_object = Authorization.from_dict(response.json())
            set_key(".env", "access_token", response_object.access_token)
            self.access_token = response_object.access_token
            logger.info("Authentication to Strava was successful. Access token has been set.")
        else:
            logger.error(f"Authentication Failed. [{response.status_code}] {response.json()}")
            raise Exception(f"Authentication Failed: [{response.status_code}] {response.json()}")

    def refresh(self) -> None: 
        response = self._request(
            method="POST",
            uri="/oauth/token",
            data={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token
            }
        )
        if response.status_code == requests.codes.ok:
            response_object = Refresh.from_dict(response.json())
            set_key(".env", "access_token", response_object.access_token)
            set_key(".env", "expires_at", str(response_object.expires_at))
            self.access_token = response_object.access_token
            self.expires_at = response_object.expires_at
            logger.info("Refresh was successful.")
        else:
            logger.error(f"Refresh Failed. [{response.status_code}] {response.json()}")
            raise Exception(f"Refresh Failed: [{response.status_code}] {response.json()}")

    def get_athlete(self) -> GetAthlete: 
        response = self._request(
            method="GET",
            uri="/api/v3/athlete",
            headers={
                "Authorization": f"Bearer {self.access_token}"
            }
        )
        if response.status_code == requests.codes.ok:
            logger.info("Successfully retrieved 'Get Athlete' data.")
            return GetAthlete.from_dict(response.json())
        else:
            msg = f"Unsuccessfully retrieved 'Get Athlete' data.\n[{response.status_code}] {response.json()}"
            logger.error(msg)
            raise Exception(msg)

    def get_athlete_activities(self) -> AthleteActivities:
        response = self._request(
            method="GET",
            uri="/api/v3/athlete/activities",
            params={
                "access_token": f"{self.access_token}",
                "after": f"{datetime.datetime.now(datetime.timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0).timestamp()}"
            }
        )
        if response.status_code == requests.codes.ok:
            logger.info("Successfully retrieved 'Get Athlete Activity' data.")
            return AthleteActivities.from_dict(response.json())
        else:
            msg = f"Unsuccessfully retrieved 'Get Athlete Activity' data.\n[{response.status_code}] {response.json()}"
            logger.error(msg)
            raise Exception(msg)
        
    def get_run_id_from_activities(self) -> list[str]:
        athlete_activities: AthleteActivities = self.get_athlete_activities()
        run_data = AthleteActivities.get_activities_by_type(athlete_activities=athlete_activities, activity_type="Run")
        run_id:list = []

        for run in run_data.activities:
            run_id.append(run.id)

        return run_id

    def get_detailed_run(self, id: str) -> DetailedRun:
        response = self._request(
            method="GET",
            uri=f"/api/v3/activities/{id}",
            params={
                "access_token": f"{self.access_token}",
                "include_all_efforts": "True"
            }
        )
        if response.status_code == requests.codes.ok:
            logger.info("Successfully retrieved 'Get Athlete' data.")
            return DetailedRun.from_dict(response.json())
        else:
            msg = f"Unsuccessfully retrieved 'Get Athlete' data.\n[{response.status_code}] {response.json()}"
            logger.error(msg)
            raise Exception(msg)