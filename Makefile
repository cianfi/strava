docker_build:
	docker build -t strava .

docker_run:
	docker run --name ai_summary_run --env-file .env strava 

