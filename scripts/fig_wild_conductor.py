"""
fig_wild_conductor.py — Figures for Paper #16
"""
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

def v2(n):
    if n == 0: return float('inf')
    n = abs(n)
    v = 0
    while n % 2 == 0: v += 1; n //= 2
    return v

def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    for d in range(3, int(n**0.5)+1, 2):
        if n % d == 0: return False
    return True

# Collect data for all pairs up to 2N = 10000
gamma_list = []
f2_pred_list = []
twoN_list = []

for twoN in range(6, 10002, 2):
    for p in range(3, twoN//2 + 1, 2):
        q = twoN - p
        if q <= p: continue
        if not is_prime(p) or not is_prime(q): continue
        gamma = max(v2(p-q), v2(p+q))
        if gamma == 2: f2 = 8
        elif gamma == 3: f2 = 7
        else: f2 = 4
        gamma_list.append(gamma)
        f2_pred_list.append(f2)
        twoN_list.append(twoN)

total = len(gamma_list)
print(f"Total pairs: {total}")

# Magma data
magma = [(3,7,8),(7,23,4),(11,19,7),(13,17,8),(3,17,8),
         (7,19,8),(3,37,7),(7,41,4),(7,53,8),(11,37,4)]

# ═══════════════════════════════════════════════════════════════
# FIGURE 1: f₂ vs γ scatter + verification
# ═══════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Panel (a): f₂ as function of γ (Magma + predicted)
ax = axes[0]

# Plot all gamma values and f₂
gamma_arr = np.array(gamma_list)
f2_arr = np.array(f2_pred_list)

# Jitter for visibility
jitter_g = np.random.normal(0, 0.08, len(gamma_arr))
jitter_f = np.random.normal(0, 0.08, len(f2_arr))

# Color by f₂ value
colors = []
for f in f2_arr:
    if f == 8: colors.append('#CC3333')
    elif f == 7: colors.append('#DD8800')
    else: colors.append('#2255BB')

# Sample for visibility (too many points)
np.random.seed(42)
idx = np.random.choice(len(gamma_arr), size=min(3000, len(gamma_arr)), replace=False)

ax.scatter(gamma_arr[idx] + jitter_g[idx], f2_arr[idx] + jitter_f[idx],
          s=4, c=[colors[i] for i in idx], alpha=0.3, zorder=3)

# Overlay Magma points
for p, q, f2 in magma:
    gamma = max(v2(p-q), v2(p+q))
    ax.scatter(gamma, f2, s=120, c='black', marker='D', zorder=10,
             edgecolors='gold', linewidths=1.5)

# Draw the step function
ax.plot([1.5, 2.5], [8, 8], 'k-', lw=3, zorder=8)
ax.plot([2.5, 3.5], [7, 7], 'k-', lw=3, zorder=8)
ax.plot([3.5, 8.5], [4, 4], 'k-', lw=3, zorder=8)
ax.plot([2.5, 2.5], [7, 8], 'k:', lw=1.5, zorder=7)
ax.plot([3.5, 3.5], [4, 7], 'k:', lw=1.5, zorder=7)

ax.set_xlabel(r'$\gamma = \max(v_2(p{-}q),\, v_2(p{+}q))$', fontsize=12)
ax.set_ylabel(r'$f_2$', fontsize=13)
ax.set_title(r'(a) Wild conductor $f_2$ vs. cluster depth $\gamma$', fontsize=12)
ax.set_xlim(1.5, 8.5)
ax.set_ylim(2.5, 9.5)
ax.set_xticks(range(2, 9))
ax.set_yticks([4, 7, 8])
ax.grid(True, alpha=0.15)

# Legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0],[0], marker='D', color='w', markerfacecolor='black',
           markeredgecolor='gold', markersize=10, label='Magma verified'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor='#CC3333',
           markersize=7, label=r'$f_2 = 8$ ($\gamma = 2$)'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor='#DD8800',
           markersize=7, label=r'$f_2 = 7$ ($\gamma = 3$)'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor='#2255BB',
           markersize=7, label=r'$f_2 = 4$ ($\gamma \geq 4$)'),
    Line2D([0],[0], color='black', lw=3,
           label='Conjectured formula'),
]
ax.legend(handles=legend_elements, fontsize=8, loc='center right')


