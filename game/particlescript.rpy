init python:
    import math

init:
    ### GENERAL INIT ###
    define sw2 = config.screen_width/2
    define sh2 = config.screen_height/2


    ### IMAGE INIT ###

    # renamed color images used for the particles because of name redundancy
    image p_black = Solid('#000')
    image p_white = Solid('#FFF')

    # LIGHTNING IMAGES
    image la = 'particle/light_a.png'
    image lb = 'particle/light_b.png'
    image lc = 'particle/light_c.png'

    # image cb = 'particle/colossus_beam.png'

    # BLAST IMAGES
    image blast         = 'particle/blast.png'
    image blast_green   = 'particle/blast_green.png'
    image blast_blue    = 'particle/blast_blue.png'
    image baneling_goo  = 'particle/baneling_goo.png'

    # auto hide goo after 1 sec; should eliminate manually hiding it
    image baneling_goo_b:
        align(0,0)
        'particle/baneling_goo.png'
        alpha 1.0
        pause 1.0
        linear 1.0 alpha 0

    # STALKER IMAGES
    image stalker       = 'particle/stalker_laser.png'
    image stalker2      = 'particle/stalker_laser.png'

    image stalker_top   = 'particle/stalker_laser.png'
    image stalker2_top  = 'particle/stalker_laser.png'

    # COLOSSUS IMAGES
    image colossus_beams        = 'particle/colossus_beams.png'
    image colossus_beams_head   = 'particle/colossus_beams_heads.png'
    image colossus_beams_mask   = Solid("#000")



    # PARTICLE IMAGES
    ## SPARK PARTICLES
    define particle_blue        = Image('particle/particle_blue.png')
    define particle_white       = Image('particle/particle_white.png')
    define particle_yellow      = Image('particle/particle_yellow.png')

    ## SMOKE PARTICLES
    define particle_smoke       = Image('particle/particle_smoke.png')
    define particle_smoke_blue  = Image('particle/particle_smoke_blue.png')
    define particle_smoke_green = Image('particle/particle_smoke_green.png')

    ## MISC PARTICLES
    define particle_goo         = Image('particle/particle_goo.png')
    define particle_fire        = Image('particle/particle_fire.png')




    ### EXPLODE PARTICLE SYSTEM INIT ###

    ## TANK BLAST
    define tank_blast_particle       = ExplodeParticle(particle_yellow, min_speed=20, max_speed=40, x=sw2, y= sh2,rand_scale=False,growth=-1)
    define tank_blast_particle_trail = ExplodeParticle(particle_smoke, count=16, min_speed=10, max_speed=20, x=sw2, y= sh2,rand_scale=True,gravity=-1,fade_after_death=False)
    define tank_blast_particle_spark = ExplodeParticle(particle_white, count=16, min_speed=20, max_speed=50, x=sw2, y= sh2,rand_scale=True)

    ## PROTOSS BLAST
    define protoss_blast_particle       = ExplodeParticle(particle_blue, min_speed=3, max_speed= 15, x=sw2, y= sh2,gravity=-.25,growth=-0.5)
    define protoss_blast_particle_smoke = ExplodeParticle(particle_smoke_blue, count=24, min_speed=2, max_speed=5, x=sw2, y= sh2,gravity=-1,fade_after_death=False)
    define protoss_blast_particle_spark = ExplodeParticle(particle_white, count=16, min_speed=2, max_speed=5, x=sw2, y= sh2,gravity=-1)

    ## BANELING BLAST
    define baneling_blast_particle       = ExplodeParticle(particle_goo, count=12, min_speed=25, max_speed=60, x=sw2, y= sh2, growth=0, rand_scale=False)
    define baneling_blast_particle_smoke = ExplodeParticle(particle_smoke_green, count=6, min_speed=10, max_speed=20, x=sw2, y= sh2, fade_after_death=False)

    # EMITTER PARTICLE SYSTEM INIT
    # x1,y1   - origin point
    # x2,y2   - destination point
    # head    - image shown at the emit point
    # jitter  - if True, randomize particle direction
    # max_age - max age for emit particles

    ## MISSILE
    define missile_left   = Emitter(particle_smoke, head=particle_yellow, x1=0, y1=0, x2=sw2, y2=sh2, time=.35)
    define missile_right  = Emitter(particle_smoke, head=particle_yellow, x1=config.screen_width, y1=0, x2=sw2, y2=sh2, time=.35)
    define missile_right2 = Emitter(particle_smoke, head=particle_yellow, x1=config.screen_width, y1=0, x2=sw2, y2=sh2, time=.35)

    ## FLAMETHROWER
    define fire1          = Emitter(particle_fire, head=None, x1=0, y1=config.screen_height/2, jitter=True, max_age= 0.5, x2=config.screen_width, y2=config.screen_height/2, time=0.4)
    define fire2          = Emitter(particle_fire, head=None, x1=config.screen_width, y1=config.screen_height/2, jitter=True, max_age= 0.5, x2=0, y2=config.screen_height/2, time=0.4)

    ## COLOSSUS
    define colossus_spark = Emitter(particle_yellow, head=particle_yellow, jitter=True, jitter_speed=20, count=32, x1=sw2, y1=sh2, x2=sw2, y2=sh2, time=.5)


    # BULLETHOLES INIT
    define bullethole_img   = Image('bullethole.png')
    define bulletholes      = Bulletholes(bullethole_img, count=32)

    # STALKER EXPLODE PARTICLE INIT
    define stalker_blast_particle       = ExplodeParticle(particle_blue, count=8, min_speed=9, max_speed=12, x=sw2-50, y= sh2,gravity=-.5,growth=-0.5)
    define stalker_blast_particle_smoke = ExplodeParticle(particle_smoke_blue, count=12, min_speed=5, max_speed=10, x=sw2-50, y= sh2,gravity=-.5,fade_after_death=False)
    define stalker_blast_particle_spark = ExplodeParticle(particle_white, count=6, min_speed=2, max_speed=5, x=sw2-50, y= sh2,gravity=-2)

    define stalker_blast_particle2       = ExplodeParticle(particle_blue, count=8, min_speed=9, max_speed=12, x=sw2+50, y= sh2,gravity=-.5,growth=-0.5)
    define stalker_blast_particle_smoke2 = ExplodeParticle(particle_smoke_blue, count=12, min_speed=5, max_speed=10, x=sw2+50, y= sh2,gravity=-.5,fade_after_death=False)
    define stalker_blast_particle_spark2 = ExplodeParticle(particle_white, count=6, min_speed=2, max_speed=5, x=sw2+50, y= sh2,gravity=-2)

    # STALKER LASER BEAM INIT
    python:
        stalker_y           = config.screen_height*2    # beam y origin
        stalker_left_from   = 0                         # left beam x origin
        stalker_right_from  = config.screen_width       # right beam x origin

        stalker_dest_y      = config.screen_height/6*2  # beam y destination
        stalker_left_x      = config.screen_width/2-50  # left beam x destination
        stalker_right_x     = config.screen_width/2+50  # right beam x destination

        # let ren'py compute rotation
        rotate_left         = math.degrees(math.atan2(stalker_dest_y-stalker_y, stalker_left_x-stalker_left_from))
        rotate_right        = math.degrees(math.atan2(stalker_dest_y-stalker_y, stalker_right_x-stalker_right_from))


