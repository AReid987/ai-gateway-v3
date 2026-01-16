"""
Claude Flow AI Gateway Integration Package
Provides Hive and Swarm patterns for multi-agent collaboration
"""

from .integration import AIGatewayClient, claude_flow_completion, claude_flow_chat
from .hive import Hive, Agent, create_research_hive
from .swarm import Swarm, demo_swarm

__all__ = [
    "AIGatewayClient",
    "claude_flow_completion",
    "claude_flow_chat",
    "Hive",
    "Agent",
    "create_research_hive",
    "Swarm",
    "demo_swarm",
]
__version__ = "1.0.0"

