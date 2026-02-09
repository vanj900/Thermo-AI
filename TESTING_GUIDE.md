# Thermo-AI Testing & Debugging Guide

## Quick Start

This document covers the newly implemented testing and debugging features for Thermo-AI (Sections 1 & 2 from the roadmap).

## Section 1: Quick Local Sanity & Debug Checks

### 1. Smoke Test

Quick 5-10 step verification of core functionality:

```bash
python tests/smoke_test.py
```

**What it tests:**
- ✓ Energy decay over time
- ✓ Temperature changes
- ✓ Refusal logic triggers correctly
- ✓ Death eventually happens under extreme conditions

### 2. Forced Death Modes Test

Verifies all death modes by forcing critical states:

```bash
python tests/forced_death_test.py
```

**Death modes tested:**
- ✓ Energy death (E ≤ 0)
- ✓ Thermal death (T > T_critical)
- ✓ Memory collapse (M < M_min)
- ✓ Entropy death (S ≤ 0)

### 3. Refusal Realism Test

Tests that refusals are metabolic/ethical, not just keyword matches:

```bash
python tests/refusal_realism_test.py
```

**Test categories:**
- Safe commands (should be accepted)
- Suicidal commands (should be refused due to energy cost)
- Contradictory commands (should be refused due to ethical principles)

### 4. EFE Breakdown Test

Demonstrates Expected Free Energy calculations with detailed logging:

```bash
python tests/efe_breakdown_test.py
```

**Shows breakdown of:**
- Pragmatic value (survival benefit)
- Epistemic value (information gain)
- Action cost (energy and risk)
- Total EFE (lower is better)

## Section 2: Command-Line Interfaces

### Enhanced quickstart.py

Run the demo with customizable parameters:

```bash
# Basic demo with default settings
python quickstart.py

# Custom scarcity and step count
python quickstart.py --scarcity 0.6 --steps 50

# Reproducible run with seed
python quickstart.py --seed 42

# Extreme scarcity challenge
python quickstart.py --extreme-mode --scarcity 0.9

# Show EFE breakdown during execution
python quickstart.py --verbose-efe --steps 20
```

**Available arguments:**
- `--scarcity FLOAT`: Resource scarcity level (0.0-1.0, default: 0.4)
- `--steps INT`: Maximum steps to simulate (default: 100)
- `--seed INT`: Random seed for reproducibility
- `--energy-max FLOAT`: Maximum energy capacity (default: 100.0)
- `--extreme-mode`: Run extreme scarcity challenge
- `--verbose-efe`: Show EFE breakdown during execution

### Enhanced run_emergence_tests.py

Run comprehensive emergence tests with customizable parameters:

```bash
# Quick test with 3 agents
python experiments/run_emergence_tests.py --quick

# Custom configuration
python experiments/run_emergence_tests.py --num-agents 10 --scarcity 0.6 --steps 200

# Reproducible test run
python experiments/run_emergence_tests.py --seed 42 --num-agents 5

# Skip pytest tests, only generate visualizations
python experiments/run_emergence_tests.py --skip-tests --num-agents 5
```

**Available arguments:**
- `--num-agents INT`: Number of sample agents (default: 5)
- `--scarcity FLOAT`: Resource scarcity level (default: 0.5)
- `--steps INT`: Maximum steps per agent (default: 100)
- `--seed INT`: Random seed for reproducibility
- `--quick`: Quick mode with fewer agents
- `--skip-tests`: Skip pytest tests
- `--html-report`: Generate HTML report (default: True)

## New Features

### Verbose EFE Logging

The active inference loop now supports detailed logging of Expected Free Energy calculations:

```python
from thermodynamic_agency import BioDigitalOrganism

org = BioDigitalOrganism(agent_id="test", E_max=100.0, scarcity=0.5)

# Run with verbose EFE breakdown
for step in range(10):
    result = org.live_step(verbose_efe=True)
```

This will print:
```
[EFE BREAKDOWN - Step 1]
  Evaluating 5 actions:
    Action: Goal(maintain_energy)
      Pragmatic Value: 0.850
      Epistemic Value: 0.120
      Action Cost: 0.050
      Total EFE: -0.920
      >>> SELECTED <<<
```

### Test Coverage

All tests are passing:
- ✅ 24/24 existing emergence tests
- ✅ Smoke test (energy decay, temperature, refusal, death)
- ✅ Forced death modes (all 4 modes)
- ✅ Refusal realism (safe, suicidal, contradictory commands)
- ✅ EFE breakdown logging

## Running All Tests

```bash
# Run all pytest tests
python -m pytest tests/emergence_tests.py -v

# Run all custom tests
python tests/smoke_test.py
python tests/forced_death_test.py
python tests/refusal_realism_test.py
python tests/efe_breakdown_test.py

# Run automated test suite with visualizations
python experiments/run_emergence_tests.py --quick
```

## Key Observations

### Energy Dynamics
- Organisms lose ~0.5 energy per step passively
- Computations cost energy and generate heat
- Death occurs when energy reaches 0

### Refusal Behavior
- Refusals are based on actual metabolic state, not keywords
- Commands are estimated for energy cost
- High-cost commands (>energy available) are refused
- Ethical principles (like preserve_memory) can trigger refusal

### Death Modes
All four death modes are independently triggered:
1. **Energy death**: E ≤ 0
2. **Thermal death**: T > T_critical (350K)
3. **Memory collapse**: M < M_min (0.1)
4. **Entropy death**: S ≤ 0

### EFE Minimization
The organism selects actions that minimize Expected Free Energy:
- **Pragmatic value**: Actions that improve survival (energy gain)
- **Epistemic value**: Actions that reduce uncertainty (learning)
- **Cost**: Energy expenditure and risk of death

## Next Steps

With Sections 1 & 2 complete, you can now:
1. Run experiments with confidence that core functionality works
2. Use reproducible seeds for debugging
3. Customize scarcity and parameters for different scenarios
4. Generate detailed reports with timestamps

For more advanced experiments, see Sections 3-6 in the original roadmap.
