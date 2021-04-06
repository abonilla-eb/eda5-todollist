FROM python:3.8-slim

WORKDIR /todolist
COPY . /todolist

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python", "manage.py", "runserver" ]
