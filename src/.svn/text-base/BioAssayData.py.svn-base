'''
Created on 09 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
from Identifiable import Identifiable
from DesignElementDimension import DesignElementDimensionList, CompositeSequenceDimension
#from Extendable import Extendable
from QuantitationType import QuantitationTypeDimension
from BioAssay import BioAssayDimensionList   
from BioEvent import Transformation 
from BioDataValues import BioDataValues

#import rdflib

class BioAssayDataPackage(Identifiable):
    '''Master class for BioAssayData package processing.    
    '''
 
    def processSubSection(self,subClass = None, subClassKey =None,nodes = None,
                          classDictionary = None, *args, **kwargs):
        '''args and kwargs allow statements passed without errors.  Subsections hardCoded'''

        classDictionary = {"BioAssayDimension_assnlist":BioAssayDimensionList,
                           "DesignElementDimension_assnlist":DesignElementDimensionList,
                           "BioAssayData_assnlist":BioAssayDataList,
                           "QuantitationTypeDimension":QuantitationTypeDimension
                           }
        self.iterateProcessSubSections(classDictionary)
        
    
    def internalGraph(self, *args, **kwargs):
        Identifiable.noInteralGraph(self)  #make no triples for package
        
class BioAssayDataList(Identifiable):
    def processSubSection(self, *args, **kwargs):
        classDictionary = {"MeasuredBioAssayData":MeasuredBioAssayData,
                           "DerivedBioAssayData":DerivedBioAssayData,
                           #from Experiment section:
                            "MeasuredBioAssayData_ref": MeasuredBioAssayData,
                            "DerivedBioAssayData_ref": DerivedBioAssayData}
        for subClassKey, subClass in classDictionary.iteritems():
            if self.subsections.get(subClassKey) == None:
                self.subsections[subClassKey] = []
            Identifiable.processSubSection(self, subClass, subClassKey) 
            #self.internalGraph()
    
    def internalGraph(self):
        Identifiable.noInteralGraph(self)
        
    def subSectionsToRDF(self, *args, **kwargs):
        predicates = {'BioAssayDimension':"bioAssayDimenions", 
                       'DesignElementDimensionList': "designElementDimension", 
                       'QuantiationTypeDimension': "quantitationTypeDimension",
                       'BioDataValues': "summaryStatistics",  
                       'Transformation': 'producerTransformation' } #, SummaryStatistics]
        for value in self.subsections.itervalues():
            if type(value) == list:
                for item in value:
                    if item.__class__.__name__ in predicates:
                        predicate = predicates.get(item.__class__.__name__)
                        print predicate
                pass   
    
class BioAssayData(Identifiable):
    def processSubSection(self, subClass = None, subClassKey = None, nodes = None,
                      classDictionary = None,
                      *args, **kwargs):
        if subClass != None:
            Identifiable.processSubSection(self, subClass, subClassKey, nodes, classDictionary)
        if classDictionary == None:
            classDictionary = {'QuantitationTypeDimension_ref':QuantitationTypeDimension,
                               'CompositeSequenceDimension_ref':CompositeSequenceDimension, #DesignElementDimensionList?
                               "BioDataValues_assn":BioDataValues, #  may need to go straight to BioDataCube
                               "Transformation":Transformation,
                               "DesignElementDimension_assnref":DesignElementDimensionList,
                               }
        self.iterateProcessSubSections(classDictionary)
    
    def connectGraphs(self, *args, **kwargs):
        subSections = ['QuantitationTypeDimension',
                       'CompositeSequenceDimension',
                       "BioDataValues",
                       "Transformation",                                   
                       "DesignElementDimensionList"
                       ]
        for section in subSections:
            try:
                self.addSectionToGraph(section)
            except: pass

class MeasuredBioAssayData(BioAssayData):
    pass


class DerivedBioAssayData(BioAssayData):
    '''Processed bioAssayData includes RMA expression values.  
    This section describes files containing.
    '''
    pass
        


