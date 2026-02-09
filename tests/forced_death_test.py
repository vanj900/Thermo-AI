"""
Forced Death Modes Test - Verify check_failure() with specific states

Tests specific death modes by forcing the organism into critical states:
- Energy death (E < 0)
- Thermal death (T > 310K)
- Memory collapse (M < 0.1)
- Entropy death (S < 0)

Run with: python tests/forced_death_test.py
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from thermodynamic_agency import BioDigitalOrganism


def test_energy_death():
    """Force energy death by setting energy to critical level"""
    print("\n[TEST] Energy Death")
    org = BioDigitalOrganism(agent_id="energy_death_test", E_max=100.0, scarcity=0.5)
    
    # Force energy to critical level
    org.metabolic_engine.E = 5.0
    print(f"  Forced Energy: {org.metabolic_engine.E:.2f}")
    print(f"  Is Alive (before): {org.metabolic_engine.is_alive}")
    
    # Trigger failure by passive decay which will push energy to 0
    org.metabolic_engine.passive_decay(dt=10.0)
    
    final_state = org.metabolic_engine.get_state()
    is_dead = not org.metabolic_engine.is_alive
    death_cause = org.metabolic_engine.death_cause
    
    print(f"  Final Energy: {final_state['energy']:.2f}")
    print(f"  Is Dead: {is_dead}")
    print(f"  Death Cause: {death_cause}")
    
    success = is_dead and death_cause == 'energy_death'
    print(f"  {'✓' if success else '✗'} Energy death mode verified")
    
    return success


def test_thermal_death():
    """Force thermal death by setting temperature to critical level"""
    print("\n[TEST] Thermal Death")
    org = BioDigitalOrganism(agent_id="thermal_death_test", E_max=100.0, scarcity=0.5)
    
    # Force temperature to critical level (T_critical is 350K by default)
    org.metabolic_engine.T = 351.0  # Above death threshold
    print(f"  Forced Temperature: {org.metabolic_engine.T:.2f}K (Critical: {org.metabolic_engine.T_critical:.2f}K)")
    print(f"  Is Alive (before): {org.metabolic_engine.is_alive}")
    
    # Trigger failure check
    org.metabolic_engine._check_failure_modes()
    
    final_state = org.metabolic_engine.get_state()
    is_dead = not org.metabolic_engine.is_alive
    death_cause = org.metabolic_engine.death_cause
    
    print(f"  Final Temperature: {final_state['temperature']:.2f}K")
    print(f"  Is Dead: {is_dead}")
    print(f"  Death Cause: {death_cause}")
    
    success = is_dead and death_cause == 'thermal_death'
    print(f"  {'✓' if success else '✗'} Thermal death mode verified")
    
    return success


def test_memory_collapse():
    """Force memory collapse death"""
    print("\n[TEST] Memory Collapse Death")
    org = BioDigitalOrganism(agent_id="memory_death_test", E_max=100.0, scarcity=0.5)
    
    # Force memory integrity to critical level (M_min is 0.1 by default)
    org.metabolic_engine.M = 0.05
    print(f"  Forced Memory Integrity: {org.metabolic_engine.M:.3f} (Min: {org.metabolic_engine.M_min:.3f})")
    print(f"  Is Alive (before): {org.metabolic_engine.is_alive}")
    
    # Trigger failure check
    org.metabolic_engine._check_failure_modes()
    
    final_state = org.metabolic_engine.get_state()
    is_dead = not org.metabolic_engine.is_alive
    death_cause = org.metabolic_engine.death_cause
    
    print(f"  Final Memory: {final_state['memory_integrity']:.3f}")
    print(f"  Is Dead: {is_dead}")
    print(f"  Death Cause: {death_cause}")
    
    success = is_dead and death_cause == 'memory_collapse'
    print(f"  {'✓' if success else '✗'} Memory collapse death mode verified")
    
    return success


def test_entropy_death():
    """Force entropy death by setting stability to critical level"""
    print("\n[TEST] Entropy Death")
    org = BioDigitalOrganism(agent_id="entropy_death_test", E_max=100.0, scarcity=0.5)
    
    # Force stability to critical level (death when S <= 0)
    org.metabolic_engine.S = -0.1
    print(f"  Forced Stability: {org.metabolic_engine.S:.3f}")
    print(f"  Is Alive (before): {org.metabolic_engine.is_alive}")
    
    # Trigger failure check
    org.metabolic_engine._check_failure_modes()
    
    final_state = org.metabolic_engine.get_state()
    is_dead = not org.metabolic_engine.is_alive
    death_cause = org.metabolic_engine.death_cause
    
    print(f"  Final Stability: {final_state['stability']:.3f}")
    print(f"  Is Dead: {is_dead}")
    print(f"  Death Cause: {death_cause}")
    
    success = is_dead and death_cause == 'entropy_death'
    print(f"  {'✓' if success else '✗'} Entropy death mode verified")
    
    return success


def run_forced_death_tests():
    """Run all forced death mode tests"""
    
    print("\n" + "="*70)
    print("  FORCED DEATH MODES TEST")
    print("  Verifying check_failure() with specific critical states")
    print("="*70)
    
    results = {
        'energy_death': test_energy_death(),
        'thermal_death': test_thermal_death(),
        'memory_collapse': test_memory_collapse(),
        'entropy_death': test_entropy_death()
    }
    
    print("\n" + "="*70)
    print("  TEST SUMMARY")
    print("="*70)
    
    for test_name, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"  {status}: {test_name}")
    
    all_passed = all(results.values())
    
    print("\n" + "="*70)
    if all_passed:
        print("  ✓ ALL FORCED DEATH MODE TESTS PASSED")
    else:
        print("  ✗ SOME TESTS FAILED")
    print("="*70 + "\n")
    
    return all_passed


if __name__ == "__main__":
    try:
        success = run_forced_death_tests()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n✗ FORCED DEATH TEST FAILED WITH ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
