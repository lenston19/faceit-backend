"""Static settings"""

from .paths import PUBLIC_MEDIA_DIR, PUBLIC_STATIC_DIR, STATIC_DIR

STATIC_URL = "/static/"
STATIC_ROOT = PUBLIC_STATIC_DIR

STATICFILES_DIRS = [
    STATIC_DIR,
]

MEDIA_ROOT = PUBLIC_MEDIA_DIR
MEDIA_URL = "/media/"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
