'''
Created on 27 Jul,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
from Identifiable import Identifiable

class ArrayDesignPackage(Identifiable):
    '''ArrayDesignPackage processes section of MAGE-ML document.
    Subsections for ArrayDesign run and added to MAGE-ML rdf graph.
    Instance not added to rdf.
    '''
    def processSubSection(self, *args, **kwargs):
        classDictionary = {'ArrayDesign':ArrayDesign}
        self.iterateProcessSubSections(classDictionary)


class ArrayDesign(Identifiable):
    '''Class instance for ArrayDesign, added to graph.
    '''
    pass


class PhysicalArrayDesign(ArrayDesign):
    '''Class instance for PhysicalArrayDesign, added to graph.
    '''    
    def processSubSection(self, *args, **kwargs):
        self.assessAttributes()
        self.internalGraph()
        