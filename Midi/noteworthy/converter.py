import ply.lex as lex
import ply.yacc as yacc

FILE = '01'

############################# UTILITIES ################################

def getFileContents(filename):
    try: 
        f = open(filename, "r")
        allLines = f.readlines()
        return " ".join(allLines)
    except IOError as e:
        print(e)
    finally:
        try: 
            f.close()
        except: 
            pass    # can't do anything if close throws

############################# CONSTANTS ################################

delta = 96
head = '''
import sys
sys.path.append("../..")
from library.mymidi import Tracks
tracks = Tracks("01", 4)
t1 = tracks.addTrack("Track 1")
t2 = tracks.addTrack("Track 2")
t3 = tracks.addTrack("Track 3")
t4 = tracks.addTrack("Track 4")
t1.setInstrument("Pad 8 (sweep)", channel = 1, pitchShift = -12, volume = 100)
t2.setInstrument("Orchestral Harp", channel = 2, pitchShift = 0, volume = 100)
t3.setInstrument("Synth Drum", channel = 3, pitchShift = -12, volume = 80)
t4.setInstrument("Bright Acoustic Piano", channel = 4, pitchShift = 0, volume = 100)

def tune(m):
''' 
tail = '''
for t in tracks.getTracks():
    tune(t)
tracks.play()
'''

############################# LEXER ################################

# token names
tokens = (
    'NOTE',
    'DURATION',
    'REVERT',
    'IDENTIFIER',
    'TEMPO',
    'COMMENT'
)

t_ignore  = ' \t'


# lexical rules
def t_SKIP(t):
    r'([+]auto[-]beam|[+]go)'
    return None

def t_COMMENT(t):
    r'[#].*\n'
    return None
    
def t_NOTE(t):
    r'\d+'
    t.value = int(t.value) + 60
    return t

def t_DURATION(t):
    r'\[\d+\]'
    t.value = int(t.value[1:-1])
    return t

def t_TEMPO(t):
    r'[+]Tempo\d+'
    t.value = int(t.value[6:])
    return t

def t_REVERT(t):
    r'[+]revert'
    t.value = t.value[1:]
    return t

def t_IDENTIFIER(t):
    r'[+][a-zA-Z]+'
    t.value = t.value[1:]
    return t

# rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex(debug=False)

############################# PARSER ################################

def p_error(x):
    print("---", x)
    
notesList = []
durationsList = []
tempo = None

def invertDuration(p):
    return int(delta/p)

def p_all(p):
    '''all : sequences'''
    def splitList(notes, durations):
        'split lists into groups of 8'
        try:
            while(True):
                outNotes = []
                outDurations = []
                for n in range(8):
                    outNotes.append(notes.pop(0))
                    outDurations.append(durations.pop(0))
                yield outNotes, outDurations
        except:
            yield outNotes, outDurations
        
    p[0] = head
    for notes, durations in splitList(notesList, durationsList):
        p[0] += "    m += {}, \\\n         {}\n".format(notes, durations)    
    print(tempo)
    p[0] += "tracks.setTempo({}/2)\n".format(tempo)
    p[0] += tail

def p_sequences(p):
    '''sequences : revert
                 | sequences sequence4
                 | sequences sequence5
                 | sequences sequence1
                 | sequences sequence2
                 | sequences sequence3
    '''

def p_revert(p):
    '''revert : REVERT'''

def p_sequence5(p):
    '''sequence5 : IDENTIFIER'''

def p_sequence4(p):
    '''sequence4 : TEMPO'''
    global tempo
    tempo = p[1]*delta

def p_sequence3(p):
    '''sequence3 : DURATION IDENTIFIER'''
    duration = invertDuration(p[1])
    identifier = p[2]    
    if identifier == 'rest':
        notesList.append(0)
        durationsList.append(duration)

def p_sequence2(p):
    '''sequence2 : DURATION IDENTIFIER notes'''
    duration = invertDuration(p[1])
    identifier = p[2]    
    notes = p[3]
  
    if identifier == 'dot': 
        duration =  int(duration * 1.5)
        
    for note in notes:
        notesList.append(note)
        durationsList.append(duration)

def p_sequence1(p):
    '''sequence1 : DURATION notes IDENTIFIER 
                 | DURATION notes'''
    duration = invertDuration(p[1])
    notes = p[2]
    if len(p) == 4:
        identifier = p[3]
        if identifier == 'triple': 
            duration = duration * 3
    for note in notes:
        notesList.append(note)
        durationsList.append(duration)
        

def p_notes(p):
    '''notes : notes NOTE
             | NOTE'''
    if type(p[1]) is int: 
        p[1] = [p[1]]
    else:
        p[1].extend([p[2]])
    p[0] = p[1]
    




# Build the parser
INFILE = 'nw-files/' + FILE + '.nw'
OUTFILE = 'py-files/' + FILE + '.py'
INSTRUMENTS = 'instrument-files/' + FILE
def parse(file):
    f = open(file, 'r')
    instruments = f.readlines()
    print(instruments)
    tracks = len(instruments)
    print(tracks)
parser = yacc.yacc()
data = getFileContents(INFILE)
instruments = parse(INSTRUMENTS)
result = parser.parse(data, debug=False)
f = open(OUTFILE, "w")
f.writelines(result)
f.close()

