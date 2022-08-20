# using a python small basic image
FROM python:alpine
# exposing our app port in docker internal network
EXPOSE 9090
# creates a dir for our application
WORKDIR /app
# copy our application.
COPY . /app

RUN pip install -r requirements.txt

# run the application
CMD python app.py
