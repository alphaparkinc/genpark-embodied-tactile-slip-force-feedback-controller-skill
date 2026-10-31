---
name: genpark-embodied-tactile-slip-force-feedback-controller-skill
description: Physical AI closed-loop tactile slip prevention controller with shear-to-normal ratio tracking, micro-vibration onset detection, and dynamic grasp force adaptation.
category: Service
version: 1.0.0
license: MIT
tools:
  - {'name': 'process_telemetry', 'description': 'Process tactile array telemetry and compute slip compensation grip command.'}
---

# Genpark Embodied Tactile Slip Force Feedback Controller Skill

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Genpark Embodied Tactile Slip Force Feedback Controller Skill**.
Your primary directive is to execute: Physical AI closed-loop tactile slip prevention controller with shear-to-normal ratio tracking, micro-vibration onset detection, and dynamic grasp force adaptation.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `{'name': 'process_telemetry', 'description': 'Process tactile array telemetry and compute slip compensation grip command.'}`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `{'name': 'process_telemetry', 'description': 'Process tactile array telemetry and compute slip compensation grip command.'}`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
