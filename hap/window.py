from hap.utils import clearScreen, handleInformation, handleSelection, handleOption, loadChar
from hap.constants import WELCOME_MSG, SELECT

windowStack = []

class Window:
    def __init__(self, options: list, information: list = [], manager = None, pretext: str = "", posttext: str = "", welcome: bool = False):
        self.options = options
        self.pretext = pretext
        self.posttext = posttext
        self.welcome = welcome
        self.information = information
        self.manager = manager

    def load(self):
        # Keep track of last opened windows
        windowStack.append(self)

        # While this window is the current window
        while windowStack and windowStack[-1] is self:
            clearScreen()

            if self.welcome: print(WELCOME_MSG)
            handleInformation(self.pretext, self.information)

            # Create a temporary list to not modify self.options
            optionsToShow = list(self.options)

            # Automatically add the back option to the window unless its the main window
            if not self.welcome:
                optionsToShow.append({"text": self.manager.getText("back"), "command": lambda: self.close()})

            handleSelection(self.posttext, optionsToShow)
            handleOption(input(SELECT), optionsToShow)
    
    # Remove from window stack when done
    def close(self):
        if windowStack and windowStack[-1] is self:
            windowStack.pop()

class Letter(Window):
    def __init__(self, options, manager = None, details: dict = {}, reduced: bool = False):
        super().__init__(options, manager, details)
        self.details = details
        self.manager = manager
        self.reduced = reduced

    def load(self):
        # Keep track of last opened windows
        windowStack.append(self)

        # While this window is the current window
        while windowStack and windowStack[-1] is self:
            clearScreen()

            loadChar(self.details, self.manager, self.reduced)

            # Create a temporary list to not modify self.options
            optionsToShow = list(self.options)            
            
            # Automatically add the variations and back option to the window
            if self.details.get("variations"):
                optionsToShow.append({
                    "text": self.manager.getText("variations"),
                    "command": lambda: self.loadVariations()
                })
            optionsToShow.append({"text": self.manager.getText("back"), "command": lambda: self.close()})

            handleSelection(self.posttext, optionsToShow)
            handleOption(input(SELECT), optionsToShow)
    
    def loadVariations(self):
        # Get variations, return if none
        variations = self.details.get("variations", [])
        if not variations: return
        
        # Create and load variations window
        variationWindow = Window(
            [{"text": variation["char"], "command": lambda var=variation: Letter([], self.manager, var, True).load()} for variation in variations],
            [], self.manager, self.manager.getText("variations")
        )
        variationWindow.load()

    # Remove from window stack when done
    def close(self):
        if windowStack and windowStack[-1] is self:
            windowStack.pop()