

from whitenoise.storage import CompressedManifestStaticFilesStorage

class CustomStaticFilesStorage(CompressedManifestStaticFilesStorage):
    # sourcemap izlash patternini olib tashlash
    patterns = (
        ("*.css", (
            r'url\([^)]+\)',
        )),
        ("*.js", (
            r'//[ \t]*[#@][ \t]*sourceMappingURL=.*\.map',
        )),
    )