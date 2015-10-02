from iocbuilder import Substitution, AutoSubstitution
from iocbuilder.arginfo import *
from iocbuilder.modules.asyn import AsynIP
from iocbuilder.modules.ADCore import _ADBase
import iocbuilder.modules


class _PSL(AutoSubstitution):
    TemplateFile = "PSL.template"


class PSL(_ADBase):
    _SpecificTemplate = _PSL

    def __init__(self, IP_PORT, BUFFERS=50, MEMORY=0, **args):
        self.ip_port = AsynIP(IP_PORT, name=args["PORT"] + ".ip")
        self.__super.__init__(**args)
        self.__dict__.update(locals())

    ArgInfo = _ADBase.ArgInfo + _SpecificTemplate.ArgInfo + makeArgInfo(
        __init__,
        IP_PORT=Simple('Address and port of the PSL box', str),
        BUFFERS=Simple('Maximum number of NDArray buffers to be created for '
                       'plugin callbacks', int),
        MEMORY=Simple('Max memory to allocate, should be maxw*maxh*nbuffer '
                      'for driver and all attached plugins', int))
    LibFileList = ['PSL']
    DbdFileList = ['PSLSupport']

    def Initialise(self):
        print('# PSLConfig(portName, serverPort, maxBuffers, maxMemory)\n'
              'PSLConfig("{PORT}", "{PORT}.ip", {BUFFERS}, {MEMORY})'.format(
                  **self.__dict__))
