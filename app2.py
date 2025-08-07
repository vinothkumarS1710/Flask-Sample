from flask import Flask,redirect,render_template,request,url_for
from flask_sqlalchemy import SQLAlchemy

from flask_mail import Mail, Message

app=Flask(__name__)

# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USERNAME'] = 'vinu33069@gmail.com'
# app.config['MAIL_PASSWORD'] = 'aldhzrycriylrjxi'
# app.config['MAIL_USE_TLS'] = True

# mail = Mail(app)

# @app.route('/send',methods=['GET','POST'])
# def sendmail():
#     if request.method == 'POST':
#         get_mail_id = request.form.get('mail_id')
#         get_info = request.form.get('receiver')
#         message = request.form.get('message')
#         msg  = Message('subject',sender = get_mail_id,recipients=[get_info])
#         msg.body = message
#         mail.send(msg)
#         return 'mail send...!'
#     return render_template('mail.html')




if __name__ == '__main__':
    app.run(debug=True)

