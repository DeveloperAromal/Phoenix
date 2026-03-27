import os
from colorama import Fore, Style  # type:ignore


class Banner:

    def __init__(self):
        self.width = os.get_terminal_size().columns

    def center(self, text):
        return text.center(self.width)

    def phoenix_banner(self):
        lines = [
            "",
            f"{Fore.RED}                            .-=========={Style.RESET_ALL}",
            f"{Fore.RED}                         .-' {Fore.YELLOW}O{Fore.RED}    ====={Style.RESET_ALL}",
            f"{Fore.RED}                        /___       ==={Style.RESET_ALL}",
            f"{Fore.RED}                           \_      |{Style.RESET_ALL}",
            f"{Fore.RED}_____________________________)    (_____________________________{Style.RESET_ALL}",
            f"{Fore.RED}\___________               .'      `,              ____________/{Style.RESET_ALL}",
            f"{Fore.RED}  \__________`.     |||<   `.      .'   >|||     .'__________/{Style.RESET_ALL}",
            f"{Fore.RED}     \_________`._  |||  <   `-..-'   >  |||  _.'_________/{Style.RESET_ALL}",
            f"{Fore.RED}        \_________`-..|_  _ <      > _  _|..-'_________/{Style.RESET_ALL}",
            f"{Fore.RED}           \_________   |_|  {Fore.YELLOW}//  \\{Fore.RED}  |_|   _________/{Style.RESET_ALL}",
            f"{Fore.RED}                      .-\   {Fore.YELLOW}//    \\{Fore.RED}   /-. {Style.RESET_ALL}",
            f"{Fore.YELLOW}      ,  .         _.'.- `._        _.' -.`._         .  ,{Style.RESET_ALL}",
            f"{Fore.YELLOW}    <<<<>>>>     .' .'  /  '``----''`  \  `. `.     <<<<>>>>{Style.RESET_ALL}",
            f"{Fore.YELLOW}      '/\`         /  .' .'.'/|..|\`.`. `.  \         '/\`{Style.RESET_ALL}",
            f"{Fore.YELLOW}      (())        `  /  / .'| |||| |`. \  \  '        (()){Style.RESET_ALL}",
            f"{Fore.YELLOW}       /\          ::_.' .' /| || |\ `. `._::          /\\{Style.RESET_ALL}",
            f"{Fore.YELLOW}      //\\           '``.' | | || | | `.''`           //\\{Style.RESET_ALL}",
            f"{Fore.YELLOW}      //\\             .` .` | || | '. '.             //\\{Style.RESET_ALL}",
            f"{Fore.YELLOW}      //\\                `  | `' |  '                //\\{Style.RESET_ALL}",
            f"{Fore.YELLOW}      \\//                                            \\//{Style.RESET_ALL}",
            f"{Fore.YELLOW}       \/                                              \/{Style.RESET_ALL}",
            "",
            f"{Fore.WHITE}          P H O E N I X  {Fore.RED}·{Fore.WHITE}  O S I N T  {Fore.RED}·{Fore.WHITE}  R E C O N{Style.RESET_ALL}",
            f"{Fore.RED}       [ deep recon · stealth · intelligence · speed ]{Style.RESET_ALL}",
            "",
        ]

        max_visible = 0
        for line in lines:
            visible = line
            for code in [Fore.RED, Fore.YELLOW, Fore.WHITE, Style.RESET_ALL]:
                visible = visible.replace(code, "")
            max_visible = max(max_visible, len(visible))

        for line in lines:
            visible = line
            for code in [Fore.RED, Fore.YELLOW, Fore.WHITE, Style.RESET_ALL]:
                visible = visible.replace(code, "")
            padding = (self.width - max_visible) // 2
            print(" " * max(padding, 0) + line)