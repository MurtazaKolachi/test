# proprietary_device_xiaomi_camera

Prebuilt modded MIUI/Leica Camera 5.0 for Mi 10T/Mi 10T pro (apollo), to include in custom ROM builds.

### How to use?

1. Clone this repo to `device/xiaomi/camera`
2. Clone https://gitlab.com/johnmart19/vendor_xiaomi_camera to 'vendor/xiaomi/camera'
3. Inherit it from `device.mk` in device tree:
```
# Camera
$(call inherit-product-if-exists, device/xiaomi/camera/miuicamera.mk)
```

3. Ensure that you added misys vintf dependencies in your framework_compatibility_matrix.xml:

```
    <hal format="hidl" optional="true">
        <name>vendor.xiaomi.hardware.misys</name>
        <version>1.0</version>
        <version>2.0</version>
        <version>3.0</version>
        <version>4.0</version>
        <interface>
            <name>IMiSys</name>
            <instance>default</instance>
        </interface>
    </hal>
```
3.1 Reference - https://github.com/PocoF3Releases/device_xiaomi_sm8250-common/commit/26b57664835c487db278dbda83fe936ceb831c63
