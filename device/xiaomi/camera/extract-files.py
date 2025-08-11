#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {
    'system/lib64/libcamera_algoup_jni.xiaomi.so': blob_fixup()
        .add_needed('libgui_shim_miuicamera.so')
        .sig_replace('08 AD 40 F9', '08 A9 40 F9'),

    'system/lib64/libcamera_mianode_jni.xiaomi.so': blob_fixup()
        .add_needed('libgui_shim_miuicamera.so'),

    # Ported logic from the shell script
    'vendor/bin/hw/android.hardware.camera.provider@2.4-service_64': blob_fixup()
        .replace_needed('vendor.qti.hardware.camera.device@1.0.so', 'vendor.qti.hardware.camera.device@1.0_vendor.so'),

    'vendor/lib/android.hardware.camera.provider@2.4-legacy.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.camera.device@1.0.so', 'vendor.qti.hardware.camera.device@1.0_vendor.so'),

    'vendor/lib/camera.device@1.0-impl.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.camera.device@1.0.so', 'vendor.qti.hardware.camera.device@1.0_vendor.so'),

    'vendor/lib64/android.hardware.camera.provider@2.4-legacy.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.camera.device@1.0.so', 'vendor.qti.hardware.camera.device@1.0_vendor.so'),

    'vendor/lib64/camera.device@1.0-impl.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.camera.device@1.0.so', 'vendor.qti.hardware.camera.device@1.0_vendor.so'),
}  # fmt: skip

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'libgrallocutils',
    ): lib_fixup_remove,
}

namespace_imports = [
    'hardware/qcom-caf/common/libqti-perfd-client',
    'vendor/qcom/opensource/display',
    'vendor/xiaomi/apollo',
]

module = ExtractUtilsModule(
    'camera',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
