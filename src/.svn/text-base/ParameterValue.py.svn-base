'''
Created on 13 Sep,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''

from Extendable import Extendable
from Parameter import Parameter

class ParameterValue(Extendable):
    def processSubSection(self, *args, **kwargs):
        classDictionary = {"Parameter_ref":Parameter}
        self.iterateProcessSubSections(classDictionary)
        
    def internalGraph(self):
        pass