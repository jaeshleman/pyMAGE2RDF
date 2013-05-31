'''
Created on 03 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
from Identifiable import Identifiable
from ArrayDesign import PhysicalArrayDesign


class ArrayPackage(Identifiable):
    '''ArrayPackage class processes ArrayPackage section of MAGE-ML document.
    Subsections for ArrayManufacturer and Array run, in turn added to MAGE_ML rdf graph.
    '''
    def processSubSection(self, *args, **kwargs):
        classDictionary = {"ArrayManufacture": ArrayManufacture,
                           "Array":Array}
        self.iterateProcessSubSections(classDictionary)
        
    def internalGraph(self, *args, **kwargs):
        Identifiable.noInteralGraph(self)

class Array(Identifiable):
    '''
    The Array object.  References manufacturer and ArrayDesign
    '''
    def processSubSection(self, *args, **kwargs):
        self.assessAttributes()
        self.internalGraph()
        classDictionary = {"ArrayManufacture_ref": ArrayManufacture,
                           "PhysicalArrayDesign_ref":PhysicalArrayDesign}
        self.iterateProcessSubSections(classDictionary)
        
    def connectGraphs(self, *args, **kwargs):
        self.addSectionToGraph("ArrayManufacture", 'hasInformation')
        self.addSectionToGraph("PhysicalArrayDesign", 'hasArrayDesign')
        

class ArrayManufacture(Identifiable):
    '''The specific manufacturer of a physical array, refereneces and referenced by Array.
    '''
    def processSubSection(self, *args, **kwargs):
        Identifiable.processSubSection(self, Array, "Array_ref")