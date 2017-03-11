SSH Port Forwarding
===================

date
:   2012-11-23 15:38

author
:   Ben

category
:   Projects, Security

slug
:   ssh-port-forwarding-2

status
:   published

I've been toying with the idea of setting up an IRC bouncer ("BNC"). A
BNC is a process that acts in a similar manner to a proxy: I connect to
it, and it connects to the IRC network. The advantage of this, for me,
is that it can stay connected to the network even when I'm not: logging
conversations and messages and holding on to my nickname for
me.[![IRC](http://interlockroc.wpengine.com/wp-content/uploads/2012/11/linkinus2-300x189.png)](http://interlockroc.wpengine.com/wp-content/uploads/2012/11/linkinus2.png)

I initially started with a blank slate: an install of Ubuntu Server
12.04 LTS in a virtual machine (thanks to our wonderful netadmin team).
Almost immediately I realized I had a problem though: the VM was behind
a firewall and NAT, with only a single firewall rule and port forward
for SSH.

One of our members recently sent out a message to our mailing list about
doing some cool things with SSH. So I thought it would be a great
opportunity to take advantage of this new knowledge. In order to set
this up, I needed to have SSH open and accessible on another machine.
For convenience sake, I made this the machine that I was going to
connect to the BNC from.

For the purposes of this article, I'm going to refer to the two
computers in question as "bwvm" which is the Ubuntu Server virtual
machine, and "bwhome" which is my MacBook Pro on my desk ("bw" being my
initials -- clever, I know).

The first thing I did was setup SSH keys so that I didn't have to use
passwords when connecting back and fourth between these two computers.
I've done this a few times before but it isn't something I do on a daily
basis, so I followed this excellent guide from Paul Keck on doing so:
[HOTWO: set up ssh keys](http://paulkeck.com/ssh/). The gist is that you
generate a public/private key-pair on each computer
(`ssh-keygen -t dsa`) and then copy the contents of the resulting
`id_dsa.pub` public key file to the `authorized_keys2` file on the
opposite computer (i.e. bwvm's `id_dsa.pub` contents go into bwhome's
`authorized_keys2` file). Now I can SSH back and fourth freely.

Next step: install and configure a BNC. At first I started with psyBNC.
I ran into some troubles with that though, in that for some reason it
would only allow me to use super insecure passwords (instead of the
insanely complex ones that I'd generated with
[1Password](https://agilebits.com/onepassword)) and it refused to
connect to some of the IRC servers I wanted to connect to. I spent some
time troubleshooting but ultimately decided it wasn't worth
the hassle and went with a recommendation to use an easier to configure
BNC: ZNC.

I got ZNC installed and configured and began the process of forwarding
the port via SSH. The command I'm using to do so looks like this:\
`ssh bwhome -R 4242:localhost:31337 -N`\
When run from a shell on bwvm what this does is links port 31337 on bwvm
to port 4242 on bwhome (which to me is localhost -- the computer I'm
sitting at). So what I can do now is  run a `/connect localhost 4242` in
my IRC client, and be connected to the BNC running on port 31337 on bwvm
without bugging the netadmin team for another port forward and firewall
rule!

This is a bit convoluted, but works. At the moment, the process looks
like this (sitting at bwhome):\
`me@bwhome:~$ ssh bwvm me@bwvm:~$ ssh bwhome -R 4242:localhost:31337 -N & [switch back to bwhome] me@bwhome:~$ irssi /connect localhost 4242 (BNC password) `

The result:\
![Yay! IRC
goodness](https://www.evernote.com/shard/s12/sh/69f51770-2020-4b17-b4a1-2b9c4ff9cec8/804981870bec3e00fb98da354041f354/res/319665fe-898d-4ba9-bb62-63820bff07f6/skitch.png)

(Yay! IRC goodness)

Instead I'd like to simply run one command from bwhome, without having
to initiate a shell session with bwvm. This should be possible by simply
switching some of the command around. To do that it will likely end up
looking something like this (again, sitting at bwhome):\
`ssh bwvm -L 4242:localhost:31337 -N &`\
(actually it looks exactly like that)

One distinct advantage of this method (using SSH) over having a firewall
rule and a port forward is an added layer of security: in order to
access my BNC someone would have to be able to SSH into my VM. Note that
I don't have to use SSL when connecting to the BNC, because all of the
traffic is already tunneled over SSH.

For anyone wondering what app that sexy screenshot came from, it is
[Linkinus](http://www.conceitedsoftware.com/linkinus) from Conceited
Software -- an IRC client for OS X -- using the Erstwhile theme. Very
retro.
