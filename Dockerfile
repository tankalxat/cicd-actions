FROM python:3.10.19
WORKDIR /app/project
COPY . .
RUN useradd -m appmanager && \
  pip3 install -r requirements.txt
USER appmanager
EXPOSE 8080
ENTRYPOINT ["python3", "main.py"]