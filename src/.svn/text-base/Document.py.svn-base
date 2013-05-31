'''
Created on 03 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
import re, logging, sys
from XMLParser import MageMLParser as Parser
from Describable import Describable  

class Document(Parser, Describable):
    '''General class for Mage ML document.
    '''
    
    def __init__(self, domObject = None):
        '''        Constructor functions for document 
        provides methods for processing document into rdf.
        '''
        Describable.__init__(self)
        '''audit and security package contains the contacts
            for the MAGE-ML document.  This is a collection of contacts (Contact),
            people (Person) and affiliations (Organization) for the people.
            '''
            
        '''Protocol package is a list of protocol steps for the experiment.
            This consists of identifiers
            '''
    
    def searchNestedSubsections(self, key, dictionaryName = 'subsections'):
        if hasattr(self,dictionaryName):
            dictionary = vars(self)[dictionaryName]
            for sectionKey in dictionary:
                if key == sectionKey:
                    yield dictionary[key] #yields a ?
                else:
                    if type(dictionary[key]) == list:
                        for item in dictionary[key]:
                            #try:
                                print "in nesting for class %s" %str(item.__class__)
                                for result in item.searchNestedSubsections(key, dictionaryName):
                                    yield result
                           
    def combineGraphs(self):
        '''Code may be too specific to MAGE-ML
        Consider moving this function elsewhere'''
        
        if hasattr(self, 'graph') == False: self.graph = self.newGraph()
        if hasattr(self, "subsections"):
            for list in self.subsections.itervalues():
                for item in list:
                    try:
                        Document.combineGraphs(self)
                        self.graph = self.combineGraphs(self.graph, item.graph)
                        item.combineGraphs()
                    except:
                        print 'failed to merge graphs at level %s' %str(self.__class__.__name__) 
                        pass
        
    def logError(self, err):
        pass


