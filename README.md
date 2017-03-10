# interlock-rochester.github.io.src
Webpage source

#Computer Setup:
sudo apt install pelican

# get the repos
'''
mkdir interlock_website
cd interlock_website
git clone git@github.com:Interlock-Rochester/interlock-rochester.github.io.src.git
cd interlock-rochester.github.io.src.git
git clone git@github.com:Interlock-Rochester/interlock-rochester.github.io.git output
'''
# Start Development version of site
'''
./develop_server.sh start
'''

# Deploy site:
'''
cd ~/interlock_website
pelican
'''
Commit and push .src git repo
'''
cd output
commit and push output git repo
'''

