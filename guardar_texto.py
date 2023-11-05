import pickle 
#a = "Texto de ejemplo" 
                         

#with open ("texto1.pickle","wb") as file:
   # pickle.dump(a,file)

with open ("texto1.pickle","rb") as file:
    texto=pickle.load(file)

print(texto)

#Primero habría que ejecutar el código puesto como comentario
#después el que no está como comentario