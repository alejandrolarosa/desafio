'''
Created on 30/10/2013

@author: root
'''
import unittest
from recipies import Recipe


class Test(unittest.TestCase):


    def testCreateMatrix(self):
        recipe = Recipe()
        combination=('dulce','dulce','dulce','confite','confite','confite','fruta','fruta','masita')
        result= recipe.createMatrix(combination)
        assert result == [['dulce', 'dulce', 'dulce'], ['confite', 'confite', 'confite'], ['fruta', 'fruta', 'masita']]
        pass
    
    def testExistJoker(self):
        recipe = Recipe()
        combination=('dulce','dulce','dulce','confite','confite','confite','fruta','fruta','masita')
        result= recipe.existIngredient(combination)
        assert result == True
        pass
    
    def testTransplant(self):
        recipe = Recipe()
        combination=('dulce','dulce','dulce','confite','confite','confite','fruta','fruta','masita')
        matrix = recipe.createMatrix(combination)
        result= recipe.transplant(matrix)
        assert result == [['dulce', 'confite', 'fruta'], ['dulce', 'confite', 'fruta'], ['dulce', 'confite', 'masita']]
        pass
    
    def testValidateIngredient(self):
        recipe = Recipe()
        combination=('dulce','dulce','dulce','confite','confite','confite','fruta','fruta','masita')
        vector = combination[6:9]
        result =recipe.validateIngredient(vector[0], vector[1])
        assert result == True
        
        result =recipe.validateIngredient(vector[0], vector[2])
        assert result == True
        
        
    def testValidateIngredientVector(self):
        recipe = Recipe()
        combination=('dulce','dulce','dulce','confite','confite','confite','fruta','fruta','masita')
        result = recipe.validateIngredientVector(combination[0:3])
        assert result == True
        
        result = recipe.validateIngredientVector(combination[3:6])
        assert result == True
        print combination[6:9]
        result = recipe.validateIngredientVector(combination[6:9])
        assert result == True
        pass
    
    def testValidateHorizontalOrder(self):
        recipe = Recipe()
        combination=('dulce','dulce','dulce','confite','confite','confite','fruta','fruta','masita')
        result = recipe.validateHorizontalOrder(combination)
        assert result == True
        pass
    
    def testValidateVerticalOrder(self):
        recipe = Recipe()
        combination=('dulce','confite','fruta','dulce','confite','fruta','dulce','confite','masita')
        result = recipe.validateVerticalOrder(combination)
        assert result == True
        pass
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()