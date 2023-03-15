#-------------------------------------------------------------------------------
# Name:        choose_chords
# Purpose:
#
# Author:      bucky
#
# Created:     23/07/2013
# Copyright:   (c) bucky 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def what_key (key,flag_sharp):
    key_num=0 # set to 0 to use as flag if no match key input
    if key in {'c','C','b#','B#',}:
        key_num=12
        key='C'
    if key in {'c#','C#','db','Db'}:
        key_num=11
        key='Db'
    if key in {'d','D'}:
        key_num=10
        key='D'
    if key in {'d#','D#','eb','Eb'}:
        key_num=9
        key='Eb'
    if key in {'e','E','fb','Fb'}:
        key_num=8
        key='E'
    if key in {'f','F','e#','E#'}:
        key_num=7
        key='F'
    if key in {'f#','F#','gb','Gb'}:
        key_num=6
        if flag_sharp==1:
            key='F#'
        else:
            key='Gb'
    if key in {'g','G'}:
        key_num=5
        key='G'
    if key in {'g#','G#','ab','Ab'}:
        key_num=4
        key='Ab'
    if key in {'a','A'} :
        key_num=3
        key='A'
    if key in {'a#','A#','bb','Bb'}:
        key_num=2
        key='Bb'
    if key in {'b','B','cb','Cb'}:
        key_num=1
        key='B'
    if key_num==0: # default to C if input not within parameters
        key_num=12
        key='C'
    return key,key_num
def what_chord (chord):
    # default chord if input not within accepted parameters
    chord_name      = 'Maj'
    chord_structure = '1,3,5'
    selected_notes  = '100010010000'
# ######################################### major chords
    if chord in                  {'M','MA','Maj','maj','',}:
        chord_name      = 'Maj'
        chord_structure =        '1,3,5'
        selected_notes  ='100010010000'
    if chord in                  {'6'}:
        chord_name      = '6'
        chord_structure =         '1,3,5,6'
        selected_notes  =                        '100010010100'
    if chord in                  {'6/9','69'}:
        chord_name      = '6/9'
        chord_structure =         '1,3,5,6,9'
        selected_notes  =                        '101010010100'
    if chord in                  {'(add 9)','add9','add 9'}:
        chord_name      = '(add 9)'
        chord_structure =         '1,3,5,9'
        selected_notes  =                        '101010010000'
    if chord in                  {'M7','M 7','MA7','MA 7','ma7','ma 7','Maj7','Maj 7','maj7','maj 7','MAJ7','MAJ 7'}:
        chord_name      = 'M7'
        chord_structure =         '1,3,5,7'
        selected_notes  =                        '100010010001'
    if chord in                  {'M7b5'}:
        chord_name      = 'M7b5'
        chord_structure =         '1,3,b5,7'
        selected_notes  =                        '100010100001'
    if chord in                  {'M7b5sus'}:
        chord_name      = 'M7b5sus'
        chord_structure =         '1,4,b5,7'
        selected_notes  =                        '100001100001'
    if chord in                  {'M7#5'}:
        chord_name      = 'M7#5'
        chord_structure =         '1,3,#5,7'
        selected_notes  =                        '100010001001'
# M7#5sus
    if chord in                  {'M9','M 9','MA9','MA 9','MAJ9','MAJ 9','ma9','ma 9','maj9','maj 9','major9','major 9','Major9','Major 9','MAJOR9','MAJOR 9'}:
        chord_name      = 'M9'
        chord_structure =         '1,3,5,7,9'
        selected_notes  =                        '101010010001'
# M9b5
# M9#5
# Mb9
# M11
# M11(omit 9)
    if chord in                  {'M7#11'}:
        chord_name      = 'M7#11'
        chord_structure =         '1,3,5,7,#11'
        selected_notes  =                        '100010110001'
    if chord in                  {'M9#11'}:
        chord_name      = 'M9#11'
        chord_structure =         '1,3,5,7,9,#11'
        selected_notes  =                        '101010110001'
    if chord in                  {'M7+13','M7 +13','M 7+13','M 7 +13','MA7(add 13)','MA7add13','MA7add 13','MA7 add13','MA7 add 13','MA7(add 13)','Ma7add13','Ma7add 13','Ma7 add13','Ma7 add 13','ma7(add 13)','ma7add13','ma7add 13','ma7 add13','ma7 add 13','ma 7(add 13)','ma 7add13','ma 7add 13','ma 7 add13','ma 7 add 13','MA 7(add 13)','MA 7add13','MA 7add 13','MA 7 add13','MA 7 add 13'}:
        chord_name      = 'M7 (add 13)'
        chord_structure =         '1,3,5,7,13'
        selected_notes  =                        '100010010101'
    if chord in                  {'M13'}:
        chord_name      = 'M13'
        chord_structure =         '1,3,5,7,9,13'
        selected_notes  =                        '101010010101'
    if chord in                  {'M13#11'}:
        chord_name      = 'M13#11'
        chord_structure =         '1,3,5,7,9,#11,13'
        selected_notes  =                        '101010110101'
