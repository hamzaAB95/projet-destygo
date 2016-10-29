# Methode de calcul 1
class FiboOne: 

	def __init__(self,n):
	  # Construction du seuil du calcul de la somme de Fibonacci
		self.n = n


	def fiboOne(self):
	  # Calcul du terme n de la suite de Fibonacci de maniere recursive
          # Analyse de la performance sans compter le calcul de la somme: Stockage =  1 terme = o(n) (petit tho)
          #                                                               Appels recurrents =   2 puissance(n)  (complexite non acceptable)  

		# Cas des deux premiers termes
		if(self.n==0):
			valeur = 0
                elif(self.n==1):
			valeur = 1
		else:
			#Calcul de fibo(n) suivant la formule donnee.
                        pred1 = FiboOne(self.n-1)
                        pred2 = FiboOne(self.n-2)
			valeur = pred1.fiboOne() + pred2.fiboOne()
		return valeur

 
        def sommeOne(self):
	   # Calcul de la somme de n termes de la suite de Fibonacci
		i = 0
                somme = 0
         	while (i<=self.n):
 			objet = FiboOne(i)
			somme = somme + objet.fiboOne()
                        i=i+1
                return somme
	

	def run(self):
	  # Methode intermediaire qui fait appel a sommeOne
		self.sommeOne()


# Methode de calcul 2
class FiboTwo:

	def __init__(self,n):
          # Construction du seuil du calcul de la somme de Fibonacci 
		self.n = n


	def fiboTwo(self):
	  # Calcul du terme n de la suite de Fibonacci de maniere iterative
          #  Analyse de la performance sans compter le calcul de la somme: Stockage = 3 termes = o(n) (petit tho)
          #                                                                Operations = 3*n  operations = O(n) (grand tho) 

		# cas de fibo(0) et fibo(1): resultat immediat.
		if(self.n==0):
                        valeur = 0
                elif(self.n==1):
                        valeur = 1
                else: 	
			#calcul des termes suivants en utilisant la formule donnee.
			i = 2  
               	        valeurp = 1     # c est fibo(i-1)
               	        valeurpp = 0    # c est fibo(i-2)
               	        while(i<=self.n):
				#calcul de fibo(i)
 				valeur = valeurp + valeurpp 
				#mise a jour des varibles
				valeurpp = valeurp  
                       	        valeurp = valeur 
                                i = i+1  
		return valeur

	
	def sommeTwo(self):
	  # Calcul de la somme de n termes de la suite de Fibonacci
                i = 0
                somme = 0
                while (i<=self.n):
                        objet = FiboTwo(i)
                        somme = somme + objet.fiboTwo()
			i=i+1
                return somme


	def run(self):
	  #  Methode intermedaire qui fait appel a sommeTwo
		self.sommeTwo()



# Methode de calcul3        
class FiboThree:

	def __init__(self,n):
	   # Construction du seuil du calcul de la somme de Fibonacci
		self.n = n


	def sommeThree(self):
	  # Calcul de la somme de  n termes de la suite de Fibonacci en utilisant les listes 
          # Analyse de la performance sans compter le calcul de la somme: Stockage = n termes = O(n) (grand tho)
	  #                                                               Operations = n  operations = O(n) 

		# initiaisation de la liste avec les deux premiers termes
		listFibo = [0,1]
                i=2
		# ajout des termes suivant a la liste
        	while (i<=self.n):
			listFibo.append(listFibo[i-2]+listFibo[i-1])
		#calcul de la somme des termes de la liste	
		i=i+1
		i=0
		somme=0
		while(i<len(listFibo)):
                     somme = somme + listFibo[i]
                     i=i+1
 		return somme


	def run(self):
	  # Methode intermedaire qui fait appel a sommeThree 
		return self.fiboThree()



# Methode qui renvoie les classes contenues dans le fichier 
def get_classes():
    return [FiboOne,FiboTwo,FiboThree] 
