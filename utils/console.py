import os
import time
from pystyle import *

fear_banner = """\n\n\n\n\n\n
                                        ╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═   ╔═╗╦ ╦╔═╗╦╔═╔═╗╦═╗
                                        ║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗───╠╣ ║ ║║  ╠╩╗║╣ ╠╦╝
                                        ╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩   ╚  ╚═╝╚═╝╩ ╩╚═╝╩╚═
                                                  Github: SeasonalKirito
\n"""
options_banner = """
                                                        - Options -
                                                    1 |- Spam-Webhook
                                                    2 |- Delete-Webhook
"""

class console():
    def fear_startup(banner=fear_banner, options=False):
        os.system("cls || clear")
        print(Colorate.Horizontal(Colors.blue_to_cyan, banner))
        if options == True:
            print(Colorate.Horizontal(Colors.blue_to_cyan, options_banner))
        else:
            pass
    