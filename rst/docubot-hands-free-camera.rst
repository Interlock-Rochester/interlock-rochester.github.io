Docubot Hands-free Camera
#########################
:date: 2011-09-28 15:05
:author: berticus
:category: Uncategorized
:slug: docubot-hands-free-camera
:status: published

|DSC_6891.jpg|

|DSC_6888.jpg|

Surely this will be my last poorly documented project: a hands-free foot
operated documentation camera. I thought it'd be handy, and I had an old
broken desk lamp kicking around, so of course, the two must be mushed
together.

|DSC_6894.jpg|

I started out with an old Canon SD1000, with
`CHDK <http://chdk.wikia.com/wiki/CHDK>`__ installed of course. For
those in the dark, CHDK is an alternate firmware that works on lots of
point and shoot cameras (not just Canon, anymore), and it lets you run
scripts, save pictures as raw files, and tweak every setting you could
ever possibly want to. It's awesome, and I needed it so I could trigger
the shutter via an external button (you basically toggle +5v on one of
the USB port pins).

|DSC_6902.jpg|

I didn't want to worry about running out of batteries mid-shoot, so I
printed a dummy battery at `Shapeways <http://www.shapeways.com/>`__,
ran some wires through it, then tinned and bent over the ends of them to
make some pseudo "terminals". These went out a hole I drilled in the
battery door, through the lamp, to a simple 5v voltage regulator, wired
up straight out of the
`datasheet <http://www.national.com/ds/LM/LM109.pdf>`__. This 5v source
also goes through an old lamp foot switch to the camera's USB port, for
the external trigger.

|DSC_6905.jpg|

|DSC_6898.jpg|

Finally, I took to the lathe to make an adapter between the weird lamp
thread and standard camera tripod thread (1/4" diameter, 20 threads per
inch). I used a bit of round delrin stock, bored out the appropriate
diameters, and just cranked a bolt through rather than threading things
properly.

I tried a few test shots last night, while I put together `Mighty Ohm's
Geiger Counter
Kit <http://mightyohm.com/blog/products/geiger-counter/>`__. It works
pretty well, but can't really zoom in close enough to document very fine
work. Hopefully it will still be useful for documenting other tasks that
require both your hands in frame. Failing that, I'm sure there will be
other uses for a scriptable camera attached to a flexible-yet-solid
base... perhaps it will turn into a time-lapse-bot.

|DocuBot Test|

|DocuBot Test|

|DocuBot Test|

.. |DSC_6891.jpg| image:: http://farm7.static.flickr.com/6080/6077141844_89382e76c4.jpg
   :class: alignleft
   :width: 380px
   :height: 250px
   :target: http://www.flickr.com/photos/bert_m_b/6077141844/
.. |DSC_6888.jpg| image:: http://farm7.static.flickr.com/6181/6077135434_f0893c06a4.jpg
   :class: alignleft
   :width: 166px
   :height: 250px
   :target: http://www.flickr.com/photos/bert_m_b/6077135434/
.. |DSC_6894.jpg| image:: http://farm7.static.flickr.com/6190/6077147088_4b3c84db77.jpg
   :width: 500px
   :height: 333px
   :target: http://www.flickr.com/photos/bert_m_b/6077147088/
.. |DSC_6902.jpg| image:: http://farm7.static.flickr.com/6205/6076628007_f98976013f.jpg
   :width: 500px
   :height: 333px
   :target: http://www.flickr.com/photos/bert_m_b/6076628007/
.. |DSC_6905.jpg| image:: http://farm7.static.flickr.com/6187/6077171350_06cb8350d0.jpg
   :width: 500px
   :height: 333px
   :target: http://www.flickr.com/photos/bert_m_b/6077171350/
.. |DSC_6898.jpg| image:: http://farm7.static.flickr.com/6061/6076615413_b204a847f4.jpg
   :width: 500px
   :height: 333px
   :target: http://www.flickr.com/photos/bert_m_b/6076615413/
.. |DocuBot Test| image:: http://farm7.static.flickr.com/6147/6190441282_7da14f7397.jpg
   :width: 500px
   :height: 375px
   :target: http://www.flickr.com/photos/bert_m_b/6190441282/
.. |DocuBot Test| image:: http://farm7.static.flickr.com/6152/6190437268_f14a3515a8.jpg
   :width: 500px
   :height: 375px
   :target: http://www.flickr.com/photos/bert_m_b/6190437268/
.. |DocuBot Test| image:: http://farm7.static.flickr.com/6145/6190437602_041ccdbf22.jpg
   :width: 500px
   :height: 375px
   :target: http://www.flickr.com/photos/bert_m_b/6190437602/
