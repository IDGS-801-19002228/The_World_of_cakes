from flask import Blueprint, redirect, render_template, request, url_for
from proveedor import insertProveedor,getallProveedor, searchProveedor, modificarProveedor, eliminarProveedor
import forms

#establecer el blueprint 
proveedor = Blueprint('proveedor',__name__)

@proveedor.route("/insertproveedor", methods=['GET','POST'])
def insertarpro():
    create_form = forms.proveedor(request.form)
    if request.method == 'POST':      
        nombre = create_form.nombre.data
        apellidos=create_form.apellidos.data
        correo= create_form.correo.data
        matricula= create_form.matricula.data
        
        insertProveedor.insertM(nombre,apellidos,correo,matricula)

        return redirect(url_for('maestros.ABCompletoProf'))
    return render_template('Profesores.html',form = create_form)

@proveedor.route("/modProveedor", methods=['GET','POST'])
def modificarProf():
    create_form = forms.proveedor(request.form)
    if request.method  =='GET':
        id = request.args.get('id')
        resultset= searchProveedor.searchPro(id)
        for row in resultset:
                create_form.id.data = id
                create_form.nombre.data = row[2]
                create_form.apellidos.data = row[3]
                create_form.correo.data = row[4]
        
    if request.method == 'POST':    
        id= create_form.id.data  
        nombre = create_form.nombre.data
        apellidos=create_form.apellidos.data
        correo= create_form.correo.data
            
        modificarProveedor.modificarPro(nombre,apellidos,id,correo)
        
        return redirect(url_for('maestros.ABCompletoProf'))
    return render_template('modificarPro.html',form = create_form)

@proveedor.route("/eliminarPro", methods=['GET','POST'])
def eliminarPro():
    create_form = forms.proveedor(request.form)
    if request.method  =='GET':
        id = request.args.get('id')
        resultset= searchProveedor.searchPro(id)
        for row in resultset:
                create_form.id.data = id
                create_form.nombre.data = row[2]
                create_form.apellidos.data = row[3]
                create_form.correo.data = row[4]
    if request.method == 'POST':    
        id= create_form.id.data  
        
        eliminarProveedor.eliminarPro(id)
        
        return redirect(url_for(''))
    return render_template('eliminarPro.html',form = create_form)

@proveedor.route("/activarPro", methods=['GET','POST'])
def activarPro():
    create_form = forms.proveedor(request.form)
    if request.method  =='GET':
        id = request.args.get('id')
        resultset= searchProveedor.searchPro(id)
        for row in resultset:
                create_form.id.data = id
                create_form.nombre.data = row[2]
                create_form.apellidos.data = row[3]
                create_form.correo.data = row[4]
    if request.method == 'POST':    
        id= create_form.id.data  
        
        eliminarProveedor.eliminarPro(id)
        
        return redirect(url_for(''))
    return render_template('eliminarPro.html',form = create_form)



@proveedor.route("/ABCompletoPro",methods=["GET","POST"])
def ABCompletoProf():
    create_formP = forms.prooveedor(request.form)
    resultset1 = getallProveedor.getallPro()
    print(resultset1)
    for row in resultset1:
         print(row)

    return render_template('ABCPro.html', form = create_formP, profesor = resultset1 ) 
