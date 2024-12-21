def on_page_markdown(markdown, page, config, files):
    if "hide" in page.meta:
        if "toc" not in page.meta["hide"]:
            page.meta["hide"].append("toc")
    else:
        page.meta["hide"] = ["toc"]
    return markdown