# M#13
#M13 (add11)
# ######################################## minor chords
    if chord in                  {'m','-','min','minor'}:
        chord_name      = 'm'
        chord_structure =         '1,b3,5'
        selected_notes  =                        '100100010000'
    if chord in                  {'m6','-6'}:
        chord_name      = 'm6'
        chord_structure =         '1,b3,5,6'
        selected_notes  =                        '100100010100'
    if chord in                  {'m69','m6/9'}:
        chord_name      = 'm6/9'
        chord_structure =         '1,b3,5,6,9'
        selected_notes  =                        '101100010100'
    if chord in                  {'m(add9)','madd9','m(add 9)'}:
        chord_name      = 'm(add 9)'
        chord_structure =         '1,b3,5,9'
        selected_notes  =                        '101100010000'
    if chord in                  {'m7','-7'}:
        chord_name      = 'm7'
        chord_structure =         '1,b3,5,b7'
        selected_notes  =                        '100100010010'
    if chord in                  {'m7(add 11)','m7(add11)','-7add11','-7 add11','-7 add 11','m7add11','-7 add11','m7 add 11'}:
        chord_name      = 'm7(add 11)'
        chord_structure =         '1,b3,5,b7,11'
        selected_notes  =                        '100101010010'
    if chord in                  {'m7(add13)','m7(add 13)'}:
        chord_name      = 'm7(add 13)'
        chord_structure =         '1,b3,5,b7,13'
        selected_notes  =                        '100100010110'
    if chord in                  {'m11(omit 9)','m11 no 9','m11 no9','m11(no 9)'}:
        chord_name      = 'm11(omit 9)'
        chord_structure =         '1,b3,5,b7,11'
        selected_notes  =                        '100101010010'
    if chord in                  {'m(M7)','-M7','mM7'}:
        chord_name      = 'm(M7)'
        chord_structure =         '1,b3,5,7'
        selected_notes  =                        '100100010010'
    if chord in                  {'m7b5','-7b5','m7-5','-7-5'}:
        chord_name      = 'm7b5'
        chord_structure =         '1,b3,b5,b7'
        selected_notes  =                        '100100100010'
    if chord in                  {'m9'}:
        chord_name      = 'm9'
        chord_structure =         '1,b3,5,b7,9'
        selected_notes  =                        '101100010010'
    if chord in                  {'m9(M7)','m9M7','-9M7','-M9','mM9'}:
        chord_name      = 'm9M7'
        chord_structure =         '1,b3,5,7,9'
        selected_notes  =                        '101100010010'
    if chord in                  {'m9b5','m9-5','-9b5','-9-5'}:
        chord_name      = 'm9b5'
        chord_structure =         '1,b3,b5,b7,9'
        selected_notes  =                        '101100100010'
# m9M7b5
# mb9
    if chord in                  {'m11'}:
        chord_name      = 'm11'
        chord_structure =         '1,b3,5,b7,9,11'
        selected_notes  =                        '101101010010'
    if chord in                  {'m11b5','m11-5','-11b5','-11-5'}:
        chord_name      = 'm11b5'
        chord_structure =         '1,b3,b5,b7,9,11'
        selected_notes  =                        '101101100010'
# m11b9
# m11b9b5
    if chord in                  {'m13'}:
        chord_name      = 'm13'
        chord_structure =         '1,b3,5,b7,9,11,13'
        selected_notes  =                        '101101010110'
