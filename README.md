# 🚨 Aplicação Insegura para Demonstração de Segurança 🚨

Esta é uma aplicação **propositalmente insegura**, criada apenas para **demonstração em TCC**.  
O objetivo é mostrar como vulnerabilidades aparecem em relatórios de scanners de segurança (Semgrep, Gitleaks, Trivy).

---

## ⚠️ O que a aplicação faz
- Simula uma **API em Flask** com várias funcionalidades inseguras:
  - `eval()` → permite execução de código arbitrário.
  - SQL via f-strings → abre porta para **SQL Injection**.
  - `subprocess(..., shell=True)` → possibilita **Command Injection**.
  - `yaml.load()` → vulnerável a **execução remota de código**.
  - Executa com `debug=True` → expõe depurador perigoso.

- Contém **segredos hardcoded** diretamente no código:
  - API Key falsa
  - Chave AWS simulada
  - Senha de banco de dados exposta

- Usa **dependências vulneráveis**:
  - `Flask==1.0`
  - `requests==2.19.0`
  - `PyYAML==5.1`

- Possui um **Dockerfile inseguro**:
  - Baseado em `python:3.7`, imagem antiga e sem atualizações de segurança.

---

## 🛑 Por que é insegura?
- **RCE (Remote Code Execution):** atacante pode executar código no servidor.  
- **SQL Injection:** invasor pode ler ou alterar dados do banco.  
- **Command Injection:** permite rodar comandos do sistema.  
- **Segredos vazados:** credenciais podem ser roubadas.  
- **Dependências vulneráveis:** exploráveis por CVEs já conhecidos.  
- **Imagem antiga:** aumenta risco de falhas não corrigidas.  

---

## 🎯 Objetivo
Esta aplicação serve como **exemplo prático** para:
- Demonstrar falhas comuns de segurança em código.  
- Mostrar como ferramentas de análise (Semgrep, Gitleaks, Trivy) detectam essas falhas.  
- Evidenciar a importância de integrar **scanners de segurança** em pipelines DevSecOps.  

---

⚠️ **Atenção:** Nunca use este código em produção. Ele foi feito **apenas para fins educacionais e de demonstração**.
