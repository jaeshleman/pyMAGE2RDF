'''
Created on 03 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
from Contact import Contact
from Organization import Organization
from Identifiable import Identifiable

import rdflib

class Person(Contact):
    '''Person subclass of Contact
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        Contact.__init__(self)
     
    def processSubSection(self, *args, **kwargs):
        '''Terminal process.
        '''
        subNodes = self.domObject.getElementsByTagName("Organization_ref")
        try:
            Identifiable.processSubSection(self,Organization, "Organization_ref", subNodes)
        except: print "failed in Person Internally"
        try:
            self.assessAttributes()
        except: pass
        self.internalGraph()
    
    def internalGraph(self):
        Contact.internalGraph(self)
        self.instance = rdflib.Namespace("http://io-informatics.com/rdf/MAGE/Person/")[self.identifier]
        self.graph.add((self.instance, rdflib.RDF['type'], self.classType))
        self.attributeToGraph(self.instance)
        self.ontologyEntryToGraph(self.instance)
    
    def connectGraphs(self, *args, **kwargs):
        subj = self.instance
        if hasattr(self, "subsections"): 
            if self.subsections.get('Organization_ref') != (None or []):
                for ref in self.subsections.get('Organization_ref'):
                    obj = ref.instance
                    self.graph.add((subj, self.predNS['hasAffiliation'], obj))
            
    

