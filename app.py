from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from flask_wtf.csrf import CSRFProtect  
import os

# Configuración de Flask
app = Flask(__name__, template_folder='templates')
app.secret_key = os.getenv('SECRET_KEY', '876-105-169')

# Configuración de las cookies 
app.config['SESSION_COOKIE_SECURE'] = True  # Usar solo en producción con HTTPS
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# Protección en los formularios
csrf = CSRFProtect(app)

# Configuración para el envío de correos
app.config['MAIL_SERVER'] = 'smtp.mail.yahoo.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'academia_chang_hun@yahoo.com'
app.config['MAIL_PASSWORD'] = 'jtug xkjx mlyc stri'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
@csrf.exempt
def home():
    return render_template('home.html')

@app.route("/Acerca_nosotros")
@csrf.exempt
def acerca_nosotros():
    return render_template('nosotros.html')

@app.route("/Galeria")
@csrf.exempt
def galeria():
    return render_template('Galery.html')

@app.route("/Contacto", methods=['GET', 'POST'])
@csrf.exempt
def contacto():
    if request.method == 'POST':
        email = request.form.get('email')

        if not email:
            flash("Por favor ingresa un correo electrónico válido.", "error")
            return redirect(url_for('contacto'))
        
        # Configurar y enviar el mensaje
        msg = Message(
            subject="Solicitud de Información - Academia Chang Hun",
            sender=app.config['MAIL_USERNAME'],
            recipients=[email],  # El correo del usuario que hizo la solicitud
            body=f"Gracias por contactarnos. Pronto nos pondremos en contacto contigo."
        )

        try:
            mail.send(msg)
            flash("El correo ha sido enviado exitosamente.", "success")
            print("El correo ha sido enviado exitosamente.", "success")
        except Exception as e:
            flash(f"Ocurrió un error al enviar el correo: {str(e)}", "error")
            print(f"Ocurrió un error al enviar el correo: {str(e)}", "error")
        
        return redirect(url_for('contacto'))

    # Si la solicitud es GET, simplemente renderiza la plantilla de contacto
    return render_template('contacto.html')

@app.route("/Horarios")
@csrf.exempt
def horarios():
    return render_template('Horarios.html')

@app.route("/Beneficios")
@csrf.exempt
def beneficios():
    return render_template('beneficios.html')





if __name__ == '__main__':
    app.run(debug=True)
