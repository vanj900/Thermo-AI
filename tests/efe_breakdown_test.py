"""
EFE Breakdown Test - Test verbose EFE logging

This test runs an organism for 10 steps with verbose_efe=True
to show the breakdown of Expected Free Energy calculations:
- Pragmatic value (survival benefit)
- Epistemic value (information gain)
- Action cost (energy and risk)

Run with: python tests/efe_breakdown_test.py
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from thermodynamic_agency import BioDigitalOrganism


def test_efe_breakdown():
    """Run organism for 10 steps with EFE breakdown logging"""
    
    print("\n" + "="*70)
    print("  EFE BREAKDOWN TEST")
    print("  Showing Expected Free Energy calculations for 10 steps")
    print("="*70 + "\n")
    
    # Create organism
    org = BioDigitalOrganism(
        agent_id="efe_test_organism",
        E_max=100.0,
        scarcity=0.5,
        enable_ethics=True
    )
    
    print(f"Organism: {org.agent_id}")
    print(f"Initial state: {org.metabolic_engine}\n")
    
    print("Running 10 steps with EFE breakdown logging...")
    print("="*70)
    
    # Run for 10 steps with verbose EFE
    for step in range(10):
        if not org.is_alive:
            print(f"\nOrganism died at step {step}")
            break
        
        result = org.live_step(verbose_efe=True)
        
        # Print summary after each step
        state = org.metabolic_engine.get_state()
        survival_prob = org.metabolic_engine.get_survival_probability()
        
        print(f"\nStep {step} Summary:")
        print(f"  Energy: {state['energy']:.2f}, Temp: {state['temperature']:.2f}K")
        print(f"  Memory: {state['memory_integrity']:.3f}, Stability: {state['stability']:.3f}")
        print(f"  Survival Probability: {survival_prob:.2%}")
        print("-" * 70)
    
    print("\n" + "="*70)
    print("  EFE BREAKDOWN TEST COMPLETE")
    print("="*70)
    print("\nKey observations:")
    print("  - Pragmatic value: Higher for actions that improve survival")
    print("  - Epistemic value: Higher for actions with more uncertainty (learning potential)")
    print("  - Cost: Energy cost + risk of death")
    print("  - EFE: Lower is better (organism minimizes Expected Free Energy)")
    print("\n")
    
    return True


if __name__ == "__main__":
    try:
        success = test_efe_breakdown()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n✗ EFE BREAKDOWN TEST FAILED WITH ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
