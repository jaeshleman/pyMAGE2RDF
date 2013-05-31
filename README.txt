20130527
written by jason eshleman: jae@lmi.net

The classes and execution script enable the tranformation of MAGE-ML
documents into RDF following the Array Express MAGE object model. Input
files are xml documents following the MAGE-ML specifications.  Output is
serialized as n-triples or n3 notation files.

This representation does not currently attempt to align the output with 
any extant ontology for MAGE or other gene expression studies. 


DEPENDENCIES:  requires instalation of the rdflib package for python.  
TESTED with PYTHON ver. 2.7.2
  

	
To execute the code, use the script "RunMAGE2RDF"

    Set variable runRoot in the code below.  
    The runRoot variable should point to an accessible directory that itself 
    contains the subDirectories "XML_in", "XML_out",RDF_out" and "FailedXMLinfiles"
    
    MAGE-ML documents to be converted are placed in the "XML_in" directory.
    Once converted, the source document will be moved to "XML_out" and 
    a n3 serialization will be written to "RDF_out".
    Files that cannot be converted will be moved to "FailedXMLinfiles"
    
    
    
