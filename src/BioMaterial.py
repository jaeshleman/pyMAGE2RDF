'''
Created on 09 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''

from Identifiable import Identifiable
from Extendable import Extendable
#from ParameterizableApplication import ProtocolApplication 
#from BioAssayData import BioAssayDataList
from BioEvent import Treatment


class BioMaterialPackage(Identifiable):
    
    def processSubSection(self, *args, **kwargs):
        classDictionary = {'Compound':Compound, 
                           #from BioMaterial_assnlist 
                           "LabeledExtract":LabeledExtract,
                           "BioSource":BioSource, 
                           "BioSample":BioSample}
        Identifiable.iterateProcessSubSections(self, classDictionary)
    
    def internalGraph(self, *args, **kwargs):
        if self.__class__.__name__ == "BioMaterialPackage":
            Identifiable.noInteralGraph(self)
        else:
            Identifiable.internalGraph(self)
            Identifiable.addInstanceLabel(self, labelKey="name")
            
class Compound(Identifiable):
    '''Compound class.
    '''
    def internalGraph(self, *args, **kwargs):
        Identifiable.internalGraph(self)
        Identifiable.addInstanceLabel(self, labelKey="name")

class BioMaterial(Identifiable):
    '''BioMaterial items from BioMaterial package
    '''
    def processSubSection(self, *args,**kwargs):
        classDictionary = {"Compound_ref":Compound, 
                           "Treatment":Treatment
                           }
        Identifiable.iterateProcessSubSections(self, classDictionary)
    
    def internalGraph(self, *args, **kwargs):
        Identifiable.internalGraph(self)
        Identifiable.addInstanceLabel(self, labelKey="name")  
        
    def connectGraphs(self, *args, **kwargs):
        self.addSectionToGraph("Compound", 'hasLabels')
        self.addSectionToGraph("Treatment")

        
class BioSample(BioMaterial):
    pass


class BioSource(BioMaterial):
    pass


class LabeledExtract(BioMaterial):
    pass
    
    
class BioMaterialMeasurement(Extendable):
    '''BioMaterialMeasurement class
    '''
    def processSubSection(self, *args, **kwargs):
        classDictionary = {'BioSource_ref':BioSource,
                           'BioSample_ref':BioSample}
        self.iterateProcessSubSections(classDictionary)
    
    def internalGraph(self, *args, **kwargs):
        Extendable.noInteralGraph(self)
        

