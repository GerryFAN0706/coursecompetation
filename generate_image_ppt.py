from pathlib import Path
from datetime import datetime
import math
import shutil
import zipfile

from PIL import Image, ImageDraw, ImageFont, ImageFilter


BASE = Path(__file__).resolve().parent
OUT = BASE / "省赛现场答辩PPT_图片版"
SLIDES = OUT / "slides"
SLIDES.mkdir(parents=True, exist_ok=True)

W, H = 1920, 1080
BLUE = (24, 92, 198)
BLUE2 = (47, 125, 236)
DARK = (22, 38, 65)
MID = (75, 92, 122)
CYAN = (25, 184, 210)
GREEN = (40, 174, 118)
ORANGE = (245, 145, 50)
RED = (222, 73, 92)
PURPLE = (115, 94, 222)

FONT_REG = r"C:\Windows\Fonts\msyh.ttc"
FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"
FONT_LIGHT = r"C:\Windows\Fonts\msyhl.ttc"


def font(size, bold=False, light=False):
    path = FONT_BOLD if bold else (FONT_LIGHT if light else FONT_REG)
    return ImageFont.truetype(path, size)


F = {
    "cover_title": font(72, True),
    "title": font(48, True),
    "body": font(26),
    "body_b": font(26, True),
    "small": font(21),
    "small_b": font(21, True),
    "tiny": font(17),
    "num2": font(46, True),
}


def text_size(draw, text, ft):
    box = draw.textbbox((0, 0), str(text), font=ft)
    return box[2] - box[0], box[3] - box[1]


def wrap_text(draw, text, ft, max_width):
    lines = []
    for para in str(text).split("\n"):
        if not para:
            lines.append("")
            continue
        cur = ""
        for ch in para:
            test = cur + ch
            if text_size(draw, test, ft)[0] <= max_width:
                cur = test
            else:
                if cur:
                    lines.append(cur)
                cur = ch
        if cur:
            lines.append(cur)
    return lines


def draw_text(draw, xy, text, ft, fill=DARK, max_width=None, line_spacing=1.18, align="left"):
    x, y = xy
    if max_width is None:
        draw.text((x, y), text, font=ft, fill=fill)
        return y + text_size(draw, text, ft)[1]
    yy = y
    for line in wrap_text(draw, text, ft, max_width):
        if align == "center":
            tw, _ = text_size(draw, line, ft)
            xx = x + (max_width - tw) // 2
        else:
            xx = x
        draw.text((xx, yy), line, font=ft, fill=fill)
        yy += int(ft.size * line_spacing)
    return yy


def shadowed_card(im, box, radius=28, fill=(255, 255, 255), outline=(226, 235, 249), shadow=True):
    if shadow:
        sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
        sd = ImageDraw.Draw(sh)
        x0, y0, x1, y1 = box
        sd.rounded_rectangle((x0, y0 + 8, x1, y1 + 8), radius=radius, fill=(21, 75, 170, 36))
        sh = sh.filter(ImageFilter.GaussianBlur(18))
        im.alpha_composite(sh)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=2)


def draw_pill(draw, xy, text, color=BLUE, ft=None, pad=(12, 6)):
    if ft is None:
        ft = F["tiny"]
    x, y = xy
    tw, th = text_size(draw, text, ft)
    bg = tuple(min(255, int(c * 0.12 + 255 * 0.88)) for c in color)
    draw.rounded_rectangle((x, y, x + tw + pad[0] * 2, y + th + pad[1] * 2), radius=18, fill=bg, outline=color)
    draw.text((x + pad[0], y + pad[1] - 2), text, font=ft, fill=color)


def arrow(draw, p1, p2, color=BLUE, width=5, head=16):
    x1, y1 = p1
    x2, y2 = p2
    draw.line((x1, y1, x2, y2), fill=color, width=width)
    ang = math.atan2(y2 - y1, x2 - x1)
    pts = []
    for a in [ang + math.pi * 0.82, ang - math.pi * 0.82]:
        pts.append((x2 + head * math.cos(a), y2 + head * math.sin(a)))
    draw.polygon([(x2, y2), pts[0], pts[1]], fill=color)


def base_slide(title=None, section=None, n=None):
    im = Image.new("RGBA", (W, H), "white")
    d = ImageDraw.Draw(im)
    for i in range(8):
        d.arc((W - 620 - i * 12, -120 + i * 4, W + 120, 360 + i * 18), 190, 315, fill=(221, 235, 255, 95), width=2)
    d.rectangle((0, 0, W, 8), fill=BLUE)
    d.rectangle((0, H - 10, W, H), fill=(232, 241, 255))
    if title:
        d.text((78, 42), title, font=F["title"], fill=BLUE)
        d.line((78, 110, 560, 110), fill=BLUE2, width=5)
        if section:
            draw_pill(d, (78, 122), section, color=BLUE)
        if n is not None:
            d.text((W - 120, 52), f"{n:02d}", font=font(34, True), fill=(185, 205, 236))
    return im


def draw_footer(im, conclusion):
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((70, 1005, 1850, 1050), radius=20, fill=(238, 246, 255), outline=(210, 228, 250))
    d.ellipse((88, 1018, 104, 1034), fill=BLUE)
    draw_text(d, (122, 1014), conclusion, F["small_b"], fill=BLUE, max_width=1660)


