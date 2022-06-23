from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, abort, jsonify
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField
from passlib.hash import sha256_crypt
from functools import wraps
from flask_uploads import UploadSet, configure_uploads, IMAGES
import timeit
import datetime
from flask_mail import Mail, Message
import os
from wtforms.fields.html5 import EmailField
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
#from google.oauth2 import id_token
#from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import pathlib
import requests
#import google.auth.transport.requests
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf
from wsgiref import headers
from werkzeug.security import generate_password_hash, check_password_hash
import smtplib
import ssl
import yaml

app = Flask(__name__)
app.secret_key = 'UBDRONE'



app.config['SECRET_KEY'] = 'ubdrone'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LdqLvUaAAAAAHsAd1e7grX9pfxVamghLUkNsrwP'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LdqLvUaAAAAAIxAD7KrlNmQ6s1dXHSbALEbVaBC'
app.config['TESTING'] = True




db = yaml.load(open('bazadedateubdrone.yaml'))
app.config['MYSQL_HOST'] = db['ubd_magazin_server']
app.config['MYSQL_USER'] = db['utilizator']
app.config['MYSQL_PASSWORD'] = db['parola_server']
app.config['MYSQL_DB'] = db['baza_date_ubdrone']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/imaginisite/produse'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)


def utilizator_conectat(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if 'conectat' in session:
            return func(*args, *kwargs)
        else:
            flash("Felicitări te-ai inregistrat cu succes", category="succes")
            return redirect(url_for('autentificare'))

    return wrap


def utilizator_neconectat(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if 'conectat' in session:
            return redirect(url_for('acasa2'))
        else:
            return func(*args, *kwargs)
    return wrap


def adminul_este_logat(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if 'admin_autentificat' in session:
            return func(*args, *kwargs)
        else:
            flash("Logheaza-te prima data", category="danger")
            return redirect(url_for('admin_autentificare'))

    return wrap


def admin_neconectat(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if 'admin_autentificat' in session:
            return redirect(url_for('admin'))
        else:
            flash("Logheaza-te prima data", category="danger")
            return func(*args, *kwargs)

    return wrap


def wrappers(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped


@app.route('/')
def acasa2():
    drona_cursor = mysql.connection.cursor()
    produs_site = 'Drone'
    drona_cursor.execute("Select * from produse where categorie=%s order by rand() LIMIT 12",  [produs_site,])
    Drone = drona_cursor.fetchall()
    accesorii_cursor = mysql.connection.cursor()
    produs_site = 'Accesorii'
    accesorii_cursor.execute("Select * from produse where categorie=%s order by rand() LIMIT 12", [produs_site,])
    Accesorii = accesorii_cursor.fetchall()
    piese_cursor = mysql.connection.cursor()
    produs_site = 'Piese'
    piese_cursor.execute("Select * from produse where categorie=%s order by rand() LIMIT 12", [produs_site,])
    Piese = piese_cursor.fetchall()
    executa = mysql.connection.cursor()
    produs_site = 'Baterii'
    executa.execute("Select * from produse where categorie=%s order by rand() LIMIT 12", [produs_site,])
    Baterii = executa.fetchall()
    executa.close()
    return render_template('acasa2.html', Drone=Drone, Accesorii=Accesorii, Piese=Piese, Baterii=Baterii)


class Autentificare(Form): 
    email = StringField(
        '', 
        [validators.length(min=5, max=20)],
        render_kw={'placeholder': 'Email'})
    parola = PasswordField(
        '', 
        [validators.length(min=5, max=20)],
        render_kw={'placeholder': 'Parola'})



@app.route('/autentificare', methods=['GET', 'POST'])
@utilizator_neconectat
def autentificare():
    form = Autentificare(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        parola_utilizator = form.parola.data
        curssor = mysql.connection.cursor()
        userupdate = curssor.execute("select * from utilizatori where email=%s", [email])
        if int(userupdate) > 0:
            data = curssor.fetchone()
            parola = data['parola']
            id_utilizator = data['id']
            email = data['email']
            if sha256_crypt.verify(parola_utilizator, parola):
                session['conectat'] = True
                session['id_utilizator'] = id_utilizator
                session['s_nume'] = email
                vector = '1'
                curssor.execute("update utilizatori SET online=%s where id=%s", [vector, id_utilizator])
                flash('Felicitari, te-ai autentificat cu succes', 'success')
                return redirect(url_for('acasa2'))
            else:
                flash('parola incorecta', 'danger')
                return render_template('autentificare.html', form=form)
        else:
            flash('Aceasta adresa de email nu este asociata niciunui cont, te rog inregistreaza-te', 'danger')           
            curssor.close()
            return render_template('autentificare.html', form=form)
    return render_template('autentificare.html', form=form)
    
@app.route('/deconectare')
def deconectare():
    if 'id_utilizator' in session:       
        curssor = mysql.connection.cursor()
        id_utilizator = session['id_utilizator']
        vector = '0'
        curssor.execute("update utilizatori SET online=%s where id=%s", [vector, id_utilizator])
        session.clear()
        flash('Sunteti deconectat', 'success')
        return redirect(url_for('acasa2'))
    return redirect(url_for('autentificare'))


class Inregistrare(Form):
    email = EmailField(
        '',
        [validators.DataRequired(), 
        validators.Email(), 
        validators.length(min=5, max=20)],
        render_kw={'placeholder': 'Email'})
    parola = PasswordField(
        '', 
        [validators.length(min=5, max=20)],
        render_kw={'placeholder': 'Parola'})
    recaptcha = RecaptchaField()


@app.route('/inregistrare', methods=['GET', 'POST'])
@utilizator_neconectat
def inregistrare():
    form = Inregistrare(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        parola = sha256_crypt.hash(str(form.parola.data))
        c = mysql.connection.cursor()  
        vector = c.execute("select * from utilizatori where email = (%s)",(email,))
        if int(vector) > 0:
            flash("Exista un cont creat cu aceasi adresa de email", "danger")
            return redirect(url_for('inregistrare'))
        else:
            c.execute("insert into utilizatori(email, parola) VALUES(%s, %s)",
                (email, parola))     
        mysql.connection.commit()     
        c.close()
        flash('Felicitari, te-ai înregistrat cu succes', 'success')
        return redirect(url_for('autentificare'))
    return render_template('inregistrare.html', form=form)



class Comanda(Form):  
    nume = StringField('', [validators.length(min=1), validators.DataRequired()],render_kw={'placeholder': 'Nume & prenume'})
    telefon_num = StringField('', [validators.length(min=1), validators.DataRequired()],render_kw={'placeholder': 'Telefon:'})
    cantitate = SelectField('', [validators.DataRequired()],choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    modalitate_plata = SelectField('', [validators.DataRequired()],choices=[('Livrare prin curier', 'Livrare prin curier'), ('Ridicare personala', 'Ridicare personala')])
    adresa_strada = StringField('', [validators.length(min=1), validators.DataRequired()],render_kw={'placeholder': 'Strada, Nr, Bloc, Ap'})                  
    adresa_locatie = StringField('', [validators.length(min=1), validators.DataRequired()],render_kw={'placeholder': 'Judet & Oras'})

@app.route('/Drone', methods=['GET', 'POST'])
def Drone():
    form = Comanda(request.form)   
    curent_produs = ['Drone']  
    dronacurs = mysql.connection.cursor()      
    dronacurs.execute("select * from produse where categorie=%s", [curent_produs])
    produse = dronacurs.fetchall()     
    dronacurs.close()
    if request.method == 'POST':       
        efectuareComanda = request.form
        modalitate_plata = form.modalitate_plata.data
        nume = efectuareComanda['nume']
        telefon = efectuareComanda['telefon_num']
        adresa_strada = efectuareComanda['adresa_strada']
        adresa_locatie = efectuareComanda['adresa_locatie']
        cantitate = efectuareComanda['cantitate']        
        id_produs = request.args['comanda']
        acum = datetime.datetime.now()        
        acum.strftime("%y-%m-%d %H:%M:%S")               
        curs = mysql.connection.cursor()        
        if 'id_utilizator' in session:           
            id_utilizator = session['id_utilizator']
            curs.execute("insert into comenzi(id_utilizator, id_produs, c_nume, telefon, strada, adr_loc, cantitate,mplata) "                         "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",                        (id_utilizator, id_produs, nume, telefon, adresa_strada, adresa_locatie, cantitate, modalitate_plata))
        else:            
            curs.execute("insert into comenzi(id_produs, c_nume, telefon, strada, adr_loc, cantitate,mplata) " "VALUES(%s, %s, %s, %s, %s, %s, %s)",(id_produs, nume, telefon, adresa_strada, adresa_locatie, cantitate, modalitate_plata))      
        mysql.connection.commit()       
        dronacurs.close()       
        flash('Comanda efectuata cu succes', 'success')
        return render_template('Drone.html', Drone=produse, form=form)
    if 'vizualizare' in request.args:      
        produs_id = request.args['vizualizare']
        crsdrona = mysql.connection.cursor()        
        crsdrona.execute("select * from produse where id=%s", (produs_id,))
        produs = crsdrona.fetchall()
        if 'id_utilizator' in session:            
            id_utilizator = session['id_utilizator']           
            dronacrs = mysql.connection.cursor()
            dronacrs.execute("select * from vizualizare_produs where utilizator_id=%s AND produs_id=%s", (id_utilizator, produs_id))
            userupdate = dronacrs.fetchall()
            if userupdate:                
                acum = datetime.datetime.now()
                timp_acum = acum.strftime("%y-%m-%d %H:%M:%S")               
                dronacrs.execute("update vizualizare_produs SET date=%s where utilizator_id=%s AND produs_id=%s",(timp_acum, id_utilizator, produs_id))
            else:             
                dronacrs.execute("insert into vizualizare_produs(utilizator_id, produs_id) VALUES(%s, %s)", (id_utilizator, produs_id))
                mysql.connection.commit()              
        return render_template('vizualizare_produs.html', Achizitii=produs)
    elif 'comanda' in request.args:       
        produs_id = request.args['comanda']
        crsdrona = mysql.connection.cursor()       
        crsdrona.execute("select * from produse where id=%s", [produs_id,])
        produs = crsdrona.fetchall()
        return render_template('comanda_produs.html', Achizitii=produs, form=form)
    return render_template('Drone.html', Drone=produse, form=form)



@app.route('/Accesorii', methods=['GET', 'POST'])
def Accesorii():
    form = Comanda(request.form)   
    accesoriicomanda = mysql.connection.cursor()   
    produs_site = 'Accesorii'
    accesoriicomanda.execute("select * from produse where categorie=%s", (produs_site,))
    produse = accesoriicomanda.fetchall()    
    accesoriicomanda.close()
    if request.method == 'POST' and form.validate():
        nume = form.nume.data
        telefon = form.telefon_num.data
        adresa_strada = form.adresa_strada.data
        adresa_locatie = form.adresa_locatie.data
        cantitate = form.cantitate.data
        modalitate_plata = form.modalitate_plata.data
        id_produs = request.args['comanda']
        acum = datetime.datetime.now()
        saptamana = datetime.timedelta(days=7)
        data_de_livrare = acum + saptamana
        timp_acum = data_de_livrare.strftime("%y-%m-%d %H:%M:%S")       
        comandaaccinsert = mysql.connection.cursor()
        if 'id_utilizator' in session:
            id_utilizator = session['id_utilizator']
            comandaaccinsert.execute("insert into comenzi(id_utilizator, id_produs, c_nume, telefon, strada, adr_loc, cantitate,mplata, data_livrare) ""VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",(id_utilizator, id_produs, nume, telefon, adresa_strada, adresa_locatie, cantitate,modalitate_plata, timp_acum))
        else:
            comandaaccinsert.execute("insert into comenzi(id_produs, c_nume, telefon, strada, adr_loc, cantitate, mplata, data_livrare) ""VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",(id_produs, nume, telefon, adresa_strada, adresa_locatie, cantitate, modalitate_plata, timp_acum))        
        mysql.connection.commit()       
        accesoriicomanda.close()
        flash('Comanda efectuata cu succes', 'success')
        return render_template('Accesorii.html', Accesorii=produse, form=form)
    if 'vizualizare' in request.args:
        accesoriiq = request.args['vizualizare']
        produs_id = accesoriiq
        crsaccesorii = mysql.connection.cursor()
        crsaccesorii.execute("select * from produse where id=%s", (accesoriiq,))
        produse = crsaccesorii.fetchall()
        return render_template('vizualizare_produs.html', Achizitii=produse)
    elif 'comanda' in request.args:
        produs_id = request.args['comanda']
        crsaccesorii = mysql.connection.cursor()
        crsaccesorii.execute("select * from produse where id=%s", [produs_id,])
        produs = crsaccesorii.fetchall()
        return render_template('comanda_produs.html', Achizitii=produs, form=form)
    return render_template('Accesorii.html', Accesorii=produse, form=form)


@app.route('/Piese', methods=['GET', 'POST'])
def Piese():
    form = Comanda(request.form)   
    comandapiese = mysql.connection.cursor()    
    produs_site = 'Piese'
    comandapiese.execute("select * from produse where categorie=%s", (produs_site,))
    produse = comandapiese.fetchall()  
    comandapiese.close()
    if request.method == 'POST' and form.validate():
        nume = form.nume.data
        telefon = form.telefon_num.data
        adresa_strada = form.adresa_strada.data
        adresa_locatie = form.adresa_locatie.data
        cantitate = form.cantitate.data
        modalitate_plata = form.modalitate_plata.data
        id_produs = request.args['comanda']
        acum = datetime.datetime.now()
        saptamana = datetime.timedelta(days=7)
        data_de_livrare = acum + saptamana
        timp_acum = data_de_livrare.strftime("%y-%m-%d %H:%M:%S")
        
        curs = mysql.connection.cursor()
        if 'id_utilizator' in session:
            id_utilizator = session['id_utilizator']
            curs.execute("insert into comenzi(id_utilizator, id_produs, c_nume, telefon, strada, adr_loc, cantitate, mplata, data_livrare) "
                         "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                         (id_utilizator, id_produs, nume, telefon, adresa_strada, adresa_locatie, cantitate, modalitate_plata, timp_acum))
        else:
            curs.execute("insert into comenzi(id_produs, c_nume, telefon, strada, adr_loc, cantitate, mplata, data_livrare) "
                         "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                         (id_produs, nume, telefon, adresa_strada, adresa_locatie, cantitate, modalitate_plata, timp_acum))

        
        mysql.connection.commit()     
        comandapiese.close()
        flash('Comanda efectuata cu succes', 'success')
        return render_template('Piese.html', Piese=produse, form=form)
    if 'vizualizare' in request.args:
        pieseq = request.args['vizualizare']
        produs_id = pieseq
        crspiese = mysql.connection.cursor()
        crspiese.execute("select * from produse where id=%s", (pieseq,))
        produse = crspiese.fetchall()
        return render_template('vizualizare_produs.html', Achizitii=produse)
    elif 'comanda' in request.args:
        produs_id = request.args['comanda']
        crspiese = mysql.connection.cursor()
        crspiese.execute("select * from produse where id=%s", [produs_id,])
        produs = crspiese.fetchall()
        return render_template('comanda_produs.html', Achizitii=produs, form=form)
    return render_template('Piese.html', Piese=produse, form=form)


@app.route('/Baterii', methods=['GET', 'POST'])
def Baterii():
    form = Comanda(request.form)   
    comandabaterii = mysql.connection.cursor()   
    produs_site = 'Baterii'
    comandabaterii.execute("select * from produse where categorie=%s", (produs_site,))
    produse = comandabaterii.fetchall()   
    comandabaterii.close()
    if request.method == 'POST' and form.validate():
        nume = form.nume.data
        telefon = form.telefon_num.data
        adresa_strada = form.adresa_strada.data
        adresa_locatie = form.adresa_locatie.data
        cantitate = form.cantitate.data
        modalitate_plata = form.modalitate_plata.data
        id_produs = request.args['comanda']
        acum = datetime.datetime.now()
        saptamana = datetime.timedelta(days=7)
        data_de_livrare = acum + saptamana
        timp_acum = data_de_livrare.strftime("%y-%m-%d %H:%M:%S")      
        curs = mysql.connection.cursor()
        if 'id_utilizator' in session:
            id_utilizator = session['id_utilizator']
            curs.execute("insert into comenzi(id_utilizator, id_produs, c_nume, telefon, strada, adr_loc, cantitate, mplata, data_livrare) ""VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",(id_utilizator, id_produs, nume, telefon, adresa_strada, adresa_locatie, cantitate, modalitate_plata, timp_acum))
        else:
            curs.execute("insert into comenzi(id_produs, c_nume, telefon, strada, adr_loc, cantitate, mplata, data_livrare) ""VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",(id_produs, nume, telefon, adresa_strada, adresa_locatie, cantitate, modalitate_plata, timp_acum))        
        mysql.connection.commit()        
        comandabaterii.close()
        flash('Comanda efectuata cu succes', 'success')
        return render_template('Baterii.html', Baterii=produse, form=form)
    if 'vizualizare' in request.args:
        bateriiq = request.args['vizualizare']
        produs_id = bateriiq
        crsbaterii = mysql.connection.cursor()
        crsbaterii.execute("select * from produse where id=%s", (bateriiq,))
        produse = crsbaterii.fetchall()
        return render_template('vizualizare_produs.html', Achizitii=produse)
    elif 'comanda' in request.args:
        produs_id = request.args['comanda']
        crsbaterii = mysql.connection.cursor()
        crsbaterii.execute("select * from produse where id=%s", [produs_id,])
        produs = crsbaterii.fetchall()
        return render_template('comanda_produs.html', Achizitii=produs, form=form)
    return render_template('Baterii.html', Baterii=produse, form=form)


@app.route('/admin_autentificare', methods=['GET', 'POST'])
@admin_neconectat
def admin_autentificare():
    if request.method == 'POST':
        numeutilizator = request.form['email']
        parola_utilizator = request.form['parola']     
        admincurs = mysql.connection.cursor()
        userupdate = admincurs.execute("select * from admin where email=%s", [numeutilizator])
        if userupdate > 0:
            data = admincurs.fetchone()
            parola = data['parola']
            id_utilizator = data['id']
            nume = data['numeadmin']
            if sha256_crypt.verify(parola_utilizator, parola):
                session['admin_autentificat'] = True
                session['admin_id_utilizator'] = id_utilizator
                session['admin_nume'] = nume
                return redirect(url_for('admin'))
            else:
                flash('Parola incorecta', 'danger')
                return render_template('admin/autentificare.html')
        else:
            flash('Admin neiregistrat', 'danger')           
            admincurs.close()
            return render_template('admin/autentificare.html')
    return render_template('admin/autentificare.html')


@app.route('/admin_logout')
def admin_deconectare():
    if 'admin_autentificat' in session:
        session.clear()
    return redirect(url_for('admin_autentificare'))


@app.route('/admin')
@adminul_este_logat
def admin():
    admin_login = mysql.connection.cursor()
    randuri_produse = admin_login.execute("select * from produse")
    userupdate = admin_login.fetchall()
    return render_template('admin/acasa2.html',userupdate=userupdate,rand=randuri_produse)


@app.route('/comenzi')
@adminul_este_logat
def comenzi():
    toate_produsele = mysql.connection.cursor()
    randuri_comanda = toate_produsele.execute("select * from comenzi")
    userupdate = toate_produsele.fetchall()
    return render_template('admin/toate_comenzile.html',userupdate=userupdate,randuri_comanda=randuri_comanda)


@app.route('/utilizatori')
@adminul_este_logat
def utilizatori():
    curso = mysql.connection.cursor()
    randuri_utilizatori = curso.execute("select * from utilizatori")
    userupdate = curso.fetchall()
    return render_template('admin/toti_utilizatorii.html',userupdate=userupdate,randuri_utilizatori=randuri_utilizatori)


@app.route('/admin_adauga_produs', methods=['POST', 'GET'])
@adminul_este_logat
def admin_adauga_produs():
    if request.method == 'POST': 
        nume = request.form.get('nume')
        pret = request.form['pret']
        descriere = request.form['descriere']
        stoc = request.form['stoc']
        categorie = request.form['categorie']
        item = request.form['item']
        cod = request.form['cod']
        fisier = request.files['imagine']
        if nume and pret and descriere and stoc and categorie and item and cod and fisier:
            imagineprodus = fisier.filename
            produsimagine = imagineprodus.replace("'", "")
            imagine = produsimagine.replace(" ", "_")
            if imagine.endswith(('.bmp','.png','.gif','tiff','.jpg','.jpeg')):
                salvare_imagine = photos.save(fisier, folder=categorie)
                if salvare_imagine:                   
                    cursul = mysql.connection.cursor()
                    cursul.execute("insert into produse(p_nume,pret,descriere,stoc,categorie,item,pcod,imagine)""VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",(nume, pret, descriere, stoc, categorie, item, cod, imagine))
                    mysql.connection.commit()
                    produs_id = cursul.lastrowid
                    cursul.execute("insert into categorie_de_produs(produs_id)" "VALUES(%s)", [produs_id])
                    if categorie == 'Drone' and 'Accesorii' and 'Baterii' and 'Piese':
                        producator = request.form.getlist('Drone')
                        producator = request.form.getlist('Accesorii')
                        producator = request.form.getlist('Baterii')
                        producator = request.form.getlist('Piese')                        
                        for ctg_produs in producator:
                            ok = 'ok'
                            updateproduse = 'update categorie_de_produs SET {spatiu}=%s where produs_id=%s'.format(spatiu=ctg_produs)
                            cursul.execute(updateproduse, (ok, produs_id))                          
                            mysql.connection.commit()
                    else:
                        flash('Nu exista acest produs', 'danger')
                        return redirect(url_for('admin_adauga_produs'))                   
                    cursul.close()
                    flash('Produs adaugat cu succes', 'success')
                    return redirect(url_for('admin_adauga_produs'))
                else:
                    flash('Reincarca imaginea', 'danger')
                    return redirect(url_for('admin_adauga_produs'))
            else:
                flash('Fisierul nu este acceptat', 'danger')
                return redirect(url_for('admin_adauga_produs'))
        else:
            flash('Completeaza toate spatiile libere', 'danger')
            return redirect(url_for('admin_adauga_produs'))
    else:
        return render_template('admin/adauga_produs.html')

@app.route('/editare_produs', methods=['POST', 'GET'])
@adminul_este_logat
def editare_produs():
    if 'id' in request.args:
        produs_id = request.args['id']
        crseditare = mysql.connection.cursor()
        cicarezultat = crseditare.execute("SELECT * FROM produse WHERE id=%s", (produs_id,))
        produs = crseditare.fetchall()
        crseditare.execute("SELECT * FROM categorie_de_produs WHERE produs_id=%s", (produs_id,))
        categorie_de_produs = crseditare.fetchall()
        if cicarezultat:
            if request.method == 'POST':
                nume = request.form.get('nume')
                pret = request.form['pret']
                descriere = request.form['descriere']
                stoc = request.form['stoc']
                categorie = request.form['categorie']
                item = request.form['item']
                cod = request.form['cod']                
                if nume and pret and descriere and stoc and categorie and item and cod:                           
                    editcursor = mysql.connection.cursor()
                    executiecursor = crseditare.execute(
                        "UPDATE produse SET p_nume=%s, pret=%s, descriere=%s, stoc=%s, categorie=%s, item=%s, pcod=%s WHERE id=%s",(nume, pret, descriere, stoc, categorie, item, cod, produs_id))
                    if executiecursor:
                        if categorie == 'Drone':
                            producator = request.form.getlist('Drone')
                            for ctg_produs in producator:
                                ok = 'ok'
                                updateproduse = 'UPDATE categorie_de_produs SET {spatiu}=%s WHERE produs_id=%s'.format(spatiu=ctg_produs)
                                editcursor.execute(updateproduse, (ok, produs_id))    
                                mysql.connection.commit()
                        else:
                            flash('Acest produs nu exista', 'danger')
                            return redirect(url_for('admin_adauga_produs', produs=produs,categorie_de_produs=categorie_de_produs))
                        flash('Produs actualizat cu succes', 'success')
                        return redirect(url_for('editare_produs', produs=produs,categorie_de_produs=categorie_de_produs))
                    else:
                        flash('Produs neactualizat', 'danger')
                        return redirect(url_for('editare_produs', produs=produs,categorie_de_produs=categorie_de_produs))
            else:
                print('Acum puteti edita produsul')
                return render_template('admin/editare_produs.html', produs=produs,categorie_de_produs=categorie_de_produs)
        else:
            print('Completeaza toate spatiile', 'danger')
            return render_template('admin/editare_produs.html', produs=produs,categorie_de_produs=categorie_de_produs)
    else:
        return redirect(url_for('admin_autentificare',))


@app.route('/search', methods=['POST', 'GET'])
def search():
    cautare_produse = request.args['produs']
    crscauta = mysql.connection.cursor()
    query_string = "select * from produse where p_nume LIKE %s"
    crscauta.execute(query_string, ('%' + cautare_produse + '%',))
    produse = crscauta.fetchall()
    crscauta.close()
    flash('Rezultate cautare: ' + cautare_produse, 'success')
    return render_template('cauta.html', produse=produse)


@app.route('/profil')
@utilizator_conectat
def profil():
    if 'utilizator' in request.args:
        rezultatcomanda = request.args['utilizator']
        profilcurs = mysql.connection.cursor()
        profilcurs.execute("select * from utilizatori where id=%s", (rezultatcomanda,))
        userupdate = profilcurs.fetchone()
        if userupdate['id'] == session['id_utilizator']:
                profilcurs.execute("select * from comenzi where id_utilizator=%s", (session['id_utilizator'],))
                updateprofil = profilcurs.fetchall()
                return render_template('profil.html', userupdate=updateprofil)
        else:
                flash('Neautorizat', 'danger')
                return redirect(url_for('autentificare'))
    return redirect(url_for('autentificare'))


class SchimbareParola(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Email(), validators.length(min=5, max=20), validators.InputRequired()],render_kw={'placeholder': 'Email'})
    parola = PasswordField('Parola', [validators.length(min=6, max=20), validators.InputRequired(), validators.EqualTo('verificare_parola', message='Parola trebuie sa fie de acelasi fel')],render_kw={'placeholder': 'Parola'})
    verificare_parola = PasswordField('Confirma Parola', [validators.length(min=6, max=20), validators.InputRequired()],render_kw={'placeholder': 'Parola'})

@app.route('/contul_meu', methods=['POST', 'GET'])
@utilizator_conectat
def contul_meu():
    form = SchimbareParola(request.form)
    if 'utilizator' in request.args:
        pass
        schimbare_parola = request.args['utilizator']
        curso = mysql.connection.cursor()
        curso.execute("select * from utilizatori where id=%s", (schimbare_parola,))
        userupdate = curso.fetchone()
        if userupdate:
            email = form.email.data
            parola = sha256_crypt.hash(str(form.parola.data))
            cursor_filtrare = mysql.connection.cursor()
            update = cursor_filtrare.execute("update utilizatori SET email=%s, parola=%s where id=%s",(email, parola, schimbare_parola))
            if update:
                print('Parola schimbata cu succes', 'success')
                return render_template('contul_meu.html', userupdate=userupdate, form=form)
            else:
                flash('Reincearca', 'danger')
    return render_template('contul_meu.html', userupdate=userupdate, form=form)


bot = ChatBot("UBD")
bot = ChatBot(name='UBD', read_only=True,)
trainer = ListTrainer(bot)
trainer.train(['Site?', 'Drone'])

corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.custom.romana')
trainer.export_for_training('./reguli.json')

@app.route("/")
def acasa():    
    return render_template("acasa2.html") 
@app.route("/raspuns")
def raspuns_bot():    
    mesajutilizator = request.args.get('obtine_mesaj')    
    return str(bot.get_response(mesajutilizator)) 




if __name__ == '__main__':
    app.run(debug=True)
