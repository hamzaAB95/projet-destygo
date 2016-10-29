# Definition de la classe somme
class Somme:
   
 	def __init__(self,n):
	  #Definition du constructeur 
		 self.n = n


	def calculSomme(self):
	  # Methode qui calcul la somme de 1 a  n des multiples de 3 ou 5
		somme = 0
		i = self.n
		while (i>=0) : 
			if ((i%3)==0 or (i%5)==0):
				somme = somme+i
			i = i-1
		return somme


	def run(self):
	  # Methode intermediaire qui fait appel a calculSomme
		self.calculSomme()


# Fonction qui renvoie les classes du fichier
def get_classes():
    return [Somme]	 
