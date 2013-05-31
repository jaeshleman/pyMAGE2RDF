'''
Created on 09 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com@io-informatics.com //jae@lmi.net
'''
from Identifiable import Identifiable

class QuantitationTypePackage(Identifiable):
    '''Quantitiation Type package rules    
    '''
    def processSubSection(self, *args, **kwargs):
        classDictionary = {'SpecializedQuantitationType': SpecializedQuantitationType, 
                           #'SpecializedQuantitationType_ref': SpecializedQuantitationType,
                           'MeasuredSignal': MeasuredSignal,
                           #'MeasuredSignal_ref': MeasuredSignal, 
                           'DerivedSignal':DerivedSignal,
                           #'DerivedSignal_ref':DerivedSignal,
                           'ConfidenceIndicator':ConfidenceIndicator, 
                           'Failed':Failed,  'PresentAbsent':PresentAbsent,
                           'Ratio':Ratio}

        self.iterateProcessSubSections(classDictionary)
   
    def internalGraph(self, *args, **kwargs):
        '''No instances for rdf necessary'''
        Identifiable.noInteralGraph(self)
        
class QuantitationTypeDimension(Identifiable):
    '''Quantitation Type Dimension class
    '''
    def processSubSection(self, *args, **kwargs):
        classDictionary = {'SpecializedQuantitationType': SpecializedQuantitationType, 
                           'SpecializedQuantitationType_ref': SpecializedQuantitationType,
                           'MeasuredSignal': MeasuredSignal,
                           'MeasuredSignal_ref': MeasuredSignal, 
                           'DerivedSignal':DerivedSignal,
                           'DerivedSignal_ref':DerivedSignal,
                           'ConfidenceIndicator':ConfidenceIndicator, 
                           'Failed':Failed,  'PresentAbsent':PresentAbsent,
                           'Ratio':Ratio}
        self.iterateProcessSubSections(classDictionary)
    
    def connectGraphs(self, *args, **kwargs):
        '''merges multiple rdflib graphs by rules according to subtypes of section.
        '''
        subTypes = ['QuantitationType',
                    'SpecializedQuantitationType', 
                    'MeasuredSignal',
                    'DerivedSignal',
                    'ConfidenceIndicator',
                    'Failed',
                    'PresentAbsent','Ratio']
        for subType in subTypes:
            try:
                self.addSectionToGraph(subType)
            except:pass
          
class QuantitationType(Identifiable):
    pass

class SpecializedQuantitationType(QuantitationType):
    pass

class StandardQuantitationType(QuantitationType):
    pass
    
class ConfidenceIndicator(StandardQuantitationType):
    pass

class DerivedSignal(StandardQuantitationType):
    pass

class Failed(StandardQuantitationType):
    pass

class MeasuredSignal(StandardQuantitationType):
    pass

class PresentAbsent(StandardQuantitationType):
    pass

class Ratio(StandardQuantitationType):
    pass
