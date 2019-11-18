''' Importing Packages '''
import sys
import nltk
from nltk.corpus.reader.tagged import TaggedCorpusReader
import numpy 

'''
Class Implemetation > TallySolution :
        def __init__ : initialises corpus and syntactic consistent type counters
        def countS : count the number of syntactic consistent type (S ..)
        def countNP : count the number of syntactic consistent type (NP ..)
        def countVP : count the number of syntactic consistent type (VP ..)
        def countDVP : count the number of syntactic consistent type (VP verb (NP ..)(NP ..))
        def countIVP : count the number of syntactic consistent type (VP verb)
'''
class TallySolution:

        def __init__(self, corpusElems):
                self.corpusElems = corpusElems
                self.Scounts = 0
                self.NPcounts = 0
                self.VPcounts = 0
                self.DVPcounts = 0
                self.IVPcounts = 0

        def countS(self):
                #''' Processing elements '''
                for currentindex in range(len(self.corpusElems)):
                        #''' Reading element, one at a time '''
                        elem = str(self.corpusElems[currentindex])
                        ''' Within S tag '''
                        if elem == '(S':
                                self.Scounts = self.Scounts + 1
                print('Sentence ',self.Scounts)

        def countNP(self):
                #''' Processing elements '''
                for currentindex in range(len(self.corpusElems)):
                        #''' Reading element, one at a time '''
                        elem = str(self.corpusElems[currentindex])
                        ''' Within NP tag '''
                        if elem == '(NP':
                                self.NPcounts = self.NPcounts + 1
                print('Noun Phrase ',self.NPcounts)
        def countVP(self):
                #''' Processing elements'''
                for currentindex in range(len(self.corpusElems)):
                        #''' Reading element, one at a time '''
                        elem = str(self.corpusElems[currentindex])
                        ''' Within VP tag '''
                        if elem == '(VP':
                                self.VPcounts = self.VPcounts + 1
                print('Verb Phrase ',self.VPcounts)

        def countDVP(self):
                #''' Processing elements '''
                for currentindex in range(len(self.corpusElems)):
                        #''' Reading element, one at a time '''
                        elem = str(self.corpusElems[currentindex])
                        ''' Within VP tag '''
                        if elem == '(VP':

                                outsideNP = True
                                NPchild = 0
                                maxNP = 2
                                openbrackets = 0
                                closebrackets = 0

                                nextindex = currentindex + 1

                                while nextindex < len(self.corpusElems):

                                        nextelem = str(self.corpusElems[nextindex])

                                        '''
                                        iF : Outside NP, accept NP tag
                                        ELSE IF : Outside NP, no tags allowed. STOP searching further.
                                        ELSE IF : Inside NP, accept any tags. Keep track of tags within NP

                                        IF : Encountering closing brackets, Tally with open brackets.
                                                IF proper CLOSE, then NP child completes. Proceed to the acceptance of next NP child. Repeat.
                                                IF 2 NP childs and no other childs within VP head,
                                                        then closing brackets need to be more than openbrackets, accounting for head VP tag.
                                        '''

                                        if nextelem == '(NP' and outsideNP : #outside NP, can accept NP
                                                openbrackets = openbrackets + 1
                                                NPchild = NPchild + 1
                                                outsideNP = False
                                        elif nextelem[0] == '(' and outsideNP : #Encountering Open bracket other than NP
                                                break #Not a ditransitive verb phrase, can break searching further
                                        elif nextelem[0] == '(' and not outsideNP:
                                                openbrackets = openbrackets + 1
					if nextelem[-1] == ')': #IF encountering Closing bracket'''

                                                sList = list(nextelem)
                                                closebrackets = closebrackets + sList.count(')')

                                                if closebrackets > openbrackets and NPchild < maxNP:
                                                #'''WRONG PHRASE. STOP HERE.'''
                                                        break
                                                elif closebrackets > openbrackets and NPchild == maxNP:
                                                #'''SEARCH SUCCESS. STOP HERE'''
                                                        self.DVPcounts = self.DVPcounts + 1
                                                        break

                                                if openbrackets == closebrackets: #Proper close of NP tag
                                                        outsideNP  = True
                                                        openbrackets = 0
                                                        closebrackets = 0

                                        nextindex = nextindex + 1

                print('Ditransitive Verb Phrase ',self.DVPcounts)


        def countIVP(self):

                for currentindex in range(len(self.corpusElems)):
                        #'''Reading element, one at a time '''
                        elem = str(self.corpusElems[currentindex])
                        '''Within VP tag '''
                        if elem == '(VP':
                                '''Intransitive verb phase'''

                                nextindex = currentindex + 1

                                while nextindex < len(self.corpusElems):

                                        nextelem = str(self.corpusElems[nextindex])

                                        '''NO POS Tags allowed within VP head tag.'''

                                        if nextelem[0] == '(':
                                        #'''WRONG PHRASE. STOP HERE'''
                                                break

                                        if nextelem[-1] == ')':
                                        #'''SEARCH SUCCESS. STOP HERE'''
                                                self.IVPcounts = self.IVPcounts + 1
                                                break

                                        nextindex = nextindex + 1

                print('Intransitive Verb Phrase ',self.IVPcounts)




''' Python Main function '''
def main():

        #''' Accessing Folder'''
        dirpath = str(sys.argv[1]) #sys.argv[0] is the name of the python program, sys.arg[1] is the directory path
        folder = nltk.data.find(dirpath)

        #''' Reading Corpus files '''
        corpus = TaggedCorpusReader(folder,'.*\.prd')

        #''' Extracting sentences in Corpus files '''
        corpusSents = corpus.sents()

        #''' Splitting notes & Combining elements '''
        corpusElems = []
        for corpusSent in corpusSents:
                for elem in corpusSent:
                        corpusElems.append(elem)


        solution = TallySolution(corpusElems)
        solution.countS()
        solution.countNP()
        solution.countVP()
        solution.countDVP()
        solution.countIVP()

''' Python Main function call '''
if __name__=="__main__":
        main()

'''
Note:
The main function call if __name__ == "main" allows us to execute Python files either as reusable modules or standalone programs.
'''

