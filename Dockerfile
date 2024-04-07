FROM docker.io/alpine:latest

RUN apk update && \
  apk upgrade --no-cache

RUN apk add --no-cache python3 py3-pip &&\
  python3 -m pip install pyTelegramBotAPI --break-system-packages && \
  mkdir -p /app/data

COPY shopping_list.py /app/shopping_list.py

WORKDIR /app

CMD ["python3", "shopping_list.py"]
