edad = int(input("Introduzca la edad: "))

if edad < 0:
    print("Ingrese una edad valida") 
else:
    entrada = 10000
    dia_semana = input("Ingrese a dia de la semana:")

    if edad < 2:
        desc = 100
    else:
        if dia_semana.lower() != "lunes":
            if edad <= 5:
                desc = 50
            elif edad <= 10:
                desc =20
            elif edad < 55:
                desc = 0
            else: # para edad mayor a 55 años
                sexo = input("Ingrese el genero (M o F): ")
                if (sexo.upper() == "M" and edad >= 65) or (sexo.upper() == "F"):
                    desc = 30
                else:
                    descuento = 0

            if desc < 30:
                estudiante = input("Es estudiante (si o no):")
                if estudiante.lower() == "si":
                    desc = 25
        else:
            desc = 50

    if desc != 0:
        monto_desc = entrada * desc / 100
        print(f"El porcentaje de descuento es: {desc}")
        print(f"El monto del descuento es: {monto_desc}")
    else:
        print("No te corresponde descuento")
        monto_desc = 0

    monto_final = entrada - monto_desc
    
    print(f"El monto total a pagar es: {monto_final}")