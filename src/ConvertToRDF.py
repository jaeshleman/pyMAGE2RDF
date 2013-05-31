'''
Created on 14 Apr,2011

@author Jason A. Eshleman: jeshleman@io-informatics.com //jae@lmi.net
'''

import rdflib, os, urllib2  

#from rdflib import ConjunctiveGraph as Graph

class RDFMaker:
    '''General class to change an object into RDF with RDFlib
    Conceptualized as object for MAGE-ML to RDF transformation
    ''' 
    def setClassNamespace(self, baseURI = 'http://io-informatics.com/rdf/'):
        '''Assigns an rdflib entity class to each object.
        Name based on the name of the python class the object is an instance of
        '''
        self.ns = rdflib.Namespace(baseURI)
        self.classType = self.ns[self.__class__.__name__]
    
    def newGraph(self):
        '''creates a new, empty graph'''
        return rdflib.ConjunctiveGraph()
    
    def getGraphName(self, filename):
        if "/" in filename:
            graphName = filename.split("/")
        elif "\\\\" in filename:
            graphName = filename.split("\\\\")
        elif "\\" in filename:
            graphName = filename.split("\\")
        return graphName
        
    
    def readGraphFile(self, filename, format = "nt"):
        curDir = os.getcwd()
        graph = self.newGraph()
        graphName = self.getGraphName(filename)
        #if "/" in filename:
        #   graphName = filename.split("/")
        #elif "\\\\" in filename:
        #    graphName = filename.split("\\\\")
        #elif "\\" in filename:
        #   graphName = filename.split("\\")    
        file = graphName[-1]
        path = "/".join(graphName[:-1])
        os.chdir(path)
        graph.parse(file, format = format)
        os.chdir(curDir)
        return graph

    def joinGraphs(self, *graphs):
        '''puts all rdflib.ConjunctiveGraph objects together in one new graph
        '''
        mergedGraph = self.newGraph()
        for gr in graphs:
            mergedGraph.__iadd__(gr)
        return mergedGraph
    
    def toCamelCase(self, text, startCap = True, spaceAs = "", addHas = False):
        '''Simple camelCase generator
        '''
        string = ''
        items = []
        text = str(text).split()
        for t in text:
            t1 = t[0]
            if len(t)>1:
                newText = t1.capitalize()+t[1:]
            else:
                newText = t1.capitalize()
               
            items.append(newText)
        joinedText = spaceAs.join(items)
        if startCap != True:
            if len(joinedText)==1: joinedText = joinedText.lower()
            else: 
                t1 = joinedText[0].lower()
                joinedText =  t1+joinedText[1:]
        else:
            pass#return joinedText
        if addHas == True:
            finalText = self.toCamelCase('has '+joinedText, startCap =False, spaceAs=spaceAs, addHas = False)
            return finalText
        else: 
            return joinedText
        for item in items:
            string+=item.capitalize()
        if addHas == True:
            string = "has"+string
        else:
            if len(string)>1:
                string = string[0].lower()+string[1:]
            else:
                string = string.lower()
        return string

    def getAttributes(self, obj, key = "attributeList"):
        '''Generator to return attributeType as predicate and attribute as property.
        '''
        attribs = vars(obj).get(key)
        for pred in attribs:
            prop = vars(obj).get(pred)
            yield pred,prop

    def printTriples(self, tripleLimit= None):
        try:
            count = 1
            for s, p, o in self.graph:
                if tripleLimit != None:
                    if count > tripleLimit:
                        break
                print "<%s> <%s> <%s>" %(str(s), str(p), str(o))
                count +=1
        except: 
            if hasattr(self, "graph"): print "no triples or unable to print"
            else: print "no graph entity"


            

class mageRDFMaker(RDFMaker):
    def __init__(self):
        self.predNS = rdflib.Namespace('http://io-informatics.com/rdf/')
    
    '''def mergeDocument(self):
        masterlist = []
        if hasattr(self, 'graph') == False: self.graph = self.newGraph()
        if hasattr(self, 'subsections') == True:
            for itemList in self.subsections:
                for item in itemList:
                    pass'''
    
    def attributeToGraph(self, instance, *args, **kwargs):
        self.checkForGraph()
        for item in self.attributeList:
            self.graph.add((instance, 
                            self.predNS[self.toCamelCase(item, addHas=True)],
                            rdflib.Literal(vars(self)[item])
                            ))
            

