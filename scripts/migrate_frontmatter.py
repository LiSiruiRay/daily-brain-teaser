"""
One-time migration: add YAML frontmatter to every questions/{slug}/question.md
and strip the old inline **Type:** / **Tags:** / **Date:** / **Difficulty:** lines.
Run: python scripts/migrate_frontmatter.py
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

# Canonical metadata for every slug.
# type must be one of: Integration | ML/Stats | analysis | algebra | topology
#                      Probability | Complex Analysis | Differential Geometry | Putnam
METADATA = {
    "lp_norm_infinity": {
        "name": "Lp Norm → L∞",
        "type": "analysis",
        "tags": ["Lp norm", "Limit", "Squeeze Theorem"],
        "date": "2026-03-09",
    },
    "expected_records": {
        "name": "Expected Number of Records",
        "type": "Probability",
        "tags": ["Expectation", "Linearity of expectation", "Permutations", "Harmonic numbers"],
        "date": "2026-03-11",
    },
    "bertrand_ballot": {
        "name": "Bertrand's Ballot Problem",
        "type": "Probability",
        "tags": ["Ballot problem", "Reflection principle", "Counting paths"],
        "date": "2026-03-11",
    },
    "schwarz_lemma": {
        "name": "The Schwarz Lemma",
        "type": "Complex Analysis",
        "tags": ["Maximum modulus principle", "Holomorphic functions", "Unit disk"],
        "date": "2026-03-12",
    },
    "parallel_transport_sphere": {
        "name": "Parallel Transport on a Sphere",
        "type": "Differential Geometry",
        "tags": ["Parallel transport", "Holonomy", "Gauss-Bonnet", "Curvature"],
        "date": "2026-03-12",
    },
    "polynomial_no_integer_roots": {
        "name": "Polynomial with No Integer Roots",
        "type": "Putnam",
        "tags": ["Polynomials", "Parity", "Integer roots", "Modular arithmetic"],
        "date": "2026-03-13",
    },
    "harmonic_not_integer": {
        "name": "Harmonic Series Is Never an Integer",
        "type": "Putnam",
        "tags": ["Harmonic series", "Primes", "Bertrand's postulate", "LCM", "Divisibility"],
        "date": "2026-03-13",
    },
    "geometric_series_integral": {
        "name": "Integral of a Geometric Series",
        "type": "Integration",
        "tags": ["Geometric series", "Interchange sum/integral", "Logarithm"],
        "date": "2026-03-14",
    },
    "bertrand_chord_paradox": {
        "name": "Bertrand's Chord Paradox",
        "type": "Probability",
        "tags": ["Geometric probability", "Measure", "Paradox", "Sample space"],
        "date": "2026-03-24",
    },
    "derangement_hat_check": {
        "name": "The Hat Check Problem",
        "type": "Probability",
        "tags": ["Derangements", "Inclusion-exclusion", "Permutations"],
        "date": "2026-03-25",
    },
    "fta_liouville": {
        "name": "FTA via Liouville's Theorem",
        "type": "Complex Analysis",
        "tags": ["Liouville", "Entire functions", "Fundamental theorem of algebra"],
        "date": "2026-03-26",
    },
    "torus_curvature": {
        "name": "Curvature of an Embedded Torus",
        "type": "Differential Geometry",
        "tags": ["Gaussian curvature", "Gauss-Bonnet", "Euler characteristic", "Torus"],
        "date": "2026-03-26",
    },
    "involution_odd_shift": {
        "name": "No Function with f(f(n)) = n + 2025",
        "type": "Putnam",
        "tags": ["Functions", "Involution", "Modular arithmetic", "Fixed points", "Parity"],
        "date": "2026-03-27",
    },
    "truncated_exp_no_repeated_roots": {
        "name": "Truncated Exponential Has No Repeated Roots",
        "type": "Putnam",
        "tags": ["Polynomials", "Repeated roots", "Derivatives", "Truncated exponential"],
        "date": "2026-03-27",
    },
    "integral_x2_sinx": {
        "name": "Integral of x² sin(x)",
        "type": "Integration",
        "tags": ["Integration by parts", "Tabular method", "Trigonometric integrals"],
        "date": "2026-03-28",
    },
    "steins_paradox": {
        "name": "Stein's Paradox",
        "type": "ML/Stats",
        "tags": ["Admissibility", "James-Stein", "Shrinkage", "MSE", "Regularization"],
        "date": "2026-03-29",
    },
    "orthogonal_to_polynomials": {
        "name": "Orthogonality to All Monomials Forces Zero",
        "type": "analysis",
        "tags": ["Weierstrass approximation", "Orthogonality", "Density argument", "L2"],
        "date": "2026-03-30",
    },
    "consecutive_sum_divisible": {
        "name": "Consecutive Subsum Divisible by n",
        "type": "Putnam",
        "tags": ["Pigeonhole", "Partial sums", "Divisibility", "Modular arithmetic"],
        "date": "2026-04-03",
    },
    "integral_x_minus_1_sq": {
        "name": "Integral of (x-1)²/(2eˣ+x²+1)",
        "type": "Integration",
        "tags": ["Logarithmic derivative", "Integration bee", "Algebraic manipulation"],
        "date": "2026-04-04",
    },
    "continuous_nowhere_differentiable": {
        "name": "Continuous but Nowhere Differentiable",
        "type": "analysis",
        "tags": ["Weierstrass function", "Uniform convergence", "Counterexample", "Fractal"],
        "date": "2026-04-06",
    },
    "lasso_vs_ridge_sparsity": {
        "name": "Why LASSO Gives Sparsity but Ridge Does Not",
        "type": "ML/Stats",
        "tags": ["LASSO", "Ridge", "Sparsity", "Regularization", "Convex geometry"],
        "date": "2026-04-19",
    },
    "cantor_set_measure_zero": {
        "name": "The Cantor Set: Measure Zero yet Uncountable",
        "type": "analysis",
        "tags": ["Cantor set", "Measure theory", "Cardinality", "Uncountability"],
        "date": "2026-04-20",
    },
    "topologist_sine_curve": {
        "name": "The Topologist's Sine Curve",
        "type": "topology",
        "tags": ["Connectedness", "Path-connectedness", "Closure", "Counterexample"],
        "date": "2026-04-21",
    },
    "entire_positive_real_part": {
        "name": "Entire Function with Non-Negative Real Part",
        "type": "Complex Analysis",
        "tags": ["Entire functions", "Liouville", "Mobius transformation", "Bounded functions"],
        "date": "2026-04-23",
    },
    "polynomial_integer_values": {
        "name": "An Impossible Integer Polynomial",
        "type": "Putnam",
        "tags": ["Polynomials", "Integer coefficients", "Divisibility", "Modular arithmetic"],
        "date": "2026-04-24",
    },
    "integral_max_circle": {
        "name": "Integral of a Max with a Circle",
        "type": "Integration",
        "tags": ["Integration bee", "Geometric interpretation", "Circular segment", "Area"],
        "date": "2026-04-25",
    },
    "dini_theorem": {
        "name": "Dini's Theorem: When Pointwise Becomes Uniform",
        "type": "analysis",
        "tags": ["Uniform convergence", "Pointwise convergence", "Compactness", "Dini"],
        "date": "2026-04-25",
    },
}

# Inline metadata lines to strip from the body (added by older question generation)
INLINE_META_RE = re.compile(
    r"^\*\*(Type|Tags|Date|Difficulty)\:\*\*.*$", re.MULTILINE
)


def make_frontmatter(meta):
    tags_yaml = "[" + ", ".join(f'"{t}"' for t in meta["tags"]) + "]"
    return (
        "---\n"
        f'name: "{meta["name"]}"\n'
        f'type: "{meta["type"]}"\n'
        f"tags: {tags_yaml}\n"
        f'date: "{meta["date"]}"\n'
        "solved: false\n"
        'comments: ""\n'
        "related: []\n"
        "redo: 0\n"
        "---\n"
    )


def migrate(slug, meta):
    path = REPO_ROOT / "questions" / slug / "question.md"
    if not path.exists():
        print(f"  SKIP (no file): {slug}")
        return

    content = path.read_text(encoding="utf-8")

    # Skip if frontmatter already present
    if content.startswith("---"):
        print(f"  SKIP (already has frontmatter): {slug}")
        return

    # Strip inline **Type:** etc. lines and collapse consecutive blank lines
    content = INLINE_META_RE.sub("", content)
    content = re.sub(r"\n{3,}", "\n\n", content).strip() + "\n"

    # Strip a stray --- separator that sometimes follows the metadata block
    content = re.sub(r"^---\s*\n", "", content)

    path.write_text(make_frontmatter(meta) + content, encoding="utf-8")
    print(f"  OK: {slug}")


def main():
    print("Migrating frontmatter...")
    for slug, meta in METADATA.items():
        migrate(slug, meta)
    print("Done.")


if __name__ == "__main__":
    main()
