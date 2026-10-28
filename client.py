# -*- coding: utf-8 -*-
"""
GenPark Physical AI Tactile Slip Force Feedback Controller
Standard Library only: math, typing.
Closed-loop adaptive controller that monitors streaming shear/normal force ratios,
detects incipient micro-vibration slip, and computes compensatory grip force commands.
"""

import math
from typing import Dict, List, Tuple, Any

class GenParkEmbodiedTactileSlipForceFeedbackController:
    def __init__(self, target_slip_margin: float = 0.65,
                 min_grip_force: float = 2.0, max_grip_force: float = 60.0,
                 kp: float = 8.0, kd: float = 3.0, kvib: float = 12.0):
        self.target_slip_margin = target_slip_margin
        self.min_grip_force = min_grip_force
        self.max_grip_force = max_grip_force
        self.kp = kp
        self.kd = kd
        self.kvib = kvib

        self.last_ratio = 0.0
        self.current_grip_force = min_grip_force

    def process_telemetry(self, current_normal_n: float, shear_x_n: float, shear_y_n: float,
                          micro_vibration_rms: float, dt: float = 0.01) -> Dict[str, Any]:
        """
        Calculates instantaneous slip probability and outputs updated commanding normal grip force.
        """
        shear_magnitude = math.sqrt(shear_x_n**2 + shear_y_n**2)
        safe_normal = max(current_normal_n, 0.1)
        instant_ratio = shear_magnitude / safe_normal

        # Rate of change of friction utilization ratio
        d_ratio = (instant_ratio - self.last_ratio) / max(dt, 1e-4) if dt > 0 else 0.0
        self.last_ratio = instant_ratio

        # Slip detection conditions
        ratio_slip_threat = instant_ratio > self.target_slip_margin
        vibration_slip_threat = micro_vibration_rms > 0.15

        is_slipping = ratio_slip_threat or vibration_slip_threat

        # Adaptive PID-style normal force increment
        delta_force = 0.0
        if is_slipping:
            # Increase normal force to restore friction margin
            error = instant_ratio - self.target_slip_margin
            p_term = self.kp * max(0.0, error)
            d_term = self.kd * max(0.0, d_ratio)
            vib_term = self.kvib * max(0.0, micro_vibration_rms - 0.1)
            delta_force = p_term + d_term + vib_term
        else:
            # Gentle relaxation towards optimal light grasp
            if instant_ratio < (self.target_slip_margin * 0.5):
                delta_force = -0.5 * (self.target_slip_margin * 0.5 - instant_ratio)

        command_force = max(self.min_grip_force, min(self.max_grip_force, safe_normal + delta_force))
        self.current_grip_force = command_force

        return {
            "is_slipping": is_slipping,
            "shear_to_normal_ratio": round(instant_ratio, 4),
            "ratio_derivative": round(d_ratio, 4),
            "command_grip_force_n": round(command_force, 3),
            "force_adjustment_delta_n": round(delta_force, 3),
            "shear_magnitude_n": round(shear_magnitude, 3),
            "micro_vibration_rms": round(micro_vibration_rms, 4)
        }