# m13b5
# m13 no 11
# m13b5 no 11
# m13b9
# m13b9 no 11
# m13b9b5
# m13b9b5 no 11
# ######################################## deminished suspension and augmented chords
    if chord in                  {'dim','d'}:
        chord_name      = 'dim'
        chord_structure =         '1,b3,b5'
        selected_notes  =                        '100100100000'
    if chord in                  {'dim7'}:
        chord_name      = 'dim7'
        chord_structure =         '1,b3,b5,bb7'
        selected_notes  =                        '100100100100'
    if chord in                  {'dim7(add M7)','dim7(addM7)'}:
        chord_name      = 'dim7(add M7)'
        chord_structure =         '1,b3,b5,6,7'
        selected_notes  =                        '100100100101'
    if chord in                  {'+','aug'}:
        chord_name      = 'aug'
        chord_structure =         '1,3,#5'
        selected_notes  =                        '100010001000'
    if chord in                  {'sus','sus4','sus 4'}:
        chord_name      = 'sus'
        chord_structure =         '1,4,5'
        selected_notes  =                        '100001010000'
    if chord in                  {'7sus','7sus4','7sus 4'}:
        chord_name      = '7sus'
        chord_structure =         '1,4,5,b7'
        selected_notes  =                        '100001010010'
    if chord in                  {'7sus(add 3)','7sus add3','7sus(add3)','7susadd3','7sus add 3'}:
        chord_name      = '7sus(add 3)'
        chord_structure =         '1,3,4,5,b7'
        selected_notes  =                        '100011010010'
    if chord in                  {'7sus4-3'}:
        chord_name      = '7sus4-3'
        chord_structure =         '1,3,4,5,b7'
        selected_notes  =                        '100011010010'
    if chord in                  {'9sus','9sus4','9sus 4'}:
        chord_name      = '9sus'
        chord_structure =         '1,4,5,b7,9'
        selected_notes  =                        '101001010010'
    if chord in                  {'13sus'}:
        chord_name      = '13sus'
        chord_structure =         '1,4,5,b7,9,13'
        selected_notes  =                        '101001010110'
    if chord in                  {'7b9sus'}:
        chord_name      = '7b9sus'
        chord_structure =         '1,4,5,b7,b9'
        selected_notes  =                        '110001010010'
    if chord in                  {'13b9sus'}:
        chord_name      = '13b9sus'
        chord_structure =         '1,4,5,b7,b9,13'
        selected_notes  =                        '110001010110'
# ########################################## dominant chords
    if chord in                  {'7','dom7','dom 7'}:
        chord_name      = '7'
        chord_structure =         '1,3,5,b7'
        selected_notes  =                        '100010010010'
    if chord in                  {'7b5'}:
        chord_name      = '7b5'
        chord_structure =         '1,3,b5,b7'
        selected_notes  =                        '100010100010'
    if chord in                  {'7#5'}:
        chord_name      = '7#5'
        chord_structure =         '1,3,#5,b7'
        selected_notes  =                        '100010001010'
    if chord in                  {'9'}:
        chord_name      = '9'
        chord_structure =         '1,3,5,b7,9'
        selected_notes  =                        '101010010010'
    if chord in                  {'9b5'}:
        chord_name      = '9b5'
        chord_structure =         '1,3,b5,b7,9'
        selected_notes  =                        '101010100010'
    if chord in                  {'9#5'}:
        chord_name      = '9#5'
        chord_structure =         '1,3,#5,b7,9'
        selected_notes  =                        '101010001010'
    if chord in                  {'7b9'}:
        chord_name      = '7b9'
        chord_structure =         '1,3,5,b7,b9'
        selected_notes  =                        '110010010010'
    if chord in                  {'7#9'}:
        chord_name      = '7#9'
        chord_structure =         '1,3,5,b7,#9'
        selected_notes  =                        '100110010010'
    if chord in                  {'7b9b5','7b5b9'}:
        chord_name      = '7b9b5'
        chord_structure =         '1,3,b5,b7,b9'
        selected_notes  =                        '110010100010'
    if chord in                  {'7#9#5','7#5#9'}:
        chord_name      = '7#9#5'
        chord_structure =         '1,3,#5,b7,#9'
        selected_notes  =                        '100110001010'
    if chord in                  {'7b9#5','7#5b9'}:
        chord_name      = '7b9#5'
        chord_structure =         '1,3,#5,b7,b9'
        selected_notes  =                        '110010001010'
    if chord in                  {'7#11'}:
        chord_name      = '7#11'
        chord_structure =         '1,3,5,b7,#11'
        selected_notes  =                        '100010110010'
    if chord in                  {'7#11b9','7b9#11'}:
        chord_name      = '7#11b9'
        chord_structure =         '1,3,5,b7,b9,#11'
        selected_notes  =                        '110010110010'
    if chord in                  {'7#11#9','7#9#11'}:
        chord_name      = '7#11#9'
        chord_structure =         '1,3,5,b7,#9,#11'
        selected_notes  =                        '100110110010'
    if chord in                  {'13'}:
        chord_name      = '13'
        chord_structure =         '1,3,5,b7,9,13'
        selected_notes  =                        '101010010110'
    if chord in                  {'13b5'}:
        chord_name      = '13b5'
        chord_structure =         '1,3,b5,b7,9,13'
        selected_notes  =                        '101010100110'
    if chord in                  {'13b9'}:
        chord_name      = '13b9'
        chord_structure =         '1,3,5,b7,b9,13'
        selected_notes  =                        '110010010110'
    if chord in                  {'13#11'}:
        chord_name      = '13#11'
        chord_structure =         '1,3,5,b7,9,#11,13'
        selected_notes  =                        '101010110110'
