
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '824540855AFB6491E9477355E371E790'
    
_lr_action_items = {'NOTE':([7,13,14,15,17,18,],[15,17,15,-16,-15,17,]),'$end':([1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,],[-8,-2,-1,0,-6,-5,-10,-4,-7,-9,-3,-14,-11,-16,-13,-15,-12,]),'REVERT':([0,],[1,]),'TEMPO':([1,2,3,5,6,8,9,10,11,12,13,14,15,16,17,18,],[-8,-2,8,-6,-5,-10,-4,-7,-9,-3,-14,-11,-16,-13,-15,-12,]),'DURATION':([1,2,3,5,6,8,9,10,11,12,13,14,15,16,17,18,],[-8,-2,7,-6,-5,-10,-4,-7,-9,-3,-14,-11,-16,-13,-15,-12,]),'IDENTIFIER':([1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,],[-8,-2,11,-6,-5,14,-10,-4,-7,-9,-3,16,-11,-16,-13,-15,-12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sequence2':([3,],[5,]),'sequence1':([3,],[6,]),'notes':([7,14,],[13,18,]),'revert':([0,],[2,]),'sequence5':([3,],[9,]),'sequence4':([3,],[12,]),'sequence3':([3,],[10,]),'sequences':([0,],[3,]),'all':([0,],[4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> all","S'",1,None,None,None),
  ('all -> sequences','all',1,'p_all','converter.py',110),
  ('sequences -> revert','sequences',1,'p_sequences','converter.py',131),
  ('sequences -> sequences sequence4','sequences',2,'p_sequences','converter.py',132),
  ('sequences -> sequences sequence5','sequences',2,'p_sequences','converter.py',133),
  ('sequences -> sequences sequence1','sequences',2,'p_sequences','converter.py',134),
  ('sequences -> sequences sequence2','sequences',2,'p_sequences','converter.py',135),
  ('sequences -> sequences sequence3','sequences',2,'p_sequences','converter.py',136),
  ('revert -> REVERT','revert',1,'p_revert','converter.py',141),
  ('sequence5 -> IDENTIFIER','sequence5',1,'p_sequence5','converter.py',146),
  ('sequence4 -> TEMPO','sequence4',1,'p_sequence4','converter.py',151),
  ('sequence3 -> DURATION IDENTIFIER','sequence3',2,'p_sequence3','converter.py',156),
  ('sequence2 -> DURATION IDENTIFIER notes','sequence2',3,'p_sequence2','converter.py',164),
  ('sequence1 -> DURATION notes IDENTIFIER','sequence1',3,'p_sequence1','converter.py',174),
  ('sequence1 -> DURATION notes','sequence1',2,'p_sequence1','converter.py',175),
  ('notes -> notes NOTE','notes',2,'p_notes','converter.py',186),
  ('notes -> NOTE','notes',1,'p_notes','converter.py',187),
]
