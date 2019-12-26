'''
Created on Mar 5, 2019

@author: Wyatt Muller
'''

import pyglet, win32gui, win32con, gc
from single_rain import Rain
from pyglet.libs.win32.constants import SPI_SETDESKWALLPAPER, SPIF_UPDATEINIFILE

back = pyglet.sprite.Sprite(img=pyglet.image.load('MatrixWallpaper.jpg'))
back.opacity = 128
window = pyglet.window.Window(fullscreen=True)
back.scale_y = window.height / back.height
back.scale_x = window.width / back.width
rain_streaks = []

def spawn(dt):
    rain_streaks.append(Rain())  
    if rain_streaks[-1].overlap:
        del rain_streaks[-1]
        
def update(dt):
    for rain in rain_streaks:
        if not rain.stopped:
            rain.update()
        if len(rain.leads) > 0:
            rain.update_leads()
        elif not rain.fading:
            rain.fading = True
            rain.start_fade(0)
        gc.collect()
            
def background_set(dt, num):
    if (num == 1):
        pyglet.image.get_buffer_manager().get_color_buffer().save('matrix_background.png')
        win32gui.SystemParametersInfo(SPI_SETDESKWALLPAPER, 'C:\\Users\\wtmul\\eclipse-photon\\raining_code\\matrix_background.png', SPIF_UPDATEINIFILE)
        pyglet.clock.schedule_once(background_set, 1/10, num=2)
    else:
        pyglet.image.get_buffer_manager().get_color_buffer().save('matrix_background2.png')
        win32gui.SystemParametersInfo(SPI_SETDESKWALLPAPER, 'C:\\Users\\wtmul\\eclipse-photon\\raining_code\\matrix_background2.png', SPIF_UPDATEINIFILE)
        pyglet.clock.schedule_once(background_set, 1/10, num=1)
        
@window.event
def on_draw():
    window.clear()
    back.draw()
    for obj in rain_streaks:
        for digit in obj.drops:
            digit.draw()
            digit.opacity = digit.opac
            
@window.event
def on_activate():
    #win32gui.ShowWindow(win32gui.FindWindow(None, 'C:\\Windows\\System32\\cmd.exe'), win32con.SW_HIDE)
    win32gui.ShowWindow(win32gui.GetActiveWindow(), win32con.SW_HIDE)

pyglet.clock.schedule_interval(spawn, 2)
pyglet.clock.schedule_interval(update, 1/10)
pyglet.clock.schedule_once(background_set, 1, num=1)
pyglet.app.run()