# ########################################### scales and modes
    if chord.upper() in                {'IO','ION','IONI','IONIA','IONIAN'}:
        chord_name      = ' Major scale (Ionian)'
        chord_structure =         '1,2,3,4,5,6,7'
        selected_notes  =                        '101011010101'
    if chord.upper() in                {'DO','DOR','DORI','DORIA','DORIAN'}:
        chord_name      = ' Dorian'
        chord_structure =         '1,2,b3,4,5,6,b7'
        selected_notes  =                        '101101010110'
    if chord.upper() in                {'PH','PHR','PHRY','PHRYG','PHRYGI','PHRYGIA','PHRYGIAN'}:
        chord_name      = ' Phrygian'
        chord_structure =         '1,b2,b3,4,5,b6,b7'
        selected_notes  =                        '110101011010'
    if chord.upper() in                {'LY','LYD','LYDI','LYDIA','LYDIAN'}:
        chord_name      = ' Lydian'
        chord_structure =         '1,2,3,#4,5,6,7'
        selected_notes  =                        '101010110101'
    if chord.upper() in                {'MI','MIX','MIXO','MIXOL','MIXOLY','MIXOLYD','MIXOLYDI','MIXOLYDIA','MIXOLYDIAN'}:
        chord_name      = ' Mixolydian'
        chord_structure =         '1,2,3,4,5,6,b7'
        selected_notes  =                        '101011010110'
    if chord.upper() in                {'AO','AOL','AE','AEO','AEOL','AEOLI','AEOLIA','AEOLIAN'}:
        chord_name      = ' Minor scale (Aeolian)'
        chord_structure =         '1,2,b3,4,5,b6,b7'
        selected_notes  =                        '101101011010'
    if chord.upper() in                {'LO','LOC','LOCR','LOCRI','LOCRIA','LOCRAIN'}:
        chord_name      = ' Locrian'
        chord_structure =         '1,b2,b3,4,b5,b6,b7'
        selected_notes  =                        '110101101010'
    if chord.upper() in                {'PENT','PENTATONIC','PENT MAJ','PENTMAJ','PENTATONIC MAJ','PENTATONIC MAJOR'}:
        chord_name      = '6/9 Pentatonic Major'
        chord_structure =         '1,2,3,5,6'
        selected_notes  =                        '101010010100'
    if chord.upper() in                {'PENT MIN','PENTMIN'}:
        chord_name      = ' Pentatonic minor'
        chord_structure =         '1,b3,4,5,b7'
        selected_notes  =                        '100101010010'
    if chord.upper() in                {'BL','BLU','BLUE','BLUES'}:
        chord_name      = ' Blues'
        chord_structure =         '1,b3,4,#4,5,b7'
        selected_notes  =                        '100101110010'
    return chord_name,chord_structure,selected_notes
