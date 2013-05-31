from Identifiable import Identifiable
from ParameterizableApplication import ProtocolApplication
from Array import Array


class BioEvent(Identifiable):
    '''Top class of BioEvent.  BioEvent describe actions performed within MicroArray experiment.
    '''
    def processSubSection(self, *args, **kwargs):
        classDictionary = {'ProtocolApplication': ProtocolApplication}
        self.iterateProcessSubSections(classDictionary)
    
    def internalGraph(self, *args, **kwargs):
        Identifiable.internalGraph(self)
        Identifiable.addInstanceLabel(self, labelKey="name")
        
    def connectGraphs(self):
        self.addSectionToGraph('Protocol', self.predNS['hasProtocolApplication'])
        

class FeatureExtraction(BioEvent):
    def processSubSection(self, *args, **kwargs):
        from BioAssay import PhysicalBioAssay, MeasuredBioAssay, DerivedBioAssay
        BioEvent.processSubSection(self)
        classDictionary = {'PhysicalBioAssay_ref':PhysicalBioAssay,
                           'MeasuredBioAssay_ref': MeasuredBioAssay,
                           'DerivedBioAssay_ref':DerivedBioAssay}
        self.iterateProcessSubSections(classDictionary)
    
    def connectGraphs(self):
        BioEvent.connectGraphs(self)
        bioAssays = ['PhysicalBioAssay', 'MeasuredBioAssay', 'DerivedBioAssay']
        for assay in bioAssays:
            try:        
                pred = "has"+assay
                self.addSectionToGraph(assay, self.predNS[pred])
            except:pass

class Transformation(BioEvent):
    pass
    ''
    def processSubSection(self, *args, **kwargs):
        #BioEvent.processSubSection(self)
        from BioAssayData import BioAssayDataList
        classDictionary = {"BioAssayDataSources_assnreflist":BioAssayDataList,
                           "ProtocolApplication":ProtocolApplication}
        self.iterateProcessSubSections(classDictionary)

    def connectGraphs(self):
        BioEvent.connectGraphs(self)
        subSections = ['MeasuredBioAssayData', 'BioAssayData', 'DerivedBioAssayData']
        for section in subSections:
            try:
                self.addSectionToGraph(section, self.predNS['hasBioAssayDataSource'])
            except: pass
                                                          
class Treatment(BioEvent):
    def processSubSection(self, *args, **kwargs):
        #BioEvent.processSubSection(self)
        from BioMaterial import BioMaterialMeasurement
        
        classDictionary = {'BioMaterialMeasurement': BioMaterialMeasurement,
                           'ProtocolApplication': ProtocolApplication}
        self.iterateProcessSubSections(classDictionary)
    
    def connectGraphs(self, *args, **kwargs):
        self.addSectionToGraph("ProtocolApplication")
        self.addSectionToGraph("BioSource")
        self.addSectionToGraph("BioSample")
        
class BioAssayTreatment(BioEvent):
    def processSubSection(self, *args, **kwargs):
        from BioAssay import PhysicalBioAssay, MeasuredBioAssay, DerivedBioAssay
        BioEvent.processSubSection(self)
        classDictionary = {'PhysicalBioAssay_ref':PhysicalBioAssay,  #target
                           'MeasuredBioAssay_ref': MeasuredBioAssay,
                           'DerivedBioAssay_ref':DerivedBioAssay}
        self.iterateProcessSubSections(classDictionary)
    
    def connectGraphs(self):
        BioEvent.connectGraphs(self)
        bioAssays = ['PhysicalBioAssay', 'MeasuredBioAssay', 'DerivedBioAssay']
        for assay in bioAssays:
            try:        
                pred = "has"+assay
                self.addSectionToGraph(assay, self.predNS[pred])
            except: pass

class ImageAcquisition(BioAssayTreatment):
    pass
    
class BioAssayCreation(BioEvent):
    def processSubSection(self, *args, **kwargs):
        from BioAssay import PhysicalBioAssay, MeasuredBioAssay, DerivedBioAssay
        BioEvent.processSubSection(self)
        classDictionary = {'PhysicalBioAssay_ref':PhysicalBioAssay,
                           'MeasuredBioAssay_ref': MeasuredBioAssay,
                           'DerivedBioAssay_ref':DerivedBioAssay}
        self.iterateProcessSubSections(classDictionary)
    
    def connectGraphs(self):
        BioEvent.connectGraphs(self)
        bioAssays = ['PhysicalBioAssay', 'MeasuredBioAssay', 'DerivedBioAssay']
        for assay in bioAssays:
            try:        
                pred = "has"+assay
                self.addSectionToGraph(assay, self.predNS[pred])
            except:pass

class Hybridization(BioAssayCreation):
    def processSubSection(self, *args, **kwargs):
        from BioMaterial import LabeledExtract
        BioAssayCreation.processSubSection(self)
        classDictionary = {'LabeledExtract_ref':LabeledExtract, "Array_ref":Array, 
                           "ProtocolApplication":ProtocolApplication}
        self.iterateProcessSubSections(classDictionary)
    
    def connectGraphs(self):
        BioAssayCreation.connectGraphs(self)
        subsections = ["LabeledExtract", 'Array']
        for section in subsections:
            self.addSectionToGraph(section)

class Map(BioEvent):
    pass

class BioAssayMap(Map):
    pass

class DesignElementMap(Map):
    pass

class QuantitationTypeMap(Map):
    pass