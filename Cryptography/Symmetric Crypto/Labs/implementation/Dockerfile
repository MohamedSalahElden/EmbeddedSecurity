FROM python:3.9-slim

WORKDIR /app
COPY server.py .
COPY symmetric_crypto_labs ./symmetric_crypto_labs
RUN pip install pycryptodome
RUN pip install flask

CMD ["python", "server.py"]
