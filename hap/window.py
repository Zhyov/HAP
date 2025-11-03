from hap.utils import clearScreen, handleInformation, handleSelection, handleOption, loadChar
from hap.constants import WELCOME_MSG, SELECT

windowStack = []

class Window:
    def __init__(self, options: list, information: list = [], manager = None, pretext: str = None, posttext: str = None, welcome: bool = False, autoTranslate: bool = True):
        self.options = options
        self.pretext = pretext
        self.posttext = posttext
        self.welcome = welcome
        self.information = information
        self.manager = manager
        self.translate = autoTranslate

    def _renderInfo(self):
        if self.welcome: print(WELCOME_MSG)
        handleInformation(self.pretext, self.information, self.manager)

    def _getOptions(self):
        options = list(self.options)

        # Automatically add the back option to the window unless its the main window
        if not self.welcome:
            options.append({"text": "back", "command": lambda: self.close()})
        
        return options

    def load(self):
        # Keep track of last opened windows
        windowStack.append(self)

        # While this window is the current window
        while windowStack and windowStack[-1] is self:
            clearScreen()

            self._renderInfo()

            # Create a temporary list to not modify self.options
            optionsToShow = self._getOptions()

            handleSelection(self.posttext, optionsToShow, self.translate, self.manager)
            handleOption(input(SELECT), optionsToShow, self.manager)
    
    # Remove from window stack when done
    def close(self):
        if windowStack and windowStack[-1] is self:
            windowStack.pop()

class Letter(Window):
    def __init__(self, options, manager = None, details: dict = {}, reduced: bool = False, autoTranslate: bool = True):
        super().__init__(options, manager=manager, autoTranslate=autoTranslate)
        self.details = details
        self.reduced = reduced

    def _renderInfo(self):
        loadChar(self.details, self.manager, self.reduced)

    def _getOptions(self):
        options = list(self.options)

        # Automatically add the variations and back option to the window
        if self.details.get("variations"):
            options.append({
                "text": "variations",
                "command": lambda: self.loadVariations()
            })
        options.append({"text": "back", "command": lambda: self.close()})

        return options
    
    def loadVariations(self):
        # Get variations, return if none
        variations = self.details.get("variations", [])
        if not variations: return
        
        # Create and load variations window
        variationWindow = Window(
            [{"text": variation["char"], "command": lambda var=variation: Letter([], self.manager, var, True).load()} for variation in variations],
            [], self.manager, "variations", autoTranslate=False
        )
        variationWindow.load()