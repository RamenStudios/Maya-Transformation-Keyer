import maya.cmds

## Functions for general functionality ##
# move the specified number of keys forward
def moveKeys(tweens):
    # get current time
    currentTime = cmds.currentTime(query=True)
    # update that time
    for i in range(1, tweens):
        currentTime += 1
        cmds.currentTime(currentTime)
        print('Moved key')
# ensures the given object exists
def ensureExist(objName):
    if not cmds.objExists(f'{objName}'):
        cmds.polyCube(name=f'{objName}')
        return False
    else:
        print('obj exists')
        return True
########################################

## Functions for rotate functionality ##
# rotate on x and set new keyframe
def rotateX(objName, currentRotate, objSpace, worldSpace):
    cmds.rotate(currentRotate, f'{objName}', rotateX=True, worldSpace=worldSpace, objectSpace=objSpace)
    cmds.setKeyframe(f'{objName}', at='rotateX')
# rotate on y and set new keyframe
def rotateY(objName, currentRotate, objSpace, worldSpace):
    cmds.rotate(currentRotate, f'{objName}', rotateY=True, worldSpace=worldSpace, objectSpace=objSpace)
    cmds.setKeyframe(f'{objName}', at='rotateY')
# rotate on z and set new keyframe
def rotateZ(objName, currentRotate, objSpace, worldSpace):
    cmds.rotate(currentRotate, f'{objName}', rotateZ=True, worldSpace=worldSpace, objectSpace=objSpace)
    cmds.setKeyframe(f'{objName}', at='rotateZ')
# applies the rotations
def applyRotations():
    # get our values
    rotations = cmds.intSliderGrp('NumberofTransformations', query=True, value=True)
    tweens = cmds.intSliderGrp('FramesBtwnKeys', query=True, value=True)
    maxRotate = cmds.intSliderGrp('TransformationAmount', query=True, value=True)
    objName = cmds.textFieldGrp('ObjectName', query=True, text=True)
    #print(cmds.listAttr(f'{objName}'))
    # get our bools
    world = False if cmds.radioButtonGrp('space', query=True, select=True) == 1 else True
    obj = False if cmds.radioButtonGrp('space', query=True, select=True) == 2 else True
    print(f'world:{world} obj:{obj}')
    x = True if cmds.radioButtonGrp('axis', query=True, select=True) == 1 else False
    y = True if cmds.radioButtonGrp('axis', query=True, select=True) == 2 else False
    z = True if cmds.radioButtonGrp('axis', query=True, select=True) == 3 else False
    print(f'x:{x} y:{y} z:{z}')
    # ensure the object exists
    exists = ensureExist(objName)
    # generate our rotation indexing values
    currentRotate = 0
    currentRotate += int(round(cmds.getAttr(f'{objName}.rz')))
    rotateIncrement = int(round(maxRotate/rotations))
    print(f'rotateIncrement:{rotateIncrement}')
    # run the rotations
    while currentRotate <= maxRotate:
        if x:
            rotateX(objName, currentRotate, obj, world)
        elif y:
            rotateY(objName, currentRotate, obj, world)
        if z:
            rotateZ(objName, currentRotate, obj, world)
        currentRotate += rotateIncrement
        moveKeys(tweens)
########################################

## Functions for translate functionality ##
# translate on x and set new keyframe
def translateX(objName, currentTranslate, objSpace, worldSpace):
    cmds.move(currentTranslate, f'{objName}', x=True, worldSpace=worldSpace, objectSpace=objSpace)
    cmds.setKeyframe(f'{objName}', at='translateX')
# translate on y and set new keyframe
def translateY(objName, currentTranslate, objSpace, worldSpace):
    cmds.move(currentTranslate, f'{objName}', y=True, worldSpace=worldSpace, objectSpace=objSpace)
    cmds.setKeyframe(f'{objName}', at='translateY')
# translate on z and set new keyframe
def translateZ(objName, currentTranslate, objSpace, worldSpace):
    cmds.move(currentTranslate, f'{objName}', z=True, worldSpace=worldSpace, objectSpace=objSpace)
    cmds.setKeyframe(f'{objName}', at='translateZ')
