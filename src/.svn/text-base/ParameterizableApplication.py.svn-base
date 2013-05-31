'''
Created on 01 Aug,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
from Describable import Describable
from Protocol import Protocol
from ParameterValue import ParameterValue


class ParameterizableApplication(Describable):
    '''Parameterizable Application class
    '''
    pass

class HardwareApplication(ParameterizableApplication):
    pass
        
class ProtocolApplication(ParameterizableApplication):
    def processSubSection(self, *args, **kwargs):
        classDictionary = {"Protocol_ref":Protocol,
                           "ParameterValue":ParameterValue}
        self.iterateProcessSubSections(classDictionary)
    
    def internalGraph(self, *args, **kwargs):
        try:
            Describable.noInteralGraph(self)
        except: pass
        try:
            subj = self.parentNode.instance
        except: pass
        try:
            self.ontologyEntryToGraph(subj)
        except: pass
        try:
            self.attributeEntryToGraph(subj)
        except: pass
            
    def connectGraphs(self, *args, **kwargs):
        ''''WON'T work, no self.instance for triple
        Do no call from Parameterizable Application
        '''
        self.addSectionToGraph('Protocol', self.predNS['treatmentHasProtocol'])

class SoftwareApplication(ParameterizableApplication):
    pass