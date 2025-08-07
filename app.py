from flask import Flask,render_template,request,redirect,url_for
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/career')
def career():
    return render_template('career.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login/sign_up')
def register():
    return render_template('register.html')

@app.route('/login/register',methods=['POST'])
def validate():
    name=request.form.get('user_name')
    mail=request.form.get('email')
    password=request.form.get('password')
    con_pass=request.form.get('con_password')

    if not name or not mail or not password or not con_pass:
        return "❌ All values are required"
    if len(name)<=3:
        return f'❌ Enter the valid name'
    if password!=con_pass:
        return f'❌ Password Mismatch'
    if '@' not in mail or '.' not in mail:
        return f'❌ Enter Valid Email'
    
    con=sql.connect('student_db.db')
    cur=con.cursor()
    cur.row_factory=sql.Row
    cur.execute('insert into stu_reg_dts values(?,?,?,?)',(name,mail,password,con_pass))
    data=cur.fetchall()
    con.commit()
    return redirect('/get')

@app.route('/get',methods=['GET'])
def get():
    con=sql.connect('student_db.db')
    cur=con.cursor()
    cur.row_factory=sql.Row
    cur.execute('select * from stu_reg_dts')
    data=cur.fetchall()
    con.commit()
    return render_template('users.html',datas=data)


@app.route('/getedit/<name>',methods=['GET','POST'])
def get_edit(name):
    con=sql.connect('student_db.db')
    cur=con.cursor()
    cur.row_factory=sql.Row
    cur.execute('select * from stu_reg_dts where Name=?',(name,))
    data=cur.fetchone()
    con.commit()
    return render_template('edit.html',data=data)

@app.route('/update/<name>', methods=['POST'])
def update(name):

    mail=request.form.get('email')
    name=request.form.get('user_name')
    cur=con.cursor()
    password=request.form.get('password')
    cur.execute('update stu_reg_dts set Name=?, Email=?, Password=?, Confirm_Password=? where Name=?',(name,mail,password,con_pass,name))
    con_pass=request.form.get('con_password')
    con=sql.connect('student_db.db')
    cur.row_factory=sql.Row
    data=cur.fetchall()    
    con.commit()    
    return redirect('/get')@app.route('/home', methods=['POST'])




def login_val():
    name=request.form.get('nme')
    passwrd=request.form.get('pass')

    con=sql.connect('student_db.db')
    cur=con.cursor()
    cur.row_factory=sql.Row
    cur.execute('insert into student(Name,Password) values (?,?)',(name,passwrd))
    cur.execute('select * from student')
    rows=cur.fetchall()
    con.commit()
    con.close()
    return render_template('details.html',rows=rows)


@app.route('/remove/<name>')
def remove(name):
    con=sql.connect('student_db.db')
    cur=con.cursor()
    cur.row_factory=sql.Row
    cur.execute('delete from stu_reg_dts where Name=?',(name,))
    rows=cur.fetchall()
    con.commit()
    con.close()
    return redirect('/get')


if __name__=='__main__':
    app.run(debug=True)


