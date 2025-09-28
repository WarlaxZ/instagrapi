API_DOMAIN = "i.instagram.com"

# Instagram 134.0.0.26.121
# Android (26/8.0.0;
# 480dpi; 1080x1920; Xiaomi;
# MI 5s; capricorn; qcom; en_US; 205280538)
USER_AGENT_BASE = (
    "Instagram {app_version} "
    "Android ({android_version}/{android_release}; "
    "{dpi}; {resolution}; {manufacturer}; "
    "{model}; {device}; {cpu}; {locale}; {version_code})"
)
# Instagram 76.0.0.15.395 (iPhone9,2; iOS 10_0_2; en_US; en-US; scale=2.61; 1080x1920) AppleWebKit/420+
# Instagram 208.0.0.32.135 (iPhone; iOS 14_7_1; en_US; en-US; scale=2.61; 1080x1920) AppleWebKit/605.1.15

SOFTWARE = (
    "{model}-user+{android_release}+OPR1.170623.032+V10.2.3.0.OAGMIXM+release-keys"
)

# QUERY_HASH_PROFILE = 'c9100bf9110dd6361671f113dd02e7d6'
# QUERY_HASH_MEDIAS = '42323d64886122307be10013ad2dcc44'
# QUERY_HASH_IGTVS = 'bc78b344a68ed16dd5d7f264681c4c76'
# QUERY_HASH_STORIES = '5ec1d322b38839230f8e256e1f638d5f'
# QUERY_HASH_HIGHLIGHTS_FOLDERS = 'ad99dd9d3646cc3c0dda65debcd266a7'
# QUERY_HASH_HIGHLIGHTS_STORIES = '5ec1d322b38839230f8e256e1f638d5f'
# QUERY_HASH_FOLLOWERS = 'c76146de99bb02f6415203be841dd25a'
# QUERY_HASH_FOLLOWINGS = 'd04b0a864b4b54837c0d870b0e77e076'
# QUERY_HASH_HASHTAG = '174a5243287c5f3a7de741089750ab3b'
# QUERY_HASH_COMMENTS = '33ba35852cb50da46f5b5e889df7d159'
# QUERY_HASH_TAGGED_MEDIAS = 'be13233562af2d229b008d2976b998b5'

LOGIN_EXPERIMENTS = (
    "ig_android_reg_nux_headers_cleanup_universe,"
    "ig_android_device_detection_info_upload,"
    "ig_android_nux_add_email_device,"
    "ig_android_gmail_oauth_in_reg,"
    "ig_android_device_info_foreground_reporting,"
    "ig_android_device_verification_fb_signup,"
    "ig_android_direct_main_tab_universe_v2,"
    "ig_android_passwordless_account_password_creation_universe,"
    "ig_android_direct_add_direct_to_android_native_photo_share_sheet,"
    "ig_growth_android_profile_pic_prefill_with_fb_pic_2,"
    "ig_account_identity_logged_out_signals_global_holdout_universe,"
    "ig_android_quickcapture_keep_screen_on,"
    "ig_android_device_based_country_verification,"
    "ig_android_login_identifier_fuzzy_match,"
    "ig_android_reg_modularization_universe,"
    "ig_android_security_intent_switchoff,"
    "ig_android_device_verification_separate_endpoint,"
    "ig_android_suma_landing_page,"
    "ig_android_sim_info_upload,"
    "ig_android_smartlock_hints_universe,"
    "ig_android_fb_account_linking_sampling_freq_universe,"
    "ig_android_retry_create_account_universe,"
    "ig_android_caption_typeahead_fix_on_o_universe"
)

SUPPORTED_CAPABILITIES = [
    {
        "value": (
            "119.0,120.0,121.0,122.0,123.0,124.0,125.0,126.0,127.0,128.0,"
            "129.0,130.0,131.0,132.0,133.0,134.0,135.0,136.0,137.0,138.0,"
            "139.0,140.0,141.0,142.0"
        ),
        "name": "SUPPORTED_SDK_VERSIONS",
    },
    {"value": "14", "name": "FACE_TRACKER_VERSION"},
    {"value": "ETC2_COMPRESSION", "name": "COMPRESSION"},
    {"value": "gyroscope_enabled", "name": "gyroscope"},
]