# applies the translations
def applyTranslations():
    # get our values
    translations = cmds.intSliderGrp('NumberofTransformations', query=True, value=True)
    tweens = cmds.intSliderGrp('FramesBtwnKeys', query=True, value=True)
    maxTranslate = cmds.intSliderGrp('TransformationAmount', query=True, value=True)
    objName = cmds.textFieldGrp('ObjectName', query=True, text=True)
    #print(cmds.listAttr(f'{objName}'))
    # get our bools
    world = False if cmds.radioButtonGrp('space', query=True, select=True) == 1 else True
    obj = False if cmds.radioButtonGrp('space', query=True, select=True) == 2 else True
    print(f'world:{world} obj:{obj}')
    x = True if cmds.radioButtonGrp('axis', query=True, select=True) == 1 else False
    y = True if cmds.radioButtonGrp('axis', query=True, select=True) == 2 else False
    z = True if cmds.radioButtonGrp('axis', query=True, select=True) == 3 else False
    print(f'x:{x} y:{y} z:{z}')
    # ensure the object exists
    exists = ensureExist(objName)
    # generate our translation indexing values
    currentTranslate = 0
    currentTranslate += int(round(cmds.getAttr(f'{objName}.tz')))
    translateIncrement = int(round(maxTranslate/translations))
    print(f'translateIncrement:{translateIncrement}')
    # run the translations
    while currentTranslate <= maxTranslate:
        if x:
            translateX(objName, currentTranslate, obj, world)
        elif y:
            translateY(objName, currentTranslate, obj, world)
        if z:
            translateZ(objName, currentTranslate, obj, world)
        currentTranslate += translateIncrement
        moveKeys(tweens)
########################################

## Functions for scale functionality ##
# scale on x and set new keyframe
def scaleX(objName, currentScale, objSpace, worldSpace):
    cmds.scale(currentScale, f'{objName}', scaleX=True, worldSpace=False, objectSpace=True)
    cmds.setKeyframe(f'{objName}', at='scaleX')
# scale on y and set new keyframe
def scaleY(objName, currentScale, objSpace, worldSpace):
    cmds.scale(currentScale, f'{objName}', scaleY=True, worldSpace=False, objectSpace=True)
    cmds.setKeyframe(f'{objName}', at='scaleY')
# scale on x and set new keyframe
def scaleZ(objName, currentScale, objSpace, worldSpace):
    cmds.scale(currentScale, f'{objName}', scaleZ=True, worldSpace=False, objectSpace=True)
    cmds.setKeyframe(f'{objName}', at='scaleZ')
# applies the scales
def applyScales():
    # get our values
    scales = cmds.intSliderGrp('NumberofTransformations', query=True, value=True)
    tweens = cmds.intSliderGrp('FramesBtwnKeys', query=True, value=True)
    maxScale = cmds.intSliderGrp('TransformationAmount', query=True, value=True)
    objName = cmds.textFieldGrp('ObjectName', query=True, text=True)
    #print(cmds.listAttr(f'{objName}'))
    # get our bools
    world = False if cmds.radioButtonGrp('space', query=True, select=True) == 1 else True
    obj = False if cmds.radioButtonGrp('space', query=True, select=True) == 2 else True
    print(f'world:{world} obj:{obj}')
    x = True if cmds.radioButtonGrp('axis', query=True, select=True) == 1 else False
    y = True if cmds.radioButtonGrp('axis', query=True, select=True) == 2 else False
    z = True if cmds.radioButtonGrp('axis', query=True, select=True) == 3 else False
    print(f'x:{x} y:{y} z:{z}')
    # ensure the object exists
    exists = ensureExist(objName)
    # generate our scaling indexing values
    currentScale = 0
    currentScale += int(round(cmds.getAttr(f'{objName}.scaleZ')))
    scaleIncrement = int(round(maxScale/scales))
    print(f'scaleIncrement:{scaleIncrement}')
    # run the scaling
    while currentScale <= maxScale:
        if x:
            scaleX(objName, currentScale, obj, world)
        elif y:
            scaleY(objName, currentScale, obj, world)
        if z:
            scaleZ(objName, currentScale, obj, world)
        currentScale += scaleIncrement
        moveKeys(tweens)
########################################

# ## Functions for frame moving function ##
# def rippleMoveKeys(arg):
    # # get inputs
    # moveAmount = cmds.intSliderGrp('NumberofKeys', query=True, value=True)
    # forward = True if cmds.radioButtonGrp('direction', query=True, select=True) == 1 else False
    # backward = True if cmds.radioButtonGrp('direction', query=True, select=True) == 2 else False
    # moveAmount = (moveAmount*-1) if backward else moveAmount
    # # get current time
    # currentTime = cmds.currentTime(query=True)
    # # move all frames from current time onward by specified amount
    # cmds.keyframe(time=(f'{currentTime}:',), timeChange=moveAmount)
# ########################################

