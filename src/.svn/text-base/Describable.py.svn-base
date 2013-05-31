'''
Created on 03 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
import re, rdflib, sys, urllib

from ConvertToRDF import mageRDFMaker 
 
class Describable(mageRDFMaker):  
    '''Describable class is parent of most MAGE-ML ontology classes.
    This class contains functions to process sections of the xml and 
    to create rdf 
    '''
    def __init__(self):
        mageRDFMaker.__init__(self)
        self.subsections = {}
        self.setClassNamespace(baseURI = 'http://mged.sourceforge.net/ontologies/MGEDOntology.owl#')
        self.instanceURI = 'http://io-informatics.com/rdf/'
        
    def setDomObject(self, domObject = None):
        if domObject == None:
            domObject = self.domObject
        else: pass
        return domObject
    
    def setAttribs(self, domObject = None, attributeList = []):
        if domObject == None: domObject = self.domObject
        if hasattr(self, "attributeList") == False:
            self.attributeList = []
        if attributeList == []:
            try: 
                attributeList = self.domObject._attrs.keys()
            except: 
                pass
            for attrib in attributeList:
                if "-" in attrib: attrib = attrib.replace("-", "_")
                try:
                    vars(self)[attrib] = self.domObject.getAttribute(attrib) #changed
                    if attrib not in self.attributeList:
                        self.attributeList.append(attrib)
                except: 
                    print "failure on attempt to set attribute for domObject"+\
                          " with attrib %s" %str(attrib)

    def getDescriptiveElements(self, domObject = None):
        '''If elements contain a "Description" section, extract the description.
        Description is formally a class in MAGE-OM but attrribute is purely text in  
        rdf implementation.
        '''
        domObject = self.setDomObject(domObject)
        if hasattr(self,'description') == False:
            self.description = []
        for node in domObject.childNodes:
            if node.nodeType != node.ELEMENT_NODE: pass
            else:
                if "_assn" in node.nodeName:
                    for subNode in node.childNodes:
                        if subNode.nodeType != subNode.ELEMENT_NODE: pass
                        else:
                            if subNode.nodeName == "Description":
                                obj = subNode._attrs.get('text').value
                                if obj not in self.description:
                                    self.description.append(obj)
     
    def getOntologyEntries(self, domObject = None):
        '''finds ontology entry for a class, adds to list.  
        Ontology entries are properties of the object
        '''
        domObject = self.setDomObject(domObject) #uses self.domObject unless otherwise specified
        if hasattr(self, 'ontologyEntries') == False:
            self.ontologyEntries = [] #list of tuples of predicate, object eg [(Roles, submitter), (Scale, linear_scale)]
        #First find "_assn" and "_assnlist" elements
        for node in domObject.childNodes:
            if node.nodeType != node.ELEMENT_NODE: pass
            else:
                if "_assn" in node.nodeName:
                    for subNode in node.childNodes:
                        if subNode.nodeType != subNode.ELEMENT_NODE: pass
                        else:
                            if subNode.nodeName == "OntologyEntry":
                                predicate = subNode._attrs.get('category').value
                                obj       = subNode._attrs.get('value').value
                                if (predicate,obj) not in self.ontologyEntries:
                                    self.ontologyEntries.append((predicate,obj))
        
    def assessAttributes(self):
        try: self.getOntologyEntries()
        except: pass
        try: self.setAttribs()
        except: pass
        try: self.getDescriptiveElements()
        except: pass
    
    def getElements(self, domObject = None):
        '''Interator function, returns only element nodes
        '''
        if domObject == None: 
            domObject = self.domObject
        for node in domObject._get_childNodes():
            if node.nodeType == node.ELEMENT_NODE:
                yield node
    
    def getRoot(self):
        root = None
        if hasattr(self,'root'):
            root = self.root
            
        else:
            if hasattr(self, 'parentNode'):
                root = self.parentNode.getRoot()
            else:
                pass
        self.root = root
        return root
                
    def newSubSectionRecord(self, subClassKey = None):
        if self.subsections.get(subClassKey) == None:
            if subClassKey != None:
                self.subsections[subClassKey] = []
            else:
                pass 
                #print 'Cannot create subsections[section]: subClassKey = %s while processing %s' %(str(subClassKey),str(self.__class__))

    def getChildElement(self, subClass = None, subClassKey = None, node = None,
                                         classDictionary = None, *args, **kwargs):
        try:
            child = subClass()
            child.domObject = node
            try:
                child.assessAttributes()
            except: pass
            return child
        except: 
            print "ERROR IN GET CHILD ELEMENT"
            return None
    
    def processTypeDoms(self, subClassKey, *args, **kwargs):
        typeDoms = self.domObject.getElementsByTagName(subClassKey)
        if isinstance(typeDoms, list):
            if len(typeDoms)>0:
                for typeDom in typeDoms:
                    self.getOntologyEntries(typeDom)
                    
        
    
    def iterateProcessSubSections(self, classDictionary, *args, **kwargs):
        
        for subClassKey, subClass in classDictionary.iteritems():
            try:
                if subClass == None:
                    self.processTypeDoms(subClassKey)
                    
                else:    
                    Describable.processSubSection(self, subClass, subClassKey)#, nodes, classDictionary)
                    if self.subsections[subClassKey] == []:
                        del self.subsections[subClassKey] 
                    #want to process by its own rules.  This dead ends.b 
            except: 
                print "\t\terror processing subsection within class %s for subClass %s\t" %(self.__class__.__name__,
                                                                                  subClassKey)
                print "error of type: ", sys.exc_info()
        self.internalGraph()

    def processSubSectionWithDictionary(self, classDictionary):
        '''When no subClass/subClassKey presented, uses a dictionary 
        of subClassKey:subClass to determine rules to process subsections
        '''
        for node in self.getElements():
            try:
                subClassKey = node.localName
                subClass = classDictionary.get(subClassKey)
                if subClass == None: 
                    pass
                elif subClassKey == None: 
                    pass
                else: 
                    self.processSubSection(subClass= subClass, subClassKey = subClassKey,
                                           nodes = [node], classDictionary = classDictionary)
            except: 
                print "\n\n\t\t\tEXCEPTION IN processSubSectionWithDictionary\n\n"
                print "\n\n\t\t\tat level %s"%str(self.__class__.__name__)
    
    def processSubSection(self, subClass = None, subClassKey = None, nodes = None,
                          classDictionary = None, *args, **kwargs):
        ''' subClassKey and/or subClass defined: return single child per node.
        Also calls method to process by dictionary "processSubSectionWithDictionary"
        as attempt to resolve if subClass/subClass key not provided.'''
        #case 1: subClassKey provided
        if subClassKey != None: 
            self.newSubSectionRecord(subClassKey)
            if subClass != None:
                if (nodes == [] or nodes == None):
                    nodes = self.domObject.getElementsByTagName(subClassKey)
                for node in nodes:
                    child = self.getChildElement(subClass = subClass, subClassKey = subClassKey, 
                                                 node = node, classDictionary = classDictionary)
                    child.parentNode = self  #allows for reference of higher level
                    child.domObject = node
                    child.processSubSection(classDictionary = classDictionary)
                    self.subsections[subClassKey].append(child)
        #case 2: no subClassKey.  Try to find from heirarchy through classDictionary 
        elif subClassKey == None:  
            if classDictionary == None:
                pass  #unable to determine where to go -- deadEnd
            else:  #subClassKey not found
                self.processSubSectionWithDictionary(classDictionary)
        #creates rdflib graph elements for instances according to rules in internalGraph function
        self.internalGraph()

    def setGraphSubjectClass(self, subjNS=rdflib.Namespace('http://io-informatics.com/rdf/')):
        self.subjectInstance = subjNS[self.__class__.__name__]
    
    def checkForSubjectClass(self):
        if hasattr(self, 'subjectInstance') == False:
            self.setGraphSubjectClass()
            
    def setGraphInstance(self, includeClassNameSpace = True, keyAttribute = 'identifier'):
        '''creates rdf entity for instance of class using 'identifier'
        Override in subclasses as necessary'''
        instanceNS = rdflib.Namespace(self.instanceURI + str(self.__class__.__name__)+"/")
        if hasattr(self, keyAttribute):
            self.instance = instanceNS[urllib.quote(self.__dict__.get(keyAttribute))]
    
    def attributeEntryToGraph(self, subj,#subjNS=rdflib.Namespace('http://io-informatics.com/rdf/'),
                            predNS = rdflib.Namespace('http://io-informatics.com/rdf/'),
                            objNS = rdflib.Literal):
        '''Takes attributes and makes them into triples
        '''
        self.checkForGraph()  #assures there is a graph to add triples to
        self.checkForSubjectClass()
        if hasattr(self, 'attributeList'): 
            s = subj
            for p, o in self.attributesToTriples():
                #make camelCase for P
                p = self.toCamelCase(p, addHas = True)
                p = predNS[p]
                if objNS == rdflib.Literal:
                    o = objNS(o)
                elif isinstance(objNS, rdflib.Namespace):
                    o = objNS[o]
                else:
                    pass
                self.graph.add((s, p, o))
                    
    def ontologyEntryToGraph(self, subj,#subjNS=rdflib.Namespace('http://io-informatics.com/rdf/'),
                            predNS = rdflib.Namespace('http://io-informatics.com/rdf/'),
                            objNS = rdflib.Literal):
        '''Takes ontologyEntries and makes them into triples
        '''
        self.checkForGraph()  #assures there is a graph to add triples to
        self.checkForSubjectClass()
        if hasattr(self, 'ontologyEntries'): 
            s = subj
            for p, o in self.ontologyEntriesToTriples():
                #make camelCase for P
                p = self.toCamelCase(p, addHas = True)
                p = predNS[p]
                if objNS == rdflib.Literal:
                    o = objNS(o)
                elif isinstance(objNS, rdflib.Namespace):
                    o = objNS[urllib.quote(o)]
                else:
                    pass
                self.graph.add((s, p, o))

    def descriptionToGraph(self, subj,#subjNS=rdflib.Namespace('http://io-informatics.com/rdf/'),
                            predNS = rdflib.Namespace('http://io-informatics.com/rdf/'),
                            objNS = rdflib.Literal):
        '''Takes ontologyEntries and makes them into triples
        '''
        self.checkForGraph()  #assures there is a graph to add triples to
        self.checkForSubjectClass()
        if hasattr(self, 'description'): 
            for item in self.description:
                s = subj 
                p = self.predNS['hasDescription']
                o = rdflib.Literal(item)
                self.graph.add((s, p, o))
    
    def checkForGraph(self):
        '''checkForGraph method assures that rdflib graph instance exists.
        This method avoids error of trying to add triples without graph instance.'''
        if hasattr(self, "graph") == False:
            self.graph = self.newGraph()
            
    def getAllNodes(self,  dictionaryName = 'subsections', filterTerm = None):#, count = 0):
        '''Recursive search for all nodes withing heirarchy created.'''
        allNodes = []
        if hasattr(self,dictionaryName):
            dictionary = vars(self)[dictionaryName]
            for itemList in dictionary.itervalues():
                for item in itemList:
                    try:
                        newList = item.getAllNodes(dictionaryName = dictionaryName)
                    except:
                        newList = []
                    for node in newList:
                        if filterTerm == None:
                            allNodes.append(node)  
                        elif node.__class__.__name__ == filterTerm:
                            allNodes.append(node)  
                    if filterTerm == None: 
                        allNodes.append(item)
                    elif item.__class__.__name__ == filterTerm:
                        allNodes.append(item)
                        
        return allNodes
    
    def getAllNodesFilter(self, *classNames):
        '''Retrieves all nodes in subsections, filters to include only those whose classNames 
        match specific class names in those provided
        '''
        allNodes = self.getAllNodes()
        filteredNodes = []
        for node in allNodes:
            if node.__class__.__name__ in classNames:
                filteredNodes.append(node)
        return filteredNodes
    
    def addSectionToGraph(self, section = "", predicate = None):
        try:
            items = self.getAllNodes(filterTerm = section)
            if predicate == None:
                predicate = self.toCamelCase(section, addHas = True)
            for item in items: 
                self.graph.add((self.instance, self.predNS[predicate], item.instance))
        except: pass
    
    def connectAllGraphs(self, *args, **kwargs):
        allNodes = self.getAllNodes()
        for node in allNodes:
            try: 
                node.connectGraphs()
            except: 
                pass
            
    def mergeAllgraphs(self,  dictionaryName = 'subsections', 
                       externalConnections = True, graph = None,
                       useInternalGraph = False):
        '''Takes graphs for instances of recursive subsections and combines into 
        graph of the instance method is called from.
        '''
        allNodes = self.getAllNodes(dictionaryName)
        #count = len(allNodes) #debugger
        if graph != None:
            productGraph = graph
        elif useInternalGraph == True:
            if hasattr(self, 'graph') == False: 
                self.graph = self.newGraph()
            productGraph = self.graph
        else: 
            productGraph = rdflib.ConjunctiveGraph()
        for node in allNodes:
            try: 
                productGraph.__iadd__(node.graph)
            except: pass
        return productGraph   
                
    def attributesToTriples(self): 
        """Generator supplies predicate/object.  This is gets converted in to
        triples at the level of the specific python class where namespace details can 
        be refined
        """
        for attrib in self.attributeList:
            entry = vars(self).get(attrib)
            pred, obj = attrib, entry
            yield pred, obj
            #graph--self entity gets an additional triple
            #need to make camelCase?  Yield?
    
    def ontologyEntriesToTriples(self):
        """Generator supplies predicate/object.  This is gets converted in to
        triples at the level of the specific python class where namespace details can 
        be refined
        """
        for pred, obj in self.ontologyEntries:
            yield pred, obj
            #graph--self entity gets an additional triple
            #need to make camelCase?  Yield?

    def fixURI(self, item):
        try: 
            return urllib.urlencode(item)
        except:
            return item
              
    def internalGraph(self, *args, **kwargs):
        '''Stub for rule in subclass. 
        parent class method creates graph if not present and creates ontology record 
        in graph for the class'''
        self.checkForGraph()
        
        self.graph.add((self.classType, rdflib.RDF['type'], rdflib.RDFS['Class']))
        try:
            if hasattr(self, 'instance') == False:
                self.setGraphInstance()
            self.graph.add((self.instance, rdflib.RDF['type'], self.classType))
        except: pass
        try:
            self.setGraphInstance()
        except:pass
        try:
            self.instance = self.fixURI(self.instance)
        except:
            pass
        try:
            self.attributeToGraph(self.instance)
        except: pass
        try:
            self.ontologyEntryToGraph(self.instance)
        except:pass
        try:
            self.descriptionToGraph(self.instance)
        except: pass
        
    def noInteralGraph(self, *args, **kwargs):
        '''Empty method prevents instances from being created.
        Instances of items within will be created if 'internalGraph'
        method is enabled with subClasses.
        '''
        pass
        
    def addInstanceLabel(self, labelKey = 'name'):
        try:
            if hasattr(self, labelKey):
                self.graph.add((self.instance, 
                                rdflib.RDFS['label'],
                                rdflib.Literal(vars(self).get(labelKey))
                                ))
        except: pass
    
    def readExtraTypeInformation(self, dictionary = None, *args, **kwargs):
        '''To get special information in lists, ontologyEntries, etc.
        NOT WORKING
        '''  #supply this in subsection
        for key,value in dictionary.iteritems():
            typeDoms = self.domObject.getElementsByTagName(key)
            if isinstance(typeDoms, list):
                if len(typeDoms)>0:
                    self.getOntologyEntries(typeDoms)
        
