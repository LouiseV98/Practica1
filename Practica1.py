#funcion para convertir numeros hexadecimales a decimales
def hexadecimal_a_decimal(numero_hexadecimal):
    return int(numero_hexadecimal, 16)

#funcion para separar, convertir de hexadecimal a decimal y volver a unir los numeros
def ipv6_a_decimal(ipv6):
    lista_hexadecimal = ipv6.split(":")
    lista_en_decimal = [hexadecimal_a_decimal(comp) for comp in lista_hexadecimal]
    return ":".join(map(str, lista_en_decimal))

#funcion para mostrar la segunda cadena de texto del archivo
def sacar_texto(linea):
    texto = linea.split(",")
    posicion = 2
    texto_final = texto[posicion]
    return texto_final

#funcion para convertir numeros decimales a hexadecimales
def decimal_a_hexadecimal(decimal):
    cadena_decimal = int(decimal)
    hexadecimal_decimal = hex(cadena_decimal)[2:]
    hexadecimal_mayusculas = hexadecimal_decimal.upper()
    return hexadecimal_mayusculas

#funcion para separar, convertir numeros de decimal a hexadecimal y volver a unirlos
def ipv4_a_hexadecimal(linea):
    lista_decimal = linea.split(",")
    posicion = 5
    aux_lista_decimal = lista_decimal[posicion]
    lista_decimal_acomodada = aux_lista_decimal.split(".")
    lista_en_hexadecimal = [decimal_a_hexadecimal(numero_decimal) for numero_decimal in lista_decimal_acomodada] 
    return ".".join(map(str, lista_en_hexadecimal))

#orden para abrir el archivo en modo lectura
with open("prueba2.txt", "r") as archivo_lectura:
    lineas_archivo = archivo_lectura.readlines()

#orden para abrir el archivo en modo escritura
with open("prueba2.txt", "w") as archivo_escritura:
    for linea in lineas_archivo:

        ipv6_prefijo = linea.strip()
        ipv6, prefijo = ipv6_prefijo.split("/")

        direccionIpv6_Decimal = ipv6_a_decimal(ipv6)
        nombre_Persona = sacar_texto(linea)
        direccionIpv4_Hexadecimal = ipv4_a_hexadecimal(linea)

        archivo_escritura.write(nombre_Persona)
        archivo_escritura.write(":")
        archivo_escritura.write(direccionIpv6_Decimal)
        archivo_escritura.write(":")
        archivo_escritura.write(direccionIpv4_Hexadecimal)
        archivo_escritura.write("\n")
        
print("Convertido")