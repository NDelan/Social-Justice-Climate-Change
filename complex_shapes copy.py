
import GraphicsPlus as gr
import random
import time


def draw (objlist , win):
    '''Function iterates through and draws each item in 'objlist' '''
    for item in objlist:
        item.draw(win)


def pillars_init(x,y,scale,line_width = 5):
    '''Function stores rectangular pillars of height 'height' in 'shape' list '''
    shapes = [] 
    # collection of different pillar heights
    height = [50,70,70,80,90,120]
    # creates rectangular pillars at different locations)
    for i in range(6):
        r = gr.Rectangle(gr.Point(x, y),gr.Point(x + 12*scale, y - height[i]* scale))
        x +=21*scale
        shapes.append(r)
        r.setWidth(5)
        r.setFill(gr.color_rgb(185 ,185 ,185))

    return shapes


def face_init(x,y,scale):
    '''Draws a face like shape using Polygon method'''

    shapes = []
    face = gr.Polygon(gr.Point(x, y), gr.Point(x + 120 * scale, y), gr.Point(x + 120 * scale, y + 20 * scale), gr.Point(x + 110 * scale, y+40*scale), gr.Point(x + 90 * scale, y+60*scale),gr.Point(x+65*scale, y+70*scale),gr.Point(x+55*scale, y+70*scale),gr.Point(x+30*scale, y+60*scale),gr.Point(x + 10 * scale, y+40*scale),gr.Point(x, y+20*scale),gr.Point(x, y))
    face.setFill(gr.color_rgb(200, 170, 150))
    face.setWidth(2)
    shapes.append(face)
    return shapes


def ear_init(x,y,scale):
    '''Draws right and left ear using Polygon method'''
    shapes = []
    r_ear= gr.Polygon(gr.Point(x, y+5*scale), gr.Point(x - 5*scale, y+5*scale),gr.Point(x - 2*scale, y+15*scale),gr.Point(x, y+15*scale))
    l_ear = gr.Polygon(gr.Point(x + 120*scale, y+5*scale), gr.Point(x + 125*scale, y+5*scale),gr.Point(x + 122*scale, y+15*scale),gr.Point(x + 120*scale, y+15*scale))
    r_ear.setFill(gr.color_rgb(200, 170, 150))
    l_ear.setFill(gr.color_rgb(200, 170, 150))
    r_ear.setWidth(2)
    l_ear.setWidth(2)
    shapes.append(r_ear)
    shapes.append(l_ear)

    return shapes


def nose_init(x,y,scale):
    '''Draws a nose shape using inbuild polygon method'''
    shapes = []
    nose = gr.Polygon(gr.Point(x+54*scale, y),gr.Point(x+52*scale, y+4),gr.Point(x + 56*scale, y+7*scale),gr.Point(x + 64*scale, y+7*scale), gr.Point(x + 68*scale, y+4),gr.Point(x + 66*scale, y))
    l_nostril = gr.Polygon(gr.Point(x + 57*scale, y+7*scale),gr.Point(x + 58*scale, y+5*scale))
    r_nostril = gr.Polygon(gr.Point(x + 63*scale, y+7*scale),gr.Point(x + 62*scale, y+5*scale))

    nose.setFill(gr.color_rgb(200, 170, 150))
    nose.setWidth(2)
    shapes.append(nose)
    shapes.append(l_nostril)
    shapes.append(r_nostril)

    return shapes


def mouth_init(x,y,scale):
    '''Draws a mouth shape using inbuild Oval method'''
    shapes = []
    outer = gr.Oval(gr.Point(x+48*scale, y+30*scale), gr.Point(x + 72*scale, y+43*scale))
    inner = gr.Oval(gr.Point(x+52*scale, y+33*scale), gr.Point(x + 68*scale, y+40*scale))

    outer.setFill(gr.color_rgb(200, 170, 150))
    inner.setFill('black')
    shapes.append(outer)
    shapes.append(inner)

    return shapes


def hand_init(x,y,scale):
    '''Creates hand shape using Polygon and Line inbuild method'''
    shapes = []
    hand = gr.Polygon(gr.Point(x+58*scale, y+20*scale), gr.Point(x + 62*scale, y+20*scale),gr.Point(x + 62*scale, y+70*scale),gr.Point(x + 43*scale, y+70*scale), gr.Point(x + 43*scale, y+55*scale),gr.Point(x + 58*scale, y+55*scale),gr.Point(x+58*scale, y+20*scale))
    hand.setFill(gr.color_rgb(200, 170, 150))
    hand.setWidth(2)
    shapes.append(hand)
    #Draws four lines on hand
    for i in range(4):   
        line = gr.Line(gr.Point(x+43*scale, y+59*scale),gr.Point(x + 54*scale, y+59*scale))
        shapes.append(line)
        line.setWidth(2)
        y += 3*scale

    return shapes


