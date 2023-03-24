from flask import Flask, render_template, redirect, request

app=Flask(__name__)

tareas_pendientes=[]
tareas_terminadas=[]
#ruta
@app.route('/')
#vista
def index():
    return render_template('index.html',tareas=tareas_pendientes)

@app.route('/agregar', methods=["GET", "POST"])
def agregar():
    if request.method=="POST":
        nueva_tarea=request.form.get("tarea")
        tareas_pendientes.append(nueva_tarea)
        return redirect('/')
@app.route('/done/<int:id>')
def done(id):
    tareas_pendientes.pop(id)
    return redirect('/')

if __name__=="main":
    app.run(debug=True)