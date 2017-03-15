Hacks/Hackers Rochester
#######################
:date: 2012-02-02 10:45
:author: berticus
:category: Uncategorized
:slug: hackshackers-rochester
:status: published

A few Wednesdays ago, after a long and cozy day of working from home, I
decided to break my "never leave the house or have meaningful human
contact" rule, and I ventured out to the snowy tundra of Henrietta. The
threshold for this odd behavior is quite high, but I just couldn't bring
myself to miss the first meeting of \ `Hacks/Hackers
Rochester <http://www.meetup.com/HackshackersROC/>`__, a local group
aiming to mush together journalists, programmers, technologists,
designers, and what-have-you, just to see what kind of nutty/useful
stuff results.

|Hacks & Hackers Rochester|

Before I get too far, I'll have you know that their next meeting is
Wednesday, February 15th (at `RIT's <http://www.rit.edu/>`__ `Center for
Student Innovation <http://www.rit.edu/innovationcenter/>`__), and you
can get at them on their `meetup
group <http://www.meetup.com/HackshackersROC/>`__, or their `twittery
bits <https://twitter.com/#!/hackshackersroc/>`__. If combining
technology and journalism sounds fun to you, you should stop by, because
it seemed like a bunch of smart and interesting people.

Ok. For the rest of our time together, I'm fixin' to dump a few links on
you. I am not a journalist, nor a programmer, but I have been quite
interested in this area for some time, and hope to contribute – at the
very least – as a well-informed cheerleader, brainstormer, facilitator,
or village idiot. We'll see. Either way, maybe I can give interested
parties some ideas of what's possible/probable before the next meeting.

Open Sesame
-----------

"Open" excites me. Open source software, open hardware designs, open
data, "free culture" in general. Fun things happen when information is
free and accessible. Maybe this first dawned on me when I saw the
`Oakland Crimespotting site <http://oakland.crimespotting.org/>`__. By
now, everybody has seen a multitude of visualizations made by dumping
data on top of Google Maps. Back then it was pretty new and exciting.
What struck me most, at the time, was that the Oakland PD was publishing
this data to a public website, and in a format that was fairly easily
scrape-able and parse-able. Wow! Amazingly pedestrian, really, but for a
city or county government it seemed unthinkable (and still does,
apparently).

Many municipalities are doing a decent job in this area nowadays. Some
have even progressed enough that sites like
`EveryBlock <http://www.everyblock.com/>`__ have sprung up, taking these
public data feeds and massaging them into a format that mere mortals can
make sense of. `Baltimore has an open data
website <http://data.baltimorecity.gov/>`__ that looks like it has lots
of useful info, in easy to digest formats. `Chicago
too <http://data.cityofchicago.org/>`__. I'm sure there are many
others... those were just the first two to pop up when I poked around
for "data dot blah blah dot gov" sites. There is no
data.cityofrochester.gov site, unfortunately. How do we make that
happen?

Dumpy Data
----------

In the meantime, we rely on `FOIA <http://www.foia.gov/>`__ requests for
information from local governments. Often times, these arrive in the
least convenient format possible, and they are likely full of sloppy and
inconsistent data. We're pretty lucky then, that after cleaning things
up, the D&C often shares this data with us on their
`RocDocs <http://rocdocs.democratandchronicle.com/>`__ site.

I wonder if they know about `Google
Refine <http://code.google.com/p/google-refine/>`__? Refine is "a power
tool for working with messy data, cleaning it up, transforming it from
one format into another, extending it with web services, and linking it
to databases like `Freebase <http://www.freebase.com/>`__." If you're
dealing with cruddy data of any sort, you should check it out. It's a
bit of a weird install, running as a web server on your computer. Ask
your `local nerds </>`__ if you're having
trouble... it's worth it.

Community Data
--------------

Even if you can get it in a decent format, governments don't always have
the data you need. Or if they do, it might be stale by the time you can
get at it. There are some fun things happening in the world of open data
acquisition. Let's call it "open mapping", although I'm sure there are
non-location-based projects I'm overlooking.

First, Google is changing the terms of service on their Maps product...
taking it out of "beta" status and reaching into your wallet for some
payback. If you have a certain amount of map views per day, it's no
longer free to use. Thankfully, all along, a large community of folks
have been creating their own street maps by compiling open government
data (TIGER files in the US), or by walking, biking, and driving routes
with a GPS logger and uploading their tracks.
`OpenStreetMap <http://www.openstreetmap.org/>`__ is the result, and
it's an amazing feat. Anybody can edit the map... so feel free to liken
it to the "Wikipedia of maps", even though that probably makes some
people bristle. Not coincidentally, the resultant data is available
under a farily open license, and has thus been mixed and remixed into a
plenitude of other projects, products, and experiments.

