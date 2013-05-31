'''
Created on 03 May,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''
from Identifiable import Identifiable 
from BioAssayData import BioAssayData
from Person import Person
from Organization import Organization
from BioAssay import BioAssay

class ExperimentPackage(Identifiable):
    ''' ExperimentPackage processes ExperimentPackage section of MAGE-ML.
    Subsections Experiment instances run, vial the ExperimentList or directly to Experiment references.
    '''
    def processSubSection(self, *args, **kwargs):
        classDictionary = {"Experiment_assnlist": ExperimentList,
                           "Experiment":Experiment}
        Identifiable.processSubSection(self, subClass = ExperimentList, subClassKey = "Experiment_assnlist",
                                       classDictionary = classDictionary)

    def internalGraph(self, *args, **kwargs):
        '''Empty method prevents instances from being created.
        Instances of items within will be created if 'internalGraph'
        method is enabled with subClasses.
        '''
        Identifiable.noInteralGraph(self)

class ExperimentList(ExperimentPackage):
    '''Encountered when Experiment_assnlist is found in document.
    Creates Experiment instances.
    '''
    def processSubSection(self, *args, **kwargs):
        Identifiable.processSubSection(self,subClass = Experiment, subClassKey = "Experiment")
                                          

class Experiment(ExperimentList):
    '''Experiment class produces experiment instances.
    Additional sections of MAGE-ML directly linked to the experiment.
    '''
    pass

    def __init__(self):
        '''
        Constructor
        '''
        Identifiable.__init__(self)
        self.instanceOfClass = 'http://mged.sourceforge.net/ontologies/MGEDOntology.owl#Experiment'
    
    def processSubSection(self, *args, **kwargs):
        classDictionary = {"BioAssayData_assnreflist":BioAssayData,
                           "Person_ref": Person, "Organization_ref":Organization,
                           #"Description": Description, 
                           "BioAssays_assnreflist":BioAssay
                           }
        try:
            self.assessAttributes()
        except:
            pass
        for subClassKey, subClass in classDictionary.iteritems():
            if self.subsections.get(subClassKey) == None:
                self.subsections[subClassKey] = []
            Identifiable.processSubSection(self, subClass, subClassKey)
        #self.internalGraph()
    
    def internalGraph(self, *args, **kwargs):
        '''reactivates internal graph, makes instance'''
        Identifiable.internalGraph(self)
        
    def connectGraphs(self, *args, **kwargs):     
        self.addSectionToGraph("MeasuredBioAssayData")   
        self.addSectionToGraph("DerivedBioAssayData")
        self.addSectionToGraph("Person", "hasProvider")
        self.addSectionToGraph("Organization", "hasProvider")
        self.addSectionToGraph("MeasuredBioAssay")   
        self.addSectionToGraph("DerivedBioAssay")
        self.addSectionToGraph("PhysicalBioAssay")
        self.addSectionToGraph("Description")
    