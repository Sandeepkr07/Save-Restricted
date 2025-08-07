import asyncio
from shared_client import start_client
import importlib
import os
import sys

async def load_and_run_plugins():
    await start_client()
    plugin_dir = "plugins"
    plugins = [f[:-3] for f in os.listdir(plugin_dir) if f.endswith(".py") and f != "__init__.py"]

    for plugin in plugins:
        module = importlib.import_module(f"plugins.{plugin}")
        func_name = f"run_{plugin}_plugin"
        if hasattr(module, func_name):
            print(f"Running {plugin} plugin...")
            await getattr(module, func_name)()

async def main():
    await load_and_run_plugins()
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1))

