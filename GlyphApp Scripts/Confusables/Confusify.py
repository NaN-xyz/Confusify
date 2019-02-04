#MenuTitle: Confusify
# -*- coding: utf-8 -*-
__doc__="""
Generates fonts that swap unicode prescribed confusables for the original reference glyph.
"""

# 
# https://twitter.com/luke_prowse
#

import codecs
import GlyphsApp

font = Glyphs.font

# could randomise order of confusables so no two fonts are the same

def updated_code( oldcode, beginsig, endsig, newcode ):
	"""Replaces text in oldcode with newcode, but only between beginsig and endsig."""
	begin_offset = oldcode.find( beginsig )
	end_offset   = oldcode.find( endsig ) + len( endsig )
	newcode = oldcode[:begin_offset] + beginsig + newcode + "\n" + endsig + oldcode[end_offset:]
	return newcode

def create_otfeature( featurename = "calt",
                      featurecode = "# empty feature code",
                      targetfont  = Font,
                      codesig     = "DEFAULT-CODE-SIGNATURE" ):
	"""
	Creates or updates an OpenType feature in the font.
	Returns a status message in form of a string.
	"""
	
	beginSig = "# BEGIN " + codesig + "\n"
	endSig   = "# END "   + codesig + "\n"
	
	if featurename in [ f.name for f in targetfont.features ]:
		# feature already exists:
		targetfeature = targetfont.features[ featurename ]
		
		if beginSig in targetfeature.code:
			# replace old code with new code:
			targetfeature.code = updated_code( targetfeature.code, beginSig, endSig, featurecode )
		else:
			# append new code:
			targetfeature.code += "\n" + beginSig + featurecode + "\n" + endSig
			
		return "Updated existing OT feature '%s'." % featurename
	else:
		# create feature with new code:
		newFeature = GSFeature()
		newFeature.name = featurename
		newFeature.code = beginSig + featurecode + "\n" + endSig
		targetfont.features.append( newFeature )
		return "Created new OT feature '%s'." % featurename

def create_otclass( classname   = "@default",
                    classglyphs = [  ],
                    targetfont  = Font ):
	"""
	Creates an OpenType class in the font.
	Default: class @default with currently selected glyphs in the current font.
	Returns a status message in form of a string.
	"""
	
	# strip '@' from beginning:
	if classname[0] == "@":
		classname = classname[1:]
	
	classCode = " ".join( classglyphs )
	
	if classname in [ c.name for c in targetfont.classes ]:
		targetfont.classes[classname].code = classCode
		return "Updated existing OT class '%s'." % classname
	else:
		newClass = GSClass()
		newClass.name = classname
		newClass.code = classCode
		targetfont.classes.append( newClass )
		return "Created new OT class: '%s'." % classname


def generateOT ():

	print "\nUsing MekkaBlue OT generation code from BEOWULFERIZER\n-"

	# Create Classes:
	print create_otclass( classname="default", classglyphs=keyDict, targetfont=font )
	for i in range( alphabets ):
		print create_otclass( classname="calt"+str(i), classglyphs=[ n+".calt"+str(i) for n in keyDict ], targetfont=Font )

	# Create OT Feature:
	ConfusoWolf = ""
	for i in range( ( alphabets * ( linelength//alphabets ) + 1 ), 0, -1 ):
		ConfusoWolf += "sub @default' " + "@default " * i + "by @calt" + str( ( range(alphabets) * ((linelength//alphabets)+2))[i] ) + ";\n"

	print create_otfeature( featurename="calt", featurecode=ConfusoWolf, targetfont=Font, codesig="CONFUSABLES via BEOWULFERIZER")


# load sorted list

fd = codecs.open('data_confusables-short.txt','r',encoding='utf-8')
data = fd.read().splitlines()
fd.close()

ConfList = list()

# convert data to list of confusables

for dataline in data:
	lstr = dataline.split("\t")
	ConfList.append(lstr)

GlyphsAvailable = 0
totalCalt = 0
confCount = 0

GlyphsToCalt = list() # list of all glyphs in font and available confusables to calt
GlyphsToCalt_local = list() # above but in glyphs naming

for dl in ConfList:

	glyphname = dl[0]
	optionsnum = len(dl)

	tmpconflist = list()
	tmpconflist_local = list()

	# check to see if glyph exists

	if font.glyphs[glyphname]: 
		tcalt = optionsnum-1

		# check if each confusable exists and create new list
	
		for conf in dl:
			if font.glyphs[conf]:
					tmpconflist.append(conf)
					tmpconflist_local.append(font.glyphs[conf].name)
					confCount+=1

		GlyphsAvailable+=1

	if len(tmpconflist)>1:
		GlyphsToCalt.append(tmpconflist)
		GlyphsToCalt_local.append(tmpconflist_local)	


print "Key glyphs available in font: " + str(GlyphsAvailable)
print "Of which have at least one confusable: " + str(len(GlyphsToCalt))
print "Total number of confusables in font: " + str(confCount)



# list for Opentype default class
keyConfs = list()
keyDict = dict()

for key in GlyphsToCalt_local:
	keyConfs.append(key[0])
	keyDict[key[0]] = key[0]

# show all available glyphs inc confusables
# count highest number of confusable for a glyph

maxconf = 0
avgconf = 0

for gc in GlyphsToCalt:
	
	gstr = ""
	thisclen = len(gc)
	avgconf += thisclen

	if thisclen>maxconf: 
		maxconf = thisclen

	for lc in gc:
		gstr = gstr + lc + " " 	
	print gstr

avgCALT = avgconf / len(GlyphsToCalt)
alphabets = maxconf
linelength = alphabets

print "Highest CALT Level: " + str(maxconf)
print "Average number of confusables: " + str(avgCALT)


font.disableUpdateInterface()

for gc in GlyphsToCalt:
	
	cyclesize = len(gc)-1
	counter=0
	tmpstring = ""

	for caltx in range(maxconf):

		tmpstring = tmpstring + gc[counter] + ""

		newGlyph = font.glyphs[gc[counter]].copy()
		newname = font.glyphs[gc[0]].name
		newGlyph.unicode = None
		newGlyph.name = newname + ".calt" + str(caltx)
		newGlyph.color = 8 #purple
		Font.glyphs.append(newGlyph)

		if counter==cyclesize: 
			counter=0
		else:
			counter+=1

font.enableUpdateInterface()


generateOT()



