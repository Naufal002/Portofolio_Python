import maya.cmds as cmds
import os
os.system('cls')

class Auto_Control:
    
    def __init__ (self) :
        pass
    
    def Auto_Control_UI(self) :
        
        UI_ID = "Auto_Control"
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

        # CheckBox
        cmds.text(label = "")
        cmds.checkBox("Check_Box", label='Unknown' )
        cmds.text(label = "")

    
        # Finall Button
        cmds.separator( style="none", height=5 )
        cmds.text( label="Add Controll" )
        cmds.separator( style="none", height=3 )
        cmds.button( label="Finall Button", c = self.finall_fnc)


        
        cmds.showWindow()


        # ======================================================

        # Funtion Search
    def search_fnc(self, *args):
        '''SEARCH FUNCTION'''
        sel = cmds.ls(sl = True, type = "joint")
        for i in sel:
            cmds.textField( "Search_TF",e = True, text = i)

            
        #  Finall Button   
    def finall_fnc(self,*args):
        nama_grp = "{0}_GROUP"

        var = cmds.textField( "Search_TF",q = True, text = True)
        qry_translate = cmds.xform( var, query=True, ws=True, t=True )
        qry_rotate = cmds.xform( var, query=True, ws=True, ro=True )

        for i in var:
            controls = cmds.circle( name="{0}_CONTROL".format(i), ch=False )[0]
            groups = cmds.group(controls, name= nama_grp)

            cmds.xform( groups, ws=True, t=qry_translate, ro=qry_rotate )
            cmds.parent(controls, groups)



Auto_Control().Auto_Control_UI()