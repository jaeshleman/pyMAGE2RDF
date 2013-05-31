'''
Created on 09 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
from Identifiable import Identifiable
from Person import Person
from Contact import Contact
from Organization import Organization
from Describable import Describable
import rdflib

class AuditAndSecurity(Identifiable):
    '''
    AuditAndSecurity section of MAGE-ML xml doc contains information about individuals and agencies
    that ran the experiment(s) and processed the data.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        Identifiable.__init__(self)
    
    def processSubSection(self, subClass = None, subClassKey =None,nodes = None,
                          classDictionary = None, *args, **kwargs):
        '''function to call to process AuditAndSecurity's subsections
        '''
        classDictionary = {"Contact_assnlist":Contact}#, "Organization":Organization,
        for subClassKey, subClass in classDictionary.iteritems():
            try:
                Identifiable.processSubSection(self, subClass = subClass, subClassKey = subClassKey,
                                               nodes = nodes, classDictionary = classDictionary)
            except:
                print "did not get through subsection %s within AuditAndSecurity"%subClassKey
                
    def internalGraph(self, *args, **kwargs):
        '''Empty method prevents instances from being created.
        Instances of items within will be created if 'internalGraph'
        method is enabled with subClasses.
        '''
        Describable.noInteralGraph(self)
    
    def setClassNamespace(self, baseURI = 'http://io-informatics.com/rdf/'):
        '''overrides self.classType assignment  ---not needed if "noInternalGraph" selected 
        '''
        self.ns = rdflib.Namespace(baseURI)
        self.classType = self.ns['Audit'] 

