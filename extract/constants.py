"""
Constants for subtitle extraction.
"""

FFMPEG_TEXT_FORMATS = {
    "srt": ["srt", "subrip", "mov_text"],
    "ass": ["ass", "ssa"],
    "vtt": ["webvtt"],
    "ttml": ["ttml"],
}


FFMPEG_BITMAP_FORMATS = [
    "dvb_subtitle",
    "dvb_teletext",
    "dvd_subtitle",
    "hdmv_pgs_subtitle",
    "xsub",
]


SUPPORTED_SUBTITLE_FORMATS = (
    "ass",
    "srt",
    "vtt",
)

SUPPORTED_VIDEO_EXTENSION = (
    "mkv",
    "mp4",
    "m4v",
    "mov",
    "ts",
    "m2ts",
    "webm",
    "ogv",
    "avi",
)
