"""
Claude Flow Swarm using AI Gateway v2
"""

import sys
from pathlib import Path

# Add gateway-client to path for local development
gateway_client_path = Path(__file__).parent.parent.parent / "gateway-client" / "src"
if gateway_client_path.exists():
    sys.path.insert(0, str(gateway_client_path))

# Use absolute imports when possible, fall back to relative
try:
    from hive import Hive, Agent
except ImportError:
    from .hive import Hive, Agent

from gateway_client import GatewayFactory
from typing import List, Dict, Any
import asyncio


class Swarm:
    def __init__(self, name: str):
        self.name = name
        self.hives: List[Hive] = []
        self.coordinator = Agent(
            "coordinator",
            "a project coordinator who delegates tasks",
            "groq/llama-3.1-70b-versatile",
            GatewayFactory.fast(),
        )

    def add_hive(self, hive: Hive):
        """Add hive to swarm"""
        self.hives.append(hive)

    async def execute_mission(self, mission: str) -> Dict[str, Any]:
        """Execute a complex mission across multiple hives"""
        # Coordinator breaks down the mission
        breakdown_prompt = f"""
        Break down this mission into specific tasks for different teams:
        Mission: {mission}
        
        Available teams: {[hive.name for hive in self.hives]}
        
        Return a JSON structure with team assignments.
        """

        coordination = await self.coordinator.process(breakdown_prompt)

        # Execute tasks across hives
        results = {}
        for hive in self.hives:
            hive_task = f"Your part of the mission: {mission}"
            hive_results = await hive.collaborate(hive_task)
            results[hive.name] = hive_results

        return {"mission": mission, "coordination": coordination, "results": results}


# Example usage
async def demo_swarm():
    # Create swarm
    swarm = Swarm("AI Research Swarm")

    # Add research hive
    try:
        from hive import create_research_hive
    except ImportError:
        from .hive import create_research_hive

    research_hive = create_research_hive()
    swarm.add_hive(research_hive)

    # Add development hive
    dev_hive = Hive("Development Team")
    dev_hive.add_agent("architect", "a software architect")
    dev_hive.add_agent("developer", "a senior developer")
    swarm.add_hive(dev_hive)

    # Execute mission
    mission = "Research and prototype a new AI feature"
    results = await swarm.execute_mission(mission)

    return results
