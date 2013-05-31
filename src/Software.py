'''
Created on 13 Sep,2011

@author: Jason A. Eshleman -- jae@lmi.net //jeshleman@io-informatics.com
'''

from Parameterizable import Parameterizable

class Software(Parameterizable):
    '''Software is part of the Protocol package
    '''
    def processSubSection(self, *args, **kwargs):
        ''' Terminal point'''
        self.assessAttributes()
        self.internalGraph()