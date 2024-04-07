#Funcion encargada de emular el manejo del ingreso de nuevas bebidas
#validando diferentes elementos del producto
def agrega_Bebida(registro):
    registro_junto = registro.replace(" ","") #Se eliminan espacios
    datos = registro_junto.split(",") #Se guardan los elementos en una lista
    
    if not datos[0].isalpha(): #Se verifica que el nombre sea alfabetico
        return False
    elif len(datos[0]) < 2 or len(datos[0]) > 15: #Se verifica que el nombre tenga entre 2 y 15 caracteres
       return False
    elif len(datos) < 2 or len(datos) > 6: #Se verifica que se agreguen entre 1 y 5 tamaños
        return False
    
    #En los siguiente casos se utiliza la funcion map y funciones anonimas 
    #para verificar las condiciones en todos los tamaños
    elif not all(map(lambda x: x.isdigit(), datos[1:])): #Se verifica que los tamaños sean numeros enteros
        return False
    elif not all(map(lambda x, y: int(x) <= int(y), datos[1:-1], datos[2:])): #Se verifica que los tamaños esten ordenados asc
        return False
    elif not all(map(lambda x: (int(x) >= 1 and int(x) <= 48), datos[1:])): #Se verifica que los tamaños esten entre 1 y 48
        return False
    
    else: #Si cumple con todas las condiciones es una entrada valida
        return True
    
#Funcion encargada de guardar los casos para el testeo
#Se ejecutan con pytest
def test_answer():
    
    #Verifica nombre alfabetico
    assert agrega_Bebida("09234,1,2,3,4") == False 
    assert agrega_Bebida("refresco,2,3,14,20") == True 

    #El nombre del artículo tiene de 2 a 15 caracteres de longitud 
    assert agrega_Bebida("a,1,2,3,4") == False
    assert agrega_Bebida("cafe,1,2,3,4") == True
    assert agrega_Bebida("abcdefghijklmnop,1,2,3,4") == False

    #El valor de los tamaños está en el rango de 1 a 48
    assert agrega_Bebida("refresco,1,2,3,4") == True
    assert agrega_Bebida("agua,40,48") == True
    assert agrega_Bebida("refresco,0,2,3,4") == False
    assert agrega_Bebida("refresco,49") == False

    #El valor del tamaño es un número entero 
    assert agrega_Bebida("refresco,1,2,3,4") == True
    assert agrega_Bebida("agua,10") == True
    assert agrega_Bebida("refresco,1.5,2,3,4") == False
    assert agrega_Bebida("refresco,abc,2,3,4") == False

    #Los valores del tamaño se ingresan en orden ascendente 
    assert agrega_Bebida("refresco,1,2,3,4") == True
    assert agrega_Bebida("agua,10,11,12,13") == True
    assert agrega_Bebida("refresco,4,3,2,1") == False
    assert agrega_Bebida("agua,13,12,11,10") == False

    #Se ingresan de uno a cinco valores de tamaño 
    assert agrega_Bebida("refresco,1") == True
    assert agrega_Bebida("agua,10,11,12,13") == True
    assert agrega_Bebida("refresco") == False
    assert agrega_Bebida("agua,10,11,12,13,14,20") == False

    #El nombre del artículo es el primero en la entrada 
    assert agrega_Bebida("refresco,1,2,3,4") == True
    assert agrega_Bebida("agua,10,11,12,13") == True
    assert agrega_Bebida("1,refresco,2,3,4") == False
    assert agrega_Bebida("10,agua,11,12,13") == False

    #Una sola coma separa cada entrada en la lista 
    assert agrega_Bebida("refresco,1,2,3,4") == True
    assert agrega_Bebida("agua,10,11,12,13") == True
    assert agrega_Bebida("refresco,1,,2,3,4") == False
    assert agrega_Bebida("agua,10 11,12,13") == False

    #Se ignoran los espacios en blanco
    assert agrega_Bebida("agua gas,1,2,3,4") == True
    assert agrega_Bebida("agua,1 1,11,12,13") == True
