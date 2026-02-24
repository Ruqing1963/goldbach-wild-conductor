\\  tate_audit.gp — Rigorous f₂ via Tate's algorithm on E₁, E₂
\\
\\  For each Goldbach pair (p,q):
\\    E₁: Y² = X(X - p²)(X - q²)  →  [0, -(p²+q²), 0, p²q², 0]
\\    E₂: Y² = X(X + p²)(X + q²)  →  [0,  (p²+q²), 0, p²q², 0]
\\
\\  elllocalred(E, 2) returns [f₂, Kodaira_code, ...]
\\  This is Tate's algorithm — unconditional, no heuristic.

{
pairs = [[3,7],[7,23],[11,19],[13,17],[3,17],[7,19],[3,37],[7,41],[7,53],[11,37]];

print("==============================================================");
print("  RIGOROUS f₂ VIA TATE'S ALGORITHM (PARI/GP elllocalred)");
print("==============================================================");
print("");
printf("  %-8s  %-4s  %-8s  %-8s  %-8s  %-6s\n",
       "(p,q)", "gam", "f2(E1)", "f2(E2)", "f2(Jac)", "check");
print("--------------------------------------------------------------");

for(i = 1, #pairs,
  p = pairs[i][1];
  q = pairs[i][2];

  gam = max(valuation(p-q, 2), valuation(p+q, 2));

  \\ E₁: Y² = X³ - (p²+q²)X² + p²q²X
  E1 = ellinit([0, -(p^2+q^2), 0, p^2*q^2, 0]);
  lr1 = elllocalred(E1, 2);
  f2_E1 = lr1[1];

  \\ E₂: Y² = X³ + (p²+q²)X² + p²q²X
  E2 = ellinit([0,  (p^2+q^2), 0, p^2*q^2, 0]);
  lr2 = elllocalred(E2, 2);
  f2_E2 = lr2[1];

  f2_Jac = f2_E1 + f2_E2;

  \\ Expected from γ-conjecture
  if(gam == 2, expected = 8,
  if(gam == 3, expected = 7,
               expected = 4));

  ok = if(f2_Jac == expected, "OK", "FAIL");

  printf("  (%2d,%2d)  %4d  %8d  %8d  %8d  %6s\n",
         p, q, gam, f2_E1, f2_E2, f2_Jac, ok);
);

print("--------------------------------------------------------------");
print("");
print("All values computed via Tate's algorithm (elllocalred).");
print("No genus-2 Ogg heuristic involved.");
}
