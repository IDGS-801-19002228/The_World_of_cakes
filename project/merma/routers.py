from flask import Blueprint, redirect, render_template, request, url_for
from merma import insertarMerma,searchMerma,getAllMerma
import forms

#establecer el blueprint 
merma = Blueprint('merma',__name__)

@merma.route("/insertmerma", methods=['GET','POST'])
def insertarmerma():
    create_form = forms.merma(request.form)
    if request.method == 'POST':      
        nombre = create_form.nombre.data
        apellidos=create_form.apellidos.data
        correo= create_form.correo.data
        matricula= create_form.matricula.data
        
        insertarMerma.insertarM(nombre,apellidos,correo,matricula)

        return redirect(url_for('maestros.ABCompletoProf'))
    return render_template('Profesores.html',form = create_form)


@merma.route("/ABCompletoMerma",methods=["GET","POST"])
def ABCompletoMerma():
    create_formP = forms.merma(request.form)
    resultset1 = getAllMerma.getallM()
    print(resultset1)
    for row in resultset1:
         print(row)

    return render_template('ABCPro.html', form = create_formP, profesor = resultset1 ) 
