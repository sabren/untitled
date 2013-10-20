"""
oberon to js compiler
"""
from __future__ import print_function
import cStringIO

def rex(pattern):       return ('rex', pattern)
def gra(pattern):       return ('gra', pattern)
def sep(patten, by):    return ('sep', patten, by)
def alt(patterns):      return ('alt', patterns)
def seq(ptn_list):      return ('seq', ptn_list)
def dfn(name, pattern): return ('dfn', name, pattern)
def ref(name):          return ('ref', name)
def opt(ptn):           return ('opt', ptn)
def rep(ptn):           return ('rep', ptn)
def orp(ptn):           return ('orp', ptn)
def known(kind):        return ('known', kind)
def initial(values):    return ('initial', values)
def ref(name):          return ('ref', name)
def new(kind, pattern): return ('new', kind, pattern)
def hold(kind):         return ('hold', kind)
def drop(kind):         return ('drop', kind)
def take(kind):         return ('take', kind)
def same(kind):         return ('same', kind)
def other(kind):        return ('other', kind)
# like known, but exclude the one we're currently defining (type x = x)
def scope(kind):        return ('scope', kind)
def fwd(rule):          return ('fwd', rule)
 # like ref but for something not declared yet
def todo(note):
    print('todo:', note)

const_expr = 'const_expr'
condition = 'condition'

block = gra([])

dfn('<vars>', [sep(new('@var', ref('iden')), by=','),
               ':', known('@type')])


# okay, this is hideous, but it's at least nicer than writing the
# entire parser out by hand. basically it's just a big data structure
# that defines the grammar for oberon/retro pascal

grammar =\
[ 'MODULE', hold(new('@module', dfn('iden', r'[a-z][a-zA-Z]+'))),
  'IMPORT', sep(ref('iden'), ','),
  dfn('<declarations>',
      [sep({
     'CONST': rep([ new('@const', ref('iden')), '=',
                    const_expr, ';']),
     'TYPE' : rep([ hold(new('@type', ref('iden'))), '=',
                    dfn('<type>',
                        alt([ other('@type'),
                              [ 'array', 'of', other('@type')],
                              [ 'record',
                                opt(['(', known('@type'), ')']),
                                sep(ref('<vars>'), ';'),
                                'end'],
                              ['procedure',
                               dfn('<signature>',
                                   [opt([scope(['(',
                                    sep([opt({'VAR', 'CONST'}),
                                         ref('<vars>')], by=';'),
                                                ')'])]),
                                    opt([':', known('@type')]) ])]
                              ])), drop('@type'), ';']),
     'VAR': rep([ref('<vars>'), opt(['=', initial('values')])]),
     'PROCEDURE':
         [opt('*'), hold(new('@proc', ref('iden'))),
          scope([ref('<signature>'), ';',
                 ref('<declarations>'), ',',
                 ref('<block>'),
                 same('@proc')]) ],
     }, by=';')]),
dfn('<block>', [
  'BEGIN', dfn('<stmts>', sep(dfn('<stmt>', alt({
    'IF' : [condition, 'THEN', ref('<stmts>'),
            rep(['ELIF', condition, 'THEN', ref('<stmts>')]),
            opt(['ELSE', ref('<stmts>')]),
            'END'],
    'FOR' : [known('@var'), ':=', const_expr, 'TO', const_expr,
             opt([{'WHILE', 'UNTIL'}, condition]),
             # retro pascal extension
             'DO', ref('<stmts>'),
             'END'],
    'CASE' : [opt('TYPE'),  # another retro pascal extension
              fwd('<expr>'), 'OF', opt({'|'}),
              sep([alt(['[',
                        dfn('<range>',
                            [const_expr,
                             opt(['..', const_expr])]),
                        sep(ref('<range>'), ','), ']']),
                   ':', ref('<stmts>')], '|'),
              'ELSE', ref('<stmts>'), 'END'],
    'WHILE' : ['DO', sep('<stmt>', ';'), 'END'],
    'REPEAT': [ref('<stmts>'), 'UNTIL', condition],
    # if it's not a key word, it should be an identifier:
    '' : [ dfn('lhs',
               [known('iden'),
                { '.' : [todo('attributes')],
                  '[' : [ref('expr')] } ]),
           { ':=' : dfn('<expr>', [todo('expressions')]),
             '('  : [sep(ref('<expr>'), ','), ')'] } ],
    })), by=';')),
  'END' ]), same('iden'), '.']

print(grammar)

class Ob2Js(object):
    """
    A simple oberon -> Js compiler.
    """
    def __init__(self, source=None):
        if source: self.source = source
        else: self.source = ""

def translate(self, source):
    """
    Creates a generator that yields lines of javascript code.
    :param source: the oberon source code to compile
    """
    pass
