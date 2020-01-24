import pyglet


class VoidWindow(pyglet.window.Window):
    # 16:9 aspect ratio.
    WIDTH = 450
    HEIGHT = 800
    
    def __init__(self):
        super().__init__(
            caption='Void',
            width=VoidWindow.WIDTH,
            height=VoidWindow.HEIGHT
        )
        
        self.label = pyglet.text.Label(
            'Hello void',
            anchor_x='center',
            anchor_y='top',
            x=self.width / 2,
            y=self.height,
        )

    def on_draw(self):
        self.clear()
        self.label.draw()


if __name__ == '__main__':
    VoidWindow()
    pyglet.app.run()
