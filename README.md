# 🚨 Aplicação Insegura para TCC 🚨

Este repositório contém uma aplicação propositalmente **insegura** para demonstrar
a importância do uso do **Scanner Universal de Segurança** no TCC.  

⚠️ **Atenção:**  
Esta aplicação contém falhas graves de segurança e **não deve ser usada em produção**.  
Ela existe apenas para fins **educacionais** e de **demonstração prática**.

---

## 🔥 Erros Intencionais

- Uso de **`eval()`** inseguro (execução arbitrária de código Python)
- **SQL Injection** via f-strings
- Uso de **`subprocess(shell=True)`** (command injection)
- **Segredos hardcoded** (API Key, AWS Key, DB Password)
- Dependências vulneráveis (`Flask==1.0`, `requests==2.19.0`, `PyYAML==5.1`)
- **`yaml.load()`** inseguro (deserialização maliciosa)
- Execução de Flask com **debug=True**
- Uso de **Dockerfile** com imagem antiga (Python 3.7)

---

## 🚀 Funcionalidades e Vulnerabilidades

A aplicação é uma API simples em **Flask**, com rotas que simulam funcionalidades comuns, mas implementadas de forma insegura.

### 1. `/`  
- Página inicial.  
- Exibe:  
