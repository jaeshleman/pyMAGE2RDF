'''
Created on 03 May,2011

@author: jeshleman
'''

import xml.dom.minidom, urllib2, re

class XmlParser(object):
    def __init__(self):
        pass
    
    def readDocument(self, file):
        '''
            File can be filename or open file handle.
        '''
        self.domObject = xml.dom.minidom.parse(file)
    
    def nextElement(self, doc = None):
        if doc == None: doc = self.doc
        if self.doc.hasChildNodes() == True:
            for node in self.doc._get_childNodes():
                if node.ELEMENT_NODE == node.nodeType:
                    yield node
                    
    def getElementNode(self, domObject):
        if domObject.nodeType == domObject.ELEMENT_NODE:
            localName = domObject._get_localName()
        else: localName = "No local name"
        return localName
            
class MageMLParser(XmlParser):
    def __init__(self):
        pass
    
    '''
    Elements:
        AuditAndSecurity_package
            Contact_assnlist : Person, Organization
        Protocol_package
        BioMaterial_package
        Array_package
        BioAssay_package
        QuantitationType_package
        BioAssayData_package
        Experiment_package
        
    element Nodes:  domObject.nodeType == domObject.ELEMENT_NODE  (1)
        to get element node name for element Nodes: 
            domObject._get_localName()
            
    '''
    
    def getMageClass_division(self, localName):
        '''Function returns titles for division and division type from
           MAGE-ML document. A MAGE-ML document has classes designated by single name 
        
        e.g. 'Person' that typically have attributes 
        e.g.  <Person firstName="Hsing-Jien"
                      identifier="ebi.ac.uk:MAGETabulator:Hsing-Jien Kung.Person"
                      lastName="Kung">)
        
        Other document divisions are used to further characterize object sections
        form typically used is <Class_modifier> e.g. <Protocol_package>  
        for a class the following suffixes can be applied.
        
        _package        :designates that the following section will be comprised of a collection
                    of class instances of the prefix. 
        _assn           :designates that the following node will contain characteristics that further
                    modify the preceding node class instance
        _assnlist       :designates that an [ordered] list of instances of the prefixed class
                    will appear
                    
        _assnref        :designates ?
        _assnreflist    :designates ?
        _ref            :designates ?
        
        '''
        searchTerm = re.compile("(\w+)_(\w+)")
        
        try:
            className, classType = searchTerm.search(localName).groups()
            return className, classType
        except: 
            return localName, "class"

    
    
    
if __name__ == "__main__":
    fileName = "c:/Users/jeshleman/Desktop/Cleanup/xmlExamples/E-GEOD-21987.xml"
    x = XmlParser
    x.getXml(fileName)