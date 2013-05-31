#jae: classes for importing text files

class FileImport:
    '''Basic object for importing files.
    readfile:  
        reads text file, turning into list matrix.  intended 
        primarily for delimited text.
    readhandle: 
        reads text file, using open file 'handle'.  Can be used for 
        url's with urllib.urlopen
    readByLine:  
        reads text file, creating a list with each element of list representing the
        a line in the original file.
    
    '''
    def __init__(self, filename = ''):        
        self.filename = filename
    
    def readwholefile(self, filename = ''):
        if filename == '':
            filename = self.filename
            if filename == '':
                print "error: filename undefined"
                return
        handle = open(filename, 'r')
        data = handle.read()
        return data
            
    def readfile(self, filename = '', sep = "\t", strip = True):
        '''reads text file, turning into list matrix.  
        intended primarily for delimited text.
        '''
        if filename == '':
            filename = self.filename
            if filename == '':
                print "error: filename undefined"
                return
        matrix = []
        handle = open(filename, 'r')    
        for x in handle:
            if strip == True:
                x = x.strip()
            if sep in x:
                line = x.split(sep)
                
            else:
                line = [x]
            matrix.append(line)
        handle.close()
        return matrix
    
    def readhandle(self, handle, sep = "\t", strip = True):
        '''reads text from open handle.
        'handle' can be url if 'urllib' library is used.
        (e.g. handle = urllib.urlopen('http://www.dougstats.com/10-11RD.txt') )
        '''
        matrix = []
        for x in handle:
            if strip == True:
                x = x.strip()
            if sep in x:
                line = x.split(sep)
            else:
                line = [x]
            matrix.append(line)
        return matrix
    
    def readByLine(self, handle, strip = True):
        '''reads text file, creating a list with each element of list representing the
        a line in the original file.
        'handle' can be url if 'urllib' library is used.
        (e.g. handle = urllib.urlopen('http://www.dougstats.com/10-11RD.txt') )
        '''
        inList = []
        for x in handle:
            if strip == True:
                x = x.strip()
            inList.append(x)
        return inList
    
    def matrixToFile(self, filename, matrix, sep="\t", append=False):
        '''takes matrix and writes as delimited file. 
        If append=True data will be appended to existing file of same name. 
        '''
        if append==False: writeAppend = 'w'
        else: writeAppend = 'a'
        output = open(filename,writeAppend)
        for line in matrix:
            l = []
            for i in line:
                l.append(str(i))
            l = sep.join(l)
            output.write(l+"\n")
        output.close()
    
    def listToFile(self, filename, outputList, append=False):
        '''takes outputList and makes each item in list a line in 
        text file.
        '''
        if append==False: writeAppend = 'w'
        else: writeAppend = 'a'
        output = open(filename,writeAppend)
        for i in outputList:
            output.write(str(i)+"\n")
        output.close()


'''

class FileSplit:
    def splitfile(self, handle, outfile, lines, append = False):
        #handle = open(filename, "r")
        if append != False:
            output = open(outfile, "a")
        else: output = open(outfile, "w")
        while lines > 0:
            line = handle.readline()
            if not line: break
            output.write(line)
            line = line -1
        #handle.close()
        output.close()
'''

if __name__ == "__main__":
    import os
    os.chdir(r"C:\Users\jeshleman\Documents\DataSets\MoviesLinkedData")
    filename = "linkedmdb-latest-dump.nt"

    '''handle = open(filename, 'r')
    count = 0
    for line in handle:
        if not line: break
        count +=1
        
    handle.close()
    print count
    '''

    blocks = (288683,577367,866050,1154734,1443417,
        1732101, 866050, 1732101, 2,3,4,5)

    fragment = 1
    handle = open(filename, "r")
    for block in blocks:
        #splitter = FileSplit()
        outfile = "linkedmdb-part_%i.nt" %fragment
        output = open(outfile, "w")
        while block > 0:
            line = handle.readline()
            output.write(line)
            if not line: break
            block = block -1
        #splitter.splitfile(filename, outfile, block)
        output.close()
        fragment +=1
    handle.close()
    
    
