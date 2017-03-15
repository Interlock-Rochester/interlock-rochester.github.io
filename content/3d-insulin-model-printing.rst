Printing a 3D Insulin Model
###########################
:date: 2012-06-05 08:10
:author: dzho
:category: Events, News, Projects
:slug: 3d-insulin-model-printing
:status: published

We've held the second of `our monthly 3D printing
meetings <http://twitter.com/#!/interlockroc/statuses/200546366982848512>`__
recently, with a fifth person getting trained up on how to use our
current printer, and are on the cusp of another advancement in our
`previously-mentioned 3D printing
capabilities </2012/03/21/quick-open-house-recap/>`__,
now that 3 people have decided which printer design they're going to
build next.

In the meantime, we continue to torture Beardicus's poor little `Huxley
RepRapPro <http://reprappro.com/Huxley>`__ making other little
tschotskes that speak to our interests. This doesn't get us closer to
the glorious future of 3D printers for everyone, but I like to think of
it as our answer to Wall Street's "profit taking": Every once in a while
it's nice to just cash out a little bit and enjoy what you've already
got.

My turn at that most recently was this little model of monomeric
insulin, based on the crystal structure reported by `Gursky et.
al. <http://www.ncbi.nlm.nih.gov/pubmed/1504238>`__

The trick is how to take a computer model of something like this:

|9ins solvent-accessible surface Z rotation|

and print it on the 3D printer so that it goes from being an
on-the-screen abstraction to something you can hold.

Consider that there are many different ways to render these things on a
screen:

|image1|

Each has its uses. But learning how to manipulate an on-screen rendering
can be a fraught experience. How much better, then, to have the option
of turning the model over directly, with your own hands?

With fused deposition printing, the problem is that the irregular
surface doesn't really present a good way of getting the nascent object
to stick to the print bed.

To start, I trolled through the `RCSB <http://www.rcsb.org>`__ web site
for a suitable small globular protein that had a bit of name
recognition. I picked
`insulin <http://en.wikipedia.org/wiki/Insulin>`__, and from among the
various insulin entries, picked
`9INS <http://www.rcsb.org/pdb/explore/explore.do?structureId=9ins>`__.

I brought that file up in `PyMOL <http://pymol.org>`__, issued "hide
everything" and then "show surface" (or their GUI equivalents) and, with
a few other visual tweaks, like setting the color, exported a VRML 2
(.wrl) file. I played around with that in meshlab a bit, exporting it
then as an .stl file.

I finally sorted out that what I really needed to do was bring it into
`Blender <http://www.blender.org>`__ and subtract a cube-shaped (well,
any volume with a flat face would probably do) volume from the molecule
to give a partial rendering of the model with a flat surface. Doing that
twice, to generate each "half" of the molecule, leaves me with two .stl
files that can be printed flat side down. In some cases, I've brought
the file into `netfabb's online service <http://cloud.netfabb.com>`__
for cleanup of manifold errors. Then, I bring each file into
`ReplicatorG <http://replicat.org>`__ to more easily scale and orient
the model. Finally, I bring the .stl files into
`Slic3r <http://slic3r.org>`__ to generate the .g file for taking over
to the printer.

|image2|

This result is a fairly small protein and a fairly small model that was
fast to design and print as a proof of concept. Future challenges will
be to find ways of dividing up larger models and of larger molecules or
multi-molecule assemblies so they can be printed, perhaps printing
different chains in different colors, preserving relative scaling
between different components and the like.

`There <http://www.thingiverse.com/thing:12283>`__
`are <http://www.thingiverse.com/thing:18928>`__
`several <http://www.thingiverse.com/thing:3511>`__
`examples <http://www.thingiverse.com/thing:21577>`__ of this sort of
thing `over <http://www.thingiverse.com/thing:21527>`__
`at <http://www.thingiverse.com/thing:19989>`__
`Thingiverse, <http://www.thingiverse.com/>`__\ but I first got the idea
from
`Chris <http://www.mail-archive.com/pymol-users@lists.sourceforge.net/msg01394.html>`__
`Want <http://bebop.cns.ualberta.ca/~cwant/wgallin-pymol.jpg>`__
`at <http://bebop.cns.ualberta.ca/~cwant/wgallin-3d-printed.jpg>`__
`University <http://www.mail-archive.com/pymol-users@lists.sourceforge.net/msg04210.html>`__
`of <http://bebop.cns.ualberta.ca/~cwant/pymol_wrl/pymol_1tii.jpg>`__
`Alberta <http://bebop.cns.ualberta.ca/~cwant/pymol_wrl/pymol_1tii_print.jpg>`__
via the `PyMOL <http://www.pymol.org>`__ mailing list several years ago.

.. |9ins solvent-accessible surface Z rotation| image:: http://deejoe.etrumeus.com/interlock/9ins/9ins.gif
.. |image1| image:: /wp-uploads/2012/05/montage2.png
   :class: alignnone size-full wp-image-928
   :width: 576px
   :height: 567px
   :target: /wp-uploads/2012/05/montage2.png
.. |image2| image:: /wp-uploads/2012/05/IMG_4786-300x225.jpg
   :class: alignnone size-medium wp-image-889
   :width: 300px
   :height: 225px
   :target: /wp-uploads/2012/05/IMG_4786.jpg
