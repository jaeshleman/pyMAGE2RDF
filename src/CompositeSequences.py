'''
Created on 10 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
from Identifiable import Identifiable
from DesignElement import CompositeSequence 

class CompositeSequences(Identifiable):
    '''
    Instance list properties hold order of probes from child objects
    '''

    def __init__(self):
        '''
        Constructor
        '''
        Identifiable.__init__(self)
        self.chip = None
        self.probeOrder = []
    
    def processSubSection(self, *args, **kwargs):
        '''Special processing for CompositeSequence level.  Ends heirarchy
        args and kwargs allow statements passed without errors.  Subsections hardCoded
        nodes = self.domObject.getElementByTageName(subClassKey)
        '''
        subClass = CompositeSequence
        subClassKey = 'CompositeSequence_ref'
        self.subsections[subClassKey]= []
        nodes = self.domObject.getElementsByTagName(subClassKey)#'DesignElementDimension_assnlist')
        for node in nodes:
            child = subClass()
            child.domObject = node
            child.parentNode = self
            child.processSubSection(self, subClass, subClassKey, nodes) #sets attributes
            self.subsections[subClassKey].append(child)
            #child.assessAttributes()
        for seq in self.subsections[subClassKey]:
            if isinstance(seq,CompositeSequence):
                try:
                    probe,chip = seq.probe, seq.chip
                    self.probeOrder.append(probe)
                    if self.chip == None:
                        self.chip = chip
                    elif self.chip == chip: pass
                    else: 
                        print "error--chip confusion %s and %s with probe %s" %(chip,self.chip,probe)
                except:
                    pass

    def retrieveSequenceDom(self, domObject = None, tagName = "CompositeSequence_ref"):
        if domObject == None: 
            domObject = self.domObject
        try: 
            return domObject.getElementsByTagName(tagName) 
        except: 
            return None
        
                            
                        
                    
            