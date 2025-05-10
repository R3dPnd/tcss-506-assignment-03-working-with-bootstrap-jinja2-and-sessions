FROM python:3.10-slim-bookworm
RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 4000
CMD ["python", "app.py"]
