FROM docker.io/alpine:latest

RUN apk update && \
    apk upgrade

RUN apk add python3 &&\
    python3 -m ensurepip --break-system-packages && \
    python3 -m pip install pyTelegramBotAPI --break-system-packages && \
    mkdir -p /app/data

COPY shopping_list.py /app/shopping_list.py

WORKDIR /app

CMD ["python3", "shopping_list.py"]
