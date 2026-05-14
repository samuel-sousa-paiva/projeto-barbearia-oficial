from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():

    return """
    <html>

    <head>

        <title>SMD Barbearia</title>

        <style>

            body{
                background: #0d0d0d;
                color: white;
                font-family: Arial;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .box{
                background: #1a1a1a;
                padding: 40px;
                border-radius: 20px;
                width: 350px;
                text-align: center;
                border-top: 5px solid gold;
            }

            h1{
                color: gold;
                margin-bottom: 25px;
            }

            input{
                width: 100%;
                padding: 12px;
                margin-bottom: 15px;
                border: none;
                border-radius: 10px;
                background: #222;
                color: white;
            }

            button{
                width: 100%;
                padding: 12px;
                border: none;
                border-radius: 10px;
                background: gold;
                color: black;
                font-weight: bold;
                cursor: pointer;
            }

            button:hover{
                opacity: 0.8;
            }

        </style>

    </head>

    <body>

        <div class="box">

            <h1>SMD BARBEARIA</h1>

            <form action="/agendar" method="POST">

                <input
                type="text"
                name="nome"
                placeholder="Nome do cliente">

                <input
                type="text"
                name="servico"
                placeholder="Serviço desejado">

                <input
                type="time"
                name="horario">

                <button type="submit">
                    AGENDAR
                </button>

            </form>

        </div>

    </body>

    </html>
    """

@app.route("/agendar", methods=["POST"])
def agendar():

    nome = request.form["nome"]
    servico = request.form["servico"]
    horario = request.form["horario"]

    return f"""

    <body style="background:#111;color:white;
    font-family:Arial;text-align:center;padding-top:100px;">

    <h1 style="color:gold;">
    HORÁRIO AGENDADO!
    </h1>

    <p>Cliente: {nome}</p>

    <p>Serviço: {servico}</p>

    <p>Horário: {horario}</p>

    </body>
    """

if __name__ == "__main__":
    app.run(debug=True)
    
    
    from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastro_ok")
def cadastro_ok():
    return render_template("cadastro_ok.html")

if __name__ == "__main__":
    app.run(debug=True)