# Definition d un noeud
class Node:

	 def __init__(self, val):
	     # Construction d un noeud a  partir d'une valeur

		self.left = None    # Le noeud de gauche
		self.right = None   # Le noeud de droite
		self.value = val    # La valeur du noeud



# Definition d'un arbre
class Tree:

	 def __init__(self, node):
	     # Construction d un arbre a  partir de sa racine

		self.root = node



# Definition d un arbre de recherche ABR
class RechercheAbr:

	def __init__(self,tree,val):
	    # Construction d un ABR, a partir d un arbre et d une valeur donnee

		self.arbre = tree
		self.value = val


	def chercher(self):
    	    # La methode qui permet de determiner si la valeur de l ABR existe dans l arbre de l ABR.
           
                result = False
		# Si valeur recherchee est celle du noeud
		if (self.arbre.root.value == self.value):
                      	result = True
		# Sinon on explore les deux sous arbres, de gauche et de droite.
		else:
                	resultG = False #resultat de l arbre fils de gauche
			resultD = False # resultat de l arbre fils de droite
			if (self.arbre.root.left != None):
				arbreG = RechercheAbr(Tree(self.arbre.root.left),self.value)
				resultG = arbreG.chercher()
			if (self.arbre.root.right != None):
				arbreD = RechercheAbr(Tree(self.arbre.root.right),self.value)
				resultD = arbreD.chercher()
			result = resultG or resultD # Resultat final = combinaison des deux resultats gauche et droite.
	        # On retourne le resultat final
		return result


	def run(self):
	     # La methode qui fait appel a la methode (chercher)

		self.chercher()



# Determination des classes du fichier
def get_classes():
    # La methode retourne le nom
	return [Node,Tree,RechercheAbr]
