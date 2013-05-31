'''
Created on 03 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
from Parameterizable import Parameterizable
from Parameter import ParameterList
import rdflib
from Hardware import Hardware
from Software import Software

class ProtocolPackage(Parameterizable):
    '''
    ProtocolPackage process section of MAGE-ML document.
    Subsections for Protocol run and added to MAGE-ML rdf graph.
    Instance not added to rdf.
    '''

    def __init__(self):
        Parameterizable.__init__(self)
    
    def processSubSection(self, subClass = None, subClassKey = None, nodes = None,
                          classDictionary = None, *args, **kwargs):
        '''Processes this document and subSections
        hard codes child level
        '''
        classDictionary = {"Protocol_assnlist":ProtocolList,"Hardware_assnlist":ProtocolList,
                           "Software_assnlist":ProtocolList}
        self.iterateProcessSubSections(classDictionary)

    def internalGraph(self,*args, **kwargs):
        Parameterizable.noInteralGraph(self)

class ProtocolList(ProtocolPackage):
    '''Protocol_assnlist lists all steps of experimental protocol for MAGE-ML doc
    Instance of class not added to graph.
    '''
    def __init__(self):
        ProtocolPackage.__init__(self)
    
    def processSubSection(self, subClass = None, subClassKey = None, nodes = None,
                          classDictionary = None, *args, **kwargs):
        classDictionary = {"Protocol":Protocol, "Protocol_ref": Protocol,
                           "Hardware":Hardware, "Hardware_ref":Hardware,
                           "Software":Software, "Software_ref":Software}
        self.iterateProcessSubSections(classDictionary)

        
class Protocol(Parameterizable):
    '''Class instances for Proctocol. 
    Instances created
    '''
    def __init__(self):
        self.setClassNamespace("http://mged.sourceforge.net/ontologies/MGEDOntology.owl#")
        Parameterizable.__init__(self)
        
    def processSubSection(self, *args, **kwargs):
        '''Terminal Level?
        '''
        classDictionary = {"ParameterTypes_assnlist":ParameterList, "Type_assn":None, 
                           "Hardware_ref":Hardware, "Software_ref":Software}
        self.iterateProcessSubSections(classDictionary)
        self.internalGraph()
    
    def internalGraph(self, *args, **kwargs):
        '''InternalGraph creates triples that do not need to reference parent or child nodes.
        Internal graph for Protocol creates protocol, with name and text, assigned to probe class 
        with label
        Needs namespace help
        '''
        self.checkForGraph()
        self.graph.add((self.classType, rdflib.RDF['type'], rdflib.RDFS['Class']))  #makes instance of cla
        instance = rdflib.Namespace("http://io-informatics.com/rdf/MAGE/Protocol/")[self.identifier]  
        self.instance = instance
        try:
            self.graph.add((instance, rdflib.RDF['type'], self.classType))
        except: pass
        try:
            self.graph.add((instance, rdflib.RDFS['label'],rdflib.Literal(str(self.identifier))))          
        except: pass
        try:
            self.graph.add((instance, self.ns['hasText'], rdflib.Literal(str(self.text))))
        except: pass
        try:
            self.graph.add((instance, self.ns['hasStepNumber'], rdflib.Literal(int(self.protocolStep))))
        except: pass
        try:
            self.addSectionToGraph("Parameter")
        except: pass
        self.ontologyEntryToGraph(instance)
        try:
            date = self.parentNode.activityDate
            self.graph.add( (instance, self.predNS['hasActivityDate'], rdflib.Literal(date) ) )
        except: pass
    
    def connectGraphs(self, *args, **kwargs): 
        self.addSectionToGraph("Hardware")
        self.addSectionToGraph("Software")