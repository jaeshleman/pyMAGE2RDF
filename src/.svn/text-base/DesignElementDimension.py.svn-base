'''
Created on 10 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
from Identifiable import Identifiable

from CompositeSequences import CompositeSequences
from ContainedFeatures import ContainedFeatures
from DesignElement import CompositeSequence, Feature

class DesignElementDimensionList(Identifiable):
    '''DesignElementDimension class
    '''

    def __init__(self):
        '''
        Constructor
        '''
        Identifiable.__init__(self)      
        #self.instanceOfClass = 'http://mged.sourceforge.net/ontologies/MGEDOntology.owl#DesignElementDimensionList'  
    
    def processSubSection(self, *args, **kwargs):
        '''Rules for processing subsections of list of DED class
        hard codes next level, replaces processSubSection inherited from identifiable
        '''
        classDictionary = {"CompositeSequenceDimension":CompositeSequenceDimension,
                           "CompositeSequenceDimension_ref":CompositeSequenceDimension,
                           "FeatureDimension": FeatureDimension, 
                           "FeatureDimension_ref":FeatureDimension
                           }
        self.iterateProcessSubSections(classDictionary)

class DesignElementDimension(Identifiable):
    pass

class FeatureDimension(DesignElementDimension):
    def processSubSection(self, *args, **kwargs):
        subClass = ContainedFeatures
        subClassKey = 'ContainedFeatures_assnreflist'
        nodes = self.domObject.getElementsByTagName(subClassKey)
        Identifiable.processSubSection(self, subClass, subClassKey, nodes)

class CompositeSequenceDimension(DesignElementDimension):
    '''Composite Sequence Dimension subclass of Design Element Dimension
    '''
    
    def processSubSection(self, *args, **kwargs):
        subClass = CompositeSequences
        subClassKey = 'CompositeSequences_assnreflist'
        nodes = self.domObject.getElementsByTagName(subClassKey)
        Identifiable.processSubSection(self, subClass, subClassKey, nodes)
    
    def connectGraphs(self, *args, **kwargs):
        comSequences = self.getAllNodesFilter("CompositeSequence")
        for seq in comSequences:
            subj = self.instance
            pred = self.predNS["hasProbe"]
            obj = seq.instance
            self.graph.add((subj, pred, obj))
        
