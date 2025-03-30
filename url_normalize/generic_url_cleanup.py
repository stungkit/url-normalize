"""URL generic cleanup operations."""

from __future__ import annotations

import re


def generic_url_cleanup(url: str) -> str:
    """Cleanup the URL from unnecessary data and convert to final form.

    Converts shebang urls to final form, removed unnecessary data from the url.

    Params:
        url : string : the URL

    Returns:
        string : update url

    """
    url = url.replace("#!", "?_escaped_fragment_=")
    url = re.sub(r"utm_source=[^&]+&?", "", url)
    return url.rstrip("&? ")
