from flask import Flask, request, render_template
import random
app= Flask (__name__)

@app.route("/")
def index():
    esimene_nimi = request.args.get("esimene_nimi", default="", type=int)
    teine_nimi = request.args.get("teine_nimi", default = "", type = int)
    
    tulemus = random.randint(1, 100)
    return render_template(
        "index.html",
        arv = tulemus,
       
    )


if __name__ == "__main__":
    app.run(debug = False)
    