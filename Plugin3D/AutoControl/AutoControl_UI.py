import maya.cmds as cmds
import os
os.system('cls')

class TransferVertex:
    
    def __init__ (self) :
        pass
    
    def TransferVertex_UI(self) :
        
        UI_ID = "Auto_Rig"
        if cmds.window( UI_ID, exists=True ) :
            cmds.deleteUI( UI_ID )
            
        cmds.window( UI_ID, width=250, height=100 )
        cmds.columnLayout( adjustableColumn=True, columnAlign="center" )
        cmds.separator( style="in", height=15 )
        
        cmds.text( label="Select joint" )
        cmds.separator( style="none", height=3 )
        cmds.rowLayout( numberOfColumns=2 )
        cmds.textField( "Search_TF",width=150 )
        cmds.button( width=100, label="Search", c = self.search_fnc)
        cmds.setParent("..")
        
        cmds.separator( style="none", height=5 )
        cmds.text( label="Add Controll" )
        cmds.separator( style="none", height=3 )
        cmds.button( label="Finall Button", c = self.finall_fnc)
        
        cmds.showWindow()


    def search_fnc(self):
        '''SEARCH FUNCTION'''
        sel = cmds.ls(sl = True, type = "joint")
        for i in sel:
            pass
            
    

    def finall_fnc(self):
        '''FINALL BUTTON'''
        pass
            
TransferVertex().TransferVertex_UI()