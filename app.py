from flask import Flask, request
import sqlite3
import subprocess
import yaml

app = Flask(__name__)

# ⚠️ Erro proposital: uso de debug=True
app.config["DEBUG"] = True

# ⚠️ Erro proposital: segredo hardcoded
API_KEY = "sk-1234567890SECRETKEY"

@app.route("/")
def home():
    return "🚨 Aplicação Insegura - Exemplo para Scanner de Segurança 🚨"

@app.route("/eval")
def executar_eval():
    # ⚠️ Erro proposital: eval inseguro
    comando = request.args.get("cmd", "2+2")
    return str(eval(comando))

@app.route("/sql")
def executar_sql():
    # ⚠️ Erro proposital: SQL injection via f-string
    usuario = request.args.get("usuario", "admin")
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("CREATE TABLE usuarios (id INTEGER, nome TEXT)")
    c.execute("INSERT INTO usuarios VALUES (1, 'admin')")
    query = f"SELECT * FROM usuarios WHERE nome = '{usuario}'"
    resultado = c.execute(query).fetchall()
    return str(resultado)

@app.route("/subprocess")
def executar_subprocess():
    # ⚠️ Erro proposital: subprocess com shell=True
    comando = request.args.get("cmd", "ls")
    saida = subprocess.run(comando, shell=True, capture_output=True, text=True)
    return saida.stdout

@app.route("/yaml")
def carregar_yaml():
    # ⚠️ Erro proposital: yaml.load inseguro
    conteudo = request.args.get("data", "!!python/object/apply:os.system ['ls']")
    return str(yaml.load(conteudo))
    

if __name__ == "__main__":
    # ⚠️ Erro proposital: execução com debug=True
    app.run(debug=True)
