# -*- coding: utf-8 -*-
# @Time    : 2022/6/24 20:37
# @Author  : zhagnyunlong
# @File    : record01.py
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Click input[name="wd"]
    page.locator("input[name=\"wd\"]").click()

    # Fill input[name="wd"]
    page.locator('css=input[name="wd"]').fill("playwright")
    page.wait_for_timeout(5*1000)

    # Press Enter
    # with page.expect_navigation(url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=playwright&fenlei=256&rsv_pq=fd2ed98f000ef26b&rsv_t=2dc9wWtRlsTeB%2FojkU4HlljyV9gLd9AvVLtQ8GG2yaAT8qO0mf5GIsfA8d0&rqlang=cn&rsv_dl=tb&rsv_enter=1&rsv_sug3=11&rsv_sug1=10&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=playwright&rsp=5&inputT=7321&rsv_sug4=10199&rsv_jmp=fail"):
    with page.expect_navigation():
        page.locator("input[name=\"wd\"]").press("Enter")
    # expect(page).to_have_url("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=playwright&fenlei=256&rsv_pq=fd2ed98f000ef26b&rsv_t=2dc9wWtRlsTeB%2FojkU4HlljyV9gLd9AvVLtQ8GG2yaAT8qO0mf5GIsfA8d0&rqlang=cn&rsv_dl=tb&rsv_enter=1&rsv_sug3=11&rsv_sug1=10&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=playwright&rsp=5&inputT=7321&rsv_sug4=10199")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
