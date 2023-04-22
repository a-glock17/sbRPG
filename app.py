import time

class MenuNav_Vars:
    def init(self, menuChoiceINT, menuChoiceSTR, isGameActive):
        self.menuChoiceINT = menuChoiceINT
        self.menuChoiceSTR = menuChoiceSTR
        self.isGameActive = isGameActive

def MainMenu():
    MenuNav_Vars.isGameActive = False
    time.sleep(1)
    print("-----sbRPG Menu-----\n1. New Game\n2. Load Game\n3. Settings\n4. Close Game\n--------------------")
    MenuNav_Vars.menuChoiceINT = int(input("Select a menu: "))

    # ! catches invalid value passing and restarts main menu
    if MenuNav_Vars.menuChoiceINT != 1 and MenuNav_Vars.menuChoiceINT != 2 and MenuNav_Vars.menuChoiceINT != 3 and MenuNav_Vars.menuChoiceINT != 4:
        time.sleep(1)
        print("The value you have passed is not valid.")
        time.sleep(2)
        MenuNav_Vars.menuChoiceINT = 0
        MainMenu()

    # * new game
    if MenuNav_Vars.menuChoiceINT == 1:
        pass

    # * load save
    if MenuNav_Vars.menuChoiceINT == 2:
        pass

    # * settings menu
    if MenuNav_Vars.menuChoiceINT == 3:
        pass

    # * closes game
    if MenuNav_Vars.menuChoiceINT == 4:
        pass

if __name__ == '''__main__''':
    MainMenu()