# Panel (b): Density pie chart / bar chart
ax = axes[1]

f2_counts = defaultdict(int)
for f in f2_pred_list:
    f2_counts[f] += 1

labels = [r'$f_2 = 8$' + f'\n({f2_counts[8]/total*100:.1f}%)',
          r'$f_2 = 7$' + f'\n({f2_counts[7]/total*100:.1f}%)',
          r'$f_2 = 4$' + f'\n({f2_counts[4]/total*100:.1f}%)']
sizes = [f2_counts[8], f2_counts[7], f2_counts[4]]
colors_pie = ['#CC3333', '#DD8800', '#2255BB']
explode = (0.03, 0.03, 0.03)

wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels,
                                   colors=colors_pie, autopct='',
                                   startangle=90, textprops={'fontsize': 11})
ax.set_title(r'(b) Distribution of $f_2$ ($2N \leq 10000$, '
            f'{total:,} pairs)', fontsize=12)

# Add Swan conductor annotations
ax.annotate('sw = 4', xy=(0.3, 0.4), fontsize=9, color='#CC3333',
           fontweight='bold')
ax.annotate('sw = 3', xy=(-0.6, -0.35), fontsize=9, color='#DD8800',
           fontweight='bold')
ax.annotate('sw = 0', xy=(-0.2, -0.6), fontsize=9, color='#2255BB',
           fontweight='bold')

plt.tight_layout()
plt.savefig('/home/claude/paper16/figures/fig_wild_conductor.pdf',
           dpi=300, bbox_inches='tight')
plt.savefig('/home/claude/paper16/figures/fig_wild_conductor.png',
           dpi=200, bbox_inches='tight')
plt.close()
print("Figure 1 done.")


# ═══════════════════════════════════════════════════════════════
# FIGURE 2: Cluster tree diagrams + γ distribution
# ═══════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

# Panel (a): Cluster tree diagrams for the three cases
ax = axes[0]
ax.set_xlim(-0.5, 3.5)
ax.set_ylim(-0.5, 5.5)
ax.axis('off')

def draw_tree(ax, x_center, gamma_val, f2_val, sw_val):
    """Draw a cluster tree for given γ."""
    w = 0.35
    
    # Title
    ax.text(x_center, 5.3, f'$\\gamma = {gamma_val}$\n$f_2 = {f2_val}$, sw = {sw_val}',
           ha='center', va='top', fontsize=10, fontweight='bold',
           bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow',
                    edgecolor='gray'))
    
    # Top: full root set
    ax.text(x_center, 4.0, r'$\{0, p, {-}p, q, {-}q\}$',
           ha='center', va='center', fontsize=8,
           bbox=dict(boxstyle='round', facecolor='#E8E8FF', edgecolor='navy'))
    
    # Level 0: 0 separates
    ax.annotate('', xy=(x_center - w, 3.3), xytext=(x_center, 3.7),
               arrowprops=dict(arrowstyle='->', color='gray'))
    ax.annotate('', xy=(x_center + w, 3.3), xytext=(x_center, 3.7),
               arrowprops=dict(arrowstyle='->', color='gray'))
    
    ax.text(x_center - w, 3.1, r'$\{0\}$', ha='center', fontsize=7,
           bbox=dict(boxstyle='round', facecolor='#FFE8E8', edgecolor='gray'))
    ax.text(x_center + w, 3.1, r'$\{p,{-}p,q,{-}q\}$', ha='center', fontsize=7,
           bbox=dict(boxstyle='round', facecolor='#E8FFE8', edgecolor='gray'))
    
    ax.text(x_center - 0.02, 3.55, '$d{=}0$', fontsize=6, color='gray', ha='center')
    
    # Level 1: pairs separate
    ax.annotate('', xy=(x_center + w - 0.2, 2.3), xytext=(x_center + w, 2.8),
               arrowprops=dict(arrowstyle='->', color='gray'))
    ax.annotate('', xy=(x_center + w + 0.2, 2.3), xytext=(x_center + w, 2.8),
               arrowprops=dict(arrowstyle='->', color='gray'))
    
    ax.text(x_center + w - 0.2, 2.1, r'$\{p,q\}$', ha='center', fontsize=7,
           bbox=dict(boxstyle='round', facecolor='#FFFFDD', edgecolor='gray'))
    ax.text(x_center + w + 0.2, 2.1, r'$\{{-}p,{-}q\}$', ha='center', fontsize=7,
           bbox=dict(boxstyle='round', facecolor='#FFFFDD', edgecolor='gray'))
    
    ax.text(x_center + w + 0.02, 2.55, '$d{=}1$', fontsize=6, color='gray', ha='center')
    
    # Level γ: final split
    ax.annotate('', xy=(x_center + w - 0.3, 1.2), xytext=(x_center + w - 0.2, 1.8),
               arrowprops=dict(arrowstyle='->', color='navy'))
    ax.annotate('', xy=(x_center + w - 0.1, 1.2), xytext=(x_center + w - 0.2, 1.8),
               arrowprops=dict(arrowstyle='->', color='navy'))
    
    ax.text(x_center + w - 0.3, 1.0, '$p$', ha='center', fontsize=8,
           fontweight='bold', color='navy')
    ax.text(x_center + w - 0.1, 1.0, '$q$', ha='center', fontsize=8,
           fontweight='bold', color='navy')
    
    ax.text(x_center + w - 0.18, 1.55, f'$d{{=}}\\gamma{{=}}{gamma_val}$',
           fontsize=6, color='navy', ha='center')
    
    # Color coding for wildness
    if f2_val == 8:
        col = '#CC3333'
    elif f2_val == 7:
        col = '#DD8800'
    else:
        col = '#2255BB'
    
    ax.add_patch(plt.Rectangle((x_center - 0.55, 0.5), 1.1, 0.35,
                               facecolor=col, alpha=0.2, edgecolor=col))
    ax.text(x_center, 0.67, f'Swan = {sw_val}', ha='center', fontsize=8,
           color=col, fontweight='bold')

