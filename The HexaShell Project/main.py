#!/usr/bin/python3
import os
import readline
from HexaShell import HexaShell

# Basic lifetime of a shell
#    1.Initialize: In this step, a typical shell would read and execute its 
#       configuration files. These change aspects of the shell’s behavior.
#    2.Interpret: Next, the shell reads commands from stdin 
#       (which could be interactive, or a file) and executes them.
#    3.Terminate: After its commands are executed, the shell 
#       executes any shutdown commands, frees up any memory, and terminates.

hexaShell = HexaShell()
hexaShell.prompt()
