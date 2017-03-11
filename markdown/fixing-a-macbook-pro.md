Fixing a MacBook Pro
====================

date
:   2012-02-01 09:56

author
:   carl

category
:   Projects

slug
:   fixing-a-macbook-pro

status
:   published

Last August I went on a business trip to Silicon Valley and the day
after I arrived my laptop, a MacBook Pro, died. When I pushed the power
button the fans would spin and the optical drive would do a seek but
there was nothing on the screen. About 1 out of 3 times I could hear the
startup gong. I could plug it into a network and ssh into the laptop so
I knew the machine was running - just nothing on the screen. I tried an
external monitor but there was nothing there either.

So I searched the net and tried all the standard resetting of the PRAM,
booting from dvd and anything I could but there was no change. So I
bought a new Lenovo laptop, installed Linux and restored all my personal
files from backups over the network from home. Very slow but within two
days I had a working laptop and continued with my work.

After five more months I still wasn't happy with my new laptop. I had
everything I needed working but there were a bunch of little annoyances.
So I decided to spend an afternoon trying to resurrect my MacBook Pro. I
started by going to ifixit.com for some pointers on disassembling and
checking on things.

<http://www.ifixit.com/Device/MacBook_Pro_15%22_Core_2_Duo_Models_A1226_and_A1260>

I had the small philips screw driver and the torx driver but I didn't
have a spudger (and really had never heard of it). But I was able to use
a small flat blade screw driver very carefully and managed.

First I opened it and tried removing/moving/replacing the ram modules
just to make sure - do the easy things first even if they aren't likely
to do anything. Then I tried checking any and all connectors
-disconnect, reconnect and test again. I followed all the cables that
had anything to do with video to see if maybe one was broken. After
checking all of this there still was no change in the behavior.

After some more searching it seemed like the last thing to try was to
reflow the solder on the GPU. There were several videos about doing this
both specifically for the MacBook Pro and for video cards in general.

<http://www.youtube.com/watch?v=1jFTi_P24z8&feature=related>

<http://www.youtube.com/watch?v=t_uN6VBqWkg&feature=related>

Since the laptop was useless as it was I had nothing to lose. So I
continued the disassembling until I had the main logic board free. There
were lots of screws and many tiny little connectors to all the other
bits in the case. I was fairly sure it would never work again because I
doubted my ability to get everything connected correctly again but I
pushed on. I cleaned all the heat sink compound off the cpu, gpu and
interface chips. Using the heat gun at our soldering station, I heated
the the little board holding the gpu onto the logic board focusing on
any solder joints I could see. After ten minutes of this it seemed like
the solder I could see was a little shinier and the board was certainly
hot. So I started the long process of assembling the laptop again.
Getting all the little connectors on top of the logic board and
reconnected was quite a tedious process. Then getting all the screws
back was also lots of fun. I tried keeping the screws generally laid out
in groups by where they came from but there was still a lot of hunting
for a hole that the screw would fit in. But eventually I had it all back
together with no left over parts.

Now the moment of truth. It was late and time to go home so I waited
until everything was back together and plugged in. Then I pushed the
power button and the startup gong sounded. Then wonder of wonders, the
screen lit up and the system booted all the way up. I was able to login
and the system was working perfectly! Several days later and everything
is still fine.

So for a few hours work I have a my laptop back.

 
