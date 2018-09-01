# Simple Explode Particle System
# 2015 Sendo <sendogfx@gmail.com>
init python:
    from random import randrange,uniform
    from math import cos, sin

    class ExplodeParticle(renpy.Displayable):
        def __init__(self, image, x=0, y=0, count=32, min_speed=3, max_speed=20, min_age=1.0, max_age=2.0, growth=0, rand_scale=True, gravity=0, fade_after_death=True, *args, **kwargs):
            super(renpy.Displayable, self).__init__(*args,**kwargs)

            self.count     = count
            self.ox        = x
            self.oy        = y
            self.image     = image
            self.particles = []
            self.growth    = growth
            self.gravity   = gravity
            self.fade_after_death = fade_after_death
            self.reset     = True
            self.st        = 0

            for x in range(self.count):
                p = {
                        'x': self.ox,
                        'y': self.oy,
                        'angle': randrange(0,360),
                        'speed': randrange(min_speed,max_speed),
                        'init_scale': uniform(0.5,1.0) if rand_scale else 1.0,
                        'age': uniform(min_age,max_age),
                        'st': 0,
                    }
                self.particles.append(p)

        def reset_positions(self):
            for p in self.particles:
                p['x']      = self.ox
                p['y']      = self.oy
                p['angle']  = randrange(0,360)

            self.reset = True

        def render(self, width, height, st, at):
            render = renpy.Render(0,0)

            # when reset, reset timebase and positions
            if self.reset:
                self.reset_positions()
                for p in self.particles:
                    p['st'] = st
                self.reset = False

            for p in self.particles:
                p['x'] += p['speed'] * cos(p['angle'])
                p['y'] += p['speed'] * sin(p['angle'])

                # current age; time passed/age
                stt = st - p['st']
                current_age = stt/p['age']

                # if gravity on, move 5 unit of speed scaled against gravity and age
                if self.gravity<>0:
                    p['y'] += self.gravity * (5*p['speed']) * current_age

                # initial scale, grow/shrink depending on growth value
                z = p['init_scale']
                if self.growth<>0:
                    z += self.growth * current_age

                # decay behavior:
                #   TRUE    = reach death first then fade ie. sparks
                #   FALSE   = fade until death ie. smoke
                if self.fade_after_death:
                    a = 1.0
                    if stt>p['age']:
                        a -= stt-p['age']
                else:
                    a = 1.0 - current_age

                t = Transform(child=self.image, subpixel=True, zoom=z if z>0 else 0, alpha=a if a>0 else 0, xanchor=0.5, yanchor=0.5)

                r = renpy.render(t,0,0,stt,at)

                w,h = r.get_size()

                render.blit(r,(p['x']-w/2,p['y']-h/2))

            renpy.redraw(self,0)
            return render

        def visit(self):
            return [self.image]