import os

from dotenv import load_dotenv

from strava.strava import Strava

def main():
    load_dotenv()

    strava = Strava(
        auth_token = str(os.getenv("auth_token")),
        client_id = str(os.getenv("client_id")),
        client_secret = str(os.getenv("client_secret")),  
        refresh_token = str(os.getenv("refresh_token")),
        access_token = str(os.getenv("access_token")),
        expires_in= str(os.getenv("expires_in"))
    )

if __name__ == "__main__":
    main()