def smk_init(x,y,scale):
    '''Creates bubble to represent smoke'''
    shapes = []

    # i number of bubbles
    i = 0
    while i<50*scale:

        # Randomly changing the position of bubble to look disordered and natural
        if i%2 == 0:
            x += random.randint(2,5)*scale
            y += random.randint(2,5) *scale
        else:
            x -= random.randint(2,5)*scale
            y -= random.randint(2,5)*scale
      
        # Create center, right and left bubbles
        factor = (50)//2                           # controls the radius of the circle
        cf = gr.Circle(gr.Point(x,y),i*scale/2)
        rf =  gr.Circle(gr.Point(x+i*scale/2, y-i*scale/2),i*scale/2)
        lf =  gr.Circle(gr.Point(x-i*scale/2, y-i*scale/2),i*scale/2)
        lf.setFill('#5c8a8a')
        rf.setFill('#5c8a8a')
        cf.setFill('#5c8a8a')
        shapes.append(cf)
        shapes.append(rf)
        shapes.append(lf)

            # x -= i
        # Moves the following line of bubbles to be created up by 'i*scale' units
        y -= i*scale
        i+=1

        # time.sleep(0.05)
        # win.update()
    return shapes


def smk_static_init(x,y,scale):
    shapes = []

    # i number of bubbles
    i = 0
    while i<50*scale:

        """Randomly changing the position of bubble to look disordered and natural"""
        if i%2 == 0:
            x += random.randint(2,5)*scale
            y += random.randint(2,5) *scale
        else:
            x -= random.randint(2,5)*scale
            y -= random.randint(2,5)*scale
      
        '''Create center right and left bubbles'''
        cf = gr.Circle(gr.Point(x,y),i*scale/2)
        rf =  gr.Circle(gr.Point(x+i*scale/2, y-i*scale/2),i*scale/2)
        lf =  gr.Circle(gr.Point(x-i*scale/2, y-i*scale/2),i*scale/2)
        lf.setFill('#e0e0d1')
        rf.setFill('#5c8a8a')
        cf.setFill('#f5f5f0')
        shapes.append(cf)
        shapes.append(rf)
        shapes.append(lf)

            # x -= i
        '''Moves the following line of bubbles to be created up by 'i*scale' units'''
        y -= i*scale
        i+=1

    return shapes

def draw_list (objlist,win):
    for item in objlist:
        item.draw(win)

def undraw (objlist,win):
    '''Undraws any drawn object in 'object_list' '''
    for item in objlist:
        item.undraw()


def static(obj,win):
    '''Draws static smoke bubbles'''
    for i in range(6):
        draw_list(obj[1][i],win) 


def animate(obj,win):
    '''Draws and undraws smoke to form animation'''
    a = 0
    while a == 0:                     #never-ending loop
        for i in obj:
            for j in range(len(i)):
                draw_list(i[j],win)
                undraw(i[j],win)


def smoke(x,y,scale):
    '''Forms a list of list of smokes'''
    smokes = []
    smoke1 = []
    smoke2 = []
    smoke3 = []
    height = [50,70,70,80,90,120]
    for i in range(6):
        fac = height[i] // (160-height[i])
        smk1 = smk_init(x+6*scale,y-height[i]*scale,0.5 + fac)
        smk2 = smk_init(x+6*scale,y-height[i]*scale,0.5 + fac)
        smk3 = smk_init(x+6*scale,y-height[i]*scale,0.5 + fac)
        smoke1.append(smk1)
        smoke2.append(smk2)
        smoke3.append(smk3)
        x +=21*scale
    smokes.append(smoke1)
    smokes.append(smoke2)
    smokes.append(smoke3)    
    return smokes

    
def platform(x,y,scale):
    '''Forms two rectangular boxes for the background'''
    shapes = []
    rec1 = gr.Rectangle(gr.Point(x-40,y),gr.Point(x+140*scale,y-200*scale))
    rec2 = gr.Rectangle(gr.Point(x-40,y),gr.Point(x+140*scale,y+200*scale))
    rec1.setFill('#990000')
    shapes.append(rec1)
    shapes.append(rec2)

    return shapes

def sun_init(x,y,scale):
    '''Forms the sun with 4 color layers'''
    shapes = []
    colors = ['#ff1a1a','#ff5500','#ff9966','#ffffff']

    for i in range(4):
        outermost = gr.Circle(gr.Point(x+60*scale, y-90*scale), 20*(4-i)*scale)
        outermost.setFill(colors[i])
        shapes.append(outermost)

    return shapes
