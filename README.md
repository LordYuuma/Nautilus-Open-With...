# Nautilus-Open-With...
Do you like how the "Open With Other Application" functionality of Nautilus (ehh... I mean GNOME Files of course) in GNOME 3 works? Do you like how it sets your standard application to whatever you used once to open that image you wanted to edit instead of view or that website that you wanted to open in a different browser to check whether it still rendered the same way? Well, I don't and I don't like making that click to open another menu either.

But fear not, for we can simply write extensions that work the way normal file managers would handle these things!

## Install
Simply copy `nautilus-open-with-menu.py` to `/usr/share/nautilus-python/extensions/`. `setup.py` does the same but with dependencies on `setuptools`. Either way, you'll need root.

## TODO

* allow setting default via selection like the old version
* find a way to replace the original "Open With Other Application" menu entry with that version
* perhaps configuration?
