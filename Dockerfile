FROM python:3

WORKDIR /app
ADD . /app

#Install the dependencies
RUN apt-get -y update
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "flask_eg.flask_eg:app"]