`OpenCycleMap <http://www.opencyclemap.org/>`__ builds upon
OpenStreetMap, and highlights cycling routes. It is rather sparse in the
US. I recently attended some public meetings on Rochester's bicycle
plan, featuring some large maps of city streets rated "A" through "F"
for bike safety. Perhaps that belongs on such a map, editable by all
those who actually ride the city streets and know that traffic volume
and speed are not the only relevant dimensions for such a grade.

|image1|

`OpenHeatMap <http://www.openheatmap.com/>`__ lets you upload a
spreadsheet of data and crank out a heat map on top of OpenStreetMap.
`Mapbox <http://mapbox.com/>`__ is a bit more sophisticated, but costs
some money for hosted maps. No matter... the Mapbox developers have
released `TileMill <http://mapbox.com/tilemill/>`__, a gorgeous
application that lets you handcraft interactive maps yourself. It
requires a bit more knowhow, but I'm sure Hacks/Hackers has plenty of
that.

The folks at `Safecast <http://blog.safecast.org/>`__ wanted to map
radiation levels following the Fukushima disaster in Japan, so they
cobbled together some GPS loggers and Geiger counters. After driving
around the country, they plopped the data on top of the OpenStreetMap.
This isn't child's play yet, but every day it's getting easier to bring
together the hardware and software needed to record data and make it
easily available.

A Brief Aside
-------------

These radiation mappers weren't "traditional journalists". Maybe it
wasn't even journalism or news. Whatever. It was really important info,
and I'll bet no reporter thought "I'll just go out and record that data,
instead of waiting by the phone for an official report". I hope, after
hanging out at Hacks/Hackers, that mindset will change.

Semi-related: Rochester has `a nuclear power
plant <http://rocwiki.org/Ginna_Nuclear_Power_Plant>`__ nearby, and
Interlock has a Geiger counter:

|Geiger Counter|

(not a terribly well calibrated Geiger counter, admittedly)

For some more thoughts on the future of local news and journalism, from
people much smarter and more cogent than I, I will simply link without
comment to some posts I've bookmarked from `Ryan
Sholin <http://ryansholin.com/2007/06/02/10-obvious-things-about-the-future-of-newspapers-you-need-to-get-through-your-head/>`__,
`Jeff
Croft <http://jeffcroft.com/blog/2006/dec/08/selected-responses-times-future-newspapers/>`__,
and `Tim
Porter <http://www.timporter.com/firstdraft/archives/000446.html>`__.

Burbling Infobrooks
-------------------

If real-time info is needed, `Pachube <https://pachube.com/>`__ is a
free clearinghouse for data feeds. It's ridiculously easy to upload
sensor data to the site, whether it be temperature, weather, energy use,
and so on. Equally important, it's also easy to retrieve that
information as a regularly updated and well-documented stream. Would you
like to browse the `2700 available feeds tagged
"radiation" <https://pachube.com/feeds?q=radiation>`__ on Pachube?
Probably not. But it'd be a relatively simple task to create a program
that retrieves and maps them in an easy to digest format.

Some folks – mainly in New York City – weren't quite satisfied with the
current status quo of air quality monitoring. So they're `building their
own sensor network <http://airqualityegg.wikispaces.com/>`__ using open
platforms to measure and make the data available to anybody that wants
it, in real time. This stuff isn't too technically challenging nowadays.
We just need to pair up those with a need for info with the people who
know how to get this stuff done.

Too Long; Still Reading
-----------------------

There's plenty more fun stuff happening in this area, but that's enough
to keep you occupied for a few hours a least. If – after you close all
your browser tabs – you still find your cravings unfulfilled, do `join
us at the next meeting <http://www.meetup.com/HackshackersROC/>`__, or
fire away in the comments here. I'm sure we'll be able to fill up or
otherwise utilize your vast cranial resources. See you there!

.. |Hacks & Hackers Rochester| image:: http://farm8.staticflickr.com/7152/6726571927_7fd2e9714b_z.jpg
   :width: 600px
   :height: 400px
   :target: http://www.flickr.com/photos/bert_m_b/6726571927/
.. |image1| image:: /wp-uploads/2012/02/tilemill_screenshot.jpg
   :class: alignnone size-full wp-image-814
   :width: 600px
   :height: 389px
   :target: /wp-uploads/2012/02/tilemill_screenshot.jpg
.. |Geiger Counter| image:: http://farm7.staticflickr.com/6145/6190437602_041ccdbf22_z.jpg
   :width: 600px
   :height: 400px
   :target: http://www.flickr.com/photos/bert_m_b/6190437602/
