def main():
    edad = int(input("Ingresa tu edad: "))
    # Escribe el código adecuado para completar el programa
    # Para pedir el dato de la idetificación oficial emplea este mensaje:
    # "¿Tienes identificación oficial? (s/n): "

    if(edad>=18):
       sino = input('¿Tienes identificación oficial? (s/n): ')
       if(sino=="s"):
           print('Trámite de licencia concedido')
       elif(sino=="n"):
           print('No cumples requisitos')
       else:
           print('Respuesta incorrecta')  
    elif(edad<18):
        print('No cumples requisitos')
    elif(edad<0):
        print('Respuesta incorrecta')

    pass

if __name__ == '__main__':
    main()
