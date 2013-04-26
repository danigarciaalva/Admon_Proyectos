def edlinea():
	texto = []
	print ':'
	linea = raw_input()
	c1 = linea[0]
	c2 = linea[1:]
	while c1 != 'q':
		if c1 == 'p':
			if len(c2) == 0:
				print 'Desplegar texto actual'
				for i, item in enumerate(texto):
					print '{}: {}'.format(i,item)
			else:
				n = int(c2)
				for i, item in enumerate(texto):
					if i == n-1:
						print '{}:{}'.format(n, item)
						break
	print 'Termina sesion de edicion'
	return (0)
	
if __name__ == '__main__':
	edlinea()
