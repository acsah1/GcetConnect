FROM python:latest
WORKDIR /app
COPY . . 
RUN ls -lrt /app
RUN pip install -r /app/requirements.txt
CMD [ "python","app.py" ]