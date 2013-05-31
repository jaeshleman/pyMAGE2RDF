'''
Created on 03 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''

class OntologyEntry(object):
    '''Ontology entry description
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.category = None
        self.description = None
        self.value = None
        
    def setCategory(self, category):
        self.category = category
    
    def setValue(self, value):
        self.value = value
        
    def setDescription(self, description):
        self.description = description
        
    def getValue(self):
        return self.value
    
    def getCategory(self):
        return self.category
    
