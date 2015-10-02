from iocbuilder import Substitution, AutoSubstitution
from iocbuilder.modules.ADCore import ADCore, ADBaseTemplate, makeTemplateInstance, includesTemplates
from iocbuilder.arginfo import *
from iocbuilder.modules.asyn import AsynIP, AsynPort
import iocbuilder.modules

@includesTemplates(ADBaseTemplate)
class _PSL(AutoSubstitution):
    TemplateFile = "PSL.template"


class PSL(AsynPort):
    Dependencies = (ADCore,)
    _SpecificTemplate = _PSL
    UniqueName = "PORT"

    def __init__(self, PORT, IP_PORT, BUFFERS=50, MEMORY=0, **args):
        self.ip_port = AsynIP(IP_PORT, name=PORT + ".ip")
        self.__super.__init__(PORT)
        self.__dict__.update(locals())
        makeTemplateInstance(self._SpecificTemplate, locals(), args)

    ArgInfo = ADBaseTemplate.ArgInfo + _SpecificTemplate.ArgInfo + makeArgInfo(
        __init__,
        PORT = Simple('Port name for the detector', str),
        IP_PORT=Simple('Address and port of the PSL box', str),
        BUFFERS=Simple('Maximum number of NDArray buffers to be created for '
                       'plugin callbacks', int),
        MEMORY=Simple('Max memory to allocate, should be maxw*maxh*nbuffer '
                      'for driver and all attached plugins', int))
    LibFileList = ['PSL']
    DbdFileList = ['PSLSupport']

    def Initialise(self):
        print('# PSLConfig(portName, serverPort, maxBuffers, maxMemory)\n'
              'PSLConfig("{PORT}", "{ip_port}", {BUFFERS}, {MEMORY})'.format(
                  **self.__dict__))
