# Conectando al servidor
import os
from pymongo import MongoClient
from dotenv import load_dotenv

#cargo las variables de entorno
load_dotenv()

URI_MONGODB = os.environ.get("URI_MONGODB")

client = MongoClient(URI_MONGODB)

# forma 1 de crear la base de datos y la coleccion (diccionarios)
db = client['python_base1']     # creacion de la base de datos

collection = db['clientes']     # creacion de la coleccion

# forma 2 de crear la base de datos y la coleccion (objetos)
# db = client.python_base1
# collection = db.clientes


# lista de bases de datos
db_list = client.list_database_names()

# lista de colecciones en db
collection_list = db.list_collection_names()

# '''
# C = create/insert
# R = read
# U = update
# D = delete
# '''

'''
# INSERSION DE DATOS

# insersion de un dato
result = collection.insert_one({'nombre': "Angel Alvarado", "Direction": "Calle 1", "DPI": 202209714,"edad": 20})
print(result.inserted_id)

# insert_one: inserta un solo dato en la coleccion

# insersion de varios datos
values = [
    {'nombre': "Angel Alvarado", "Direction": "Guatemala", "DPI": 202209714,"edad": 20},
    {'nombre': "Alan Sacalxot", "Direction": "Mixco", "DPI": 202209715,"edad": 21},
    {'nombre': "Edgar Garcia", "Direction": "Peten", "DPI": 202209716,"edad": 22},
    {'nombre': "Rebeca Torres", "Direction": "Xelaju", "DPI": 202209717,"edad": 23},
    {'nombre': "Santiago Vasquez", "Direction": "Guatemala", "DPI": 202209718,"edad": 24},
]
result = collection.insert_many(values)

# insert_many: inserta varios datos en la coleccion
'''

'''
# LECTURA DE DATOS

# los datos son llamados tambien como documentos por eso ponemos doc
result = collection.find()
for doc in result:
    print(doc)

firma = {"edad": 20}        #creando FIRMA de datos: para buscar datos en especifico
# realizamos el proceso de clave=valor para buscar datos en especifico con filter=firma
result = collection.find(filter=firma)
for doc in result:
    print(doc)

filt  = {"edad": 20}        #creando FILTRO de datos: para buscar datos en especifico
# find_one : busca un solo dato en la coleccion, me devuelve el primer dato que encuentre
result = collection.find_one(filter=filt)
print(result)
'''

'''
filtroEmpty = {"edad": 20}
collection.delete_one(filter=filtroEmpty)
#delete_one: elimina un solo dato en la coleccion
#delete_many: elimina varios datos en la coleccion
'''

'''
filtro = {"DPI": 202209717}
upd = {"$set": {"nombre": "Dayan Bermudez","edad": 19}}
result = collection.update_one(filtro, upd)
# update_one & update_many tiene la misma logica que anteriormente
'''

# # muestra datos en base de datos 
# result = collection.find()
# for doc in result:
#     print(doc)