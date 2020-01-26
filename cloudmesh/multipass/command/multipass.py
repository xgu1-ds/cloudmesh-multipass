from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.multipass.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

class MultipassCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_multipass(self, args, arguments):
        """
        ::

          Usage:
                multipass list
                multipass images
                multipass start [NAME]
                multipass stop [NAME]
                multipass delete [NAME]
                multipass shell [NAME]
                multipass run [NAME]

          Interface to multipass

          Arguments:
              NAME   the name of the virtual machine

          Options:
              -f      specify the file

        """
        name = arguments.NAME

        VERBOSE(arguments)


        if arguments.list:

            print("list")

            return ""

        elif arguments.images:

            print("images")

            return ""
        
        else:
            Console.error("Not yet implemented")
        return ""
