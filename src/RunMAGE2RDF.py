'''
Created on 08 Aug,2011
last updated 5/31/2013
@author: jeshleman@io-informatics.com //jae@lmi.net


"Main" class to execute code.  

To execute
    Set variable runRoot in the code below.  
    The runRoot variable should point to an accessible directory that itself 
    contains the subDirectories "XML_in", "XML_out",RDF_out" and "FailedXMLinfiles".
	This path should utilize forward ("/") slashes and should contain a trailing slash.
    
    MAGE-ML documents to be converted are placed in the "XML_in" directory.
    Once converted, the source document will be moved to "XML_out" and 
    a n3 serialization will be written to "RDF_out".
    Files that cannot be converted will be moved to "FailedXMLinfiles"
    
    
    
'''

runRoot = r'C:/Users/jeshleman.IO-INFORMATICS/Desktop/MAGE_2_RDF/' #path to directory, must contain trailing slash

print 'running %s' %__name__

while True:   # if __name__ == '__main__':
    
    import os
    from MAGE_ML import MAGE_ML
    from Document import Document
    from AuditAndSecurity import AuditAndSecurity
    from BioAssay import BioAssayPackage
    from QuantitationType import QuantitationTypePackage
    from Protocol import ProtocolPackage
    from Array import ArrayPackage
    from ArrayDesign import ArrayDesignPackage
    from BioMaterial import BioMaterialPackage
    from BioAssayData import BioAssayDataPackage
    from Experiment import ExperimentPackage
    
    classDictionary = {"MAGE-ML":MAGE_ML,
                   "AuditAndSecurity_package":AuditAndSecurity,
                   'Protocol_package':ProtocolPackage, #'Protocol_assnlist':ProtocolList,'Protocol':Protocol
                   'BioMaterial_package':BioMaterialPackage,
                   'Array_package':ArrayPackage,
                   'ArrayDesign_package':ArrayDesignPackage,
                   'BioAssay_package':BioAssayPackage,
                   'QuantitationType_package':QuantitationTypePackage,
                   "BioAssayData_package": BioAssayDataPackage,
                   'Experiment_package':ExperimentPackage #"BioAssayData_assnlist":BioAssayData,
                   }
    print "working..."

    while 1:
        print "starting cycle"
        inDir = runRoot+"/XML_in/"
        fileList = os.listdir(inDir)
        for file in fileList:
            if not file: break
            if os.path.isfile(inDir+file):
                if file.lower().endswith(".xml"):
                    fileRoot = file.split(".")[0]
                try:
                    print "opening %s" %file
                    doc = Document()
                    doc.readDocument(inDir+file)
                    print "read document, beginning xml to rdf conversion"
                    doc.processSubSection(classDictionary = classDictionary)
                    doc.connectAllGraphs()
                    mastergraph = doc.mergeAllgraphs()
                    mastergraph.serialize(runRoot+'/RDF_out/%s.n3' %fileRoot, 'n3')
                    os.rename(inDir+file, runRoot+'/XML_processed/%s' %file )
                    print "converted %s" %fileRoot
                except:
                    os.rename(inDir+file,runRoot+'/FailedXMLinfiles/%s' %file )
                    print 'Failed for %s' %fileRoot
    
	print "fin!"