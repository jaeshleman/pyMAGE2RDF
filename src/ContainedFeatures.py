'''
Created on 12 Sep,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''

from Identifiable import Identifiable
from DesignElement import Feature

class ContainedFeatures(Identifiable):
    '''List containing features --analogous to 'CompositeSequences'
    '''
    def __init__(self):
        Identifiable.__init__(self)
        self.featureOrder = []
        
    def processSubSection(self, *args, **kwargs):
        subClass = Feature
        subClassKey = "Feature_ref"
        self.subsections[subClassKey] = []
        nodes = self.domObject.getElementsByTagName(subClassKey)
        for node in nodes:
            child = subClass()
            child.domObject = node
            child.parentNode = self
            child.processSubSection(self, subClass, subClassKey, nodes) #sets attributes
            self.subsections[subClassKey].append(child)
        for feature in self.subsections:
            if isinstance(feature, Feature):
                try:
                    self.featureOrder.append(feature.identifier)
                except: pass
        