draw_tree(ax, 0.5, 2, 8, 4)
draw_tree(ax, 1.7, 3, 7, 3)
draw_tree(ax, 2.9, '≥4', 4, 0)

ax.set_title('(a) Cluster trees over $\\mathbb{Q}_2$', fontsize=12, pad=15)


# Panel (b): Distribution of γ
ax = axes[1]

gamma_counts = defaultdict(int)
for g in gamma_list:
    gamma_counts[g] += 1

gammas = sorted(gamma_counts.keys())
counts = [gamma_counts[g] for g in gammas]
pcts = [c/total*100 for c in counts]

# Color by f₂
bar_colors = []
for g in gammas:
    if g == 2: bar_colors.append('#CC3333')
    elif g == 3: bar_colors.append('#DD8800')
    else: bar_colors.append('#2255BB')

bars = ax.bar(gammas, pcts, color=bar_colors, alpha=0.7, edgecolor='black', lw=0.5)

# Add theoretical prediction
for g in gammas:
    if g <= 10:
        # P(γ = k) ≈ 2^{-k} for k ≥ 2
        pred = 2**(-g) * 100
        ax.plot(g, pred, 'ko', markersize=8, zorder=5)

ax.plot([], [], 'ko', markersize=8, label=r'Predicted: $P(\gamma{=}k) = 2^{-k}$')

# Labels
for i, (g, pct) in enumerate(zip(gammas, pcts)):
    if pct > 0.5:
        ax.text(g, pct + 0.5, f'{pct:.1f}%', ha='center', fontsize=8)

ax.set_xlabel(r'$\gamma = \max(v_2(p{-}q),\, v_2(p{+}q))$', fontsize=12)
ax.set_ylabel(r'Percentage of pairs (\%)', fontsize=12)
ax.set_title(r'(b) Distribution of $\gamma$ ($2N \leq 10000$)', fontsize=12)
ax.set_xticks(range(2, max(gammas)+1))
ax.legend(fontsize=9)
ax.grid(True, alpha=0.15, axis='y')

plt.tight_layout()
plt.savefig('/home/claude/paper16/figures/fig_cluster_tree.pdf',
           dpi=300, bbox_inches='tight')
plt.savefig('/home/claude/paper16/figures/fig_cluster_tree.png',
           dpi=200, bbox_inches='tight')
plt.close()
print("Figure 2 done.")
