
ls content/*rst \
| xargs -n1 -i basename {} .rst \
| xargs -n1 -i echo \
grep \":date\" content/{}.rst \
\| tr \'-\' \' \' \
\| awk \'{print \"Redirect 301 /\" \$2 \"/\" \$3 \"/\" \$4 \"/\" \"{} \
\" \"/{}\" \".html\" }\'  \
| sh > interlock-redirects

