FROM python:3.12.12-slim
WORKDIR /app/project
COPY . .
USER appmanager
RUN pip3 install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python3", "main.py"]