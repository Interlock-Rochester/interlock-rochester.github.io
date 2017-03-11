Flat panel light box
====================

date
:   2014-11-05 11:18

author
:   BleuLlama

category
:   Uncategorized

slug
:   flat-panel-light-box

status
:   published

[![image0](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F3.bp.blogspot.com%2F--EgFkTCN9Jk%2FVFpB9PasgBI%2FAAAAAAAAC7s%2F4jenoIWTxCc%2Fs1600%2F2014-11-04%252B23.16.21.jpg&container=blogger&gadget=a&rewriteMime=image%2F*)](http://3.bp.blogspot.com/--EgFkTCN9Jk/VFpB9PasgBI/AAAAAAAAC7s/4jenoIWTxCc/s1600/2014-11-04%2B23.16.21.jpg)

I've been getting into making stained glass pieces, as I've been taking
a class at the Rochester Memorial Art Gallery.  One of the tools they
have available there is a light box, which I have used to make the
template for the macaw piece I'm making.  I used it to help me adapt a
pattern I found online into something that better suits my needs.  I
traced it, then retraced that sketch.

The light box also works well to see how things look with light behind
them, however it's not something I can use a lot for this, since my
project is a couple dozen pieces of glass and we have to share the light
box.

 

On the recycle pile at work was a couple of old, broken laptops.  I
snagged two of them; one with an LED backlight, and one with a CCFT
backlight.  I thought that the LED one would be easier to get working.

 

Over at [Interlock](http://interlockroc.org/), I tore apart the screens,
tossing out the LCD panel, so I was left with just the light source,
light guide, diffusion screens, and control circuitry.  Its
control/driver board also managed the LCD itself.  There were many test
points on the back, so I applied power to the "LED PWR" pin, ground to a
ground point, then about +5 volts to the BLEN (assuming it to be
"backlight enable") as well as the "PWM" test point. After futzing with
it for a little bit, I gave up and focused efforts on the CCFT-based
one.

The slightly larger CCFT (Fluorescent) based one had a single board that
connected to the backlight tube through standard white/pink
silicone-insulated wiring.  The board itself had one tiny connector on
one side with a few pins that seemed to have obvious use.  V+, which
assumably powers the backlight circuitry, should be connected to +5 or
maybe +12.  GND, which of course is ground. Then two other connections
"EN" and "CTRL", which I guessed to be "Enable" and "Control".  A guess
would be to tie these to a logic "high" which might maybe enable the
thing.

I connected just the V+ and GND to a power supply, and applied power.
 Ranging from 0v up through 12v yielded no results. I connected the
other two logic lines to power too, and started ramping up the power.
 At around 7v, the backlight flickered on, but then wouldn't do anything
until I brought the power back to 0v, and then back up again.

On a hunch, I figured that the backlight needs a higher voltage, and the
logic stays at TTL levels.  Applying the same power to both would give a
possible point between the two where both kinda worked, which is where I
saw the flicker.  I hacked together two power supplies, with grounds
tied together, 5v from one power brick, and the V+ to the variable
supply.

[![image1](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F1.bp.blogspot.com%2F-9We5elFk1J8%2FVFpB9JnXiDI%2FAAAAAAAAC7w%2FUR087-rhETA%2Fs1600%2F2014-11-04%252B22.18.15.jpg&container=blogger&gadget=a&rewriteMime=image%2F*)](http://1.bp.blogspot.com/-9We5elFk1J8/VFpB9JnXiDI/AAAAAAAAC7w/UR087-rhETA/s1600/2014-11-04%2B22.18.15.jpg)

I ramped up the voltage, and sure enough, it would get dim around 7v,
then go full brightness around 12v.  It seemed to use about 300mA to
drive it too. Good to know.  I found a 12v power brick and.. it would
light for about 20 seconds then power itself off.  The 12v brick put out
18v.

I eventually found a brick that worked, so i hooked up two supplies, a
5v and a 12v and it was stable and bright.  Next would be the task to
put in a 5v regulator to provide the 5v it needs, so i can run it all on
one single power supply.

[![image2](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F4.bp.blogspot.com%2F-stT0iwcG9FE%2FVFpFzcS57OI%2FAAAAAAAAC8E%2F5trk7YF5Vsc%2Fs1600%2Fmain-qimg-d1e728f2f684a47d10b25686f66e93f9.gif&container=blogger&gadget=a&rewriteMime=image%2F*)](http://4.bp.blogspot.com/-stT0iwcG9FE/VFpFzcS57OI/AAAAAAAAC8E/5trk7YF5Vsc/s1600/main-qimg-d1e728f2f684a47d10b25686f66e93f9.gif)

A simple circuit using a 7805 and two capacitors later, and I have 12v
in, and a backlight lit!  I wrapped the circuit in tape (purple because
it was there), hooked it up to a power connector, and reassembled the
case.

[![image3](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F2.bp.blogspot.com%2F-qaXCEb0O6bA%2FVFpB9O9cu6I%2FAAAAAAAAC70%2Ff4be5tcJKVU%2Fs1600%2F2014-11-04%252B22.59.53.jpg&container=blogger&gadget=a&rewriteMime=image%2F*)](http://2.bp.blogspot.com/-qaXCEb0O6bA/VFpB9O9cu6I/AAAAAAAAC70/f4be5tcJKVU/s1600/2014-11-04%2B22.59.53.jpg)

Best of all, it all managed to fit within the old plastics. Huzzah!

Now I just need to put something on the diffusers to protect them from
cut glass, maybe a piece of plexi, or even a large Ziplock or plastic
wrap, and I'll be set!
