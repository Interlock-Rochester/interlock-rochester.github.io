
# ls rst/*rst | xargs -n1 -i echo rm content/\*rst \; cp {} content \; make html \&\& echo {} succeeded | sh

mkdir rst-successful ; ls rst/*rst | xargs -n1 -i echo rm content/\*rst \; cp {} content \; make html \&\&  cp {} rst-successful/ | sh
