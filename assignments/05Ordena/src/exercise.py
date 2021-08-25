def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))

    if(x<=y)&(x<=z):
        print(x)
        if(y<=z):
            print(y)
            print(z)
        else:
            print(z)
            print(y)
    if(y<=x)&(y<=z):
        print(y)
        if(x<=z):
            print(x)
            print(z)
        else:
            print(z)
            print(x)
    if(z<=y)&(z<=x):
        print(z)
        if(y<=x):
            print(y)
            print(x)
        else:
            print(x)
            print(y)
    
    pass
if __name__ == '__main__':
    main()
