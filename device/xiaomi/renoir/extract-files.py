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
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/renoir',
    'hardware/qcom-caf/sm8350',
    'hardware/qcom-caf/wlan',
    'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qualcomm.qti.dpm.api@1.0',
        'libmmosal',
        'vendor.qti.diaghal@1.0',
        'vendor.qti.hardware.wifidisplaysession@1.0',
        'vendor.qti.imsrtpservice@3.0',
        'vendor.xiaomi.hardware.misys@1.0',
        'vendor.xiaomi.hardware.misys@2.0',
        'vendor.xiaomi.hardware.misys@3.0',
        'vendor.xiaomi.hardware.misys@4.0',
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/etc/init/wfdservice.rc': blob_fixup()
        .regex_replace(r'(start|stop) wfdservice\b', r'\1 wfdservice64'),
    'system_ext/lib64/libwfdmmsrc_system.so': blob_fixup()
        .add_needed('libgui_shim.so'),
    'system_ext/lib64/libwfdservice.so': blob_fixup()
        .add_needed('libaudioclient_shim.so')
        .replace_needed('android.media.audio.common.types-V2-cpp.so', 'android.media.audio.common.types-V4-cpp.so'),
    'system_ext/lib64/libwfdnative.so': blob_fixup()
        .remove_needed('android.hidl.base@1.0.so')
        .add_needed('libbinder_shim.so')
        .add_needed('libinput_shim.so'),
    ('vendor/etc/media_lahaina/video_system_specs.json', 'vendor/etc/media_shima_v1/video_system_specs.json', 'vendor/etc/media_yupik_v1/video_system_specs.json'): blob_fixup()
        .regex_replace('"max_retry_alloc_output_timeout": 10000,', '"max_retry_alloc_output_timeout": 0,'),
    'vendor/etc/vintf/manifest/c2_manifest_vendor.xml': blob_fixup()
        .regex_replace('.*ozoaudio.*\n?', ''),
    ('vendor/lib64/mediadrm/libwvdrmengine.so', 'vendor/lib64/libwvhidl.so'): blob_fixup()
        .add_needed('libcrypto_shim.so'),
    'vendor/lib/libaudioroute_ext.so': blob_fixup()
        .replace_needed('libaudioroute.so', 'libaudioroute-v34.so'),
    'vendor/lib/hw/audio.primary.kona.so': blob_fixup()
        .replace_needed('libaudioroute.so', 'libaudioroute-v34.so'),
    'vendor/lib64/android.hardware.secure_element@1.0-impl.so': blob_fixup()
        .remove_needed('android.hidl.base@1.0.so'),
    'vendor/etc/camera/pureShot_parameter.xml': blob_fixup()
        .regex_replace(r'=(\d+)>', r'="\1">'),
    ('vendor/lib64/hw/camera.qcom.so', 'vendor/lib64/libFaceDetectpp-0.5.2.so', 'vendor/lib64/libfacedet.so'): blob_fixup()
        .binary_regex_replace(b'\x73\x74\x5F\x6C\x69\x63\x65\x6E\x73\x65\x2E\x6C\x69\x63', b'\x63\x61\x6D\x65\x72\x61\x5F\x63\x6E\x66\x2E\x74\x78\x74')
        .binary_regex_replace(b'libmegface.so', b'libfacedet.so')
        .binary_regex_replace(b'libMegviiFacepp-0.5.2.so', b'libFaceDetectpp-0.5.2.so')
        .binary_regex_replace(b'megviifacepp_0_5_2_model', b'facedetectpp_0_5_2_model')
        .add_needed('libprocessgroup_shim.so'),
    'vendor/lib64/hw/camera.xiaomi.so': blob_fixup()
        .sig_replace('5e 07 00 94', '1F 20 03 D5'),
    'vendor/lib64/hw/com.qti.chi.override.so': blob_fixup()
        .add_needed('libprocessgroup_shim.so'),
    ('vendor/lib64/libalAILDC.so', 'vendor/lib64/libalLDC.so', 'vendor/lib64/libalhLDC.so'): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    'vendor/lib64/libanc_dc_plugin_xiaomi_v2.so': blob_fixup()
        .add_needed('libc++_shared.so'),
    'vendor/lib64/libarcsoft_hdrplus_hvx_stub.so': blob_fixup()
        .clear_symbol_version('remote_handle_close')
        .clear_symbol_version('remote_handle_invoke')
        .clear_symbol_version('remote_handle_open'),
    ('vendor/lib64/libarcsoft_super_night_raw.so', 'vendor/lib64/libmialgo_pureShot.so', 'vendor/lib64/libmialgo_rfs.so'): blob_fixup()
        .clear_symbol_version('remote_handle64_close')
        .clear_symbol_version('remote_handle64_invoke')
        .clear_symbol_version('remote_handle64_open')
        .clear_symbol_version('remote_register_buf_attr')
        .clear_symbol_version('remote_session_control')
        .clear_symbol_version('rpcmem_alloc')
        .clear_symbol_version('rpcmem_free')
        .clear_symbol_version('rpcmem_to_fd'),
    'vendor/lib64/libmialgoengine.so': blob_fixup()
        .add_needed('libprocessgroup_shim.so'),
    'vendor/lib64/vendor.xiaomi.hardware.cameraperf@1.0-impl.so': blob_fixup()
        .sig_replace('21 00 80 52 7c 00 00 94', '21 00 80 52 1F 20 03 D5'),
    ('vendor/lib/c2.dolby.avc.dec.so', 'vendor/lib/c2.dolby.avc.sec.dec.so', 'vendor/lib/c2.dolby.hevc.dec.so', 'vendor/lib/c2.dolby.hevc.sec.dec.so'): blob_fixup()
        .add_needed('libstagefright_foundation-v33.so'),
    ('vendor/lib64/c2.dolby.avc.dec.so', 'vendor/lib64/c2.dolby.avc.sec.dec.so', 'vendor/lib64/c2.dolby.hevc.dec.so', 'vendor/lib64/c2.dolby.hevc.sec.dec.so'): blob_fixup()
        .add_needed('libstagefright_foundation-v33.so'),
    ('vendor/bin/hw/dolbycodec2'): blob_fixup()
        .add_needed('libstagefright_foundation-v33.so'),
    ('vendor/lib/c2.dolby.client.so', 'vendor/lib64/c2.dolby.client.so'): blob_fixup()
        .add_needed('libcodec2_hidl_shim.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'renoir',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
