CONJECTUREPANEL ModelProjectProofs
PROOF "P1POSITION2, P2POSITION3, (P1POSITION2∧P2POSITION3)→ADJACENT, T1, T2, ((T1∧T2)∧ADJACENT)→Q ⊢ Q"
INFER P1POSITION2,
     P2POSITION3,
     (P1POSITION2∧P2POSITION3)→ADJACENT,
     T1,
     T2,
     ((T1∧T2)∧ADJACENT)→Q 
     ⊢ Q 
FORMULAE
0 Q,
1 T1∧T2∧ADJACENT,
2 T1∧T2∧ADJACENT→Q,
3 ADJACENT,
4 T1∧T2,
5 P1POSITION2∧P2POSITION3,
6 P1POSITION2∧P2POSITION3→ADJACENT,
7 P2POSITION3,
8 P1POSITION2,
9 T2,
10 T1,
11 (P1POSITION2∧P2POSITION3)→ADJACENT,
12 ((T1∧T2)∧ADJACENT)→Q 
IS
SEQ (cut[B,C\4,0]) ("∧ intro"[A,B\10,9]) (hyp[A\10]) (hyp[A\9]) (cut[B,C\5,0]) ("∧ intro"[A,B\8,7]) (hyp[A\8]) (hyp[A\7]) (cut[B,C\3,0]) ("→ elim"[A,B\5,3]) (hyp[A\6]) (hyp[A\5]) (cut[B,C\1,0]) ("∧ intro"[A,B\4,3]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("→ elim"[A,B\1,0]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Assignment
PROOF "∃z.¬T(z), ∀z.(P(z)→Q(z)), ∀z.(Q(z)→T(z)) ⊢ ∃z.¬P(z)"
INFER ∃z.¬T(z),
     ∀z.(P(z)→Q(z)),
     ∀z.(Q(z)→T(z))
     ⊢ ∃z.¬P(z)
FORMULAE
0 actual i,
1 ¬P(i),
2 ¬P(z),
3 i,
4 z,
5 ⊥,
6 ¬T(i),
7 T(i),
8 Q(i),
9 Q(i)→T(i),
10 P(i),
11 P(i)→Q(i),
12 ∃z.¬P(z),
13 ∀z.(P(z)→Q(z)),
14 P(z)→Q(z),
15 ∀z.(Q(z)→T(z)),
16 Q(z)→T(z),
17 ∃z.¬T(z),
18 ¬T(z)
IS
SEQ ("∃ elim"[i,C,P,x\3,12,18,4]) (hyp[A\17]) (cut[B,C\9,12]) ("∀ elim"[P,i,x\16,3,4]) (hyp[A\15]) (hyp[A\0]) (cut[B,C\11,12]) ("∀ elim"[P,i,x\14,3,4]) (hyp[A\13]) (hyp[A\0]) (cut[B,C\1,12]) ("¬ intro"[A\10]) (cut[B,C\8,5]) ("→ elim"[A,B\10,8]) (hyp[A\11]) (hyp[A\10]) (cut[B,C\7,5]) ("→ elim"[A,B\8,7]) (hyp[A\9]) (hyp[A\8]) (cut[B,C\5,5]) ("¬ elim"[B\7]) (hyp[A\7]) (hyp[A\6]) (hyp[A\5]) ("∃ intro"[P,i,x\2,3,4]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Assignment
PROOF "∀x.(P(x)→Q(x)), ∀x.(P(x)∧R(x)) ⊢ ∀x.(Q(x))"
INFER ∀x.(P(x)→Q(x)),
     ∀x.(P(x)∧R(x))
     ⊢ ∀x.(Q(x))
FORMULAE
0 Q(i),
1 P(i),
2 P(i)→Q(i),
3 actual i,
4 ∀x.(P(x)→Q(x)),
5 P(x)→Q(x),
6 i,
7 x,
8 P(i)∧R(i),
9 R(i),
10 ∀x.(P(x)∧R(x)),
11 P(x)∧R(x),
12 Q(x)
IS
SEQ ("∀ intro"[i,P,x\6,12,7]) (cut[B,C\8,0]) ("∀ elim"[P,i,x\11,6,7]) (hyp[A\10]) (hyp[A\3]) (cut[B,C\1,0]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\1,9]) (hyp[A\8])) (cut[B,C\2,0]) ("∀ elim"[P,i,x\5,6,7]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("→ elim"[A,B\1,0]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "¬¬P ⊢ P"
INFER ¬¬P 
     ⊢ P 
FORMULAE
0 ⊥,
1 ¬¬P,
2 ¬P,
3 P 
IS
SEQ ("contra (classical)"[A\3]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "P→Q ⊢ ¬Q→¬P"
INFER P→Q 
     ⊢ ¬Q→¬P 
FORMULAE
0 ⊥,
1 ¬Q,
2 Q,
3 P,
4 P→Q,
5 ¬P 
IS
SEQ ("→ intro"[A,B\1,5]) ("¬ intro"[A\3]) (cut[B,C\2,0]) ("→ elim"[A,B\3,2]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Assignment
PROOF "∀z.(S(z)∨T(z)), ∃z.¬S(z) ⊢ ∃z.T(z)"
INFER ∀z.(S(z)∨T(z)),
     ∃z.¬S(z)
     ⊢ ∃z.T(z)
FORMULAE
0 actual i,
1 T(i),
2 T(z),
3 i,
4 z,
5 ⊥,
6 ¬S(i),
7 S(i),
8 S(i)∨T(i),
9 ∃z.T(z),
10 ∀z.(S(z)∨T(z)),
11 S(z)∨T(z),
12 ∃z.¬S(z),
13 ¬S(z)
IS
SEQ ("∃ elim"[i,C,P,x\3,9,13,4]) (hyp[A\12]) (cut[B,C\8,9]) ("∀ elim"[P,i,x\11,3,4]) (hyp[A\10]) (hyp[A\0]) (cut[B,C\1,9]) ("∨ elim"[A,B,C\7,1,1]) (hyp[A\8]) (cut[B,C\5,1]) ("¬ elim"[B\7]) (hyp[A\7]) (hyp[A\6]) ("contra (constructive)"[B\1]) (hyp[A\5]) (hyp[A\1]) ("∃ intro"[P,i,x\2,3,4]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL ModelProjectProofs
PROOF "P1POSITION0, P2POSITION3, (P1POSITION0∧P2POSITION3)→H2, R, (R∧H2)→Q ⊢ Q"
INFER P1POSITION0,
     P2POSITION3,
     (P1POSITION0∧P2POSITION3)→H2,
     R,
     (R∧H2)→Q 
     ⊢ Q 
FORMULAE
0 Q,
1 R∧H2,
2 R∧H2→Q,
3 H2,
4 R,
5 P1POSITION0∧P2POSITION3,
6 P1POSITION0∧P2POSITION3→H2,
7 P2POSITION3,
8 P1POSITION0,
9 (P1POSITION0∧P2POSITION3)→H2,
10 (R∧H2)→Q 
IS
SEQ (cut[B,C\5,0]) ("∧ intro"[A,B\8,7]) (hyp[A\8]) (hyp[A\7]) (cut[B,C\3,0]) ("→ elim"[A,B\5,3]) (hyp[A\6]) (hyp[A\5]) (cut[B,C\1,0]) ("∧ intro"[A,B\4,3]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("→ elim"[A,B\1,0]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Assignment
PROOF "∀z.(∃y.R(y)→T(z)) ⊢ ∃y.R(y)→∀z.T(z)"
INFER ∀z.(∃y.R(y)→T(z))
     ⊢ ∃y.R(y)→∀z.T(z)
FORMULAE
0 T(i),
1 ∃y.R(y),
2 ∃y.R(y)→T(i),
3 actual i,
4 ∀z.(∃y.R(y)→T(z)),
5 ∃y.R(y)→T(z),
6 i,
7 z,
8 T(z),
9 ∀z.T(z)
IS
SEQ ("→ intro"[A,B\1,9]) ("∀ intro"[i,P,x\6,8,7]) (cut[B,C\2,0]) ("∀ elim"[P,i,x\5,6,7]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("→ elim"[A,B\1,0]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "P→Q, ¬Q ⊢ ¬P"
INFER P→Q,
     ¬Q 
     ⊢ ¬P 
FORMULAE
0 ⊥,
1 ¬Q,
2 Q,
3 P,
4 P→Q 
IS
SEQ ("¬ intro"[A\3]) (cut[B,C\2,0]) ("→ elim"[A,B\3,2]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Assignment
PROOF "∀y.∀x.(S(y)→T(x)) ⊢ ∃y.S(y)→∀x.T(x)"
INFER ∀y.∀x.(S(y)→T(x))
     ⊢ ∃y.S(y)→∀x.T(x)
FORMULAE
0 T(i1),
1 S(i),
2 S(i)→T(i1),
3 actual i1,
4 ∀x.(S(i)→T(x)),
5 S(i)→T(x),
6 i1,
7 x,
8 T(x),
9 actual i,
10 ∀y.∀x.(S(y)→T(x)),
11 ∀x.(S(y)→T(x)),
12 i,
13 y,
14 ∀x.T(x),
15 ∃y.S(y),
16 S(y)
IS
SEQ ("→ intro"[A,B\15,14]) ("∃ elim"[i,C,P,x\12,14,16,13]) (hyp[A\15]) (cut[B,C\4,14]) ("∀ elim"[P,i,x\11,12,13]) (hyp[A\10]) (hyp[A\9]) ("∀ intro"[i,P,x\6,8,7]) (cut[B,C\2,0]) ("∀ elim"[P,i,x\5,6,7]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("→ elim"[A,B\1,0]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL ModelProjectProofs
PROOF "P1POSITION2, P2POSITION3, (P1POSITION2∧P2POSITION3)→ADJACENT ⊢ ADJACENT"
INFER P1POSITION2,
     P2POSITION3,
     (P1POSITION2∧P2POSITION3)→ADJACENT 
     ⊢ ADJACENT 
FORMULAE
0 ADJACENT,
1 P1POSITION2∧P2POSITION3,
2 P1POSITION2∧P2POSITION3→ADJACENT,
3 P2POSITION3,
4 P1POSITION2,
5 (P1POSITION2∧P2POSITION3)→ADJACENT 
IS
SEQ (cut[B,C\1,0]) ("∧ intro"[A,B\4,3]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("→ elim"[A,B\1,0]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "P∨¬P"
INFER P∨¬P 
FORMULAE
0 ⊥,
1 ¬(P∨¬P),
2 P∨¬P,
3 P,
4 ¬P,
5 ¬(P∨¬P)
IS
SEQ ("contra (classical)"[A\2]) (cut[B,C\3,0]) ("contra (classical)"[A\3]) (cut[B,C\2,0]) (LAYOUT "∨ intro" (0) ("∨ intro(R)"[B,A\3,4]) (hyp[A\4])) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0]) (cut[B,C\2,0]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\4,3]) (hyp[A\3])) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "P ⊢ ¬¬P"
INFER P 
     ⊢ ¬¬P 
FORMULAE
0 ⊥,
1 ¬P,
2 P 
IS
SEQ ("¬ intro"[A\1]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Assignment
PROOF "∀z.((T(z)∧P(z))→Q(z)), ∃z.(P(z)∧¬Q(z)) ⊢ ∃z.¬T(z)"
INFER ∀z.((T(z)∧P(z))→Q(z)),
     ∃z.(P(z)∧¬Q(z))
     ⊢ ∃z.¬T(z)
FORMULAE
0 actual i,
1 ¬T(i),
2 ¬T(z),
3 i,
4 z,
5 ⊥,
6 ¬Q(i),
7 Q(i),
8 T(i)∧P(i),
9 T(i)∧P(i)→Q(i),
10 P(i),
11 T(i),
12 ∃z.¬T(z),
13 ∀z.((T(z)∧P(z))→Q(z)),
14 (T(z)∧P(z))→Q(z),
15 (T(i)∧P(i))→Q(i),
16 P(i)∧¬Q(i),
17 ∃z.(P(z)∧¬Q(z)),
18 P(z)∧¬Q(z)
IS
SEQ ("∃ elim"[i,C,P,x\3,12,18,4]) (hyp[A\17]) (cut[B,C\6,12]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\10,6]) (hyp[A\16])) (cut[B,C\10,12]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\10,6]) (hyp[A\16])) (cut[B,C\15,12]) ("∀ elim"[P,i,x\14,3,4]) (hyp[A\13]) (hyp[A\0]) (cut[B,C\1,12]) ("¬ intro"[A\11]) (cut[B,C\8,5]) ("∧ intro"[A,B\11,10]) (hyp[A\11]) (hyp[A\10]) (cut[B,C\7,5]) ("→ elim"[A,B\8,7]) (hyp[A\9]) (hyp[A\8]) (cut[B,C\5,5]) ("¬ elim"[B\7]) (hyp[A\7]) (hyp[A\6]) (hyp[A\5]) ("∃ intro"[P,i,x\2,3,4]) (hyp[A\1]) (hyp[A\0])
END
