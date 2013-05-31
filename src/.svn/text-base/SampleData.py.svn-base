'''
Created on 06 Jun,2011

@author: Jason A. Eshleman -- jae@lmi.net //Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com@io-informatics.com
'''

from FileIO import FileImport

class SampleData:
    '''In progress.  Class to retrieve sample data from spreadsheet.
    
    '''
    def retrieveData(self, fileName, filePath, sep = "\t",):
        fileImport = FileImport()
        self.data = fileImport.readfile(filename = "/".join([filePath,fileName]), sep = sep)
    
    def bioDataCubeResults(self, data, probeOrder):
        return dict(zip(probeOrder, data))