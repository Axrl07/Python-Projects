# importando libreria para el manejo del archivo .env
import os
from dotenv import load_dotenv
load_dotenv()
# importando libreria para la conexion con la base de datos
from pymongo import MongoClient

MONGODB_URI = os.getenv("MONGODB_URI")

cliente = MongoClient(MONGODB_URI)
listado_db = cliente.list_database_names()
db = cliente['ExamenFinal']

# insertando documentos a la coleccion "alumnos"
# lista = [
#     # {'nombre': ,'apellido': ,'asignatura': , 'nota final': ,'edad': ,'facultad de ingenieria': },
#     {'nombre': "Angel Enrique",'apellido': "Alvarado Ruiz",'asignatura': "IPC1", 'nota final': 40,'edad': 20,'facultad de ingenieria': "sistemas"},
#     {'nombre': "Juan Santiago",'apellido': "Revolorio Cruz",'asignatura': "MC2", 'nota final': 50,'edad': 21,'facultad de ingenieria': "industrial"},
#     {'nombre': "Diego Armando",'apellido': "Escobar Yugo",'asignatura': "INTER 2", 'nota final': 62,'edad': 22,'facultad de ingenieria': "mecanica"},
#     {'nombre': "Linda Julia",'apellido': "Mejia Gonzales",'asignatura': "INTER 3", 'nota final': 15,'edad': 23,'facultad de ingenieria': "electrica"},
#     {'nombre': "Hellen Geisel",'apellido': "Rizcoxot",'asignatura': "PY INTER", 'nota final': 26,'edad': 25,'facultad de ingenieria': "electronica"},
#     {'nombre': "Emilio Gabriel",'apellido': "Yurrita Sandoval",'asignatura': "MC2", 'nota final': 37,'edad': 26,  'facultad de ingenieria': "sistemas"},
#     {'nombre': "Roberto Alexander",'apellido': "Garcia Marquez",'asignatura': "IPC2", 'nota final': 88,'edad': 24,  'facultad de ingenieria': "civil"},
#     {'nombre': "Vanessa Julissa",'apellido': "Perez Goto",'asignatura': "IPC2", 'nota final': 100,'edad': 20,  'facultad de ingenieria': "agraria"},
#     {'nombre': "Valeria Salome",'apellido': "Arreaga Maldonado",'asignatura': "LOGICA", 'nota final': 46,'edad': 24,  'facultad de ingenieria': "civil"},
#     {'nombre': "Fernanda Maria",'apellido': "Quintanilla Xolt",'asignatura': "IPC2", 'nota final': 92,'edad': 23,  'facultad de ingenieria': "agraria"},
# ]

listado_collec = db.list_collection_names()
collec = db['alumnos']
#result = collec.insert_many(lista)

# eliminando a Angel Enrique y Vanessa Julissa
'''
filtroEmpty = {"edad": 20}
collec.delete_many(filter=filtroEmpty)
print(listado_collec)
'''

# insertando a Angel Enrique
'''
result = collec.insert_one({'nombre': "Angel Enrique",'apellido': "Alvarado Ruiz",'asignatura': "IPC1", 'nota final': 0,'edad': 20,'facultad de ingenieria': "sistemas"},)
'''
# actualizando a Angel Enrique
'''
filtro = {'nombre': "Angel Enrique"}
updateNota = {"$set": {'nota final': 100, 'edad': 18, 'asinatura': "APLICADA 3"}}
result = collec.update_one(filtro, updateNota)
'''



# Imprimiendo db, colec y documentos insertados
busquedaGeneral = collec.find()
for doc in busquedaGeneral:
    print(doc)
print(listado_db)


