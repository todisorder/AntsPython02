echo "Press Return to use same parameters, other key to change parameters."
read -s -n 1 key  # -s: do not echo input character. -n 1: read only 1 character (separate with space)
# double brackets to test, single equals sign, empty string for just 'enter' in this case...
# if [[ ... ]] is followed by semicolon and 'then' keyword
DIR=Plots
if [ -d "$DIR" ]; then
rm -rf "$DIR"
fi
mkdir "$DIR"

if [[ $key = "" ]]; then
    python3 AntsParalell.py
else
    python3 GUIpy.py && python3 AntsParalell.py
fi


