FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["daphne", "djangochat.asgi:application", "-b", "0.0.0.0", "-p", "8000"]