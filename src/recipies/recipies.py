'''
Created on 22/10/2013

@author: alejandrolarosa@gmail.com
'''
import itertools
JOKER_INGREDIENT  = 'masita'

class Recipe():
    
    def existIngredient(self,permutation):
        iterPermutation = iter(permutation)
        if JOKER_INGREDIENT in iterPermutation:
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

    def validateHorizontalOrder(self,permutation):
        if self.validateIngredientVector(permutation[0:3]):
            if self.validateIngredientVector(permutation[3:6]):
                if self.validateIngredientVector(permutation[6:9]):
                    return True
        return False
    
    def createMatrix(self,permutation):
        iterPermutation = iter(permutation)
        matrix = [[None for _ in range(3)] for _ in range(3)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j]=next(iterPermutation)
        return matrix
    
    def transplant(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        return [[matrix[j][i] for j in xrange(rows)] for i in xrange(cols)]

    def validateVerticalOrder(self,permutation):
        matrix = self.createMatrix(permutation)
        matrixTransplant = self.transplant(matrix)
        permutationTransplant = []
        for i in range(len(matrixTransplant)):
            for j in range(len(matrixTransplant[i])):
                permutationTransplant.append(matrixTransplant[i][j])
        return self.validateHorizontalOrder(permutationTransplant)
    
if __name__ == '__main__':
    setRecipe = set()
    recipe = Recipe()
    ingredients = ['dulce','dulce','dulce','confite','confite','confite','fruta','fruta','fruta','masita']
    for permutation in itertools.permutations(ingredients, 9):
        validPermutation = None
        if recipe.existIngredient(permutation):
            if recipe.validateHorizontalOrder(permutation):
                validPermutation= permutation
            elif recipe.validateVerticalOrder(permutation):
                validPermutation= permutation
        if validPermutation:
            setRecipe.add(validPermutation)
            validPermutation=None
    for recipe in setRecipe:
        print recipe
    print len(setRecipe)
    pass

