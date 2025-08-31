# 🚨 Aplicação Insegura para TCC 🚨

Este repositório contém uma aplicação propositalmente **insegura** para demonstrar
a importância do uso do **Scanner Universal de Segurança** no TCC.

## Erros Intencionais
- Uso de **`eval()`** inseguro
- **SQL Injection** via f-strings
- Uso de **`subprocess(shell=True)`**
- **Segredos hardcoded** (API Key, AWS Key, DB Password)
- Dependências vulneráveis (`Flask==1.0`, `requests==2.19.0`, `PyYAML==5.1`)
- **`yaml.load()`** inseguro
- Execução de Flask com **debug=True**
- Uso de **Dockerfile** com imagem antiga (Python 3.7)

## Como rodar
```bash
pip install -r requirements.txt
python app.py
