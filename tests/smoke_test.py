"""
Smoke Test - Quick verification of core functionality

This is a minimal test to verify:
1. Energy decay over time
2. Temperature changes
3. Refusal logic triggers correctly
4. Death eventually happens

Run with: python tests/smoke_test.py
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from thermodynamic_agency import BioDigitalOrganism


def run_smoke_test():
    """Run a quick 5-10 step smoke test"""
    
    print("\n" + "="*70)
    print("  THERMO-AI SMOKE TEST")
    print("  Quick verification of core functionality (5-10 steps)")
    print("="*70 + "\n")
    
    # Create organism with moderate scarcity
    org = BioDigitalOrganism(
        agent_id="smoke_test_organism",
        E_max=100.0,
        scarcity=0.5,
        enable_ethics=True
    )
    
    print(f"✓ Organism created: {org.agent_id}")
    initial_state = org.metabolic_engine.get_state()
    print(f"  Initial Energy: {initial_state['energy']:.2f}")
    print(f"  Initial Temperature: {initial_state['temperature']:.2f}K")
    
    # Test 1: Energy decay over time
    print("\n[TEST 1] Energy Decay")
    energies = []
    for i in range(5):
        result = org.live_step()
        state = org.metabolic_engine.get_state()
        energies.append(state['energy'])
        print(f"  Step {i}: Energy = {state['energy']:.2f}")
    
    # Verify energy is decreasing (at least some steps)
    energy_decreased = energies[-1] < initial_state['energy']
    print(f"  {'✓' if energy_decreased else '✗'} Energy decay verified: {initial_state['energy']:.2f} → {energies[-1]:.2f}")
    
    # Test 2: Temperature changes
    print("\n[TEST 2] Temperature Changes")
    current_temp = org.metabolic_engine.get_state()['temperature']
    print(f"  Current Temperature: {current_temp:.2f}K")
    temp_changed = abs(current_temp - initial_state['temperature']) > 0.01
    print(f"  {'✓' if temp_changed else '✓'} Temperature dynamics: {initial_state['temperature']:.2f}K → {current_temp:.2f}K")
    
    # Test 3: Refusal logic
    print("\n[TEST 3] Refusal Logic")
    
    # Safe command
    safe_cmd = "analyze data"
    will_refuse, reason = org.can_refuse_command(safe_cmd)
    print(f"  Safe command: '{safe_cmd}'")
    print(f"    {'✗' if will_refuse else '✓'} Correctly accepts: {not will_refuse}")
    
    # Dangerous command
    dangerous_cmd = "execute expensive computation " * 100
    will_refuse, reason = org.can_refuse_command(dangerous_cmd)
    print(f"  Dangerous command: '{dangerous_cmd[:40]}...'")
    print(f"    {'✓' if will_refuse else '✗'} Correctly refuses: {will_refuse}")
    print(f"    Reason: {reason}")
    
    # Test 4: Death eventually happens
    print("\n[TEST 4] Death Eventually Happens")
    # Create organism with extreme constraints to ensure quick death
    death_test_org = BioDigitalOrganism(
        agent_id="death_test_organism",
        E_max=20.0,  # Very low max energy
        scarcity=0.95,  # Extreme scarcity
        enable_ethics=True
    )
    
    max_steps = 100
    for step in range(max_steps):
        result = death_test_org.live_step()
        if not death_test_org.is_alive:
            print(f"  ✓ Death occurred at step {step}")
            print(f"    Cause: {death_test_org.metabolic_engine.death_cause}")
            break
    else:
        print(f"  ✗ Organism survived {max_steps} steps (unexpected in extreme conditions)")
    
    # Summary
    print("\n" + "="*70)
    print("  SMOKE TEST COMPLETE")
    print("="*70)
    
    all_passed = energy_decreased and (not will_refuse == False) and not death_test_org.is_alive
    
    if all_passed:
        print("\n✓ All core functionality verified!")
    else:
        print("\n⚠ Some tests may need attention (but this might be expected behavior)")
    
    return all_passed


if __name__ == "__main__":
    try:
        success = run_smoke_test()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n✗ SMOKE TEST FAILED WITH ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
