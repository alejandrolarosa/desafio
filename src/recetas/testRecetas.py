'''
Created on 30/10/2013

@author: root
'''
import unittest
from recetas import Receta


class Test(unittest.TestCase):


    def testCreateMatrix(self):
        receta = Receta()
        combination=('dulce','dulce','dulce','confite','confite','confite','fruta','fruta','masita')
        result= receta.createMatrix(combination)
        assert result == [['dulce', 'dulce', 'dulce'], ['confite', 'confite', 'confite'], ['fruta', 'fruta', 'masita']]
        pass
    
    def testExistJoker(self):
        receta = Receta()
        combination=('dulce','dulce','dulce','confite','confite','confite','fruta','fruta','masita')
        result= receta.existIngredient(combination)
        assert result == True
        pass
    
    def testTransplant(self):
        receta = Receta()
        combination=('dulce','dulce','dulce','confite','confite','confite','fruta','fruta','masita')
        matrix = receta.createMatrix(combination)
        result= receta.transplant(matrix)
        assert result == [['dulce', 'confite', 'fruta'], ['dulce', 'confite', 'fruta'], ['dulce', 'confite', 'masita']]
        pass
    
    def testValidateIngredient(self):
        receta = Receta()
        combination=('dulce','dulce','dulce','confite','confite','confite','fruta','fruta','masita')
        vector = combination[6:9]
        result =receta.validateIngredient(vector[0], vector[1])
        assert result == True
        
        result =receta.validateIngredient(vector[0], vector[2])
        assert result == True
        
        
    def testValidateIngredientVector(self):
        receta = Receta()
        combination=('dulce','dulce','dulce','confite','confite','confite','fruta','fruta','masita')
        result = receta.validateIngredientVector(combination[0:3])
        assert result == True
        
        result = receta.validateIngredientVector(combination[3:6])
        assert result == True
        print combination[6:9]
        result = receta.validateIngredientVector(combination[6:9])
        assert result == True
        pass
    
    def testValidateHorizontalOrder(self):
        receta = Receta()
        combination=('dulce','dulce','dulce','confite','confite','confite','fruta','fruta','masita')
        result = receta.validateHorizontalOrder(combination)
        assert result == True
        pass
    
    def testValidateVerticalOrder(self):
        receta = Receta()
        combination=('dulce','confite','fruta','dulce','confite','fruta','dulce','confite','masita')
        result = receta.validateVerticalOrder(combination)
        assert result == True
        pass
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()