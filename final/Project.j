CONJECTUREPANEL Project
PROOF "PK, DEF, (PK→ADJ)∧(PK→1 SP)∧(PK→¬2 SP), DEF→((PUN∧ADJ)∨(BLO∧1 SP)∨(PMJ∧2 SP)) ⊢ PUN∨BLO"
INFER PK,
     DEF,
     (PK→ADJ)∧(PK→1 SP)∧(PK→¬2 SP),
     DEF→((PUN∧ADJ)∨(BLO∧1 SP)∨(PMJ∧2 SP))
     ⊢ PUN∨BLO 
FORMULAE
0 ⊥,
1 PUN∨BLO,
2 ¬2 SP,
3 2 SP,
4 PMJ∧2 SP,
5 PMJ,
6 BLO,
7 PUN,
8 BLO∧1 SP,
9 1 SP,
10 PUN∧ADJ,
11 ADJ,
12 PUN∧ADJ∨BLO∧1 SP,
13 (PUN∧ADJ)∨(BLO∧1 SP)∨PMJ∧2 SP,
14 (PUN∧ADJ)∨(BLO∧1 SP),
15 DEF,
16 DEF→(PUN∧ADJ)∨(BLO∧1 SP)∨(PMJ∧2 SP),
17 (PUN∧ADJ)∨(BLO∧1 SP)∨(PMJ∧2 SP),
18 PK,
19 PK→¬2 SP,
20 (PK→ADJ)∧(PK→1 SP)∧(PK→¬2 SP),
21 (PK→ADJ)∧(PK→1 SP),
22 (PK→ADJ)∧(PK→1 SP),
23 PK→ADJ,
24 PK→1 SP,
25 DEF→((PUN∧ADJ)∨(BLO∧1 SP)∨(PMJ∧2 SP)),
26 (PK→ADJ)∧(PK→1 SP)∧(PK→¬2 SP)
IS
SEQ (cut[B,C\21,1]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\21,19]) (hyp[A\20])) (cut[B,C\23,1]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\23,24]) (hyp[A\22])) (cut[B,C\24,1]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\23,24]) (hyp[A\22])) (cut[B,C\19,1]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\21,19]) (hyp[A\20])) (cut[B,C\2,1]) ("→ elim"[A,B\18,2]) (hyp[A\19]) (hyp[A\18]) (cut[B,C\17,1]) ("→ elim"[A,B\15,17]) (hyp[A\16]) (hyp[A\15]) ("∨ elim"[A,B,C\14,4,1]) (hyp[A\13]) ("∨ elim"[A,B,C\10,8,1]) (hyp[A\12]) (cut[B,C\7,1]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\7,11]) (hyp[A\10])) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\6,7]) (hyp[A\7])) (cut[B,C\6,1]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\6,9]) (hyp[A\8])) (LAYOUT "∨ intro" (0) ("∨ intro(R)"[B,A\7,6]) (hyp[A\6])) (cut[B,C\3,1]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\5,3]) (hyp[A\4])) (cut[B,C\0,1]) ("¬ elim"[B\3]) (hyp[A\3]) (hyp[A\2]) ("contra (constructive)"[B\1]) (hyp[A\0])
END
CONJECTUREPANEL Project
PROOF "PJ, PH→¬(PM∨PL), PJ→¬PK∧¬PP, (PK∧PL)∨(PP∧PM)∨(PJ∧PH) ⊢ ¬(PM∨PL)"
INFER PJ,
     PH→¬(PM∨PL),
     PJ→¬PK∧¬PP,
     (PK∧PL)∨(PP∧PM)∨(PJ∧PH)
     ⊢ ¬(PM∨PL)
