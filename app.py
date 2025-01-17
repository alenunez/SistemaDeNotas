from flask import Flask
from flask import render_template as render
from flask import redirect

app = Flask(__name__)

sesion_iniciada = False;

@app.route("/", methods=['GET', 'POST'])
def inicio():
    #Pagina index para inciar sesión
    return render("index.html")

@app.route('/recordarPass', methods=['GET'])
def recordar_pass():
    return render("recordarPass.html")



@app.route('/dashboard/<rol_usuario>', methods=['GET', 'POST'])
def usuario(rol_usuario):
    if rol_usuario == "estudiante":
        return render("homeEstudiante.html")
    elif rol_usuario == "profesor":
        return render("homeProfesor.html")
    elif rol_usuario == "admin":
        return render("dashboard.html")



#ADMINISTRAD0R----------------------------------------------------------------------------------------------
@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    return render("dashboard.html")

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    return render("registro.html")

@app.route("/BuscarCursosAdministrador", methods=['GET', 'POST'])
def BuscarCursosAdministrador():
    return render("BuscarCursosAdministrador.html")


@app.route("/BuscarUsuarioAdministrador", methods=['GET', 'POST'])
def BuscarUsuarioAdministrador():
    return render("BuscarUsuario.html")


@app.route("/BuscarAsignaturaAdministrador", methods=['GET', 'POST'])
def BuscarAsignaturaAdministrador():
    return render("BuscarAsignaturasAdministrador.html")


@app.route("/crearCursos", methods=['GET', 'POST'])
def crearCursos():
    return render("crearCursos.html")


@app.route("/crearAsignatura", methods=['GET', 'POST'])
def crearAsignatura():
    return render("crearAsignatura.html")


@app.route("/informacionAdministrador", methods=['GET', 'POST'])
def informacionAdministrador():
    return render("informacionAdministrador.html")

#PAGINAS DE PROFESOR-------------------------------------------------------------------------------------

@app.route("/homeProfesor", methods=['GET', 'POST'])
def homeProfesor():
    return render("homeProfesor.html")

@app.route("/misCursosProfesor", methods=['GET', 'POST'])
def misCursosProfesor():
    return render("misCursosProfesor.html")

@app.route("/informacionProfesor", methods=['GET', 'POST'])
def informacionProfesor():
    return render("informacionProfesor.html")

@app.route("/cursoProfesor", methods=['GET', 'POST'])
def cursoProfesor():
    return render("cursoProfesor.html")

@app.route("/detalleActividadProfesor", methods=['GET', 'POST'])
def detalleActividadProfesor():
    return render("detalleActividadProfesor.html")

#PAGINAS DE Estudiante----------------------------------------------------------------------------------

@app.route("/homeEstudiante", methods=['GET', 'POST'])
def homeEstudiante():
    return render("homeEstudiante.html")

@app.route("/registroAsignatura", methods=['GET', 'POST'])
def registroAsignatura():
    return render("registroAsignatura.html")

@app.route("/verNotasEstudiante", methods=['GET', 'POST'])
def verNotasEstudiante():
    return render("verNotasEstudiante.html")

@app.route("/informacionEstudiante", methods=['GET', 'POST'])
def informacionEstudiante():
    return render("informacionEstudiante.html")

@app.route("/cursoEstudiante", methods=['GET', 'POST'])
def cursoEstudiante():
    return render("cursoEstudiante.html")

@app.route("/detalleActividadEstudiante", methods=['GET', 'POST'])
def detalleActividadEstudiante():
    return render("detalleActividadEstudiante.html")

@app.route("/retroalimentacionEstudiante", methods=['GET', 'POST'])
def dretroalimentacionEstudiante():
    return render("retroalimentacionEstudiante.html")

#----------------------------------------------------------------------------------------------------------



@app.route('/perfil', methods=['GET'])
def perfil():
    return render("dashboard.html")



@app.route('/editar', methods=['GET', 'POST'])
def editar():
    return render("informacionEstudiante.html")

@app.route('/MisCursos', methods=['GET'])
def cursos(id_usuario):
    return f"Pagina mis cursos del usuario: {id_usuario}"

@app.route('/verActividades', methods=['GET', 'POST'])
def Actividades():
    return "Pagina para crear/ver actividades de los cursos de acuerdo al rol"

@app.route('/Notas', methods=['GET', 'POST'])
def notas():
    return "Página para ver/asignar notas de acuerdo al rol"

@app.route('/calificaciones', methods=['GET', 'POST'])
def calificaciones():
    return "Pagina para registrar/ver califiacaiones finales de las asignaturas"

@app.route('/detalle', methods=['GET'])
def detalle():
    return "Pagina para ver detalle de actividades y retroalimentacion de notas"

if __name__ == "__main__":
    app.run(debug=True);