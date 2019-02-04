# Confusables

A collection of [GlyphsApp](https://glyphsapp.com/) scripts to »Confusify« any given font as well as sample fonts to download and use under their respective licences.

A *confusable* is a glyph that is so similar to another that it may be confused for it. ſ for f, Ꮟ for b or strung together as 5໐meтhiתg 1ıк℮ τհiՏ. 

Confusify.py generates fonts that when typed automatically swap confusables for the original. All confusables generated are existing characters in the source font. In that sense it's a remix.

The original reference list of *similar-to* characters is downloadable from [unicode.org](http://unicode.org/cldr/utility/confusables.jsp). 


## Confusify.py

Where the action happens. The script analyses an open font for potential confusables against the abridged local list **confusables-list-short.txt**. If successful it will generate .calt contextual alternates for each as well as the necessary opentype classes and feature. You can then export the font as you see fit.

**Conf-makelist.py** was used to strip the source reference down from 600kb to 40kb. I then manually abridged the resulting file further to save on processing. The pre-abridged file *confusables-sorted.txt* contains lists for a wider range of scripts beyond latin should that interest you. It's worth nothing that you could roll-your-own confusables by editing the list by hand. I found some questionable choices inside the list but have chosen to interpret the data as I found it.

The larger the glyph set the more confusables and confused the text will be. In order to see the effect in action you must have contextual alternates enabled software. [scripts.sil.org](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=fontdownloads) is a great place to find useable fonts under the Open Font License.

The boat just about floats. Please leave any comments, requests, bugs here on GitHub. 

Thanks to [Georg Seifert](https://github.com/schriftgestalt) for a critical bux fix. I made more than liberal use of Rainer Erich Scheichelbauer's script [Beowulferize.py](https://github.com/mekkablue/Glyphs-Scripts/blob/master/Effects/Beowulferize.py) to generate the opentype code.


## License

Copyright 2019 [Luke Prowse](http://twitter.com/luke_prowse). Licensed under the Apache License, Version 2.0 (the "License"); you may not use the software provided here except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
	
