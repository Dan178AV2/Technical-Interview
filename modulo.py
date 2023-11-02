class Ponquesito:
    unit = 'c'

    def __init__(self,unit='c'):
        ''' unit = Unidad a usar que acepta como valor un string "c" para centigrados o "f" para Fahrenheit
            por defecto se le asigna el valor de centigrados, por lo que todas las transformaciones se haran
            a Fahrenheit '''
        self.unit = unit
    
    def __convertirCentigrados(self,value):
        ''' Convertir valor de Fahrenheit  a centigrados.
        
        value = number'''
        return (value - 32) * 5/9
    
    def __convertirFahrenheit (self,value):
        ''' Convertir valor de centigrados a Fahrenheit  

        value = number'''
        return (value*9/5)+32
    
    def transform(self,value):
        ''' Transforma un valor a la unidad establecida si la unidad acual
         es distinta a la unidad el valor.
          
           formato aceptado: 
           
           { "value":number, "unit": "c" | "f" } '''
        result = 0
        if self.unit == 'c':
            if value['unit']=='f':
                result = self.__convertirCentigrados(value['value'])
                return result
            else:
                result = value['value']
                return result
        else:
            if value['unit'] == 'c':
                result = self.__convertirFahrenheit (value['value'])
                return result
            else:
                result = value['value']
                return result