def scale (n,f): # still need to add special lables to accomidate all chords in all keys
    all_notes_flats='--C-|--Db|--D-|--Eb|--E-|--F-|--Gb|--G-|--Ab|--A-|--Bb|--B-|'# Db,Eb,F,Bb,Ab
    all_notes_sharp='--C-|--C#|--D-|--D#|--E-|--F-|--F#|--G-|--G#|--A-|--A#|--B-|'# C,D,E,G,A
    special_f_sharp='--C-|--C#|--D-|--D#|--E-|--E#|--F#|--G-|--G#|--A-|--A#|--B-|'# F#
    special_g_flat ='--C-|--Db|--D-|--Eb|--E-|--F-|--Gb|--G-|--Ab|--A-|--Bb|--Cb|'# Gb
    special_100    ='--C-|--Db|--D-|--D#|--E-|--F-|--F#|--G-|--Ab|--A-|--A#|--B-|'# G7b9b5 Gm7
    special_101    ='--B#|--C#|--D-|--D#|--E-|--E#|--F#|--G-|--G#|--A-|--A#|--B-|'# F#Lydian,M7#11,M9#11,M13#11
    special_102    ='--B#|--C#|--D-|--D#|--E-|--E#|--F#|--G-|--G#|-G##|--A#|--B-|'# F#7#11 type chords
    if n==1:# B
        all_notes=all_notes_sharp+all_notes_sharp
    if n==2:# Bb
        all_notes=all_notes_flats+all_notes_flats
    if n==3:# A
        all_notes=all_notes_sharp+all_notes_sharp
    if n==4:# Ab
        all_notes=all_notes_flats+all_notes_flats
    if n==5:# G
        all_notes=all_notes_sharp+all_notes_sharp
        if chord_name in {'7b9','7b5','7b9b5','m7','7'}:
            all_notes=special_g_flat+special_g_flat
    if n==6: # F#,Gb
        if f==1:
            all_notes=special_f_sharp+special_f_sharp
            if chord_name in {' Lydian','M7#11','M9#11','M13#11','7#11','13#11','7#11b9'}:
                all_notes=special_101+special_101
            if chord_name in {'7#11#9','7#9'}:
                all_notes=special_102
        else:
            all_notes=special_g_flat+special_g_flat
    if n==7:# F
        all_notes=all_notes_flats+all_notes_flats
    if n==8:# E
        all_notes=all_notes_sharp+all_notes_sharp
    if n==9:# Eb
        all_notes=all_notes_flats+all_notes_flats
    if n==10:# D
        all_notes=all_notes_sharp+all_notes_sharp
    if n==11:# Db
        all_notes=all_notes_flats+all_notes_flats
    if n==12:# C
        all_notes=all_notes_sharp+all_notes_sharp
    return all_notes
def printout_of_fretboard1 (sdec,all_notes,key,string_names,frets):
    note_names=''
    ef='----|'
    fret_board_image=''
    x=0
    for i in range (12):
        if sdec[x]=='0':
            fret_board_image=fret_board_image+ef
        else:
            fret_board_image=fret_board_image+all_notes[x*5:x*5+5]
            note_names=note_names+all_notes[x*5+2:x*5+3]
            if all_notes[x*5+3:x*5+4] in {'b','#'}:
                note_names=note_names+all_notes[x*5+3:x*5+4]
        x=x+1
    fret_board_image='|'+fret_board_image+fret_board_image+fret_board_image+fret_board_image
    k,sf=what_key(string_names[0],1)
    s1=(fret_board_image[(12-sf)*5:(12-sf)*5+(frets[0]*5+1)])
    k,sf=what_key(string_names[1],1)
    s2=(fret_board_image[(12-sf)*5:(12-sf)*5+(frets[1]*5+1)])
    k,sf=what_key(string_names[2],1)
    s3=(fret_board_image[(12-sf)*5:(12-sf)*5+(frets[2]*5+1)])
    k,sf=what_key(string_names[3],1)
    s4=(fret_board_image[(12-sf)*5:(12-sf)*5+(frets[3]*5+1)])
    k,sf=what_key(string_names[4],1)
    s5=(fret_board_image[(12-sf)*5:(12-sf)*5+(frets[4]*5+1)])
    k,sf=what_key(string_names[5],1)
    s6=(fret_board_image[(12-sf)*5:(12-sf)*5+(frets[5]*5+1)])
    k,sf=what_key(string_names[6],1)
    s7=(fret_board_image[(12-sf)*5:(12-sf)*5+(frets[6]*5+1)])
    k,sf=what_key(string_names[7],1)
    s8=(fret_board_image[(12-sf)*5:(12-sf)*5+(frets[7]*5+1)])
    k,sf=what_key(string_names[8],1)
    s9=(fret_board_image[(12-sf)*5:(12-sf)*5+(frets[8]*5+1)])
    k,sf=what_key(string_names[9],1)
    s10=(fret_board_image[(12-sf)*5:(12-sf)*5+(frets[9]*5+1)])
    k,sf=what_key(string_names[10],1)
    s11=(fret_board_image[(12-sf)*5:(12-sf)*5+(frets[10]*5+1)])
    k,sf=what_key(string_names[11],1)
    s12=(fret_board_image[(12-sf)*5:(12-sf)*5+(frets[11]*5+1)])
    note_names=note_names[note_names.find(key):]+note_names[:note_names.find(key)]
    return s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,note_names
