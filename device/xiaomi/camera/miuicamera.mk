#
# Copyright (C) 2024 VoidUI Project
#
# SPDX-License-Identifier: Apache-2.0
#

CAMERA_PATH := device/xiaomi/camera
CAMERA_VENDOR_PATH := vendor/xiaomi/camera

# Permissions
PRODUCT_COPY_FILES += \
     $(call find-copy-subdir-files,*,$(CAMERA_PATH)/configs/permissions/,$(TARGET_COPY_OUT_SYSTEM)/etc)

PRODUCT_PACKAGES += \
    libgui_shim_miuicamera

# CameraX Config Overwrite
PRODUCT_COPY_FILES += \
     $(CAMERA_PATH)/configs/camera/camxoverridesettings.txt:$(TARGET_COPY_OUT_VENDOR)/etc/camera/camxoverridesettings.txt

# Camera Extensions
PRODUCT_SYSTEM_PROPERTIES += \
    ro.camerax.extensions.enabled=true

# Camera Extensions permissions
PRODUCT_COPY_FILES += \
    $(CAMERA_PATH)/configs/permissions/extensions/camerax-vendor-extensions.xml:$(TARGET_COPY_OUT_SYSTEM)/etc/permissions/camerax-vendor-extensions.xml

# Device-Features
PRODUCT_COPY_FILES += \
     $(CAMERA_PATH)/configs/device_features/apollo.xml:$(TARGET_COPY_OUT_PRODUCT)/etc/device_features/apollo.xml

# Symlinks
PRODUCT_PACKAGES += \
    miui_camera_libcamera_algoup_symlink \
    miui_camera_libcamera_mianode_symlink \
    miui_camera_libmicampostproc_symlink \
    miui_camera_campostproc_vendor_symlink \
    miui_camera_libOpenCL_symlink \
    miui_camera_libmqsas_symlink \
    miui_camera_libcameraimpl_symlink \
    miui_camera_libopencl_camera_symlink

# Properties
PRODUCT_SYSTEM_PROPERTIES += \
    ro.com.google.lens.oem_camera_package=com.android.camera \
    ro.miui.notch=1 \
    persist.sys.cam.skip_detach_image=true

# Logging
PRODUCT_SYSTEM_PROPERTIES += \
   log.tag.CHIUSECASE=ERROR

PRODUCT_VENDOR_PROPERTIES += \
   persist.vendor.camera.logInfoMask=false

# Sepolicy Camera
BOARD_VENDOR_SEPOLICY_DIRS += \
    $(CAMERA_PATH)/sepolicy/camera/vendor

SYSTEM_EXT_PRIVATE_SEPOLICY_DIRS += \
    $(CAMERA_PATH)/sepolicy/camera/private

# Sepolicy MiSys
BOARD_VENDOR_SEPOLICY_DIRS += \
    $(CAMERA_PATH)/sepolicy/misys/vendor

SYSTEM_EXT_PRIVATE_SEPOLICY_DIRS += \
    $(CAMERA_PATH)/sepolicy/misys/private

SYSTEM_EXT_PUBLIC_SEPOLICY_DIRS += \
    $(CAMERA_PATH)/sepolicy/misys/public

# Qualcomm Gralloc
PRODUCT_PACKAGES += \
     gralloc.qcom

# MiSys HIDL deps
PRODUCT_PACKAGES += \
    android.hidl.manager@1.0 \
    android.hidl.manager@1.0.vendor \
    android.hidl.memory.block@1.0 \
    android.hidl.memory.block@1.0.vendor \
    android.hidl.memory@1.0-impl

# RRO Overlays
PRODUCT_PACKAGES += \
    MiuiCameraOverlay \
    MiuiCameraOverlayLos \
    MiuiCameraOverlayAosp

# System Properties
PRODUCT_SYSTEM_PROPERTIES += \
    persist.vendor.camera.privapp.list=com.android.camera \
    ro.com.google.lens.oem_camera_package=com.android.camera

$(call inherit-product, $(CAMERA_VENDOR_PATH)/camera-vendor.mk)
