# Moving Emitter System
# 2015 Sendo <sendogfx@gmail.com>

init python:

    from random import randrange,uniform
    import math

    class Emitter(renpy.Displayable):
        def __init__(self, image, head=None, x1=0, y1=0, x2=0, y2=0, min_age=0.5, max_age=2.0, jitter=False, jitter_speed=0, time=1, count=48, *args, **kwargs):
            super(renpy.Displayable, self).__init__(*args,**kwargs)

            self.count      = count
            self.x1         = x1
            self.y1         = y1
            self.x2         = x2
            self.x2         = y2
            self.image      = image
            self.image_head = head
            self.min_age    = min_age
            self.max_age    = max_age
            self.reset      = True
            self.old_st     = 0
            self.time       = time
            self.jitter     = jitter
            self.jitter_speed = jitter_speed

            # precompute some stuff
            self.angle      = math.atan2(y2-y1, x2-x1)
            self.distance   = math.hypot(x2-x1, y2-y1)
            self.vx         = math.cos(self.angle)
            self.vy         = math.sin(self.angle)

            self.particles = []

        def reset_positions(self):
            self.particles = []
            self.reset = True

        def create_particle(self,x,y,stt):
            return {
                        'x': x,
                        'y': y,
                        'init_scale': uniform(0.25,0.5),
                        'age': uniform(self.min_age,self.max_age),
                        'st': stt,
                        'rot': randrange(0,360),
                        'dir': renpy.random.choice([-1,1]),
                        'jx': randrange(-5,5) if self.jitter_speed <= 0 else randrange(-self.jitter_speed,self.jitter_speed),
                        'jy': randrange(-5,5) if self.jitter_speed <= 0 else randrange(-self.jitter_speed,self.jitter_speed),
                    }

        def render(self, width, height, st, at):
            render = renpy.Render(0,0)

            if self.reset:
                self.reset_positions()
                self.old_st = st # - self.old_st
                self.reset  = False

            stt = st - self.old_st

            age = stt/self.time # normalize

            if age >= 1:
                age = 1

            x = self.x1 + age * self.distance * self.vx
            y = self.y1 + age * self.distance * self.vy

            for i,v in enumerate(self.particles):
                if stt - v['st'] >= v['age']:
                    del self.particles[i]

            # create as many particles
            if stt < self.time:
                if len(self.particles) < self.count:
                    self.particles.append(self.create_particle(x,y,stt))

            # move particles
            for p in self.particles:
                current_age = (stt-p['st'])/p['age']
                z = 1.0 - current_age
                p['rot'] += p['dir']*3
                p['y'] -= 5 * current_age

                if self.jitter:
                    p['x'] += p['jx']
                    p['y'] += p['jy']

                t = Transform(child=self.image, rotate=p['rot'], subpixel=True, zoom = z if z>0 else 0, alpha = z if z>0 else 0, xanchor=0.5, yanchor=0.5)
                pr = renpy.render(t,0,0,stt,at)
                pw, ph = pr.get_size()
                render.blit(pr,(p['x']-pw/2, p['y']-ph/2))

            if self.image_head:
                if stt < self.time:
                    r = renpy.render(self.image_head,0,0,stt,at)
                    w, h = r.get_size()
                    render.blit(r,(x-w/2,y-h/2))

            renpy.redraw(self,0)
            return render

        def visit(self):
            return [self.image, self.image_head]
