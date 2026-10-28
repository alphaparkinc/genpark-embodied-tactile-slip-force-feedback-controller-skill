# -*- coding: utf-8 -*-
import sys, json
from client import GenParkEmbodiedTactileSlipForceFeedbackController

controller = GenParkEmbodiedTactileSlipForceFeedbackController()

def run_tool(name, args):
    if name == "process_telemetry":
        fn = float(args.get("current_normal_n", 5.0))
        fx = float(args.get("shear_x_n", 1.0))
        fy = float(args.get("shear_y_n", 0.0))
        rms = float(args.get("micro_vibration_rms", 0.05))
        dt = float(args.get("dt", 0.01))
        return controller.process_telemetry(fn, fx, fy, rms, dt)
    else:
        raise ValueError(f"Unknown tool: {name}")

def main():
    if "--test" in sys.argv:
        print("[TEST] Running GenPark Tactile Slip Feedback Controller Self-Test...")
        res = controller.process_telemetry(current_normal_n=5.0, shear_x_n=4.5, shear_y_n=0.0, micro_vibration_rms=0.25)
        assert res["is_slipping"] is True, "Should detect impending slip"
        assert res["command_grip_force_n"] > 5.0, "Should increase grip force command"
        print("[TEST] All tests passed successfully!")
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = run_tool(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"jsonrpc": "2.0", "id": req.get("id"), "result": res}))
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
