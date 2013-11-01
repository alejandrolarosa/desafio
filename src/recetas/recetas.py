'''
Created on 22/10/2013

@author: alejandrolarosa@gmail.com
'''
import itertools
JOKER_INGREDIENT  = 'masita'

class Receta():
    
    def existIngredient(self,combination):
        iterCombination = iter(combination)
        if JOKER_INGREDIENT in iterCombination:
            return True
        return False

    def validateIngredient(self,ingredientA,ingredientB):
        if ingredientA == ingredientB or ingredientA == JOKER_INGREDIENT or ingredientB == JOKER_INGREDIENT:
            return True
        return False

    def validateIngredientVector(self,vector):
        if self.validateIngredient(vector[0],vector[1]):
            if self.validateIngredient(vector[0],vector[2]):
                return True
        return False

    def validateHorizontalOrder(self,combination):
        if self.validateIngredientVector(combination[0:3]):
            if self.validateIngredientVector(combination[3:6]):
                if self.validateIngredientVector(combination[6:9]):
                    return True
        return False
    
    def createMatrix(self,combination):
        iterPermutation = iter(combination)
        matrix = [[None for _ in range(3)] for _ in range(3)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j]=next(iterPermutation)
        return matrix
    
    def transplant(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        return [[matrix[j][i] for j in xrange(rows)] for i in xrange(cols)]

    def validateVerticalOrder(self,combination):
        matrix = self.createMatrix(combination)
        matrixTransplant = self.transplant(matrix)
        combinationTransplant = []
        for i in range(len(matrixTransplant)):
            for j in range(len(matrixTransplant[i])):
                combinationTransplant.append(matrixTransplant[i][j])
        return self.validateHorizontalOrder(combinationTransplant)
    
if __name__ == '__main__':
    setRecetas = set()
    receta = Receta()
    ingredientes = ['dulce','dulce','dulce','confite','confite','confite','fruta','fruta','fruta','masita']
    for permutation in itertools.permutations(ingredientes, 9):
        validPermutation = None
        if receta.existIngredient(permutation):
            if receta.validateHorizontalOrder(permutation):
                validPermutation= permutation
            elif receta.validateVerticalOrder(permutation):
                validPermutation= permutation
        if validPermutation:
            setRecetas.add(validPermutation)
            validPermutation=None
    for receta in setRecetas:
        print receta
    print len(setRecetas)
    pass

