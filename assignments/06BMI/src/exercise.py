def main():
    # Escribe el código adecuado para completar el programa
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    imc = float

    if(peso>0)&(altura>0):
        imc = peso/(altura**2)
        if(imc<20):
            print('PESO BAJO')
        elif(20<=imc)&(imc<25):
            print('NORMAL')
        elif(25<=imc)&(imc<30):
            print('SOBREPESO')
        elif(30<=imc)&(imc<40):
            print('OBESIDAD')
        elif(imc>=40):
            print('OBESIDAD MORBIDA')

    elif((peso<=0)or(altura<=0)):
        print('Revisa tus datos, alguno de ellos es erróneo.')

    pass
if __name__ == '__main__':
    main()
