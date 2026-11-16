# 2026-11-16T14:21:45.664076600
import vitis

client = vitis.create_client()
client.set_workspace(path="vitisWorkspace")

platform = client.get_component(name="ePWM_platform")
status = platform.build()

comp = client.get_component(name="enhancedPWM_application")
comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