### WRAPPERS ###
init python:

    def show_tank_blast():
        tank_blast_particle.reset_positions()
        tank_blast_particle_trail.reset_positions()
        tank_blast_particle_spark.reset_positions()

        renpy.show('blast', at_list=[blast])
        renpy.show_screen('tank_particles')
        renpy.show('p_white', at_list=[flash])

    def show_protoss_blast():
        protoss_blast_particle.reset_positions()
        protoss_blast_particle_smoke.reset_positions()
        protoss_blast_particle_spark.reset_positions()

        renpy.show('blast_blue', at_list= [blast])
        renpy.show_screen('protoss_particles')
        renpy.show('p_white', at_list=[flash])

    def show_baneling_blast():
        baneling_blast_particle.reset_positions()
        baneling_blast_particle_smoke.reset_positions()

        renpy.show('blast_green', at_list=[blast])
        renpy.show_screen('baneling_particles')
        #renpy.show('p_white', at_list=[flash])
        renpy.show('baneling_goo_b')

    def show_stalker_lasers():
        renpy.show('stalker', at_list=[stalker_laser_left])
        renpy.show('stalker2', at_list=[stalker_laser_right])
        renpy.pause(0.35)
        show_protoss_blast()
        renpy.hide('stalker')
        renpy.hide('stalker2')

    def show_stalker_lasers_top():
        renpy.show('stalker_top', at_list=[stalker_laser_left_top])
        renpy.show('stalker2_top', at_list=[stalker_laser_right_top])
        renpy.pause(0.35)
        show_protoss_blast()
        renpy.hide('stalker_top')
        renpy.hide('stalker2_top')

    def show_stalker_lasers_right():
        renpy.show('stalker2', at_list=[stalker_laser_right])
        renpy.pause(0.35)
        show_protoss_blast()
        renpy.hide('stalker2')

    def show_stalker_blast():
        protoss_blast_particle.reset_positions()
        protoss_blast_particle_smoke.reset_positions()
        protoss_blast_particle_spark.reset_positions()

        renpy.show('blast_blue', at_list= [blast])
        renpy.show_screen('protoss_particles')
        renpy.show('p_white', at_list=[flash])

    def show_flamethrower_left():
        fire1.reset_positions()
        renpy.show_screen('flamethrower_particles')

    def show_flamethrower_right():
        fire2.reset_positions()
        renpy.show_screen('flamethrower_particles_right')


    def show_missile_both():
        missile_left.reset_positions()
        missile_right.reset_positions()
        renpy.show_screen('missile_particles')
        renpy.pause(0.35)
        show_tank_blast()

    def show_missile_right():
        missile_right2.reset_positions()
        renpy.show_screen('missile_particles_right')
        renpy.pause(0.35)
        show_tank_blast()





### SCREENS ###

# ============= FIRE PARTICLES
screen flamethrower_particles():
    add fire1

