FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN chmod +x start.sh

CMD ["sh", "start.sh"]