# 
# https://twitter.com/luke_prowse
#

txtA = 'Generate fonts that automatically switch glyphs for unicode confusables......'
txtB = 'The quick brown fox jumps over the lazy dog you know...'
txtC = "Hello world..."
txtD = "iii"

#p1 font
font_default = ("DejaVuLukeMono","DEJAVU MONO")

#define all fonts when tiles>1
fontlist = (
            ("IBMPlexMono_CF","PLEX MONO"),
            ("CharisSIL_CF","CHARIS"),
            ("GentiumI_CF","GENTIUM ITALIC"),
            ("DejaVu_CF","DEJAVU"),
            ("GentiumPlus_CF","GENTIUM"),
            ("IBMPlexSerifItalic_CF","PLEX SERIF ITALIC"),
            ("DejaVuSansMono_CF","DEJAVU MONO"), 
            ("CharisSIL_i_CF","CHARIS ITALIC"),
            ("Roboto_CF","ROBOTO"),
            ("IBMPlexSans_CF","PLEX SANS"),
            )

fontnumber = len(fontlist)
page_width = 1600
page_height = 1600

col1r,col1g,col1b = 0, 0, 0 # black and white
col2r,col2g,col2b = 1, 1, 1


def DrawSquare(tilenum,txt):

    for i in range(1,len(txt)+1):

        hsnapx = 0
        hsnapy = 0
        tiles = tilenum

        if tilenum==4:
            jump = page_width/2
            cheight = page_height/2
            inc = 2
            fmultiply = 1.4

        elif tilenum==16:
            jump = page_width/4
            cheight = page_height/4
            inc = 4
            fmultiply = 2

        elif tilenum==64:
            jump = page_width/8
            cheight = page_height/8
            inc = 8
            fmultiply = 3

        elif tilenum==256:
            jump = page_width/16
            cheight = page_height/16
            inc = 16
            fmultiply = 3.4

        else:
            jump = page_width
            cheight = page_height
            inc = 1
            fmultiply = 1

        cwidth = cheight

        newPage(page_width, page_height)

        startx = 0
        starty = 0

        colour = 0
        colourswitch = 0 # for the b/w tiling effect
        fontswitch = 0 # to cycle through font list

        for thistile in range(tiles):

            startx = hsnapx * jump
            starty = hsnapy * jump

            font_size = cheight / 13 # fsize 120 for a 1600 height
            line_height = font_size + (font_size*.25)
            
            #main textbox proportions
            margin = cheight / 20
            tx = startx + 0 + margin
            ty = starty + ( margin * -1 )
            tw = cwidth - (margin*2)
            th = cheight - (margin*2)
            capy = starty + margin

            #b/g square
            if colour==0: 
                currentr, currentg, currentb = col1r,col1g,col1b
                currentr2, currentg2, currentb2 = col2r,col2g,col2b
            else: 
                currentr, currentg, currentb = col2r,col2g,col2b
                currentr2, currentg2, currentb2 = col1r,col1g,col1b

            fill(currentr, currentg, currentb) # set container colour
            rect(startx, starty, cwidth, cheight)

            #set font
            if tiles==1:
                mainfont = font_default[0]
            else:
                mainfont = fontlist[fontswitch][0]

            font(mainfont)
            fontSize(font_size*fmultiply)
            lineHeight(line_height*fmultiply)        
            openTypeFeatures(calt=True)
            fill(currentr2, currentg2, currentb2) # set text colour colour

            cut = slice(0,i)
            displaystr = txt[cut]
            textBox(displaystr,(tx, ty, tw, th), align="left")

            # for any tilenumber under 64 show the caption
            if (tiles<64):
                captionsize = cheight / 40
                fontSize(captionsize*fmultiply)
                openTypeFeatures(calt=False)
                font("DejaVuLukeMono")

                # set label txt
                if tiles==1:
                    mainfonttxt = font_default[1]
                else:
                    mainfonttxt = fontlist[fontswitch][1]

                text(mainfonttxt, (tx, capy))


            # the ordering of the squares
            if hsnapx==inc-1:
                hsnapx=0
                hsnapy+=1
            else:
                hsnapx+=1

            #
            if colour==1:
                colour=0
            else:
                colour+=1

            #used for colour tiling effect
            if colourswitch==(inc-1):
                colour=1
                colourswitch+=1 
            
            elif colourswitch==((inc*2)-1): 
                colour=0
                colourswitch=0

            else:
                colourswitch+=1  

            #font switch
            if fontswitch==fontnumber-1:
                fontswitch=0
            else:
                fontswitch+=1





DrawSquare(1,txtA)

DrawSquare(4,txtB)

DrawSquare(16,txtC)

DrawSquare(64,txtD)

DrawSquare(256,"aaa")

    
saveImage('~/Desktop/drawbot-confusable.gif')


