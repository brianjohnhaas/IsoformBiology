# Records review C: NEU-181..NEU-219 against sources (chapter 7)

Every one of the 39 audit quotes is byte-exact (whitespace collapsed, as
scripts/verify_claims.py does it) inside a cited line, and every quote is <=25
words. 19 FDA quotes checked against local full dumps of the 7 regulatory
documents; 20 paper quotes checked against their cited line ranges. All
text_access flags correct; no record's lines were a preprint's.

## Verdicts

NEU-181 ok              NEU-194 ok                NEU-207 tier wrong
NEU-182 ok              NEU-195 ok                NEU-208 scope too wide
NEU-183 ok              NEU-196 scope too wide    NEU-209 tier wrong
NEU-184 ok              NEU-197 ok                NEU-210 qualifier lost
NEU-185 ok              NEU-198 proposal as finding NEU-211 ok
NEU-186 qualifier lost  NEU-199 tier wrong        NEU-212 ok
NEU-187 qualifier lost  NEU-200 ok                NEU-213 ok
NEU-188 ok              NEU-201 ok                NEU-214 source metadata wrong
NEU-189 ok              NEU-202 ok                NEU-215 ok
NEU-190 ok              NEU-203 ok                NEU-216 ok
NEU-191 ok              NEU-204 tier wrong        NEU-217 ok
NEU-192 ok              NEU-205 tier wrong        NEU-218 qualifier lost
NEU-193 ok              NEU-206 ok                NEU-219 scope too wide

(Full blocks, note-level defects, tier judgement, missing-element list and
item-by-item confirmation are in the handback report delivered to the caller.)

## Cross-document facts established (for the record)
- fda_753dc30bc176: 0 hits for ENDEAR, CHERISH, NURTURE, any NCT number,
  "accelerated approval", "Subpart H".
- fda_753dc30bc176 L51/L53: interim set n=78 (nusinersen 51, sham 27), HINE
  responder 41% vs 0%; the 21/52 vs 0/30 at L15 is the sensitivity analysis
  including patients who died or withdrew after baseline (L53 gives it as 40%
  vs 0% only).
- 46565666 L1 (ENDEAR): interim 21/51 (41%) vs 0/27 P<0.001; final 37/73 (51%)
  vs 0/37. The 51/27 interim set matches the review exactly.
- fda_753dc30bc176 L58/L59: Study CS4 = 15-month sham-controlled later-onset
  trial, interim 126 patients (84 nusinersen, 42 controls), HFMSE 4.0 vs -1.9,
  p=0.000002, 57% vs 21% reaching >=3 points at 15 months (publication's final
  analysis gives 57% vs 26%).
- fda_bf81b52deeaf L12/L32: BP39056 = FIREFISH, BP39055 = SUNFISH (named).
- fda_ca7816e187dc L685 and fda_24dc180d65a2 L1576: ESSENCE (Study 4045-301) is
  designated the confirmatory study for golodirsen and for casimersen.
  4045-301 IS ESSENCE, so NEU-209 and NEU-214 are one trial's interim and final
  analyses.
- Golodirsen approval date: fda_24dc180d65a2 L84/L323 say "approved 2019"
  (PI December 2019 version); fda_17d7a5bb3fe4's approved-products table says
  "2020". Two FDA documents disagree.
- fda_24dc180d65a2 L322-L323: three precedents named (eteplirsen 2016 first,
  golodirsen 2019 second ASO, viltolarsen 2020 most recent); L810 says
  casimersen's surrogate "is consistent with those used for accelerated
  approval of the therapies just cited".
- fda_17d7a5bb3fe4 L502: "There was no dose related difference in dystrophin
  production at the 40 and 80 mg/kg/week dose"; the 4.6/3.8 medians are
  "normalized to myosin heavy chain". L367-L370: immunofluorescence
  dystrophin-positive myofibres, mean increases 12.8% and 33.0% at Week 25.
- fda_269d14f43e60 L815-L818: three methods for values below the 0.25% LOQ;
  mean change 0.22% to 0.32% irrespective of method. L433/L441 call 0.93% the
  Week-180 level; L138 calls it the mean increase.
- fda_269d14f43e60 L937: at least 3% inadequate, minimum of 10% perhaps needed,
  Study 301's 0.22-0.32% an order of magnitude below.
- Evrysdi EPAR: not present. search -s epar, search -s ema, and
  `grep --exhaustive "Evrysdi" /fda/eu/` return only two paragraphs, both
  inside Spinraza EPARs. /fda/eu/tri_bed44da74c39/content.lines L60 states
  risdiplam was "first approved in the United States (August 2020) and has
  since received approval in several other markets, including in the European
  Union (March 2021)".
