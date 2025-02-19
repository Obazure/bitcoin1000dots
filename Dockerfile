FROM python:3.8.5

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./main.py ./main.py
COPY ./src ./src


ENTRYPOINT ["python", "main.py"]