flag_open_string=0 # Nothing done with this yet. Will eventually be used to indicate open strings such as guitar vs. non open strings such as Stick
num_of_frets_per_string=[22,22,22,22,22,22,22,22,21,21,20,20] # strings 1-12 MUST BE 12 ELEMENTS!!!!
string_names=['G','D','A','E','B','F#','G','D','A','E','B','F#'] # strings 1-12 MUST BE 12 ELEMENTS!!!!
string_octaves=[4,4,3,3,2,2,1,2,2,3,3,4] # strings 1-12 # middle c is 4 # # Nothing done with this yet. Will indicate the octave of every note ie. middle C would be 4C one octave higher 5C.
flag_sharp=1
title=input('enter name of text file')
if title=='':# if no title was entered then this 'temp.txt' will be the saved text
    from random import randint
    title='stick_fretboard_printout_'+str(randint(1,10000))# if no title was entered then this 'temp.txt' will be the saved text
print ('text file will be',title+'.txt')
text_file = open (title+'.txt','w')
running = True
while running: # if typo mistakes, default value is CMaj 1,3,5  CEG
    root_note = input ('input root note or <\'stop\'> to end ')# input A,B,C,D,E,F,G and # of b (upper or lower case acceptable)
    if root_note =='stop':
        running=False
    if running==True:
        if len(root_note)>2:
            root_note=root_note[:2] # only first two characters are recognised
        root_note,root_note_num = what_key(root_note,flag_sharp)
        chord_or_scale = input ('input chord or scale ')# input chord type ie 7b9b5 or lydian
        chord_name,chord_structure,selected_notes=what_chord(chord_or_scale)
        new_selected_notes=selected_notes[root_note_num:]+selected_notes[:root_note_num]# used to bring root key note to left of string
        all_notes=scale(root_note_num,flag_sharp)
        temp=''
        x=len(root_note+chord_name)
        for i in range (20-x):
            temp=temp+' '
            x=x+1
        print (root_note+chord_name+temp+chord_structure)
        text_file.write(root_note+chord_name+temp+chord_structure+'\n')
#
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,note_names=printout_of_fretboard1 (new_selected_notes,all_notes,root_note,string_names,num_of_frets_per_string)
        frt_mk='x         x         x         x             xx              x         x'
        temp=''
        x=len(note_names)
        for i in range (18-x):
           temp=temp+' '
           x=x+1
        print (note_names)#+temp+frt_mk)
        print(s1)
        print(s2)
        print(s3)
        print(s4)
        print(s5)
        print(s6)
        print('                  '+frt_mk)
        print(s7)
        print(s8)
        print(s9)
        print(s10)
        print(s11)
        print(s12)
        print()
        text_file.write(note_names+temp+frt_mk+'\n')
        text_file.write(s1+'\n')
        text_file.write(s2+'\n')
        text_file.write(s3+'\n')
        text_file.write(s4+'\n')
        text_file.write(s5+'\n')
        text_file.write(s6+'\n')
        text_file.write('                  '+frt_mk+'\n')
        text_file.write(s7+'\n')
        text_file.write(s8+'\n')
        text_file.write(s9+'\n')
        text_file.write(s10+'\n')
        text_file.write(s11+'\n')
        text_file.write(s12+'\n')
        text_file.write('\n')
        text_file.write('\n')
text_file.close()
print ('End of program ... your text file \''+title+'.txt\'')
print ('has been saved in the same directory as this program. ')
print ('This window will shut down in approximately 15 seconds. ')
print ('Thank you for using this program designed by Bucky! ')
print()
print()
import time
time.sleep(5)
print ('Good Bye! :)')
time.sleep(1)
print()
time.sleep(1)
print('Make sure you put the milk in the refridgerator.')
time.sleep(1)
print()
time.sleep(1)
print()
time.sleep(1)
print()
time.sleep(1)
print()
time.sleep(1)
print()
time.sleep(1)
print()
