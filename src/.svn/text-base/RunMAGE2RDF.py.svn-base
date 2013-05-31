'''
Created on 08 Aug,2011

@author: jeshleman@io-informatics.com //jae@lmi.net
'''

print 'running %s' %__name__

if __name__ == '__main__':
    
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
        rootIn = "./XML_in/"
        fileList = os.listdir(r"./XML_in/")
        for file in fileList:
            if os.path.isfile(rootIn+file):
                if file.lower().endswith(".xml"):
                    fileRoot = file.split(".")[0]
                    try:
                        print "opening %s" %file
                        doc = Document()
                        doc.readDocument(rootIn+file)
                        print "read document, beginning xml to rdf conversion"
                        doc.processSubSection(classDictionary = classDictionary)
                        doc.connectAllGraphs()
                        mastergraph = doc.mergeAllgraphs()
                        mastergraph.serialize('./RDF_out/%s.n3' %fileRoot, 'n3')
                        os.rename(rootIn+file,'./XML_processed/%s' %file )
                        print "converted %s" %fileRoot
                    except:
                        os.rename(rootIn+file,'./FailedXMLinfiles/%s' %file )
                        print 'Failed for %s' %fileRoot
        
    