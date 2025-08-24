FROM python:3.11-alpine

WORKDIR /app

COPY src/ /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

RUN crontab utilities/crontab

CMD ["crond", "-f"]