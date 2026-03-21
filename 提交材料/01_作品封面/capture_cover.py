# -*- coding: utf-8 -*-
"""Capture the cover HTML as a 1920x1080 PNG using Playwright."""
import os
from playwright.sync_api import sync_playwright

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(script_dir, "cover.html")
    output_path = os.path.join(script_dir, "\u4f5c\u54c1\u5c01\u9762.png")

    html_url = "file:///" + html_path.replace("\\", "/")

    print("HTML path: " + html_path)
    print("Output path: " + output_path)
    print("URL: " + html_url)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        print("Navigating to HTML file...")
        page.goto(html_url)
        page.wait_for_timeout(2000)

        print("Taking screenshot...")
        page.screenshot(path=output_path, full_page=False)

        browser.close()

    if os.path.exists(output_path):
        size_bytes = os.path.getsize(output_path)
        print("SUCCESS: Screenshot saved (" + str(size_bytes) + " bytes)")
    else:
        print("ERROR: Screenshot file not created")

if __name__ == "__main__":
    main()
