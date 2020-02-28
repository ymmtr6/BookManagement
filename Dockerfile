FROM ubuntu

ADD requirements.txt /tmp/requirements.txt
ADD *.py /app/
ADD bookmanagement/build /app/bookmanagement/build

RUN apt-get update \
  && apt-get install -y python3 python3-pip \
  && pip3 install --upgrade pip \
  && pip3 install -r /tmp/requirements.txt

WORKDIR /app
ENV HOME /app
ENV MONGO_URL "localhost"

CMD ["python3", "app.py"]
