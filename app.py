from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta'

# Lista para almacenar usuarios
usuarios = []

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre_usuario = request.form['nombre_usuario']
        correo_electronico = request.form['correo_electronico']
        contraseña = request.form['contraseña']

        # Verificar si el usuario o correo electrónico ya existe
        for usuario in usuarios:
            if usuario['nombre_usuario'] == nombre_usuario or usuario['correo_electronico'] == correo_electronico:
                flash('El registro del usuario falló. El usuario ya existe.', 'danger')
                return render_template('registro.html')

        nuevo_usuario = {'nombre_usuario': nombre_usuario, 'correo_electronico': correo_electronico, 'contraseña': contraseña}
        usuarios.append(nuevo_usuario)
        flash('¡Usuario registrado con éxito!', 'success')
        return redirect(url_for('registro'))

    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)
