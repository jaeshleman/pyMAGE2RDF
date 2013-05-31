'''
Created on 09 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
from Identifiable import Identifiable
from BioMaterial import Compound
from BioEvent import FeatureExtraction, Hybridization, BioAssayMap, ImageAcquisition

from FactorValue import FactorValue

class BioAssayPackage(Identifiable):    
    
    def processSubSection(self, *args, **kwargs):
        classDictionary = {'Channel':Channel,
                           "MeasuredBioAssay":MeasuredBioAssay,
                           "DerivedBioAssay":DerivedBioAssay,
                           "PhysicalBioAssay":PhysicalBioAssay}
        self.iterateProcessSubSections(classDictionary)
    
    def internalGraph(self, *args, **kwargs):
        Identifiable.noInteralGraph(self)
        

class BioAssay(Identifiable):
    def processSubSection(self, *args, **kwargs):
        classDictionary = {"PhysicalBioAssay_ref":PhysicalBioAssay, 
                           "MeasuredBioAssay_ref":MeasuredBioAssay,
                           "DerivedBioAssay_ref":DerivedBioAssay, 
                           'FactorValue_ref':FactorValue}
        self.iterateProcessSubSections(classDictionary)
        
    def internalGraph(self, *args, **kwargs):
        if self.__class__.__name__== 'BioAssay':
            Identifiable.noInteralGraph(self)
        else:
            Identifiable.internalGraph(self)
            Identifiable.addInstanceLabel(self, labelKey = 'name')
    
    def connectGraphs(self):
        subsections = [ 'FactorValue', 'MeasuredBioAssay', 'PhysicalBioAssay', 'DerivedBioAssay']
        for section in subsections:
            try:
                self.addSectionToGraph(section)
            except:
                pass
        try: 
            self.addSectionToGraph("FeatureExtraction")
        except: pass


class MeasuredBioAssay(BioAssay):
    def __init__(self):
        Identifiable.__init__(self)
            
    def processSubSection(self, *args, **kwargs):
        from BioAssayData import MeasuredBioAssayData 
        classDictionary = {"FeatureExtraction":FeatureExtraction,
                           "MeasuredBioAssayData_ref": MeasuredBioAssayData}
        self.iterateProcessSubSections(classDictionary)
        BioAssay.processSubSection(self)

    def connectGraphs(self, *args, **kwargs):
        BioAssay.connectGraphs(self)
        subsections = [ 'FeatureExtraction', 'MeasuredBioAssayData']
        for section in subsections:
            try:
                self.addSectionToGraph(section)
            except:
                pass
        
class DerivedBioAssay(BioAssay):
    def processSubSection(self, *args, **kwargs):
        from BioAssayData import DerivedBioAssayData 
        classDictionary = {'DerivedBioAssayData_ref':DerivedBioAssayData,
                           'BioAssayMap_ref':BioAssayMap
                           }
        self.iterateProcessSubSections(classDictionary)
        BioAssay.processSubSection(self)
    
    def connectGraphs(self):
        BioAssay.connectGraphs(self)
        subsections = ['DerivedBioAssayData', 'BioAssayMap']
        for section in subsections:
            try:
                self.addSectionToGraph(section)
            except:
                pass
        

class PhysicalBioAssay(BioAssay):
    def processSubSection(self, *args, **kwargs):
        BioAssay.processSubSection(self)
        classDictionary = {'Channel_ref':Channel,
                           'Hybridization':Hybridization,
                           'ImageAcquisition':ImageAcquisition}
        self.iterateProcessSubSections(classDictionary)
        
    def connectGraphs(self):
        BioAssay.connectGraphs(self)
        subsections = ['Channel', 'Hybridization','FactorValue']
        for section in subsections:
            try:
                self.addSectionToGraph(section)
            except: pass
        try: 
            self.addSectionToGraph('ImageAcquisition', "hasBioAssayTreatment")
        except:pass

class BioAssayDimensionList(Identifiable):
    def processSubSection(self, *args, **kwargs):
        classDictionary = {"BioAssayDimension":BioAssayDimension}
        self.iterateProcessSubSections(classDictionary)
    
    def internalGraph(self):
        self.noInteralGraph()

class BioAssayDimension(Identifiable):
    '''BioAssayDimension section of BioAssayData package
    '''
    def processSubSection(self, *args, **kwargs):
        classDictionary =  {"PhysicalBioAssay_ref":PhysicalBioAssay, 
                           "MeasuredBioAssay_ref":MeasuredBioAssay,
                           "DerivedBioAssay_ref":DerivedBioAssay, }
        self.iterateProcessSubSections(classDictionary)
    
    def connectGraphs(self):
        sectionList = ['MeasuredBioAssay', 'PhysicalBioAssay', 'DerivedBioAssay']
        for section in sectionList:
            self.addSectionToGraph(section)


class Channel(Identifiable):
    def processSubSection(self, *args, **kwargs):
        classDictionary = {'Compound_ref':Compound}
        self.iterateProcessSubSections(classDictionary)
            
    def connectGraphs(self):
        self.addSectionToGraph("Compound")
        
        