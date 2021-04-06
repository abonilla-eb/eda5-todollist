FROM python:3.8-slim

WORKDIR /todolist

COPY requirements.txt /todolist
RUN pip install -r requirements.txt

COPY . /todolist

EXPOSE 8000

ENTRYPOINT [ "python", "manage.py", "runserver" ]
