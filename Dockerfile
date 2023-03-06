FROM python:3.10.8-alpine3.17

RUN mkdir /opt/project
WORKDIR /opt/project
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt
#CMD ["/bin/sh"]
EXPOSE 8000