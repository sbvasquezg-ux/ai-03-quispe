"""Casos límite y equivalencia observacional del umbral de entrada."""

from __future__ import annotations

import csv
import math
from pathlib import Path


def normal_cdf(x: float, mean: float = 0.0, sd: float = 1.0) -> float:
    return 0.5 * (1.0 + math.erf((x - mean) / (sd * math.sqrt(2.0))))


def activation_probability(threshold_s: float, reduction: float, *, mean: float = 0.0, sd: float = 1.0) -> float:
    """P(TS-reduction <= omega < TS) under a Normal opportunity shock."""
    return normal_cdf(threshold_s, mean, sd) - normal_cdf(threshold_s - reduction, mean, sd)


def cumulative_gap(p1: float, p2: float, horizon: int, unfamiliar: int = 1) -> float:
    assert 0.0 <= p1 <= p2 <= 1.0
    assert horizon >= 0 and unfamiliar >= 0
    return unfamiliar * ((1.0 - p1) ** (horizon + 1) - (1.0 - p2) ** (horizon + 1))


def main() -> None:
    threshold_s = 0.8
    agent_B = 0.35
    generic_q = agent_B

    p_agent = activation_probability(threshold_s, agent_B)
    p_rival = activation_probability(threshold_s, generic_q)
    assert math.isclose(p_agent, p_rival, rel_tol=0.0, abs_tol=1e-15)

    # Contraejemplo mínimo de la Proposición 3 impresa: p1=0, p2=1.
    endpoint = [cumulative_gap(0.0, 1.0, s) for s in range(8)]
    assert endpoint == [1.0] * 8

    # La reparación interior produce aumentos positivos y decrecientes.
    interior = [cumulative_gap(0.0, 0.35, s) for s in range(8)]
    increments = [interior[j + 1] - interior[j] for j in range(len(interior) - 1)]
    assert all(x > 0.0 for x in increments)
    assert all(increments[j + 1] < increments[j] for j in range(len(increments) - 1))

    rows = []
    for s in range(8):
        rows.append(
            {
                "horizon": s,
                "prop3_endpoint_p2_1": endpoint[s],
                "prop3_interior_p2_035": interior[s],
                "agent_band_probability": p_agent,
                "generic_shock_probability": p_rival,
            }
        )

    output = Path(__file__).with_name("simulation.csv")
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"equivalencia q=B: {p_agent:.12f} = {p_rival:.12f}")
    print(f"endpoint p2=1: {endpoint}")
    print(f"resultado: {output}")


if __name__ == "__main__":
    main()
