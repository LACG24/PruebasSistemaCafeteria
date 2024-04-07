#Luis Angel Cruz Garcia 07/04/2024

#Funcion encargada de emular el manejo del ingreso de nuevas bebidas
#validando diferentes elementos del producto
def agrega_bebida(registro):
    registro_junto = registro.replace(" ","") #Se eliminan espacios
    datos = registro_junto.split(",") #Se guardan los elementos en una lista
    
    if len(datos) < 2 or len(datos) > 6: #Se verifica que se agreguen entre 1 y 5 tamaños
        return False
    elif not datos[0].isalpha(): #Se verifica que el nombre sea alfabetico
        return False
    elif len(datos[0]) < 2 or len(datos[0]) > 15: #Se verifica que el nombre tenga entre 2 y 15 caracteres
       return False
    
    #Se utiliza la funcion map y funciones anonimas para verificar las condiciones en todos los tamaños
    elif not all(map(lambda x: x.isdigit(), datos[1:])): #Se verifica que los tamaños sean numeros enteros
        return False
    elif not all(map(lambda x, y: int(x) < int(y), datos[1:-1], datos[2:])): #Se verifica que los tamaños esten ordenados asc
        return False
    elif not all(map(lambda x: (int(x) >= 1 and int(x) <= 48), datos[1:])): #Se verifica que los tamaños esten entre 1 y 48
        return False
    
    else: #Si cumple con todas las condiciones es una entrada valida
        return True
    
#Funcion encargada de guardar los casos para el testeo
#Se ejecutan con pytest
def test_answer():
    
    #1. Verifica nombre alfabetico
    #Nombre con números 
    assert agrega_bebida("a09234,1,2,3,4") == False
    #Nombre alfabético 
    assert agrega_bebida("refresco,2,3,14,20") == True 
    #Nombre con números y letras 
    assert agrega_bebida("x127aaj,2,3,14,20") == False 

    #2. El nombre del artículo tiene de 2 a 15 caracteres de longitud 
    #Nombre con un caracter 
    assert agrega_bebida("a,1,2,3,4") == False
    #Nombre con 15 caracteres (válido)
    assert agrega_bebida("abcdefghijklmno,1,2,3,4") == True
    #Nombre con 2 caracteres (válido)
    assert agrega_bebida("ab,1,2,3,4") == True
    #Nombre con 16 caracteres 
    assert agrega_bebida("abcdefghijklmnop,1,2,3,4") == False
    #Nombre con caracter vacio 
    assert agrega_bebida(" ,1,2,3,4") == False
    
    #3. El valor de los tamaños está en el rango de 1 a 48
    #Valores en el rango y limite inferior
    assert agrega_bebida("refresco,1,2,3,4") == True
    #Limite superior
    assert agrega_bebida("agua,40,48") == True
    #Valores que incluyan 0
    assert agrega_bebida("refresco,0,2,3,4") == False
    #Valores que sean mayores al rango
    assert agrega_bebida("refresco,49,50") == False
    #Valores negativos
    assert agrega_bebida("refresco,-3,-5") == False

    #4. El valor del tamaño es un número entero 
    #Recibir un numero entero
    assert agrega_bebida("agua,10") == True
    #Recibir un numero decimal
    assert agrega_bebida("refresco,1.5,2,3,4") == False
    #Recibir un string
    assert agrega_bebida("refresco,abc,2,3,4") == False

    #5. Los valores del tamaño se ingresan en orden ascendente 
    #Valores ordenados asc
    assert agrega_bebida("agua,10,11,12,13") == True
    #Valores ordenados des
    assert agrega_bebida("agua,13,12,11,10") == False
    #Valores sin ordenar
    assert agrega_bebida("refresco,4,3,5,1") == False
    
    #6. Se ingresan de uno a cinco valores de tamaño 
    #Agregar un tamaño
    assert agrega_bebida("refresco,1") == True
    #Agregar 5 tamaños
    assert agrega_bebida("agua,10,11,12,13,22") == True
    #No agregar ningun tamaño
    assert agrega_bebida("refresco") == False
    #Agregar mas de 5 tamaños
    assert agrega_bebida("agua,10,11,12,13,14,20") == False

    #7. El nombre del artículo es el primero en la entrada 
    #Agregar un nombre correcto
    assert agrega_bebida("refresco,1,2,3,4") == True
    #Agregar el nombre despues de un tamaño
    assert agrega_bebida("1,refresco,2,3,4") == False

    #8. Una sola coma separa cada entrada en la lista 
    #Usar una sola coma
    assert agrega_bebida("refresco,31,32,33,34") == True
    #Agregar dos comas en un elemento
    assert agrega_bebida("refresco,1,,2,3,4") == False
    #Usar otro caracter para separar(|)
    assert agrega_bebida("agua|10|11|12|13") == False

    #9. Se ignoran los espacios en blanco
    #Usar espacios en el nombre
    assert agrega_bebida("agua gas,1,2,3,4") == True
    #Usar espacios en los tamaños
    assert agrega_bebida("agua,1 0,11,12,1  3") == True

    #10. Otros casos
    #No ingresar ningun valor
    assert agrega_bebida("") == False
    #Ingresar tamaños iguales
    assert agrega_bebida("agua,11,11,11,11,11") == False