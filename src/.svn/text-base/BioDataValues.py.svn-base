'''
Created on 25 Jul,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
from Extendable import Extendable

from FileIO import FileImport

class BioDataValues(Extendable):
    def processSubSection(self, *args, **kwargs):
        self.assessAttributes()
        self.iterateProcessSubSections({"BioDataCube":BioDataCube})

    def internalGraph(self):
        Extendable.noInteralGraph(self)

class BioDataCube(BioDataValues):
    '''BioDataCube class describes how three-column data file is laid out.
    Three letters indicate order of data.
    
    D=DesignDimension
    B=BioAssayDimension
    Q=QuantitationDimension
    
    Note: do all files have "DataExternal"?  Example of 'internal' data would be 
    useful.
    '''
    def internalGraph(self):
        pass
    
    def processSubSection(self, *args, **kwargs):
        classDictionary = {"DataExternal_assn":DataExternalList}
        self.iterateProcessSubSections(classDictionary)
        #self.assessAttributes()
        
    
class DataExternalList(BioDataValues):
    def processSubSection(self, subClass = None , subClassKey= None, *args, **kwargs):
        self.assessAttributes()
        self.iterateProcessSubSections({"DataExternal":DataExternal})

    def setGraphInstance(self, includeClassNameSpace = True):
        '''Instances named after 'filenameURI' as items do not have 'identifier'
         '''
        Extendable.setGraphInstance(self, includeClassNameSpace = True, keyAttribute = 'filenameURI') 
        
    def internalGraph(self, *args, **kwargs):
        Extendable.noInteralGraph(self)
        
class DataExternal(Extendable):
    def processSubSection(self, *args, **kwargs):
        self.assessAttributes()
        self.internalGraph()#terminal
    
    def internalGraph(self, *args, **kwargs):
        self.setGraphInstance(keyAttribute = "filenameURI")
        Extendable.internalGraph(self)
        
    def readFile(self, set = True):
        if ((self.filenameURI =="") or (self.filenameURI == None) or (hasattr(self, "filenameURI") == False)):
            pass
        else:
            io = FileImport() 
            matrix = io.readfile(self.getRoot()+self.filenameURI)
            if set == True:
                self.data = matrix
            else: 
                return matrix

    