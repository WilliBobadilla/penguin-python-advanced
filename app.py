#app.py

from flask import Flask, request #import main Flask class and request object


import csv 
app = Flask(__name__) #create the Flask app

@app.route('/')
def query_example():
    return 'Probandooooooo'

@app.route('/nombres')
def lectura():
    try: 
        lista_nombre=[]
        lista_apellido=[]
        with open('datos_nuevos.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f' {", ".join(row)}')
                    line_count += 1
                print(f'\t{row["temperatura"]} es {row["fecha"]}')
                line_count += 1
            print(f'procesado {line_count} lineas')
            lista_nombre.append(row["temperatura"])
            lista_apellido.append(row["fecha"])
    except FileNotFoundError: # manejo el error
        print("archivo no encontrado")
    return "  <h1> Nombre, Apellido</h1> " + str(lista_nombre)
    



@app.route('/form-example',methods = ['POST'])
def formexample():
    if request.method == 'POST':
        nombre = request.form["nombre"]
        apellido=request.form["apellido"]
    with open("datos_nuevos.csv","a+") as data_temp_csv:
        # agregar lo de leer si es que ya esta escrito open
        # la cabecera, la posible solucion es de abrir el 
        #archivo y verificar si es que ya esta o no 
        nombrefilas= ["Nombre","Apellido"]  # nombre de los campos
        writer=csv.DictWriter(data_temp_csv,fieldnames=nombrefilas) # creamos un objeto writer sobre el archivo, y le especificamos el nombre de kis campos
        #writer.writeheader() #escribimos la primera

        writer.writerow({'Nombre' : nombre, 'Apellido':apellido})

    return '<h2> Recibido!  </h2>'

@app.route('/json')
def jsonexample():
    return 'Todo...'

if __name__== '__main_':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000