# Realistic device profiles with proper correlations
app_version = "399.0.0.51.85" # TODO I added, was 269.0.0.18.75
# TODO TODO - The version strings and devices are wrong here and could do with improving
REALISTIC_DEVICES = [
    {
        "app_version": app_version,
        "android_version": 31,
        "android_release": "12",
        "dpi": "420dpi",
        "resolution": "1080x2400",
        "manufacturer": "Samsung",
        "device": "SM-G991B",
        "model": "Galaxy S21 5G",
        "cpu": "exynos2100",
        "version_code": "314665256",
    },
    {
        "app_version": app_version,
        "android_version": 32,
        "android_release": "12L",
        "dpi": "411dpi",
        "resolution": "1080x2340",
        "manufacturer": "Google",
        "device": "oriole",
        "model": "Pixel 6",
        "cpu": "tensor",
        "version_code": "314665256",
    },
    {
        "app_version": app_version,
        "android_version": 30,
        "android_release": "11",
        "dpi": "440dpi",
        "resolution": "1080x2340",
        "manufacturer": "OnePlus",
        "device": "OnePlus9",
        "model": "LE2113",
        "cpu": "snapdragon888",
        "version_code": "314665256",
    },
    {
        "app_version": app_version,
        "android_version": 29,
        "android_release": "10",
        "dpi": "393dpi",
        "resolution": "1080x2280",
        "manufacturer": "Xiaomi",
        "device": "cmi",
        "model": "Mi 10",
        "cpu": "snapdragon865",
        "version_code": "314665256",
    },
    {
        "app_version": app_version,
        "android_version": 31,
        "android_release": "12",
        "dpi": "420dpi",
        "resolution": "1080x2400",
        "manufacturer": "Samsung",
        "device": "SM-A525F",
        "model": "Galaxy A52s 5G",
        "cpu": "snapdragon778G",
        "version_code": "314665256",
    },
    {
        "app_version": app_version,
        "android_version": 31,
        "android_release": "12",
        "dpi": "401dpi",
        "resolution": "1080x2400",
        "manufacturer": "Oppo",
        "device": "OP4F2F",
        "model": "Find X3 Pro",
        "cpu": "snapdragon888",
        "version_code": "314665256",
    },
    {
        "app_version": app_version,
        "android_version": 30,
        "android_release": "11",
        "dpi": "440dpi",
        "resolution": "1080x2400",
        "manufacturer": "Huawei",
        "device": "ELS-NX9",
        "model": "P40 Pro",
        "cpu": "kirin990",
        "version_code": "314665256",
    },
    {
        "app_version": app_version,
        "android_version": 29,
        "android_release": "10",
        "dpi": "420dpi",
        "resolution": "1080x2340",
        "manufacturer": "Sony",
        "device": "XQ-AT52",
        "model": "Xperia 1 II",
        "cpu": "snapdragon865",
        "version_code": "314665256",
    },
    {
        "app_version": app_version,
        "android_version": 31,
        "android_release": "12",
        "dpi": "480dpi",
        "resolution": "1080x2460",
        "manufacturer": "Realme",
        "device": "RMX3366",
        "model": "GT Master Edition",
        "cpu": "snapdragon778G",
        "version_code": "314665256",
    },
    {
        "app_version": app_version,
        "android_version": 30,
        "android_release": "11",
        "dpi": "440dpi",
        "resolution": "1080x2400",
        "manufacturer": "Vivo",
        "device": "V2057",
        "model": "X60 Pro",
        "cpu": "exynos1080",
        "version_code": "314665256",
    },
    {
        "app_version": app_version,
        "android_version": 32,
        "android_release": "12L",
        "dpi": "420dpi",
        "resolution": "1080x2400",
        "manufacturer": "Nothing",
        "device": "Spacewar",
        "model": "Phone (1)",
        "cpu": "snapdragon778G",
        "version_code": "314665256",
    },
    {
        "app_version": app_version,
        "android_version": 31,
        "android_release": "12",
        "dpi": "440dpi",
        "resolution": "1080x2412",
        "manufacturer": "Motorola",
        "device": "nio",
        "model": "Edge 20 Pro",
        "cpu": "snapdragon870",
        "version_code": "314665256",
    },
]

# Geographic regions with timezone data
GEOGRAPHIC_REGIONS = {
    "US": {
        "country": "US",
        "country_code": 1,
        "locale": "en_US",
        "timezone_offsets": [-28800, -25200, -21600, -18000, -14400],  # PST, MST, CST, EST, AST
        "languages": ["en-US"],
    },
    "GB": {
        "country": "GB",
        "country_code": 44,
        "locale": "en_GB",
        "timezone_offsets": [0, 3600],  # GMT, BST
        "languages": ["en-GB"],
    },
    "DE": {
        "country": "DE",
        "country_code": 49,
        "locale": "de_DE",
        "timezone_offsets": [3600, 7200],  # CET, CEST
        "languages": ["de-DE", "en-US"],
    },
    "FR": {
        "country": "FR",
        "country_code": 33,
        "locale": "fr_FR",
        "timezone_offsets": [3600, 7200],  # CET, CEST
        "languages": ["fr-FR", "en-US"],
    },
    "CA": {
        "country": "CA",
        "country_code": 1,
        "locale": "en_CA",
        "timezone_offsets": [-28800, -25200, -21600, -18000, -14400, -12600],
        "languages": ["en-CA", "fr-CA"],
    },
    "AU": {
        "country": "AU",
        "country_code": 61,
        "locale": "en_AU",
        "timezone_offsets": [28800, 32400, 34200, 36000, 37800, 39600],
        "languages": ["en-AU"],
    },
}

# Connection types with realistic bandwidth ranges (kbps)
CONNECTION_TYPES = {
    "WIFI": {
        "bandwidth_range": (15000, 100000),
        "latency_range": (1, 15),
        "total_bytes_range": (50000000, 500000000),
        "total_time_range": (5000, 30000),
    },
    "4G": {
        "bandwidth_range": (5000, 50000),
        "latency_range": (20, 80),
        "total_bytes_range": (10000000, 100000000),
        "total_time_range": (8000, 45000),
    },
    "5G": {
        "bandwidth_range": (50000, 300000),
        "latency_range": (1, 10),
        "total_bytes_range": (100000000, 800000000),
        "total_time_range": (2000, 15000),
    },
}
