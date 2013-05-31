'''
Created on 18 Jul,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
import rdflib
from Describable import Describable

class Description(Describable):
    '''
    OBSOLETE -- dealt with as method within describable
    Description attributes:  text and URI
    '''
    def processSubSection(self, *args, **kwargs):
        self.assessAttributes()
        self.internalGraph()
     
    def internalGraph(self, *args, **kwargs):
        self.checkForGraph()
        for attribute in self.attributeList:
            try:
                self.graph.add(( self.parentNode.instance,
                                 self.parentNode.predNS['hasDescription'+str(attribute).capitalize()],
                                 rdflib.Literal(  ( vars(self).get(attribute) ) )
                                           ))
            except: pass
            try:
                self.ontologyEntryToGraph(self.parentNode.instance, self.parentNode.predNS)
            except: pass
        
            
   
        