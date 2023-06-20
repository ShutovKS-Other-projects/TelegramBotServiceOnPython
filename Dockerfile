FROM python:3.10

RUN mkdir -p /app/
WORKDIR /app/

COPY . /app/
RUN pip install -r requirements.txt

WORKDIR /app/bot/
ENV PYTHONPATH "${PYTHONPATH}:/app/"

CMD ["python", "__main__.py"]
