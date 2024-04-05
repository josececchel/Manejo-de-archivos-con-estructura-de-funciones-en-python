def lectura_notas(archivo):
    try:
        lista_alumnos=[]
        with open(archivo,"r") as dato:
            for i in dato:
                datos = i.strip().split(",")
                nombre = datos[0]
                materia = datos[1]
                nota1 = float(datos[2])
                nota2 = float(datos[3])
                lista_alumnos.append((nombre,materia,nota1,nota2))

        return lista_alumnos
    except FileNotFoundError:
        print("ERROR AL ENCONTRAR EL ARCHIVO, REINICIE EL SISTEMA")
    except FileExistsError:
        print("NO SE ENCONTRO EL ARCHIVO SOLICITADO")

def estado(nota1,nota2):
    promedio = (nota1 + nota2) / 2
    if promedio >= 8:
        estadodemateria = "Aprobado"
    elif promedio >= 6 : 
        estadodemateria = "Promocionado"
    else:
        estadodemateria = "Desaprobado"

    return estadodemateria

def escribir_archivo(lista_alumnos):
    try:
        with open("estados_alumnos.txt", "w") as archivo:
            archivo.write("Nombre, Materia, Nota 1, Nota 2, Estado\n")
            for alumno in lista_alumnos:
                nombre, materia, nota1, nota2 = alumno
                estado_materia = estado(nota1, nota2)
                archivo.write(f"{nombre}, {materia.upper()}, {nota1}, {nota2}, {estado_materia}\n")
        print("Se ha creado el archivo 'estados_alumnos.txt' exitosamente.")
    except IOError:
        print("Error al escribir el archivo.")


def main():
    
    print("BIENVENIDO, ESTE ES EL LISTADO DE ALUMNOS, MATERIAS Y SU ESTADO EN CADA UNA DE ELLAS")
    lista_alumnos = lectura_notas("archivo_notas.csv")
    if lista_alumnos:
        for alumno in lista_alumnos:
            nombre, materia, nota1, nota2 = alumno
            estado_materia = estado(nota1, nota2)
            print(f"Nombre: {nombre}, Materia: {materia}, Nota 1: {nota1}, Nota 2: {nota2}, Estado: {estado_materia}")
        escribir_archivo(lista_alumnos)
    else:
        print("No se encontraron datos de alumnos en el archivo.")


if __name__ == "__main__":
    main()