screen flamethrower_particles_right():
    add fire2

# ============= MISSILE/BANSHEE PARTICLES
screen missile_particles():
    add missile_left
    add missile_right

screen missile_particles_right():
    add missile_right2


# ============= TANK BLAST PARTICLES
screen tank_particles():
    add tank_blast_particle_trail
    add tank_blast_particle_spark
    add tank_blast_particle


# ============= BANELING BLAST PARTICLES
screen baneling_particles():
    add baneling_blast_particle
    add baneling_blast_particle_smoke


# ============= PROTOSS BLAST PARTICLES
screen protoss_particles():
    add protoss_blast_particle_smoke
    add protoss_blast_particle_spark
    add protoss_blast_particle


# ============= STALKER SCREENS
screen stalker_particles():
    add stalker_blast_particle_smoke
    add stalker_blast_particle_spark
    add stalker_blast_particle

    add stalker_blast_particle_smoke2
    add stalker_blast_particle_spark2
    add stalker_blast_particle2


# ============= BULLETS SCREENS
screen bullet_holes():
    add bulletholes


# ============= COLOSSUS SCREENS
screen colossus_particles():
    add colossus_spark




### TRANSFORMS ###
transform lightning_bolt(d):
    alpha 0
    pause 0.05*d
    alpha 1.0
    pause 0.35
    linear 0.25+0.15*d alpha 0


transform flash(d=0):
    alpha 0
    pause d
    alpha 1
    linear 0.25 alpha 0


transform flashtest(d=0):
    alpha 0
    pause d
    alpha 1
    linear 0.10 alpha 0

transform blast():
    alpha 1
    xalign 0.5
    yalign 0.5
    align (0,0)

    parallel:
        linear 0.25 alpha 0
    parallel:
        linear 0.25 zoom 2


## STALKER TRANSFORMS
transform stalker_laser_left:
    yanchor 0.0
    xanchor 0.5
    ypos stalker_y
    xpos stalker_left_from
    zoom 1
    alpha 1
    rotate rotate_left

    parallel:
        linear 0.35 ypos stalker_dest_y
    parallel:
        linear 0.35 xpos stalker_left_x
    parallel:
        linear 0.35 zoom 0.5

transform stalker_laser_left_top:
    yanchor 0.0
    xanchor 0.5
    ypos -1 * stalker_y
    xpos stalker_left_from
    zoom 1
    alpha 1
    rotate rotate_right

    parallel:
        linear 0.35 ypos stalker_dest_y
    parallel:
        linear 0.35 xpos stalker_left_x
    parallel:
        linear 0.35 zoom 0.5

transform stalker_laser_right:
    yanchor 0.0
    xanchor 0.5
    ypos stalker_y
    xpos stalker_right_from
    zoom 1
    alpha 1
    rotate rotate_right

    parallel:
        linear 0.35 ypos stalker_dest_y
    parallel:
        linear 0.35 xpos stalker_right_x
    parallel:
        linear 0.35 zoom 0.5

transform stalker_laser_right_top:
    yanchor 0.0
    xanchor 0.5
    ypos -1 * stalker_y
    xpos stalker_right_from
    zoom 1
    alpha 1
    rotate rotate_left

    parallel:
        linear 0.35 ypos stalker_dest_y
    parallel:
        linear 0.35 xpos stalker_right_x
    parallel:
        linear 0.35 zoom 0.5

transform beam_masks():
    ypos 0
    subpixel True
    linear 0.1 ypos config.screen_height

transform beam_head(x):
    xanchor 0.5
    yanchor 0.5

    xpos x
    ypos 0

    parallel:
        linear 0.1 ypos config.screen_height/2
    parallel:
        linear 0.1 xpos config.screen_width/2






# revised demo script
# please use the definitions here
label particle_demo_2:
    scene p_black:
        align (0,0)

    'Particle Test'

    'flame left'
    $ show_flamethrower_left()

    'flame right'
    $ show_flamethrower_right()

    'flame left'
    $ show_flamethrower_left()

    'flame right'
    $ show_flamethrower_right()

    'tank blast'
    $ show_tank_blast()

    'protoss blast'
    $ show_protoss_blast()

    'baneling blast'
    $ show_baneling_blast()

    'stalker blast'
    $ show_stalker_blast()

    'stalker lasers'
    $ show_stalker_lasers()

    'stalker lasers top'
    $ show_stalker_lasers_top()

    'stalker lasers right'
    $ show_stalker_lasers_right()

    'banshee missile both'
    $ show_missile_both()

    'banshee missile right'
    $ show_missile_right()

    'colossus beam'
    $ colossus_spark.reset_positions()
    show colossus_beams:
        align (0.5,0.0)
    show colossus_beams_mask at beam_masks
    show colossus_beams_head at beam_head(435)
    show colossus_beams_head as right_head at beam_head(845)
    pause 0.1
    hide colossus_beams_head
    hide right_head
    show screen colossus_particles
    pause .5
    hide colossus_beams
    hide colossus_particles
    $ show_protoss_blast()
    pause 1.0

    'End Particle Test'
    return