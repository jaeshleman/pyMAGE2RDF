'''
Created on 18 Jul,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
#import sys
from Identifiable import Identifiable


class ParameterList(Identifiable):
    def __init__(self):
        '''
        Constructor
        '''
        Identifiable.__init__(self)
    
    def processSubSection(self, *args, **kwargs):
        try:
            Identifiable.processSubSection(self, subClass = Parameter, subClassKey = "Parameter")#, nodes = nodes)
        except: pass
        self.assessAttributes()
        self.internalGraph()
    
    def internalGraph(self, *args, **kwargs):
        Identifiable.noInteralGraph(self)
    
class Parameter(Identifiable):
    '''Parameter class, generally a component of a protocol step
    '''
    def processSubSection(self, *args, **kwargs):
        '''Terminal.  The parameter is last in chain'''
        self.assessAttributes()
        if hasattr(self, 'parentNode'):
            try:
                self.parameterValue = self.parentNode.value
                self.attributeList.append('parameterValue')
            except: 
                pass
        self.getOntologyEntries()
        self.internalGraph()

        