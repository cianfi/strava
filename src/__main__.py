import os

from dotenv import load_dotenv

from strava.strava import Strava
from llm.llm import LLM
from communication.webex import Webex
from logging import getLogger

logger = getLogger(__name__)
load_dotenv()

def main():
    strava = Strava(
        auth_token = str(os.getenv("auth_token")),
        client_id = str(os.getenv("client_id")),
        client_secret = str(os.getenv("client_secret")),  
        refresh_token = str(os.getenv("refresh_token")),
        access_token = str(os.getenv("access_token")),
        expires_at= str(os.getenv("expires_at"))
    )

    run_ids = strava.get_run_id_from_activities()
    
    parsed_detailed_runs: list[dict] = []
    for id in run_ids:
        detailed_run_data = strava.get_detailed_run(id)

        lap_data: list[dict] = []
        for data in detailed_run_data.laps:
            lap_data.append({
                "name": data["name"],
                "elapsed_time": data["elapsed_time"],
                "distance": data["distance"],
            })
        parsed_detailed_runs.append({
            "name": detailed_run_data.name,
            "distance": detailed_run_data.distance,
            "moving_time": detailed_run_data.moving_time,
            "elapsed_time": detailed_run_data.elapsed_time,
            "calories burnt": detailed_run_data.calories,
            "average_cadence": detailed_run_data.average_cadence,
            "temperature": detailed_run_data.average_temp,
            "average_watts": detailed_run_data.average_watts,
            "laps": lap_data,
        }) 
    logger.debug(f"Here is the parsed detailed run:\n{parsed_detailed_runs}")

    llm = LLM(
        api_key=os.getenv("gemini_api_key"),
        )
    
    for run in parsed_detailed_runs:

        ai_insights = llm.generate_content(running_data=run)

        webex = Webex(
            api_key=str(os.getenv("webex_api_key")),
            )

        email_str = os.getenv("webex_email")
        emails: list[str] = [email.strip() for email in email_str.split(',') if email.strip()]

        for webex_email in emails:
            webex.message_user(email=webex_email, message=ai_insights.response)


if __name__ == "__main__":
    main()