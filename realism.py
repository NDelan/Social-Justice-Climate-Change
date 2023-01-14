'''
Calls other methods form 'complex_shapes.py'
to form a scene.
'''
import GraphicsPlus as gr
import complex_shapes as cs


def main():
    win = gr.GraphWin('Social Realism: Climate Justice', 800 , 800)
    '''Tests all functions created'''

    # Command line argument in conjunction with extension
    
    # Scene
    pillars = cs.pillars_init(300,400,2)
    face = cs.face_init(300,400,2)
    mouth = cs.mouth_init(300,400,2)
    ear = cs.ear_init(300,400,2)
    nose = cs.nose_init(300,400,2)
    hand = cs.hand_init(300,400,2)
    Sun = cs.sun_init(300,400,2)
    plat = cs.platform(300,400,2)

    cs.draw(plat,win)
    cs.draw(Sun,win)
    cs.draw(pillars,win)
    cs.draw(face,win)
    cs.draw(mouth,win)
    cs.draw(ear,win)
    cs.draw(nose,win)
    cs.draw(hand,win) 

    # i =0
    # while i<1:
    s = cs.smoke(300,400,2)
    cs.static(s,win)
    t = cs. smoke(300,400,2)
    cs.animate(t,win)
 
    win.update()
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()


