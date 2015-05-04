class pefile:

    DOS_HEADER_LIST=['e_magic','e_cblp','e_cp','e_crlc',
                'e_cparhdr','e_minalloc','e_maxalloc',
                'e_ss','e_sp','e_csum','e_lfarlc','e_ovno',
                'e_res','e_oemid','e_oeminfo','e_res2','e_lfanew']
    DOS_HEADER_VALUE=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    NT_HEADER_LIST=['signature','fileheader','optionalheader']
    NT_HEADER_VALUE=[0,0,0]

    FILE_HEADER_LIST=['machine','numberofsections','timedatestamp',
                'pointertosymboltable','numberofsymbols',
                'sizeofoptionalheader','characteristics']
    FILE_HEADER_VALUE=[0,0,0,0,0,0,0]

    OPTIONAL_HEADER_LIST=['magic','majorlinkerversion','minorlinkerversion','sizeofcode',
                'sizeofinitializeddata','sizeofuninitializeddata','addressofentrypoint',
                'baseofcode','baseofdata','imagebase','sectionalignment','filealignment',
                'majoroperationSystemVersion','minorOperationSystemVersion',
                'majorImageVersion','minorImageVersion','majorSubsystemVersion','minorSubsystemVersion',
                'win32VersionValue','sizeOfImage','sizeOfHeader','checkSum','subsystem','dllCharacteristics',
                'sizeOfStackReserve','sizeOfStackCommit','sizeOfHeapReserve','sizeOfHeapCommit',
                'loaderFlags','numberOfRvaAndSizes','dataDirectory']
    OPTIONAL_HEADER_VALUE=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    DATA_DIRECTORY_LIST=['virtualAddress','size']
    DATA_DIRECTORY_VALUE=[0,0]


    print(OPTIONAL_HEADER_VALUE[OPTIONAL_HEADER_LIST.index('magic')])

    def __init__(self,fileName):
        self.__read__(fileName)

    def __read__(self,fileName):
            if fileName is None:
                    print 'file is null'
                    return None
            
            print fileName+' in __read__'

            peFile = file(fileName,'rb')
            self.fileno = peFile.fileno()

            #print('a ' +str(self.fileno))

            self.__setValue__('DOS_HEADER','e_magic',3)
            print self.__getValue__('DOS_HEADER','e_magic')



    def __setValue__(self,headerName,attrName,attrValue):
        if headerName=='DOS_HEADER':
            self.DOS_HEADER_VALUE[self.DOS_HEADER_LIST.index(attrName)] = attrValue
        elif headerName=='NT_HEADER':
            self.NT_HEADER_VALUE[self.NT_HEADER_LIST.index(attrName)] = attrValue
        elif headerName=='FILE_HEADER':
            self.FILE_HEADER_VALUE[self.FILE_HEADER_LIST.index(attrName)] = attrValue
        elif headerName=='OPTIONAL_HEADER':
            self.OPTIONAL_HEADER_VALUE[self.OPTIONAL_HEADER_LIST.index(attrName)] = attrValue

    def __getValue__(self,headerName,attrName):
        if headerName=='DOS_HEADER':
            return self.DOS_HEADER_VALUE[self.DOS_HEADER_LIST.index(attrName)]
        elif headerName=='NT_HEADER':
            return self.NT_HEADER_VALUE[self.NT_HEADER_LIST.index(attrName)]
        elif headerName=='FILE_HEADER':
            return self.FILE_HEADER_VALUE[self.FILE_HEADER_LIST.index(attrName)]
        elif headerName=='OPTIONAL_HEADER':
            return self.OPTIONAL_HEADER_VALUE[self.OPTIONAL_HEADER_LIST.index(attrName)]