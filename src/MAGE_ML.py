'''
Created on 05 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''

from Document import Document

class MAGE_ML(Document):
    def __init__(self):
        Document.__init__(self)
        self.sectionList = ['Array', 'ArrayDesign', 'Person', 'Organization', 
                            'Protocol', 'Experiment'
                            ]
        pass
                

    def valueList(self, valueKey):
        '''Finds items matching the valueKey and creates a list with all values matching the key.
        The list will be identified as a property of the object with name equal to the valueKey.
        '''
        if hasattr(self, valueKey) == False:
            vars(self)[valueKey] = []
            for value in  self.searchSubSections(self.subsections, valueKey):
                if type(value) == list:
                    vars(self)[valueKey].extend(value)
                else:
                    vars(self)[valueKey].append(value)
            
    def searchSubSections(self, dictionary, subSectionKey):
        '''recursive search for all items with a dictionary key within the
        mage ml document''' 
        for key in dictionary.keys():
            if subSectionKey == key:
                yield dictionary[subSectionKey]  #should yield a list
            else:
                if type(dictionary.get(key)) == list:
                    for item in dictionary.get(key):
                        if hasattr(item, 'subsections'):
                            nextDictionary = item.subsections
                            for result in self.searchSubSections(nextDictionary, subSectionKey):
                                yield result
                        else: pass
    
    def searchSubSectionsByAttrib(self, dictionary, identType):
        for key, item in dictionary.iteritems():
            if hasattr(item, identType):
                #if vars(item)[identType] == identKey:
                yield item
            else:
                if hasattr(item, 'subsections'):
                    nextDictionary = item.subsections
                    for result in self.searchSubSectionsByIdent(nextDictionary, identType):
                        yield result
    
    def connectGraphs(self, sectionList = None):
    
        if sectionList == None:
            sectionList = self.sectionList
        for section in sectionList:
            self.addSectionToGraph(section)
        
                   
    def getSequenceDimensions(self):
        '''incomplete method.  IN PROGRESS 2012-1-11
        '''
        self.sequenceDimensionList = []
        key = "CompositeSequenceDimension"
        for item in self.searchSubSectionsByAttrib(self.subsections, key):
                pass