def paste_img(im, path, box, radius=22, label=None, crop=False):
    p = Path(path)
    if not p.exists():
        return
    src = Image.open(p).convert("RGBA")
    x0, y0, x1, y1 = box
    bw, bh = x1 - x0, y1 - y0
    if crop:
        src_ratio = src.width / src.height
        dst_ratio = bw / bh
        if src_ratio > dst_ratio:
            new_w = int(src.height * dst_ratio)
            left = (src.width - new_w) // 2
            src = src.crop((left, 0, left + new_w, src.height))
        else:
            new_h = int(src.width / dst_ratio)
            top = (src.height - new_h) // 2
            src = src.crop((0, top, src.width, top + new_h))
    src.thumbnail((bw, bh), Image.LANCZOS)
    tmp = Image.new("RGBA", (bw, bh), (255, 255, 255, 0))
    tmp.alpha_composite(src, ((bw - src.width) // 2, (bh - src.height) // 2))
    mask = Image.new("L", (bw, bh), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((0, 0, bw, bh), radius=radius, fill=255)
    im.alpha_composite(Image.composite(tmp, Image.new("RGBA", (bw, bh), (255, 255, 255, 0)), mask), (x0, y0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(box, radius=radius, outline=(220, 232, 248), width=2)
    if label:
        tw, _ = text_size(d, label, F["tiny"])
        d.rounded_rectangle((x0 + 16, y0 + 16, x0 + 40 + tw, y0 + 48), radius=13, fill=(255, 255, 255, 225), outline=(219, 232, 250))
        d.text((x0 + 28, y0 + 22), label, font=F["tiny"], fill=BLUE)


shots = BASE / "提交材料" / "05_AI赛道证明材料_匿名版" / "screenshots"
slide_paths = []


def save(im, idx):
    p = SLIDES / f"slide_{idx:02d}.png"
    im.convert("RGB").save(p, quality=96)
    slide_paths.append(p)


def make_slides():
    # 1
    im = Image.new("RGBA", (W, H), "white")
    d = ImageDraw.Draw(im)
    for i in range(16):
        d.arc((W - 850 - i * 18, 70 + i * 6, W + 160, 850 + i * 20), 185, 320, fill=(216, 233, 255, 110), width=2)
    for x, y, r, c in [(1460, 290, 88, BLUE), (1640, 455, 48, CYAN), (1390, 610, 38, ORANGE), (1735, 670, 66, GREEN)]:
        d.ellipse((x - r, y - r, x + r, y + r), outline=(*c, 65), width=3)
        d.ellipse((x - 8, y - 8, x + 8, y + 8), fill=(*c, 155))
    d.rectangle((0, 0, W, 10), fill=BLUE)
    d.text((90, 170), "数据驱动 · 人机协同 · 责任导向", font=font(44, True), fill=BLUE)
    d.text((90, 258), "Web应用开发课程", font=F["cover_title"], fill=DARK)
    d.text((90, 350), "AI赋能教学创新实践", font=F["cover_title"], fill=BLUE)
    d.line((90, 455, 750, 455), fill=BLUE2, width=6)
    draw_text(d, (90, 500), "第六届全国高校教师教学创新大赛 · 人工智能赛道\n现场答辩汇报", font(30), fill=MID, max_width=1000, line_spacing=1.45)
    for i, (t, sub, c) in enumerate([("真问题", "回应编程实践教学真实断点", BLUE), ("真融入", "贯穿课前·课中·课后", GREEN), ("真成效", "多源数据验证能力变化", ORANGE)]):
        x, y = 90 + i * 360, 705
        shadowed_card(im, (x, y, x + 320, y + 150), radius=28)
        d = ImageDraw.Draw(im)
        d.text((x + 28, y + 28), t, font=font(34, True), fill=c)
        draw_text(d, (x + 28, y + 78), sub, F["small"], fill=MID, max_width=260)
    d.text((90, 990), "AI不是课堂点缀，而是课程目标、教学过程、评价方式和育人路径的系统重构", font=font(28, True), fill=BLUE)
    save(im, 1)

    # 2
    im = base_slide("课程目标升级：为什么这门课需要AI重构", "观点页 · 课程逻辑起点", 2)
    d = ImageDraw.Draw(im)
    d.text((120, 190), "从“会写代码”", font=font(42, True), fill=(120, 132, 152))
    d.text((1410, 190), "到“会负责地开发系统”", font=font(42, True), fill=BLUE)
    arrow(d, (610, 220), (1280, 220), color=BLUE2, width=8, head=28)
    d.text((760, 165), "AI时代课程目标升级", font=font(30, True), fill=BLUE)
    left = [("完成功能代码", "页面能打开、功能能运行"), ("掌握孤立知识点", "Servlet / Session / Filter 分散学习"), ("独立完成实验", "统一题目、统一路径"), ("只看最终代码", "忽略过程、协作与AI使用")]
    right = [("安全可信开发", "关注权限、数据、安全与可维护性"), ("真实问题迁移", "在漏洞、项目、调试中调用知识"), ("人机协同判断", "会提问、会质疑、会验证AI"), ("多维过程评价", "功能·规范·安全·协作·AI素养")]
    for i in range(4):
        y = 310 + i * 145
        shadowed_card(im, (100, y, 820, y + 105), radius=24, fill=(248, 250, 253), shadow=False, outline=(226, 231, 240))
        shadowed_card(im, (1100, y, 1820, y + 105), radius=24, fill=(245, 250, 255), outline=(196, 220, 250))
        d = ImageDraw.Draw(im)
        d.text((135, y + 22), left[i][0], font=font(26, True), fill=(92, 103, 122))
        d.text((135, y + 62), left[i][1], font=F["small"], fill=(128, 139, 156))
        d.text((1135, y + 22), right[i][0], font=font(28, True), fill=BLUE)
        d.text((1135, y + 62), right[i][1], font=F["small"], fill=MID)
        arrow(d, (840, y + 52), (1070, y + 52), color=(163, 196, 240), width=4, head=14)
    draw_footer(im, "课程目标升级，是AI融入课程的逻辑起点。")
    save(im, 2)

    # 3
    im = base_slide("真实挑战：传统教学难以支撑新目标", "矛盾页 · 先讲论点，再给证据", 3)
    d = ImageDraw.Draw(im)
    shadowed_card(im, (360, 185, 1560, 355), radius=34, fill=(248, 251, 255), outline=(204, 224, 252))
    d = ImageDraw.Draw(im)
    draw_text(d, (430, 220), "课程目标已经升级，但传统教学流程仍停留在\n统一任务、滞后反馈、结果评价", font(42, True), fill=DARK, max_width=1060, line_spacing=1.2, align="center")
    d.text((770, 322), "→ 无法支撑AI时代工程实践能力培养", font=font(30, True), fill=RED)
    items = [
        ("真实能力不可见", "代码同质 + 团队贡献不可见", "45.2% MOSS相似度", BLUE, (220, 500)),
        ("学习反馈不及时", "批改滞后 + 个性化支持不足", "32.8min/份", ORANGE, (810, 500)),
        ("工程/AI素养不足", "安全意识弱 + 盲信AI输出", "12.1% SQL注入识别率", GREEN, (1400, 500)),
    ]
    for title, desc, num, c, (cx, cy) in items:
        d.ellipse((cx - 145, cy - 145, cx + 145, cy + 145), fill=tuple(int(v * 0.12 + 255 * 0.88) for v in c), outline=c, width=4)
        d.text((cx - 95, cy - 72), title, font=font(28, True), fill=c)
        draw_text(d, (cx - 105, cy - 25), desc, F["small"], fill=DARK, max_width=210, align="center")
        d.rounded_rectangle((cx - 116, cy + 68, cx + 116, cy + 112), radius=18, fill="white", outline=c, width=2)
        tw, _ = text_size(d, num, F["small_b"])
        d.text((cx - tw // 2, cy + 77), num, font=F["small_b"], fill=c)
    arrow(d, (505, 500), (665, 500), color=(182, 205, 236), width=3, head=10)
    arrow(d, (955, 500), (1255, 500), color=(182, 205, 236), width=3, head=10)
    draw_footer(im, "这页不是数据盘点，而是说明：必须重构课程流程，才能支撑新的能力目标。")
    save(im, 3)

    # 4
    im = base_slide("总体设计：16讲持续迭代的AI教学闭环", "架构页 · 课程级设计", 4)
    d = ImageDraw.Draw(im)
    stages = [("第N讲课前", "WebDev学情诊断\nTeamCoach周报\n个性化任务生成", BLUE), ("第N讲课中", "WebSec闯关\nCode Review Battle\n教师即时干预", GREEN), ("第N讲课后", "AI代码审查\n个性化反馈\nGit过程追踪", ORANGE), ("第N+1讲课前", "数据回流\n调整重点\n关注特定学生", PURPLE)]
    xs, y = [95, 555, 1015, 1475], 325
    for i, (tit, body, c) in enumerate(stages):
        shadowed_card(im, (xs[i], y, xs[i] + 350, y + 250), radius=32, outline=tuple(int(v * 0.35 + 255 * 0.65) for v in c))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((xs[i] + 22, y + 24, xs[i] + 152, y + 64), radius=18, fill=tuple(int(v * 0.15 + 255 * 0.85) for v in c), outline=c, width=1)
        d.text((xs[i] + 40, y + 31), tit, font=F["small_b"], fill=c)
        draw_text(d, (xs[i] + 35, y + 90), body, font(28, True), fill=DARK, max_width=280, line_spacing=1.35)
        if i < 3:
            arrow(d, (xs[i] + 365, y + 125), (xs[i + 1] - 20, y + 125), color=BLUE2, width=5, head=20)
    arrow(d, (1650, 610), (260, 610), color=(151, 184, 230), width=5, head=22)
    d.text((720, 635), "课后数据回流，驱动下一讲教学调整", font=font(30, True), fill=BLUE)
    d.rounded_rectangle((210, 760, 1710, 900), radius=28, fill=(242, 248, 255), outline=(205, 224, 248), width=2)
    d.text((250, 790), "关键设计", font=font(30, True), fill=BLUE)
    draw_text(d, (410, 785), "每一讲都产生数据，每一次数据都改变下一次教学设计；16讲形成持续改进链，而不是单节课展示。", font(30), fill=DARK, max_width=1220, line_spacing=1.3)
    draw_footer(im, "AI不是替代教师和学生，而是让教师看见过程、让学生获得即时反馈、让课程持续改进。")
    save(im, 4)

    # 5
    im = base_slide("三个重构：AI到底重构了什么", "原理页 · 不讲工具功能，讲教学变化", 5)
    d = ImageDraw.Draw(im)
    panels = [("内容重构", "安全开发\nAI协作\n工程伦理", "把权限控制、漏洞修复、人机审查纳入核心任务", BLUE), ("方法重构", "发现问题\n判断建议\n修复验证", "从教师示范转向学生借助AI完成问题解决", GREEN), ("评价重构", "功能\n规范\n安全\n协作\nAI素养", "从最终代码评价转向多维过程评价", ORANGE)]
    for i, (tit, keywords, desc, c) in enumerate(panels):
        x, y = 120 + i * 590, 240
        shadowed_card(im, (x, y, x + 500, y + 570), radius=34, outline=tuple(int(v * 0.45 + 255 * 0.55) for v in c))
        d = ImageDraw.Draw(im)
        d.ellipse((x + 45, y + 45, x + 125, y + 125), fill=tuple(int(v * 0.13 + 255 * 0.87) for v in c), outline=c, width=3)
        d.text((x + 150, y + 55), tit, font=font(36, True), fill=c)
        yy = y + 160
        for k in keywords.split("\n"):
            d.rounded_rectangle((x + 60, yy, x + 440, yy + 48), radius=18, fill=tuple(int(v * 0.1 + 255 * 0.9) for v in c), outline=(230, 238, 250))
            d.text((x + 90, yy + 9), k, font=font(24, True), fill=DARK)
            yy += 64
        d.line((x + 60, y + 440, x + 440, y + 440), fill=(220, 230, 245), width=2)
        draw_text(d, (x + 60, y + 462), desc, F["body"], fill=MID, max_width=390, line_spacing=1.25)
    d.text((120, 865), "评委要记住：创新点不在工具数量，而在课程关键要素被系统改变。", font=font(34, True), fill=RED)
    draw_footer(im, "AI推动教学内容、方法和评价整体重构。")
    save(im, 5)

    # 6
    im = base_slide("五维工具体系：每个工具对应一个教学断点", "系统页 · 工具地图", 6)
    d = ImageDraw.Draw(im)
    center = (960, 525)
    d.ellipse((760, 325, 1160, 725), fill=(244, 249, 255), outline=BLUE, width=5)
    draw_text(d, (825, 440), "AI赋能\nWeb实践教学\n闭环", font(38, True), fill=BLUE, max_width=270, align="center", line_spacing=1.18)
    tools = [("WebDev助教", "学情不可见", "课前/课后", BLUE, (320, 240)), ("AI资料重构", "任务同质", "课前", CYAN, (1240, 240)), ("WebSec挑战", "安全意识弱", "课中/课后", GREEN, (1450, 600)), ("Code Review Battle", "盲信AI", "课中", PURPLE, (710, 780)), ("TeamCoach", "团队贡献不可见", "课前/课后", ORANGE, (160, 600))]
    for name, problem, pos, c, (x, y) in tools:
        shadowed_card(im, (x, y, x + 360, y + 140), radius=26, outline=tuple(int(v * 0.45 + 255 * 0.55) for v in c))
        d = ImageDraw.Draw(im)
        d.text((x + 28, y + 22), name, font=font(27, True), fill=c)
        d.text((x + 28, y + 63), f"补断点：{problem}", font=F["small_b"], fill=DARK)
        d.text((x + 28, y + 96), f"嵌入：{pos}", font=F["small"], fill=MID)
        arrow(d, (x + 180, y + 70), (center[0] + (x + 180 - center[0]) * 0.62, center[1] + (y + 70 - center[1]) * 0.62), color=(185, 210, 240), width=3, head=10)
    draw_footer(im, "五个工具不是并列堆放，而是分别补上教学流程中的关键断点，最终回到学生能力发展。")
    save(im, 6)

    # 7
    im = base_slide("第十五讲：整门课程闭环的集中样例", "故事场景页 · 课堂案例", 7)
    d = ImageDraw.Draw(im)
    d.text((120, 180), "能登录", font=font(64, True), fill=DARK)
    d.text((350, 180), "≠", font=font(70, True), fill=RED)
    d.text((450, 180), "能安全控制访问", font=font(64, True), fill=BLUE)
    d.text((120, 265), "以“普通用户误入后台”为真实问题，组织认证、授权、Session、Filter、RBAC的综合学习。", font=font(30), fill=MID)
    cards = [("01 问题暴露", "普通用户 tom 登录后\n也能进入管理后台", RED), ("02 AI诊断", "候选问题：缺少角色检查\nFilter白名单/Session处理风险", ORANGE), ("03 学生验证", "补充RBAC过滤器\n普通用户返回403，管理员放行", GREEN)]
    for i, (tit, body, c) in enumerate(cards):
        x, y = 110 + i * 600, 420
        shadowed_card(im, (x, y, x + 520, y + 390), radius=32, outline=tuple(int(v * 0.45 + 255 * 0.55) for v in c))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((x + 30, y + 28, x + 205, y + 68), radius=16, fill=tuple(int(v * 0.15 + 255 * 0.85) for v in c), outline=c)
        d.text((x + 48, y + 35), tit, font=F["small_b"], fill=c)
        d.rounded_rectangle((x + 42, y + 105, x + 478, y + 240), radius=14, fill=(248, 250, 254), outline=(220, 230, 246))
        d.rectangle((x + 42, y + 105, x + 478, y + 135), fill=(232, 240, 254))
        if i == 0:
            d.text((x + 70, y + 158), "/admin/panel", font=font(25, True), fill=RED)
            d.rounded_rectangle((x + 70, y + 198, x + 315, y + 225), radius=10, fill=(255, 237, 239), outline=RED)
            d.text((x + 82, y + 202), "USER 也可访问后台", font=F["tiny"], fill=RED)
        elif i == 1:
            for j, t in enumerate(["权限检查缺失", "仅判断已登录", "未验证 user.role"]):
                d.rounded_rectangle((x + 70, y + 148 + j * 32, x + 380, y + 174 + j * 32), radius=10, fill=(255, 245, 235), outline=ORANGE)
                d.text((x + 84, y + 151 + j * 32), t, font=F["tiny"], fill=DARK)
        else:
            d.text((x + 70, y + 158), "HTTP 403", font=font(34, True), fill=GREEN)
            d.rounded_rectangle((x + 70, y + 205, x + 360, y + 232), radius=10, fill=(235, 250, 244), outline=GREEN)
            d.text((x + 82, y + 209), "角色校验生效", font=F["tiny"], fill=GREEN)
        draw_text(d, (x + 45, y + 268), body, F["body_b"], fill=DARK, max_width=430, line_spacing=1.32)
        if i < 2:
            arrow(d, (x + 535, y + 195), (x + 580, y + 195), color=BLUE2, width=5, head=18)
    draw_footer(im, "第十五讲不是单独展示的一节课，而是整门课程AI赋能闭环的缩影。")
    save(im, 7)

    # 8
    im = base_slide("第十五讲课前：AI让备课从“凭经验”变成“看数据”", "决策页 · 数据改变教学", 8)
    d = ImageDraw.Draw(im)
    steps = [("课前3天", "WebDev发布预习问题\n学生自主提问"), ("课前1天", "AI汇总热力图\n识别高频薄弱点"), ("上课当天", "教师调整重难点\n关注特定学生")]
    for i, (tit, body) in enumerate(steps):
        x, y = 95 + i * 430, 210
        shadowed_card(im, (x, y, x + 350, y + 160), radius=25, outline=(205, 224, 250))
        d = ImageDraw.Draw(im)
        d.text((x + 28, y + 25), tit, font=font(27, True), fill=BLUE)
        draw_text(d, (x + 28, y + 72), body, F["small_b"], fill=DARK, max_width=290, line_spacing=1.35)
        if i < 2:
            arrow(d, (x + 365, y + 80), (x + 420, y + 80), color=BLUE2, width=4, head=15)
    stats = [("42/58", "参与学生"), ("72.4%", "课前参与率"), ("8→15min", "Session安全讲授调整")]
    for i, (num, label) in enumerate(stats):
        x, y = 110 + i * 320, 440
        d.rounded_rectangle((x, y, x + 270, y + 110), radius=26, fill=(244, 249, 255), outline=(202, 224, 250), width=2)
        d.text((x + 28, y + 18), num, font=F["num2"], fill=BLUE if i < 2 else ORANGE)
        d.text((x + 30, y + 73), label, font=F["small_b"], fill=MID)
    paste_img(im, shots / "shot_03_webdev_teacher.png", (1120, 205, 1815, 710), radius=26, label="WebDev助教教师端 · 学情看板", crop=True)
    shadowed_card(im, (110, 790, 1810, 930), radius=28, outline=(215, 230, 250))
    d = ImageDraw.Draw(im)
    d.text((150, 823), "教学决策改变", font=font(32, True), fill=BLUE)
    draw_text(d, (380, 820), "AI不是只“采集学情”，而是让教师据真实数据调整课堂重点：认证概念压缩，Session安全与角色权限控制强化。", font(29), fill=DARK, max_width=1340, line_spacing=1.25)
    draw_footer(im, "AI的价值首先体现在教学决策：教师不是凭经验备课，而是依据学生真实数据调整重点。")
    save(im, 8)

    # 9
    im = base_slide("第十五讲课中：学生在“发现-判断-修复-验证”中学习", "过程页 · 人机协同课堂", 9)
    d = ImageDraw.Draw(im)
    nodes = [("漏洞演示", "普通用户进入后台", RED), ("WebSec闯关", "AI生成越权代码", GREEN), ("人工审查", "学生先独立找问题", BLUE), ("AI审查", "生成候选问题", PURPLE), ("对比辩论", "采纳/拒绝/说明理由", ORANGE), ("代码修复", "补Filter角色检查", BLUE), ("测试验证", "USER 403 / ADMIN 放行", GREEN)]
    start_x, y, gap = 90, 270, 250
    for i, (tit, body, c) in enumerate(nodes):
        x = start_x + i * gap
        d.ellipse((x, y, x + 105, y + 105), fill=tuple(int(v * 0.14 + 255 * 0.86) for v in c), outline=c, width=3)
        label = str(i + 1).zfill(2)
        tw, _ = text_size(d, label, font(26, True))
        d.text((x + 52 - tw / 2, y + 28), label, font=font(26, True), fill=c)
        d.text((x - 20, y + 125), tit, font=font(24, True), fill=c)
        draw_text(d, (x - 45, y + 160), body, F["tiny"], fill=MID, max_width=180, align="center")
        if i < len(nodes) - 1:
            arrow(d, (x + 112, y + 52), (x + gap - 10, y + 52), color=(170, 200, 238), width=4, head=14)
    paste_img(im, shots / "shot_05_websec_main.png", (120, 590, 640, 890), radius=24, label="WebSec挑战 · 越权访问关", crop=True)
    paste_img(im, shots / "shot_15_codereview_compare.png", (700, 590, 1220, 890), radius=24, label="Code Review Battle · 人机对比", crop=True)
    paste_img(im, shots / "shot_16_codereview_code.png", (1280, 590, 1800, 890), radius=24, label="代码审查与讨论材料", crop=True)
    draw_footer(im, "AI输出不是标准答案，而是学生讨论、质疑和验证的材料。")
    save(im, 9)

    # 10
    im = base_slide("第十五讲课后：反馈、迭代与数据回流", "证据页 · 二次学习", 10)
    d = ImageDraw.Draw(im)
    chain = [("AI反馈", "问题位置\n风险说明\n对应知识点"), ("学生修改", "二次提交\n解释采纳理由"), ("测试验证", "T1-T5测试\n证明修复有效"), ("数据回流", "进入下讲\n精准干预")]
    for i, (tit, body) in enumerate(chain):
        x, y = 90 + i * 440, 190
        shadowed_card(im, (x, y, x + 330, y + 140), radius=25, outline=(210, 228, 250))
        d = ImageDraw.Draw(im)
        d.text((x + 26, y + 20), tit, font=font(28, True), fill=BLUE if i % 2 == 0 else GREEN)
        draw_text(d, (x + 26, y + 62), body, F["small_b"], fill=DARK, max_width=270, line_spacing=1.18)
        if i < 3:
            arrow(d, (x + 345, y + 70), (x + 425, y + 70), color=BLUE2, width=4, head=15)
    shadowed_card(im, (120, 430, 890, 815), radius=30, outline=(230, 236, 248))
    shadowed_card(im, (1030, 430, 1800, 815), radius=30, outline=(230, 236, 248))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((150, 460, 360, 500), radius=16, fill=(255, 238, 240), outline=RED)
    d.text((170, 467), "修改前", font=F["small_b"], fill=RED)
    d.rounded_rectangle((1060, 460, 1270, 500), radius=16, fill=(235, 250, 244), outline=GREEN)
    d.text((1080, 467), "修改后", font=F["small_b"], fill=GREEN)
    code_font = font(23)
    before = 'if (session != null) {\n    session.removeAttribute(\"user\");\n}\n\nif (isLoggedIn) {\n    chain.doFilter(req, res);\n}'
    after = 'if (session != null) {\n    session.invalidate();\n}\n\nif (user != null &&\n    \"ADMIN\".equals(user.getRole())) {\n    chain.doFilter(req, res);\n} else { response.sendError(403); }'
    d.rounded_rectangle((160, 535, 850, 775), radius=18, fill=(248, 250, 253), outline=(225, 232, 243))
    d.rounded_rectangle((1070, 535, 1760, 775), radius=18, fill=(248, 250, 253), outline=(225, 232, 243))
    draw_text(d, (190, 560), before, code_font, fill=(80, 91, 110), max_width=620, line_spacing=1.35)
    draw_text(d, (1100, 560), after, code_font, fill=(46, 91, 78), max_width=630, line_spacing=1.35)
    arrow(d, (910, 625), (1010, 625), color=BLUE2, width=7, head=24)
    d.text((760, 860), "不给完整代码，只指方向；学生必须修改、解释并验证。", font=font(34, True), fill=BLUE)
    draw_footer(im, "课后AI反馈不是给答案，而是推动学生完成“修改-验证-反思”的二次学习。")
    save(im, 10)

    # 11
    im = base_slide("核心成效：能力、行为与评价方式的可验证改变", "成效页 · 数据作为主角", 11)
    d = ImageDraw.Draw(im)
    shadowed_card(im, (80, 185, 1120, 675), radius=30, outline=(220, 232, 248))
    d = ImageDraw.Draw(im)
    d.text((120, 220), "核心指标对比", font=font(34, True), fill=BLUE)
    metrics = [("SQL注入识别率", 12.1, 89.7, "%"), ("代码相似度", 45.2, 4.7, "%"), ("审查时间", 32.8, 11.9, "min"), ("AI误报识别率", 12, 43, "%")]
    chart_x, chart_y, row_h = 170, 300, 78
    for i, (lab, a, b, unit) in enumerate(metrics):
        y = chart_y + i * row_h
        d.text((chart_x, y + 8), lab, font=F["small_b"], fill=DARK)
        base_len = 360 * (a / 100 if unit != "min" else a / 35)
        new_len = 360 * (b / 100 if unit != "min" else b / 35)
        d.rounded_rectangle((chart_x + 220, y + 8, chart_x + 580, y + 32), radius=10, fill=(235, 240, 248))
        d.rounded_rectangle((chart_x + 220, y + 8, chart_x + 220 + base_len, y + 32), radius=10, fill=(152, 180, 218))
        d.rounded_rectangle((chart_x + 220, y + 42, chart_x + 580, y + 66), radius=10, fill=(235, 240, 248))
        color = GREEN
        d.rounded_rectangle((chart_x + 220, y + 42, chart_x + 220 + new_len, y + 66), radius=10, fill=color)
        d.text((chart_x + 600, y + 4), f"{a:g}{unit}", font=F["tiny"], fill=(110, 124, 145))
        d.text((chart_x + 600, y + 39), f"{b:g}{unit}", font=F["small_b"], fill=color)
    cards = [("安全能力", "12.1% → 89.7%", "SQL注入识别率"), ("学术诚信", "45.2% → 4.7%", "代码相似度"), ("反馈效率", "32.8min → 11.9min", "单份审查时间"), ("AI素养", "12% → 43%", "误报识别率")]
    for i, (t, num, desc) in enumerate(cards):
        x, y = 1180 + (i % 2) * 330, 210 + (i // 2) * 230
        c = [BLUE, GREEN, ORANGE, PURPLE][i]
        shadowed_card(im, (x, y, x + 285, y + 180), radius=28, outline=tuple(int(v * 0.45 + 255 * 0.55) for v in c))
        d = ImageDraw.Draw(im)
        d.text((x + 26, y + 24), t, font=font(27, True), fill=c)
        num_font = font(28, True) if "min" in num else font(32, True)
        if "min" in num:
            draw_text(d, (x + 26, y + 72), num.replace(" → ", " →\n"), num_font, fill=DARK, max_width=230, line_spacing=1.05)
            desc_y = y + 132
        else:
            d.text((x + 26, y + 76), num, font=num_font, fill=DARK)
            desc_y = y + 125
        draw_text(d, (x + 26, desc_y), desc, F["small"], fill=MID, max_width=230)
    shadowed_card(im, (110, 760, 1810, 920), radius=28, fill=(248, 251, 255), outline=(210, 228, 250))
    d = ImageDraw.Draw(im)
    d.text((160, 800), "学生反馈", font=font(32, True), fill=BLUE)
    d.text((390, 800), "92.6%", font=font(45, True), fill=GREEN)
    d.text((560, 810), "愿意继续使用AI辅助学习", font=font(26, True), fill=DARK)
    d.text((1000, 800), "83.4%", font=font(45, True), fill=PURPLE)
    d.text((1170, 810), "认为AI建议需要批判性判断", font=font(26, True), fill=DARK)
    draw_footer(im, "AI带来的不是形式变化，而是学生安全能力、学术诚信、反馈效率和AI素养的共同提升。")
    save(im, 11)

    # 12
    im = base_slide("总结推广：可复制的“人工智能+编程实践教学”模式", "模式页 · 收束升华", 12)
    d = ImageDraw.Draw(im)
    d.text((190, 170), "真问题", font=font(42, True), fill=BLUE)
    d.text((470, 170), "+", font=font(48, True), fill=(160, 174, 194))
    d.text((570, 170), "真融入", font=font(42, True), fill=GREEN)
    d.text((875, 170), "+", font=font(48, True), fill=(160, 174, 194))
    d.text((975, 170), "真数据", font=font(42, True), fill=ORANGE)
    d.text((1275, 170), "+", font=font(48, True), fill=(160, 174, 194))
    d.text((1375, 170), "真成效", font=font(42, True), fill=PURPLE)
    d.text((760, 250), "= 可推广的AI赋能编程实践教学模式", font=font(38, True), fill=DARK)
    blocks = [("流程", "学情诊断\n个性化任务\n人机协同\n智能评价\n精准干预", BLUE), ("模板", "出题约束\n代码审查提示词\n评价指标\nAI使用规则", GREEN), ("工具链", "RAG智能体\n闯关平台\nGit过程分析\nMOSS + JUnit", ORANGE), ("边界机制", "三允许三禁止\n不给完整代码\n教师复核\n数据匿名", PURPLE)]
    for i, (tit, body, c) in enumerate(blocks):
        x, y = 105 + i * 455, 405
        shadowed_card(im, (x, y, x + 390, y + 350), radius=30, outline=tuple(int(v * 0.43 + 255 * 0.57) for v in c))
        d = ImageDraw.Draw(im)
        d.ellipse((x + 32, y + 34, x + 92, y + 94), fill=tuple(int(v * 0.14 + 255 * 0.86) for v in c), outline=c, width=2)
        d.text((x + 115, y + 42), tit, font=font(34, True), fill=c)
        draw_text(d, (x + 55, y + 125), body, font(25, True), fill=DARK, max_width=290, line_spacing=1.5)
    shadowed_card(im, (185, 825, 1735, 935), radius=30, fill=(244, 249, 255), outline=(207, 226, 252))
    d = ImageDraw.Draw(im)
    draw_text(d, (250, 850), "AI赋能的目标，是培养能面对真实系统、真实用户和真实AI工具作出专业判断的未来工程师。", font(34, True), fill=BLUE, max_width=1420, align="center")
    d.text((720, 1002), "恳请各位专家批评指导", font=font(28, True), fill=MID)
    save(im, 12)


def rels_xml(rels):
    items = "".join([f'<Relationship Id="{rid}" Type="{typ}" Target="{target}"/>' for rid, typ, target in rels])
    return f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{items}</Relationships>'


def make_pptx():
    pptx_path = OUT / "省赛现场答辩PPT_图片版.pptx"
    if pptx_path.exists():
        pptx_path.unlink()
    slide_cx, slide_cy = 12192000, 6858000
    content_overrides = "".join([f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/><Override PartName="/ppt/media/image{i}.png" ContentType="image/png"/>' for i in range(1, 13)])
    content_types = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Default Extension="png" ContentType="image/png"/><Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/><Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/><Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/><Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/><Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/><Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>{content_overrides}</Types>'''
    pres_slds = "".join([f'<p:sldId id="{255+i}" r:id="rId{i}"/>' for i in range(1, 13)])
    presentation = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId13"/></p:sldMasterIdLst><p:sldIdLst>{pres_slds}</p:sldIdLst><p:sldSz cx="{slide_cx}" cy="{slide_cy}" type="wide"/><p:notesSz cx="6858000" cy="9144000"/><p:defaultTextStyle/></p:presentation>'''
    pres_rels = [(f"rId{i}", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide", f"slides/slide{i}.xml") for i in range(1, 13)]
    pres_rels += [("rId13", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster", "slideMasters/slideMaster1.xml"), ("rId14", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme", "theme/theme1.xml")]
    slide_master = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:cSld><p:bg><p:bgPr><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill><a:effectLst/></p:bgPr></p:bg><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld><p:clrMap accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" bg1="lt1" bg2="lt2" folHlink="folHlink" hlink="hlink" tx1="dk1" tx2="dk2"/><p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst><p:txStyles><p:titleStyle/><p:bodyStyle/><p:otherStyle/></p:txStyles></p:sldMaster>'''
    slide_layout = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank" preserve="1"><p:cSld name="Blank"><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sldLayout>'''
    theme = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Office Theme"><a:themeElements><a:clrScheme name="Custom"><a:dk1><a:srgbClr val="000000"/></a:dk1><a:lt1><a:srgbClr val="FFFFFF"/></a:lt1><a:dk2><a:srgbClr val="1F497D"/></a:dk2><a:lt2><a:srgbClr val="EEECE1"/></a:lt2><a:accent1><a:srgbClr val="155CC6"/></a:accent1><a:accent2><a:srgbClr val="28AE76"/></a:accent2><a:accent3><a:srgbClr val="F59132"/></a:accent3><a:accent4><a:srgbClr val="DE495C"/></a:accent4><a:accent5><a:srgbClr val="735EDE"/></a:accent5><a:accent6><a:srgbClr val="19B8D2"/></a:accent6><a:hlink><a:srgbClr val="0000FF"/></a:hlink><a:folHlink><a:srgbClr val="800080"/></a:folHlink></a:clrScheme><a:fontScheme name="Custom"><a:majorFont><a:latin typeface="Microsoft YaHei"/><a:ea typeface="Microsoft YaHei"/><a:cs typeface="Microsoft YaHei"/></a:majorFont><a:minorFont><a:latin typeface="Microsoft YaHei"/><a:ea typeface="Microsoft YaHei"/><a:cs typeface="Microsoft YaHei"/></a:minorFont></a:fontScheme><a:fmtScheme name="Office"><a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:fillStyleLst><a:lnStyleLst><a:ln w="9525"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln></a:lnStyleLst><a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst><a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:bgFillStyleLst></a:fmtScheme></a:themeElements></a:theme>'''
    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    core = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>省赛现场答辩PPT 图片版</dc:title><dc:creator>Codex</dc:creator><cp:lastModifiedBy>Codex</cp:lastModifiedBy><dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified></cp:coreProperties>'''
    app = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"><Application>Codex</Application><PresentationFormat>宽屏</PresentationFormat><Slides>12</Slides><ScaleCrop>false</ScaleCrop></Properties>'''

    def slide_xml(i):
        return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:cSld><p:bg><p:bgPr><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill><a:effectLst/></p:bgPr></p:bg><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr><p:pic><p:nvPicPr><p:cNvPr id="2" name="slide_{i:02d}.png"/><p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr><p:nvPr/></p:nvPicPr><p:blipFill><a:blip r:embed="rId1"/><a:stretch><a:fillRect/></a:stretch></p:blipFill><p:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{slide_cx}" cy="{slide_cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic></p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>'''

    with zipfile.ZipFile(pptx_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels_xml([("rId1", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument", "ppt/presentation.xml"), ("rId2", "http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties", "docProps/core.xml"), ("rId3", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties", "docProps/app.xml")]))
        z.writestr("docProps/core.xml", core)
        z.writestr("docProps/app.xml", app)
        z.writestr("ppt/presentation.xml", presentation)
        z.writestr("ppt/_rels/presentation.xml.rels", rels_xml(pres_rels))
        z.writestr("ppt/slideMasters/slideMaster1.xml", slide_master)
        z.writestr("ppt/slideMasters/_rels/slideMaster1.xml.rels", rels_xml([("rId1", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout", "../slideLayouts/slideLayout1.xml"), ("rId2", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme", "../theme/theme1.xml")]))
        z.writestr("ppt/slideLayouts/slideLayout1.xml", slide_layout)
        z.writestr("ppt/slideLayouts/_rels/slideLayout1.xml.rels", rels_xml([("rId1", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster", "../slideMasters/slideMaster1.xml")]))
        z.writestr("ppt/theme/theme1.xml", theme)
        for i, p in enumerate(slide_paths, start=1):
            z.write(p, f"ppt/media/image{i}.png")
            z.writestr(f"ppt/slides/slide{i}.xml", slide_xml(i))
            z.writestr(f"ppt/slides/_rels/slide{i}.xml.rels", rels_xml([("rId1", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image", f"../media/image{i}.png")]))
    root_pptx = BASE / "省赛现场答辩PPT_图片版.pptx"
    shutil.copy2(pptx_path, root_pptx)
    return pptx_path, root_pptx


if __name__ == "__main__":
    make_slides()
    pptx_path, root_pptx = make_pptx()
    print("OUT_DIR", OUT)
    print("PPTX", pptx_path)
    print("ROOT_PPTX", root_pptx)
    print("SLIDES", len(slide_paths))
    for p in slide_paths:
        print(p.name, Image.open(p).size)
