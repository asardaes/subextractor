"""
Constants for subtitle extraction.
"""

FFMPEG_TEXT_FORMATS = (
    "arib_caption",
    "ass",
    "eia_608",
    "hdmv_text_subtitle",
    "jacosub",
    "microdvd",
    "mov_text",
    "mpl2",
    "pjs",
    "realtext",
    "sami",
    "srt",
    "ssa",
    "stl",
    "subrip",
    "subviewer",
    "subviewer1",
    "text",
    "ttml",
    "vplayer",
    "webvtt",
)

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
