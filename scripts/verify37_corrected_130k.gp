\\ ============================================================
\\ Paper #17 — CORRECTED Euler factors, FULL 130k
\\ ============================================================
\\ ALL f2=4..8 tested DEFINITIVELY (130000 > 124967).
\\ Correct Euler factors at p=2,3,5,7 (see 65k script for derivation).
\\
\\ Time: ~40-50 hours.
\\ Usage: gp < verify37_corrected_130k.gp
\\ ============================================================

default(parisize,"2G");

f37=x^5-58*x^3+441*x;

print("=== (3,7) CORRECTED FULL Test: 130,000 coefficients ===");
print("=== ALL f2 values testable definitively ===");
print("=== Estimated time: ~40-50 hours ===");
print("=== Start: ", getwalltime()/1000, " ===");
print("");

print("Computing 130,000 Dirichlet coefficients (corrected bad primes)...");
an37=direuler(p=2,130000, \
  if(p==2, 1/(1+O(X^5)), \
  if(p==3, 1/(1+3*X^2+O(X^5)), \
  if(p==5, 1/(1+2*X+X^2+O(X^5)), \
  if(p==7, 1/(1+7*X^2+O(X^5)), \
  1/(subst(polrecip(hyperellcharpoly(Mod(1,p)*f37)),x,X)+O(X^5)) \
  )))), 130000);
print("Done. #an=",#an37);
print("=== Finished direuler: ", getwalltime()/1000, " ===");

print("");
print("--- ALL tests DEFINITIVE (130000 > 124967) ---");
print("Correct pair: err ~ -19.  Wrong pair: err ~ 0.");
print("");

{for(f2=4,8,for(ei=1,2,my(ep,N,L,e);ep=if(ei==1,1,-1);N=2^f2*11025;L=lfuncreate([an37,0,[0,0,1,1],2,N,ep]);e=lfuncheckfeq(L);print("  f2=",f2," eps=",ep," N=",N," err=",e)))}

print("");
print("=== DONE ===");
print("Correct (f2,eps): err closest to -19.");
print("Magma prediction: f2=8.");
