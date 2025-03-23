FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PORT=5000

EXPOSE 5000

ENTRYPOINT ["gunicorn", "--workers=2", "main:app"]
