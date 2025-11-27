FROM python:3.10.19
WORKDIR /app/project
COPY . .
USER appmanager
RUN pip3 install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python3", "main.py"]
