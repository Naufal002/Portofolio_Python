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
        
        # cmds.text( label="Select joint" )
        # cmds.separator( style="none", height=3 )
        # cmds.rowLayout( numberOfColumns=2 )
        # cmds.textField( "Search_TF",width=150 )
        # cmds.button( width=100, label="Search", c = self.search_fnc)
        # cmds.setParent("..")

        # Finall Button
        cmds.separator( style="none", height=5 )
        cmds.text( label="Add Controll" )
        cmds.separator( style="none", height=3 )
        cmds.button( label="Finall Button", c = self.finall_fnc)
        
        cmds.showWindow()


    # def search_fnc(self,*args):
    #     '''SEARCH FUNCTION'''
    #     sel = cmds.ls(sl = True, type = "joint")
    #     for i in sel:
    #         x = i.split(".")[-1]
    #         var_text = cmds.textField( "Search_TF",q = True, text =True)
    #         if var_text == "":
    #             cmds.textField( "Search_TF", q = True, text = x)
    #         else:
    #             cmds.textField( "Search_TF", q =True, text = var_text + ", " + x)


            
            
    

    def finall_fnc(self,*args):
        '''FINALL BUTTON'''
        sel = cmds.ls(sl = True, type = "joint")
        name_controls = "_CONTROL"
        for i in sel:

            qry_translate = cmds.xform( i, query=True, ws=True, t=True )
            qry_rotate = cmds.xform( i, query=True, ws=True, ro=True )

            control = cmds.circle(name = name_controls.format(i))
            grp = cmds.group(name = "Main Group".format(i))

            cmds.xform( grp, ws=True, t=qry_translate, ro=qry_rotate )
            cmds.parent(control, i, grp)

TransferVertex().TransferVertex_UI()



'''
 for i in sel:
            x = i.split(".")[-1]
            var_text = cmds.textField( "Search_TF", q=True, text=True ) 
            
            if var_text == "" :
                cmds.textField( "Search_TF", e=True, text=x )
            else :
                cmds.textField( "Search_TF", e=True, text=var_text + ", " + x )
'''