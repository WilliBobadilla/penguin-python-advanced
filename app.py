#app.py

from flask import Flask, request , render_template #import main Flask class and request object


import csv 
app = Flask(__name__) #create the Flask app

@app.route('/')
def query_example():
    return 'Probandooooooo'
@app.route('/crear')
def crear():
    try:
        with open('datos_nuevos.csv', mode='r') as csv_file:
            nombre_columnas=['Nombre','Apellido']
            writer=csv.DictWriter(csv_file, fieldnames=nombre_columnas )
            writer.writeheader() #escribimos la cabecera
    except FileNotFoundError:
        return "archivo no encontrado"
    return "creado cabecera con exito"




@app.route('/nombres')
def lectura():
    try: 
        lista_nombre=[]
        lista_apellido=[]
        with open('datos_nuevos.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            print("entre aqui en el with")
            print(csv_reader)
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                print(row["Nombre"], " ----" ,row["Apellido"],"\n" ,"\n")
                line_count += 1
            print("lineas:",line_count)
            lista_nombre.append(str(row["Nombre"]) + str(row["Apellido"]))
        
            print("el tipo es", type(lista_nombre),"la li es:", lista_nombre)
            #string= " ".join(lista_apellido )
    except FileNotFoundError: # manejo el error
        print("archivo no encontrado")
        return  "NO HAY ARCHIVO"
    
    dic= { "Nombres":lista_nombre 
    
    }
    return render_template("alumnos.html", datos=dic)
    



@app.route('/form-example',methods = ['POST','GET'])
def formexample():
    if request.method == 'POST':
        nombre = request.form["nombre"]
        apellido=request.form["apellido"]
        print("este es el post", nombre,apellido )
        with open("datos_nuevos.csv","a") as data_temp_csv:
            # agregar lo de leer si es que ya esta escrito open
            # la cabecera, la posible solucion es de abrir el 
            #archivo y verificar si es que ya esta o no 
            nombrefilas= ["Nombre","Apellido"]  # nombre de los campos
            writer=csv.DictWriter(data_temp_csv,fieldnames=nombrefilas) # creamos un objeto writer sobre el archivo, y le especificamos el nombre de kis campos
            #writer.writeheader() #escribimos la primera

            writer.writerow({'Nombre' : nombre, 'Apellido':apellido})

        return '<h2> Recibido!  </h2>'
    else:
        return "no recibi nada"
        

@app.route('/json')
def jsonexample():
    return 'Todo...'

if __name__== '__main_':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000