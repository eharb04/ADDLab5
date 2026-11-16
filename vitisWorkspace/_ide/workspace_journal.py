# 2026-11-16T09:39:53.295143900
import vitis

client = vitis.create_client()
client.set_workspace(path="vitisWorkspace")

platform = client.create_platform_component(name = "ePWM_platform",hw_design = "$COMPONENT_LOCATION/../../ADDLab5/ARMWithPWM_wrapper.xsa",os = "standalone",cpu = "ps7_cortexa9_0",domain_name = "standalone_ps7_cortexa9_0",compiler = "gcc")

platform = client.get_component(name="ePWM_platform")
status = platform.build()

comp = client.create_app_component(name="enhancedPWM_application",platform = "$COMPONENT_LOCATION/../ePWM_platform/export/ePWM_platform/ePWM_platform.xpfm",domain = "standalone_ps7_cortexa9_0",template = "hello_world")

comp = client.get_component(name="enhancedPWM_application")
status = comp.import_files(from_loc="$COMPONENT_LOCATION/../ePWM_platform/ps7_cortexa9_0/standalone_ps7_cortexa9_0/bsp/hw_artifacts/drivers/enhancedPwm_AXI_v1_0/src", files=["enhancedPwm_AXI.h"], dest_dir_in_cmp = "src", is_skip_copy_sources = False)

status = comp.import_files(from_loc="$COMPONENT_LOCATION/../ePWM_platform/ps7_cortexa9_0/standalone_ps7_cortexa9_0/bsp/hw_artifacts/drivers/enhancedPwm_AXI_v1_0/src", files=["enhancedPwm_AXI.c"], dest_dir_in_cmp = "src", is_skip_copy_sources = False)

status = platform.build()

