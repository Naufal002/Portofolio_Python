import maya.cmds as cmds
import os
os.system('cls')

def funtion_control():
    sel = cmds.ls(sl = True, type = "joint")
    name_controls = "_CONTROL"
    for i in sel:

        qry_translate = cmds.xform( i, query=True, ws=True, t=True )
        qry_rotate = cmds.xform( i, query=True, ws=True, ro=True )

        control = cmds.circle(name = name_controls.format(i))
        grp = cmds.group(name = "Main Group".format(i))

        cmds.xform( grp, ws=True, t=qry_translate, ro=qry_rotate )
        cmds.parent(control, i, grp)

funtion_control()