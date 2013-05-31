'''
Created on 03 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
from Identifiable import Identifiable 
import rdflib

class Contact(Identifiable):
    '''Contact class.
    MGED namespace for contact class = http://mged.sourceforge.net/ontologies/MGEDOntology.owl#Contact
    '''
    def __init__(self):
        Identifiable.__init__(self)
        #self.instance = 'http://mged.sourceforge.net/ontologies/MGEDOntology.owl#Contact'
        #
    
    def processSubSection(self, subClass = None, subClassKey = None, nodes = None,
                          classDictionary = None, *args, **kwargs):
        '''
        Imports Person/Organization to avoid conflicts.
        '''
        from Person import Person
        from Organization import Organization
        classDictionary = {'Person':Person, "Organization":Organization}
        for subClassKey, subClass in classDictionary.iteritems():
            try:
                Identifiable.processSubSection(self, subClass = subClass, subClassKey = subClassKey,
                                               nodes = None, classDictionary = classDictionary)
            except:
                pass
        self.internalGraph()
    
    def internalGraph(self):
        self.checkForGraph()
        self.graph.add((self.classType, rdflib.RDF['type'], rdflib.RDFS['Class']))
        
class Affiliation(Contact):
    """Affiliation 
    """
    pass