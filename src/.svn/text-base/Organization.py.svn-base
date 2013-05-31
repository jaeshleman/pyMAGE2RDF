'''
Created on 03 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
from Contact import Contact
import rdflib

class Organization(Contact):
    '''Organization subclass of contact
    
    '''

    def __init__(self, *params):
        '''
        Constructor
        '''
        Contact.__init__(self)
        #self.instanceOfClass = 'http://mged.sourceforge.net/ontologies/MGEDOntology.owl#Organization'

    def processSubsection(self, *args, **kwargs):
        '''Terminal process
        Do not search below Organization level
        '''
        try:
            self.assessAttributes()
        except: pass
        #self.internalGraph()
    
    def internalGraph(self):
        Contact.internalGraph(self)
        instance = rdflib.Namespace("http://io-informatics.com/rdf/MAGE/Organization/")[self.identifier]
        self.instance = instance
        self.graph.add((instance, rdflib.RDF['type'], self.classType))
        self.attributeToGraph(instance)
        self.ontologyEntryToGraph(instance)



        