##### Functions for window creation/deletion ####
def makeWindow(windowName, windowTitle):
    # avoid 'already exists' bug
    if cmds.window(f'{windowTitle}', query=True, exists=True):
        deleteWindow(windowTitle)
    
    # create window box
    window = cmds.window(f'{windowTitle}', title=f'{windowTitle}', iconName=f'{windowName}', widthHeight=(520,620), menuBar=True)
    
    # create the menuBar
    filemenu = cmds.menu(label='File')
    cmds.menuItem(label='Reset', parent=filemenu, command=('makeWindow(\"' + windowName + '\",\"' + windowTitle + '\")' ))
    cmds.menuItem(label='Quit', parent=filemenu, command=('cmds.deleteUI(\"' + windowTitle + '\", window=True)'))
    
    # set the layout
    cmds.frameLayout(lv = 0)
    cmds.columnLayout(adjustableColumn=True)
    cmds.rowLayout( numberOfColumns=4 )
    
    cmds.separator()
    cmds.setParent('..')
    
    # descriptive text
    cmds.text('Desc', label="Enter the name of the object you'd like to transform. If the object doesn't exist, a default cube will be generated. Then select the desired transformation.", align="left", wordWrap=True)
    # allows user to give object name
    cmds.textFieldGrp('ObjectName', label='Object Name', text='newCube', columnAlign=[1, 'left'])
    
    cmds.separator(height = 20, width = 400)
    
    # allows user to choose whether they are rotating, translating, or scaling
    cmds.radioButtonGrp('type', label='Transformation', labelArray3=['Rotate', 'Translate', 'Scale'], numberOfRadioButtons=3, select=1, columnAlign=[1, 'left'])
    
    cmds.separator(height = 20, width = 400)
    
    # allows user to enter how many transformations they want to animate
    # how many frames to put between the keyframes
    # and the maximum amount of units to transform by (360 by default)
    cmds.intSliderGrp('NumberofTransformations', label='Number of Transformations', field=True, minValue=1, maxValue=10, fieldMinValue=1, fieldMaxValue=100, value=1, columnAlign=[1, 'left'])
    cmds.intSliderGrp('FramesBtwnKeys', label='Frames Btwn Keys', field=True, minValue=1, maxValue=10, fieldMinValue=1, fieldMaxValue=100, value=1, columnAlign=[1, 'left'])
    cmds.intSliderGrp('TransformationAmount', label='Max Transformations (Units)', field=True, minValue=1, maxValue=360, fieldMinValue=1, fieldMaxValue=7200, value=360, columnAlign=[1, 'left'])
    
    cmds.separator(height = 20, width = 400)
    
    # radio group to choose which axis the rotation is on
    cmds.radioButtonGrp('axis', label='Rotation Axis', labelArray3=['X', 'Y', 'Z'], numberOfRadioButtons=3, select=1, columnAlign=[1, 'left'])
    
    cmds.separator(height = 20, width = 400)
    
    # radio group to choose if world or object space
    cmds.radioButtonGrp('space', label='Working Space', labelArray2=['Object', 'World'], numberOfRadioButtons=2, select=2, columnAlign=[1, 'left'])
    
    cmds.separator(height = 20, width = 400)
    
    # buttons to apply transformations
    cmds.button(label='Apply Transformations', command=applyTransformations)
    
    # cmds.separator(height = 20, width = 400)
    
    # # allows user to ripple move keyframes on timeline
    # cmds.text('DescKeys', label="Ensure your selected key+the keys after it are the keys you want to move. Then enter the amount you want to move them by, and whether you are moving forwards or backwards.", align="left", wordWrap=True)
    # cmds.intSliderGrp('NumberofKeys', label='# Of Keys to Move By', field=True, minValue=1, maxValue=10, fieldMinValue=1, fieldMaxValue=100, value=1, columnAlign=[1, 'left'])
    # cmds.radioButtonGrp('direction', label='Movement Direction', labelArray2=['Forwards', 'Backwards'], numberOfRadioButtons=2, select=2, columnAlign=[1, 'left'])
    # cmds.button(label='Ripple Move', command=rippleMoveKeys)
    
    cmds.showWindow(windowTitle)

def deleteWindow(windowTitle):
    cmds.deleteUI(f'{windowTitle}')
########################################

######## Functions for window UI #######
def applyTransformations(args):
    transType = cmds.radioButtonGrp('type', query=True, select=True)
    if transType == 1:
        applyRotations()
    elif transType == 2:
        applyTranslations()
    elif transType == 3:
        applyScales()
########################################

######### Creating the window ##########
makeWindow("Animation Helper", "AnimationHelper")
########################################