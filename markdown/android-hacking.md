Android Hacking
===============

date
:   2011-09-07 09:43

author
:   antitree

category
:   Classes, Projects

slug
:   android-hacking

status
:   published

[![image0](http://interlockroc.wpengine.com/wp-content/uploads/2011/09/android_hack_logo-150x150.jpg)](http://interlockroc.wpengine.com/wp-content/uploads/2011/09/android_hack_logo.jpg)Android
right now makes up 52% of the smartphone market share and a third of the
tablets. I've been focused on Android lately and wanted to do
an introduction to the hackability of these devices. From a security
perspective, Android offers some interesting opportunities: rooting your
phone, hacking an app, or malware analysis. For the hardware hackers,
Google and others are offering hardware tools that can plug into your
Android device to enable use them for your hardware projects. If you're
interested in the creative path, it's really easy to get started doing
app development.

**Rooting:**

Rooting your device offers the user full control of the device to allow
to change the version of the operating system, install or uninstall any
apps you'd like, and in some cases gain access to features that would
otherwise be locked out by the carrier. If none of those interest you,
the geek cred alone may be good enough.

Rooting is nothing more than a privilege escalation attack. You are
granted standard user access to your phone but you'd like to escalate to
root level privileges. Android, being built on top of Linux follows the
common practice of granting root only when necessary to your device's
operations. There are a bunch of attack vectors like exploiting a
service running as root, exploiting a file that has root access,

**App Hacking:**

There's a lot of fun stuff you can do to hack an Android app. It's
originally coded in Java and although Android runs it's own Java
environment called Dalvik VM, an app can be decompiled from it's byte
code to Java class files. From there you can do some reverse engineering
to take a look at how the app operates. With a little luck and skill,
you can recompile a modified version of the app. I'm not going to go too
deep into this idea but if you're interested, I'll be doing a
presentation at this years [Rochester Security
Summit](http://www.rochestersecurity.org) that will give you the tools
to do this analysis yourself.

**Malware:**

For the security guys now, malware analysis is a fun way to get a peek
into how the bad guys work. Android is in a battle with malware usually
available in alternative markets. Nasty apps like "Nickispy" will steal
your personal information and even record your calls to upload them back
to a server. Some will root your device and install a backdoor like the
latest variant of DroidKungFu. With some tools and some different
analysis techniques, you can perform the analysis yourself. Jason Ross
will also be presenting this year at RSS on this topic if you're
interested.

**Hardware Hacking:**

At this years Google IO, they announced the release of the [Android
Development
Kit](http://www.google.com/events/io/2011/sessions/android-open-accessory-api-and-development-kit-adk.html) which
is a bridge between your Android device and your hardware projects.
Imagine controlling an Arduino with a touch screen interface or using
the sensors from your phone to control a robot. As a cheap alternative
to the \$300+ kit, Sparkfun has created the [Android
IOIO](http://www.sparkfun.com/products/10748), pronounced yoyo. This is
what my next project will include with a little help from the robot crew
at Interlock.

**App Development:**

If programming or art is your thing, or you want to make your next
million dollars on an Angry Birds killer, you can get started developing
apps on the [Android Marketplace](http://market.android.com/publish) for
\$25. This gets you an account to upload your app to the public
directory and it will show up on thousands of people's phones. The
Android SDK along with the Eclipse plugins make it pretty easy to
develop without too much programming knowledge.

**Android At Interlock:**

In the coming months, along with all the other changes, we're planning
on doing an Android workshop at the space. Depending on the interest it
may be related to rooting or application development.
