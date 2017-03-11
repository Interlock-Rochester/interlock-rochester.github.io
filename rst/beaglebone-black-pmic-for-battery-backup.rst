Beaglebone Black PMIC for battery backup
########################################
:date: 2015-03-02 16:03
:author: antitree
:category: Hardware, Projects, Security
:slug: beaglebone-black-pmic-for-battery-backup
:status: published

One of my `Interlock
projects <https://trello.com/c/Hlx0umUw/12-tactical-beaglebone>`__ has
been to explore the capabilities of the Beaglebone Black's built-in
Power Management Integrated Circuit
(`PMIC <http://en.wikipedia.org/wiki/Power_management_integrated_circuit>`__)
that gives the BBB a pretty useful feature; charging and operating off
of li-po batteries. If you look at the BBB board, you will see 4
through-holes behind the 5v plug. These are break outs for the PMIC and
can be used to hook up to a battery.

|beaglebone with sparkfun battery|

Having a battery connected to your board gives you the ability to do
things like making a UPS for you beaglebone so in the case of a power
loss, it can politely shut-down, run a custom command, or just continue
running for as long as the battery can charge it.\ |bbb_pinouts|

**Power**
=========

In most of the use cases, you're going to find a lithium polymer that
can produce around 3.7V which is under the BBB's 5v requirement. 3.7V
will work fine to power the board but of course your 5V USB port will
not work while on the
battery. \ `Sparkfun <https://www.sparkfun.com/products/8483>`__\ has a
few nice ones that have the voltage protection circuits built in to help
limit the risk you brick your li-po.

**Configuration**
=================

There are 4 pins we're talking about:\ **|bbb-batt-srm|**

-  TP5
-  TP6
-  TP7
-  TP8

You can see in the diagram what each pin-out is. Li-po's are riskier
than some batteries because they're known to explode in some cases of
over powering. A temperature sensor that is designed to check how hot
the battery is getting and decide how to handle it, is built into the
PMIC in case your battery doesn't have this capability already(many do).
The directions below are going to show you how to jump this temperatur
check with a 10k resistor, which is not recommended if you value your
home or hackerspace. If you don't trust the battery you're charging, I'd
suggest looking into accurately reading the temperature from your
battery. My Sparkfun batteries do no break out the temperature sensor so
this wasn't plausible.

**Directions**:
===============

-  jumper pins TP5 to TP6 (or use an SMT zero ohm resistor)
-  connect a 10K resistor between TP7 and TP8
-  Install a JST connector on TP6 and TP8
-  Connect your battery into the JST connector

With a little luck and the correct battery, you should be in business.
You'll need to let your battery charge before you try and yank the power
cable from it. In the mean time, you can query the status of the battery
via the i2cget command built into the OS.

**Testing**
===========

The PMIC is accessible using I2C and the builti-n OS for BBB has a
simple command line interface to query its state. The following command
will tell you whether or not battery is plugged in:

`` i2cget -y -f 0 0x24 0xA``

This will return information that contains this:

::

    0 device 0x24
    On battery power only? 0
    STATUS: r[0xa]=0x88
    Push Button = 0
    USB Power = 0
    AC Power = 1
    CHARGER: r[0x3]=0x1
    Active (charging) = 1

"Active" refers to whether it can recognize the battery you have plugged
in.  You can also read this state to detect a power failure and
automatically failover. If you're using the default OS for the
Beaglebone Black (the one that comes pre-installed), the OS will
automatically shut itself down in the case of a power loss. You'll want
to either install another OS, or disable that service if you'd like to
change how long the battery should stay online.

More info
=========

A decent amount of research went into this simple project. There are a
ton of warnings and caveats that I'm not going to cram into this blog
post (i2c address is read only, pin-outs are not a standard size, beware
of jumping the resistor next to the pins). You can find out more
information here:

-  Detailed information on how to interface the PMIC with a 3 pin
   li-po \ http://www.beaglebone-asterisk.org/uninterruptible-power-supply-ups-for-beaglebone-black-a-diy-project/
-  Python wrapper to query the PMIC via
   I2C \ https://github.com/pehrtree/beaglebone_snippets/tree/master/power
-  Discussion of powering the BBB with
   3.7V \ https://groups.google.com/forum/#!topic/beagleboard/Ahzk6Ut7xYE

Thanks to Alex for finding a fatal flaw in the 10k resistor I was using.

.. |beaglebone with sparkfun battery| image:: {filename}wp-uploads/2015/03/IMAG0734.jpg-300x170.jpeg
   :class: aligncenter size-medium wp-image-1906
   :width: 300px
   :height: 170px
   :target: {filename}wp-uploads/2015/03/IMAG0734.jpg.jpeg
.. |bbb_pinouts| image:: {filename}wp-uploads/2015/03/bbb_pinouts-e1425329803523-267x300.jpg
   :class: aligncenter size-medium wp-image-1907
   :width: 267px
   :height: 300px
.. |bbb-batt-srm| image:: {filename}wp-uploads/2015/03/bbb-batt-srm-300x109.jpg
   :class: alignright wp-image-1905
   :width: 377px
   :height: 137px
