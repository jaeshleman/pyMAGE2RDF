'''
Created on 10 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
import rdflib
from Identifiable import Identifiable

class DesignElement(Identifiable):
    '''Design Element class
    '''
    def processSubSection(self, *args, **kwargs):
        '''CompositeSequence are terminal point in heirarchy"
        '''
        self.assessAttributes()
        self.getOntologyEntries()
        
        ### for RDF
        self.internalGraph()

class Feature(DesignElement):
    pass

class CompositeSequence(DesignElement):
    '''Composite Sequence class
    When set the instance will contain the probe,
    and chip name as well as MAGE-ML identifier
    '''
        
    def processSubSection(self, *args, **kwargs):
        '''CompositeSequence are terminal point in heirarchy"
        '''
        self.assessAttributes()
        self.getOntologyEntries()
        self.setProbe()
        ### for RDF
        self.internalGraph()
    
    def setProbe(self):
        try:
            self.assessAttributes()
        except: pass
        try:
            identifier = self.identifier.split(":")
            try:
                self.chip, self.probe = identifier[-2:]
            except:
                print "cannot retrieve chip and probe"
            try: 
                pass #self = self.probe
            except:
                print "setting self as self.probe did not work"
        except:
            print "cannot retrieve and split identifier"
            
    def internalGraph(self, *args, **kwargs):
        '''InternalGraph creates triples that do not need to reference parent or child nodes.
        Internal graph for CompositeSequence creates probe entity, assigned to probe class 
        with label
        
        Needs namespace help.
        '''
        self.checkForGraph()
        self.graph.add((self.classType, rdflib.RDF['type'], rdflib.RDFS['Class']))
        instance = rdflib.Namespace("http://io-informatics.com/rdf/MAGE/Probe/")[self.probe]
        self.instance = instance
        self.graph.add((instance, rdflib.RDF['type'], self.classType))
        self.addInstanceLabel(labelKey = 'probe')
        chipPred = rdflib.Namespace('http://io-informatics.com/rdf/')['hasProbe']
        chip     = rdflib.Namespace('http://io-informatics.com/rdf/Array/')[self.chip]
        self.graph.add((chip ,chipPred, instance))
        