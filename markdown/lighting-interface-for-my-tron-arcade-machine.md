Lighting Interface for my TRON Arcade Machine
=============================================

date
:   2013-02-02 19:50

author
:   BleuLlama

category
:   Hardware, Projects

slug
:   lighting-interface-for-my-tron-arcade-machine

status
:   published

[![image0](http://4.bp.blogspot.com/-jgA1Mx_FONA/UQllN2T7gfI/AAAAAAAACRc/xk0nmv3X2r4/s400/2013-01-15+23.49.41.jpg)](http://4.bp.blogspot.com/-jgA1Mx_FONA/UQllN2T7gfI/AAAAAAAACRc/xk0nmv3X2r4/s1600/2013-01-15+23.49.41.jpg)

As seen in a previous post, I have a Tron Mini/Cabaret arcade machine.
 I used to have a Tron full-sized (FS) machine, but sold it many years
ago.  One thing that the FS had over the mini was lots of extra
lighting.

[![image1](http://3.bp.blogspot.com/-wAw8kLCJag4/UQllSEPSjjI/AAAAAAAACRk/LkvM9em4lmA/s640/tron-borne-arcade.jpg)](http://3.bp.blogspot.com/-wAw8kLCJag4/UQllSEPSjjI/AAAAAAAACRk/LkvM9em4lmA/s1600/tron-borne-arcade.jpg)

It had artwork beyond the monitor lit with a regular light, it had a
blacklight above the control panel to make the traces glow, and make the
joystick glow.  There's also a second blacklight below the control panel
to backlight the bottom portion as well.  All of these lights are always
lit, making the machine extra awesome.  On the mini, there is glow
artwork, but no light to illuminate them.  Ever since the late 90s, I've
had a plan to change this, so I bought a pack of UV LEDs, but they've
sat dormant in my parts bin until now!

[![image2](http://1.bp.blogspot.com/-3PQ37GAflKU/UQllX60VInI/AAAAAAAACRs/6bSx7ymUibk/s640/91b64d71ed8b3555b56265edc340dccf.jpg)](http://1.bp.blogspot.com/-3PQ37GAflKU/UQllX60VInI/AAAAAAAACRs/6bSx7ymUibk/s1600/91b64d71ed8b3555b56265edc340dccf.jpg)

One thing that I'd like to bring to this, is to go an extra step, and
bring some ideas over from the "Environmental Discs Of Tron" (EDOT)
machine.  On the EDOT, you walk inside of it... one of the few, if not
the only, games where you can do this.  Around the monitor and control
panel are lights, similar to the FS Tron. However, on EDOT, they're
controlled by the game.  They will flash and such when certain game
events happen. I can make this happen with Tron, using an interface to
the game, and a ROM hack.

Above all, the modifications made **must be reversible without any
damage to the machine**.  I do not want to inflict any permanent damage
or changes to the cabinet.  I will simply add lighting, make a ROM hack
to control the lights, and mount an additional board inside the cabinet.

[![image3](http://1.bp.blogspot.com/-alUmFfgO7IU/UQllj55GK0I/AAAAAAAACR0/9DRz_vTT-7Y/s640/2013-01-29+21.45.04.jpg)](http://1.bp.blogspot.com/-alUmFfgO7IU/UQllj55GK0I/AAAAAAAACR0/9DRz_vTT-7Y/s1600/2013-01-29+21.45.04.jpg)

To start with, I need a secondary micro to control the lights. I'll use
one of my stepper motor controller/Arduino devices. I made the FTDI
programming and power interface seen above in about 30 minutes on the
piece of strip board at Interlock this past Tuesday.  You can see the
resistor/capacitor pair to handle the programmer's reset, power, and
TX/RX lines, and a red power indicator LED for the heck of it.

[![image4](http://4.bp.blogspot.com/-IZXdgylhkJM/UQlmBOhEWjI/AAAAAAAACR8/tgu_9wa8Lcw/s640/2013-01-29+23.37.25.jpg)](http://4.bp.blogspot.com/-IZXdgylhkJM/UQlmBOhEWjI/AAAAAAAACR8/tgu_9wa8Lcw/s1600/2013-01-29+23.37.25.jpg)

After a bit more work, I had the 3 LED driver chips wired up, with their
8 outputs, along with the 5 pin header which I'll be using to interface
it with the arcade machine.  The pinout there is two bits of input, 5v
power input, and ground.  I'll add in SPI-like (clock+data)
communications from the TRON game.  I figure that the first version will
just send down a packet stating the lighting effect, but in the future I
can use this to send down high scores as well, which can be sent out via
serial to a host PC and post them on the net or something like that.

At first it didn't power on properly, and the LED driver chips got VERY
hot.  Then I remembered that the circuit diagram I was referring to
while soldering this up was incorrect and had power and ground reversed
to the chip.  I also had + and - wired backwards for the LEDs as well. I
forgot that these driver chips sink current, rather than sourcing it.
 After a little bit of emergency soldering, all of that got worked out.

[![image5](http://1.bp.blogspot.com/-BAv4m00YYho/UQlnQYvBDNI/AAAAAAAACSE/KIVSIgF94PA/s640/2013-01-30+00.07.36.jpg)](http://1.bp.blogspot.com/-BAv4m00YYho/UQlnQYvBDNI/AAAAAAAACSE/KIVSIgF94PA/s1600/2013-01-30+00.07.36.jpg)

*I've since cleaned up the wiring a bit, adding some insulation.*

I decided to wire up the LEDs such that the current limiting resistor
was wired up with the LEDs, rather than on the main board.  I'm glad I
did this, as the resistance I picked (220 ohms) was way too high.

[![image6](http://4.bp.blogspot.com/-YhLD_7PXFZI/UQlnzncUnXI/AAAAAAAACSU/RoJJSDb4td4/s640/2013-01-30+01.39.00.jpg)](http://4.bp.blogspot.com/-YhLD_7PXFZI/UQlnzncUnXI/AAAAAAAACSU/RoJJSDb4td4/s1600/2013-01-30+01.39.00.jpg)

*Enhanced image. It sadly doesn't look quite this intense in person.*

[![image7](http://1.bp.blogspot.com/-oE-ZamW4Z-Y/UQloCRkoH5I/AAAAAAAACSc/pEc8tMDBtXE/s640/2013-01-30+01.40.49.jpg)](http://1.bp.blogspot.com/-oE-ZamW4Z-Y/UQloCRkoH5I/AAAAAAAACSc/pEc8tMDBtXE/s1600/2013-01-30+01.40.49.jpg)

*Experimenting with how it will look to have LEDs inside of the joystick
to illuminate it.*

The output from these LEDs was much dimmer than I was hoping for. I will
be experimenting with lower-valued resistors, as well as possibly
doubling-up LEDs for lighting the various artwork elements.  I also need
to figure out how to mount the LEDs without damaging the machine at all.

Next up is the ROM hack to talk with this!
