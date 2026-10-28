# -*- coding: utf-8 -*-
from client import GenParkEmbodiedTactileSlipForceFeedbackController

def main():
    controller = GenParkEmbodiedTactileSlipForceFeedbackController(target_slip_margin=0.6)
    print("=== GenPark Physical AI Tactile Slip Closed-Loop Controller ===")

    # Simulation: payload starts slipping in gripper
    telemetry_stream = [
        {"fn": 10.0, "fx": 2.0, "fy": 0.0, "vib": 0.02}, # Stable hold
        {"fn": 10.0, "fx": 4.5, "fy": 1.0, "vib": 0.08}, # Rising shear load
        {"fn": 10.0, "fx": 7.5, "fy": 2.0, "vib": 0.22}, # Incipient slip detected!
        {"fn": 18.0, "fx": 7.5, "fy": 2.0, "vib": 0.04}  # Gripper squeezed, slip stabilized
    ]

    for i, step in enumerate(telemetry_stream):
        out = controller.process_telemetry(step["fn"], step["fx"], step["fy"], step["vib"])
        print(f"Step {i+1}: Slip={out['is_slipping']}, Ratio={out['shear_to_normal_ratio']}, Command={out['command_grip_force_n']}N (Delta={out['force_adjustment_delta_n']}N)")

if __name__ == "__main__":
    main()
