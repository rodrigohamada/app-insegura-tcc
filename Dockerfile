FROM python:3.7-slim

# ⚠️ Usando imagem antiga propositalmente
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
