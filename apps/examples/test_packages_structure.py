#!/usr/bin/env python3
"""
Test that packages are correctly structured and can be imported
This test does NOT require the gateway to be running
"""

import sys
from pathlib import Path


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def test_gateway_client_import():
    """Test importing gateway-client package"""
    print_section("TEST 1: Gateway Client Package Import")

    try:
        from gateway_client import AIGatewayClient, GatewayFactory

        print("✅ Successfully imported AIGatewayClient")
        print("✅ Successfully imported GatewayFactory")

        # Test creating instances (without connecting)
        client = GatewayFactory.balanced()
        print(f"✅ Created balanced client: {type(client).__name__}")

        fast_client = GatewayFactory.fast()
        print(f"✅ Created fast client: {type(fast_client).__name__}")

        custom_client = AIGatewayClient(
            base_url="http://localhost:8080", router_id="custom"
        )
        print(f"✅ Created custom client: {type(custom_client).__name__}")

        return True

    except ImportError as e:
        print(f"❌ Import failed: {e}")
        print("\n💡 Make sure you installed the package:")
        print("   pip3 install -e packages/gateway-client")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_claude_flow_import():
    """Test importing claude-flow package"""
    print_section("TEST 2: Claude Flow Package Import")

    try:
        # Add claude-flow to path
        sys.path.insert(
            0, str(Path(__file__).parent / "packages" / "claude-flow" / "src")
        )

        # Test main imports
        from integration import (
            AIGatewayClient,
            claude_flow_completion,
            claude_flow_chat,
        )

        print("✅ Successfully imported integration module")

        from hive import Hive, Agent, create_research_hive

        print("✅ Successfully imported hive module")

        from swarm import Swarm

        print("✅ Successfully imported swarm module")

        # Test creating instances (without connecting)
        hive = Hive("test-hive")
        print(f"✅ Created Hive instance: {hive.name}")

        swarm = Swarm("test-swarm")
        print(f"✅ Created Swarm instance: {swarm.name}")

        return True

    except ImportError as e:
        print(f"❌ Import failed: {e}")
        print("\n💡 Make sure you installed the package:")
        print("   pip3 install -e packages/claude-flow")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback

        traceback.print_exc()
        return False


def test_package_structure():
    """Test that package files exist in correct locations"""
    print_section("TEST 3: Package File Structure")

    base_path = Path(__file__).parent

    # Check gateway-client structure
    print("\n📁 Checking gateway-client structure...")
    gateway_files = [
        "packages/gateway-client/setup.py",
        "packages/gateway-client/package.json",
        "packages/gateway-client/README.md",
        "packages/gateway-client/src/__init__.py",
        "packages/gateway-client/src/gateway_client.py",
    ]

    gateway_ok = True
    for file_path in gateway_files:
        full_path = base_path / file_path
        if full_path.exists():
            print(f"   ✅ {file_path}")
        else:
            print(f"   ❌ {file_path} - NOT FOUND")
            gateway_ok = False

    # Check claude-flow structure
    print("\n📁 Checking claude-flow structure...")
    claude_files = [
        "packages/claude-flow/setup.py",
        "packages/claude-flow/package.json",
        "packages/claude-flow/README.md",
        "packages/claude-flow/src/__init__.py",
        "packages/claude-flow/src/integration.py",
        "packages/claude-flow/src/hive.py",
        "packages/claude-flow/src/swarm.py",
    ]

    claude_ok = True
    for file_path in claude_files:
        full_path = base_path / file_path
        if full_path.exists():
            print(f"   ✅ {file_path}")
        else:
            print(f"   ❌ {file_path} - NOT FOUND")
            claude_ok = False

    return gateway_ok and claude_ok


def test_package_metadata():
    """Test package metadata"""
    print_section("TEST 4: Package Metadata")

    try:
        # Test gateway-client metadata
        print("\n📦 Gateway Client Package:")
        # Read version from the package file directly
        gateway_client_file = (
            Path(__file__).parent
            / "packages"
            / "gateway-client"
            / "src"
            / "gateway_client.py"
        )
        if gateway_client_file.exists():
            with open(gateway_client_file) as f:
                for line in f:
                    if "__version__" in line and "=" in line:
                        version = line.split("=")[1].strip().strip('"').strip("'")
                        print(f"   Version: {version}")
                        break

        # Test claude-flow metadata
        print("\n📦 Claude Flow Package:")
        claude_flow_init = (
            Path(__file__).parent / "packages" / "claude-flow" / "src" / "__init__.py"
        )
        if claude_flow_init.exists():
            with open(claude_flow_init) as f:
                for line in f:
                    if "__version__" in line and "=" in line:
                        version = line.split("=")[1].strip().strip('"').strip("'")
                        print(f"   Version: {version}")
                        break

        return True

    except Exception as e:
        print(f"❌ Error reading metadata: {e}")
        import traceback

        traceback.print_exc()
        return False


def test_dependencies():
    """Test that required dependencies are available"""
    print_section("TEST 5: Dependencies")

    try:
        import requests

        print(f"✅ requests: {requests.__version__}")

        # Check if asyncio is available (built-in)
        import asyncio

        print("✅ asyncio: available")

        # Check if json is available (built-in)
        import json

        print("✅ json: available")

        return True

    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("\n💡 Install missing dependencies:")
        print("   pip3 install requests")
        return False


def main():
    """Run all structure tests"""
    print("\n" + "🔍" * 35)
    print("  AI GATEWAY v3 - PACKAGE STRUCTURE TEST")
    print("🔍" * 35)
    print("\nThis test verifies packages are correctly structured.")
    print("It does NOT require the gateway to be running.")

    results = {}

    # Run tests
    results["gateway_client_import"] = test_gateway_client_import()
    results["claude_flow_import"] = test_claude_flow_import()
    results["package_structure"] = test_package_structure()
    results["package_metadata"] = test_package_metadata()
    results["dependencies"] = test_dependencies()

    # Print summary
    print_section("TEST SUMMARY")

    total = len(results)
    passed = sum(1 for v in results.values() if v)
    failed = total - passed

    print(f"\nTotal Tests: {total}")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")

    print("\nDetailed Results:")
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status} - {test_name.replace('_', ' ').title()}")

    if failed == 0:
        print("\n" + "🎉" * 35)
        print("  ALL STRUCTURE TESTS PASSED!")
        print("  Packages are correctly installed and structured.")
        print("🎉" * 35)
        print("\n📝 Next step: Test with running gateway")
        print("   python test_claude_flow_integration.py")
    else:
        print("\n" + "⚠️ " * 35)
        print(f"  {failed} test(s) failed. Check the output above.")
        print("⚠️ " * 35)

    return results


if __name__ == "__main__":
    results = main()

    # Exit with error code if any tests failed
    if not all(results.values()):
        sys.exit(1)
