# Bullethole Script
# 2015 Sendo <sendogfx@gmail.com>

init python:

    from random import randrange,uniform

    class Bulletholes(renpy.Displayable):
        def __init__(self, image, time=1, count=32, *args, **kwargs):
            super(renpy.Displayable, self).__init__(*args,**kwargs)

            self.count     = count
            self.image     = image
            self.particles = []
            self.time      = time
            self.st        = 0
            self.reset_particles()

        def reset_particles(self):
            self.particles = []
            for i in xrange(0,self.count):
                self.particles.append({
                        'x': randrange(0,config.screen_width),
                        'y': randrange(0,config.screen_height),
                        's': uniform(0.25, 1.0),
                        'b': uniform(0.0, self.time),
                        'r': randrange(0,360),
                    })

        def render(self, width, height, st, at):
            render = renpy.Render(0,0)

            if st > self.st:
                self.st = st
            else:
                self.reset_particles()
                self.st = st - self.st

            stt = self.st

            for p in self.particles:
                if stt < p['b']:
                    continue

                a = 1
                if stt > self.time:
                    a -= stt - self.time
                    if a <= 0:
                        continue

                t = Transform(child=self.image, subpixel=True, rotate=p['r'], zoom=p['s'], alpha=a, xanchor=0.5, yanchor=0.5)

                r = renpy.render(t,0,0,stt,at)

                render.blit(r,(p['x'],p['y']))

            renpy.redraw(self,0)
            return render

        def visit(self):
            return [self.image]