from flask import Flask, request
import joblib as jb
import json

app = Flask(__name__)

mdl = jb.load("mdl.pkl.z")

@app.route("/", methods=["GET"])
def index():
    return "<div style='ajust-content:center'><h2>Esta API foi criada por Adriano Avelar:eam.avelar@gmail.com</h2><br> \
            <h3>Para consumir, faça uma requisição para /api/v1 com parâmetro title</h3><br> \
            <h3> a resposta é em json com o title e a probabilidade da notícia ser Verdadeira</h3><br>\
              <h3>Versão atual: 1</h3><br> \
                  <h3>ex: https://fakenewsdetector-api.herokuapp.com/api/v1?title='Titulo da noticia em ingles' </h3> \
              </div> "
@app.route("/api/v1", methods=["GET"])
def main():
    
    print(request.args)
    
    title = request.args.get("title",default='')
    res = {"title": title, "p": mdl.predict_proba([title])[0][1]}
    return json.dumps(res)


def createapp():
    return app
    
if __name__ == "__main__":
    app.run()
