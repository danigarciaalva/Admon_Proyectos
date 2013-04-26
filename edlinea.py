#!/usr/bin/env python
# coding: iso-8859-1
def edlinea():
    # lista vacia que almacenará el texto a editar.
    texto = []
    # depliega un mensaje y el prompt del editor
    print 'Bienvenido al editor de líneas edlinea versión 0.1'
    print ':',
    linea = raw_input()   # linea = lee_linea de caracteres
    c1 = linea[0].lower() # c1 = linea[0] en minúscula
    c2 = linea[1:]        # c2 = resto(linea)
    while c1 != 'q':
        if c1 == 'p':
            if len(c2) == 0:
                print 'Desplegar texto actual'
                for i, l in enumerate(texto):
                    print '{}: {}'.format(i, l)
            else:
                n = int(c2)
                print 'Desplegar linea {}'.format(n)
                for i, l in enumerate(texto):
                    if i == n:
                        print '{}: {}'.format(i, l)
                        break
        elif c1 == 'n':
			if len(c2) == 0:
				print 'Nueva linea:',
				nuevalinea = raw_input()
				texto.append(nuevalinea)
			else:
				n = int(c2)
				if n < len(texto):
					print 'Editar linea {}'.format(c2)
					nuevalinea = raw_input()
					texto[n] = nuevalinea
				else:
					print 'La linea {} no existe'.format(n)
        elif c1 == 'd' and len(c2) > 0:
            n = int(c2)
            if n < len(texto):
                del texto[n]
                print 'Linea {} borrada'.format(n)
            else:
                print 'La linea {} no existe'.format(n)
        elif c1 == 'f' and len(c2) > 0:
            if not '%' in c2:
                print 'La cadena a buscar debe indicarse entre "%"'
            else:
                cadenaABuscar = c2.split('%')[1]
                print 'Buscando cadena {}'.format(cadenaABuscar)
                for i, l in enumerate(texto):
                    if cadenaABuscar in l:
                        print '{}: {}'.format(i, l)
        elif c1 == 's' and len(c2) > 0:
            print 'Intercambiar líneas'
            if not ',' in c2:
                print ('Debe indicar las líneas a intercambiar separadas por ","')
            else:
                c2 = c2.split(',')
                l1 = int(c2[0])
                l2 = int(c2[1])
                if l1 > len(texto) or l2 > len(texto):
                    print 'Al menos una de las líneas indicadas no existe'
                else:
                    ltemp = texto[l1]
                    texto[l1] = texto[l2]
                    texto[l2] = ltemp
        elif c1 == 'r' and len(c2) > 0:
			print 'Abrir archivo'
			b = False
			try:
				f = open(c2.strip(),'r')
				texto = []
				while True:
					linea = f.readline()
					texto.append(linea)
					if not linea:
						break
				b = True
				f.close()
			except IOError:
				print 'El archivo no existe, favor de verificar'
			if b == True:
				print 'Archivo abierto exitosamente'
        elif c1 == 'w' and len(c2) > 0:
			print 'Guardar archivo'
			b = False
			try:
				f = open(c2.strip(),'w')
				for linea in texto:
					f.write(linea+"\n")
				b = True
				f.close()
			except IOError:
				print 'El archivo no existe, favor de verificar'
			if b == True:
				print 'Archivo guardado exitosamente'
			
        else:
            print 'Comando desconocido'
        print ':',  # despliega el prompt
        linea = raw_input()
        c1 = linea[0].lower()
        c2 = linea[1:]
    print 'Termina sesión de edición'
    return(0)

if __name__ == '__main__':
    edlinea()



def main():
	
	return 0

if __name__ == '__main__':
	main()