FORMULAE
0 ⊥,
1 ¬(PM∨PL),
2 PM∨PL,
3 PH,
4 PH→¬(PM∨PL),
5 ¬(PM∨PL),
6 PJ∧PH,
7 PJ,
8 ¬PP,
9 PP,
10 PP∧PM,
11 PM,
12 ¬PK,
13 PK,
14 PK∧PL,
15 PL,
16 PK∧PL∨PP∧PM,
17 (PK∧PL)∨(PP∧PM)∨PJ∧PH,
18 (PK∧PL)∨(PP∧PM),
19 ¬PK∧¬PP,
20 PJ→¬PK∧¬PP,
21 (PK∧PL)∨(PP∧PM)∨(PJ∧PH)
IS
SEQ (cut[B,C\19,5]) ("→ elim"[A,B\7,19]) (hyp[A\20]) (hyp[A\7]) (cut[B,C\12,5]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\12,8]) (hyp[A\19])) (cut[B,C\8,5]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\12,8]) (hyp[A\19])) ("∨ elim"[A,B,C\18,6,5]) (hyp[A\17]) ("∨ elim"[A,B,C\14,10,5]) (hyp[A\16]) (cut[B,C\13,5]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\13,15]) (hyp[A\14])) (cut[B,C\0,5]) ("¬ elim"[B\13]) (hyp[A\13]) (hyp[A\12]) ("¬ intro"[A\2]) (hyp[A\0]) (cut[B,C\9,5]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\9,11]) (hyp[A\10])) (cut[B,C\0,5]) ("¬ elim"[B\9]) (hyp[A\9]) (hyp[A\8]) ("¬ intro"[A\2]) (hyp[A\0]) (cut[B,C\3,5]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\7,3]) (hyp[A\6])) (cut[B,C\5,5]) ("→ elim"[A,B\3,5]) (hyp[A\4]) (hyp[A\3]) ("¬ intro"[A\2]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Project
PROOF "(P1A→HAD∧ADJ)∨(P1A→PUN∧ADJ), P1A, HAD, HAD∧PUN→¬P1A, PUN, HAD∧ADJ→((P1W∧P2L)∨(P1L∧P2W)), ¬(P1L∧P2W) ⊢ (P1W∧P2L)"
INFER (P1A→HAD∧ADJ)∨(P1A→PUN∧ADJ),
     P1A,
     HAD,
     HAD∧PUN→¬P1A,
     PUN,
     HAD∧ADJ→((P1W∧P2L)∨(P1L∧P2W)),
     ¬(P1L∧P2W)
     ⊢ (P1W∧P2L)
FORMULAE
0 ⊥,
1 P1W∧P2L,
2 ¬P1A,
3 P1A,
4 HAD∧PUN,
5 HAD∧PUN→¬P1A,
6 PUN,
7 HAD,
8 PUN∧ADJ,
9 ADJ,
10 P1A→PUN∧ADJ,
11 ¬(P1L∧P2W),
12 P1L∧P2W,
13 P1W∧P2L∨P1L∧P2W,
14 HAD∧ADJ,
15 HAD∧ADJ→(P1W∧P2L)∨(P1L∧P2W),
16 (P1W∧P2L)∨(P1L∧P2W),
17 P1A→HAD∧ADJ,
18 (P1A→HAD∧ADJ)∨(P1A→PUN∧ADJ),
19 ¬(P1L∧P2W),
20 HAD∧ADJ→((P1W∧P2L)∨(P1L∧P2W)),
21 (P1A→HAD∧ADJ)∨(P1A→PUN∧ADJ)
IS
SEQ ("∨ elim"[A,B,C\17,10,1]) (hyp[A\18]) (cut[B,C\14,1]) ("→ elim"[A,B\3,14]) (hyp[A\17]) (hyp[A\3]) (cut[B,C\16,1]) ("→ elim"[A,B\14,16]) (hyp[A\15]) (hyp[A\14]) ("∨ elim"[A,B,C\1,12,1]) (hyp[A\13]) (hyp[A\1]) (cut[B,C\0,1]) ("¬ elim"[B\12]) (hyp[A\12]) (hyp[A\11]) ("contra (constructive)"[B\1]) (hyp[A\0]) (cut[B,C\8,1]) ("→ elim"[A,B\3,8]) (hyp[A\10]) (hyp[A\3]) (cut[B,C\6,1]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\6,9]) (hyp[A\8])) (cut[B,C\4,1]) ("∧ intro"[A,B\7,6]) (hyp[A\7]) (hyp[A\6]) (cut[B,C\2,1]) ("→ elim"[A,B\4,2]) (hyp[A\5]) (hyp[A\4]) (cut[B,C\0,1]) ("¬ elim"[B\3]) (hyp[A\3]) (hyp[A\2]) ("contra (constructive)"[B\1]) (hyp[A\0])
END
