Near Field Communication Primer
===============================

date
:   2011-12-21 12:00

author
:   antitree

category
:   Projects

tags
:   hacking, infosec, near field communication, NFC, security

slug
:   near-field-communication-primer

status
:   published

[![image0](http://interlockroc.wpengine.com/wp-content/uploads/2011/08/NFC-logo.png)](http://interlockroc.wpengine.com/wp-content/uploads/2011/08/NFC-logo.png)I
thought I'd do a primer about NFC since Samsung's Galaxy Nexus is
getting a lot of press about it. You may have heard of Google Wallet or
how NFC is going to be built into smart phones in the future. Maybe you
haven't thought about how it works or how to hack it. As a
side[side(side)] project I've been working on NFC research with (as
always for me) a specific focus on the security perspectives. This is an
overview of NFC to maybe peak your interest.

**Define:NFC**

Near Field Communication is a way to transmit information between
intelligent devices. I know you're already thinking Bluetooth but wait.
NFC has a limitation that says in its spec that it can't be more than
.2m away from its partner during communication. It may be a bit more
depending on the implementation but the thing to remember here is that
the protocol itself is what limits the distance, not just the hardware.
(Quit pointing that gigantic antenna at my pocket right now!) It
transmits on the HF band 13.56MHz, a frequency already used by some RFID
chips and fun devices like the Proxmark 3.

**Modes**

Here's what's different about NFC: There are three different modes.

-   Reader/Writer: Commonly used in smart posters or smart stickers.
    Think QR code but subtle.
-   Peer to Peer: Data is exchanged back and forth between devices;
    securely exchange credit cards, give your friend your home WIFI
    settings, or exchange business cards.
-   Card Emulation: A device acts like a contactless smart card. What if
    you could use your phone as a bus pass instead of keeping that
    flimsy magstripe pass in your pocket?

**NFC != RFID**

Lets take care of that up front. NFC sounds a lot like RFID (they share
the whole RF thing) and it seems to get stored in people's heads that
way because NFC has the card emulation mode where it emulates at "tag"
or an RFID chip.  RFID isn't usually much more than a tag blindly
broadcasting data hoping a receiver picks it up. Passive tags (or little
antennas without a power source) sit and wait for an RFID reader to come
by to energize them. They get all excited and tell the reader everything
they know. Imagine a dog just waiting at the door for it's owner to come
home. The active RFID tags have a battery in them that constantly
broadcasts itself to anyone that will listen. Kind of like that annoying
friend you have that tells you everything about their life even though
you never asked. NFC on the other hand is like an intelligent college
student. She can have an intimate conversation with you, she can make a
presentation in front of a class, but she can still get drunk and act
stupid if that's what everyone else is doing at the party.

**NFC is not a new technology**

We've seen them in European phones since 2003 or 4 and they've been
hacked on for just as long. The folks at the [Chaos Computer
Club](http://www.ccc.de/en/) have been hacking on NFC since it's
original inception; when manufacturers like Nokia started installing it
into their feature phones, AKA dumb phones. It never made it across the
water - some may say due to some FCC regulations on the 13.56 frequency
but I'll leave that topic to the Ham guys.

**Security[![image1](http://interlockroc.wpengine.com/wp-content/uploads/2011/08/tinfoilhat.jpg)](http://interlockroc.wpengine.com/wp-content/uploads/2011/08/tinfoilhat.jpg)**

If you haven't already, you should put on your tin foil hat now. **NFC
is a way for corporations to take over our bodies, man!** Well...most
likely not. But you're already thinking about the security problems as
soon as I wrote "credit card." I'm going to save this whole discussion
for another day but the tl;dr version is that NFC has been designed with
security in mind but a lot is left up to the developer to implement
securely. We all know how well that works especially for mobile app
developers so I'm sure everything is going to be fine, right? Maybe next
time I'll tell you about the butt sniffing attack. No seriously.

**Android and The Galaxy Nexus**

How is Android implementing NFC in the Galaxy Nexus? Here's an example
of a peer to peer mode connection: When you put a Galaxy Nexus next to
another Galaxy Nexus, the phone will make an NFC connection as long as
both phones are unlocked. If the app that you  have open supports NFC
(i.e. Google Maps) it will allow you to communicate data from your app
to the other device. Some examples of this are sharing contact
information, location data, websites, etc but apparently it's going to
be used for games or whatever developers can think of.

The Reader/Writer mode will allow you to take an NFC tag and shove it
next to the phone. Depending on the data stored on the card, it will
open an appropriate app to view the content. In the case of an NFC tag
that is contains a URL, it will automatically go to that page. Ask me
about some of the NFC tags I've made at a 2600 meeting sometime. :)

**More info:**

If you want to see a much better post that's chock full of info check
this
out: <http://www.engadget.com/2011/06/10/engadget-primed-what-is-nfc-and-why-do-we-care/>

Here' s a random YouTube video of two guys with Galaxy Nexuses so I
don't have to make one: <http://www.youtube.com/watch?v=ZQSc4uiakv4>
