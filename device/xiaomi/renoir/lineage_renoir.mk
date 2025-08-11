#
# Copyright (C) 2021-2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from renoir device
$(call inherit-product, device/xiaomi/renoir/device.mk)

TARGET_BOOT_ANIMATION_RES := 1080
WITH_GMS := true
TARGET_USES_MINI_GAPPS := true
BUILD_BCR := true

ifeq ($(TARGET_USES_MINI_GAPPS),true)
PRODUCT_PACKAGES += \
    TurboAdapter
endif
TARGET_DISABLE_EPPE := true

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_BRAND := Xiaomi
PRODUCT_DEVICE := renoir
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_MODEL := M2101K9R
PRODUCT_NAME := lineage_renoir

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="renoir_global-user 13 TKQ1.220829.002 V14.0.7.0.TKIMIXM release-keys" \
    BuildFingerprint=Xiaomi/renoir_global/renoir:13/TKQ1.220829.002/V14.0.7.0.TKIMIXM:user/release-keys \
    DeviceProduct=renoir \
    SystemName=renoir_global

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi
