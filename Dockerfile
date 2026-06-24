# Proximidades do Assaí — imagem de produção
# Build: docker build -t app-assai .
# Railway injeta PORT em tempo de execução.

FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY server.py index.html ./
COPY dados/ ./dados/

EXPOSE 8000
ENV PORT=8000

CMD ["sh", "-c", "python server.py"]
