"""Generate figures 9-12 for the Innovation Report: AI Tool Architecture & Data."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import os

# ── Global config (match existing figures) ────────────────────
plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'

BLUE = '#4472C4'
GREEN = '#4CAF50'
CYAN = '#00BCD4'
PURPLE = '#7c3aed'
RED = '#C0504D'
ORANGE = '#ED7D31'
GOLD = '#FFC000'

OUT = os.path.join(os.path.dirname(__file__), 'figures')
os.makedirs(OUT, exist_ok=True)


# ════════════════════════════════════════════════════════════════
# Fig 2  Five-dimension AI Fusion Innovation Teaching Tool Architecture
# ════════════════════════════════════════════════════════════════
def fig2_architecture():
    fig, ax = plt.subplots(figsize=(14, 11))
    ax.set_xlim(0, 14)
    ax.set_ylim(-0.5, 11)
    ax.axis('off')
    ax.set_title('图2  五维AI融合创新教学工具体系架构', fontsize=16, fontweight='bold', pad=20)

    # Center circle
    center_x, center_y = 7, 5.5
    center_r = 1.3
    circle = plt.Circle((center_x, center_y), center_r, facecolor='#FFF8E1',
                         edgecolor=ORANGE, linewidth=2.5, zorder=5)
    ax.add_patch(circle)
    ax.text(center_x, center_y + 0.3, '五维融合', ha='center', va='center',
            fontsize=13, fontweight='bold', color=ORANGE, zorder=6)
    ax.text(center_x, center_y - 0.25, '数据闭环', ha='center', va='center',
            fontsize=13, fontweight='bold', color=ORANGE, zorder=6)

    # 5 tools arranged in a pentagon around center
    # Positions: top, upper-right, lower-right, lower-left, upper-left
    PINK = '#E91E63'
    tools = [
        (7, 9.5, '维度一：智能助教', 'WebDev助教 · RAG智能体', BLUE, '#D6E4F0',
         '学情采集 · 24h问答 · 预习引导', '课前+课后'),
        (11.5, 7.2, '维度二：编程挑战', 'WebSec挑战 · 攻防闯关', CYAN, '#E0F7FA',
         '游戏化训练 · 自适应难度 · 实时大屏', '课中'),
        (10.2, 2.5, '维度三：团队教练', 'TeamCoach · Git分析', GREEN, '#E8F5E9',
         '贡献度追踪 · 搭便车预警 · AI周报', '课后'),
        (3.8, 2.5, '维度四：人机对抗', 'Code Review Battle', PURPLE, '#EDE7F6',
         '人机同台审查 · 批判性思维 · 辩论', '课中'),
        (2.5, 7.2, '维度五：资料重构', 'AI辅助教学资料重构', PINK, '#FCE4EC',
         '一人一题 · 分层任务 · AI课件生成', '课前'),
    ]

    box_w, box_h = 3.2, 1.5

    for cx, cy, name, subtitle, color, bg_color, scenarios, phase in tools:
        # Main box
        rect = mpatches.FancyBboxPatch(
            (cx - box_w / 2, cy - box_h / 2), box_w, box_h,
            boxstyle="round,pad=0.2", facecolor=bg_color,
            edgecolor=color, linewidth=2.5, zorder=4)
        ax.add_patch(rect)
        ax.text(cx, cy + 0.3, name, ha='center', va='center',
                fontsize=11, fontweight='bold', color=color, zorder=5)
        ax.text(cx, cy - 0.25, subtitle, ha='center', va='center',
                fontsize=9, color='#555555', zorder=5)

        # Phase badge
        ax.text(cx + box_w / 2 - 0.1, cy + box_h / 2 - 0.1, phase,
                ha='right', va='top', fontsize=8,
                fontweight='bold', color='white',
                bbox=dict(boxstyle='round,pad=0.2', facecolor=color, edgecolor='none'),
                zorder=6)

        # Scenario labels below box
        ax.text(cx, cy - box_h / 2 - 0.25, scenarios, ha='center', va='top',
                fontsize=7.5, color='#666666', zorder=5)

        # Dashed line to center
        ax.plot([cx, center_x], [cy, center_y], '--', color=color,
                linewidth=1.2, alpha=0.4, zorder=2)

    # Arrows forming the cycle (pentagon edges)
    arrow_pairs = [
        (0, 1, '课前→课中'),
        (1, 2, '课中→课后'),
        (2, 3, '课后→课中'),
        (3, 4, '对抗→重构'),
        (4, 0, '重构→智能体'),
    ]
    for i_from, i_to, label in arrow_pairs:
        x1, y1 = tools[i_from][0], tools[i_from][1]
        x2, y2 = tools[i_to][0], tools[i_to][1]
        color_from = tools[i_from][4]
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=color_from, lw=1.8,
                                    connectionstyle='arc3,rad=0.15'), zorder=3)

    # Footer
    ax.text(7, 0.0, '教师角色: 审核决策者    学生角色: 理解判断者    AI角色: 辅助执行者',
            ha='center', va='center', fontsize=9, color='#888888', style='italic')

    # Coverage note
    ax.text(7, -0.45, '五维融合覆盖全部六大AI教学情境：学情采集·数字资源·场景设计·多维评价·人机协同·个性化支持',
            ha='center', va='center', fontsize=8, color='#999999')

    fig.savefig(os.path.join(OUT, '图2_五维AI融合创新教学工具体系架构.png'))
    plt.close(fig)
    print('[OK] Fig2 done')


# ════════════════════════════════════════════════════════════════
# Fig 10  WebSec Challenge Pass Rate Data
# ════════════════════════════════════════════════════════════════
def fig10_websec_passrate():
    fig, ax = plt.subplots(figsize=(11, 7))

    levels = ['第1关\nSQL注入', '第2关\n越权访问', '第3关\nSession劫持',
              '第4关\nXSS', '第5关\n综合']
    first_pass = [72, 40, 35, 28, 15]
    final_pass = [95, 82, 78, 71, 58]

    x = np.arange(len(levels))
    w = 0.35

    light_blue = '#93C5FD'
    dark_blue = '#1D4ED8'

    b1 = ax.bar(x - w / 2, first_pass, w, color=light_blue, label='首次通过率',
                edgecolor='white', linewidth=0.5)
    b2 = ax.bar(x + w / 2, final_pass, w, color=dark_blue, label='最终通过率',
                edgecolor='white', linewidth=0.5)

    # Value labels
    for bar, val in zip(b1, first_pass):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.2,
                f'{val}%', ha='center', va='bottom', fontsize=11,
                fontweight='bold', color=light_blue)
    for bar, val in zip(b2, final_pass):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.2,
                f'{val}%', ha='center', va='bottom', fontsize=11,
                fontweight='bold', color=dark_blue)

    # Improvement arrows between bars
    for i in range(len(levels)):
        diff = final_pass[i] - first_pass[i]
        mid_x = x[i]
        mid_y = max(first_pass[i], final_pass[i]) + 8
        ax.text(mid_x, mid_y, f'+{diff}pp', ha='center', fontsize=9,
                color=RED, fontweight='bold')

    # Annotation on Level 2
    ax.annotate('教师干预后通过率翻倍',
                xy=(1 + w / 2, 82), xytext=(2.8, 92),
                fontsize=10, color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF0F0',
                          edgecolor=RED, alpha=0.9))

    # Difficulty gradient bar at top
    ax.text(0, -12, '难度递增 >>>', fontsize=9, color='#999999',
            style='italic', ha='left')

    ax.set_ylabel('通过率 (%)', fontsize=12)
    ax.set_xlabel('闯关关卡', fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(levels, fontsize=11)
    ax.set_ylim(0, 110)
    ax.legend(fontsize=11, loc='upper right')
    ax.set_title('图3  WebSec安全攻防闯关平台通关率数据（N=58）', fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)

    fig.savefig(os.path.join(OUT, '图3_WebSec安全攻防闯关平台通关率数据.png'))
    plt.close(fig)
    print('[OK] Fig3 done')


# ════════════════════════════════════════════════════════════════
# Fig 11  Code Review Human vs AI Comparison
# ════════════════════════════════════════════════════════════════
def fig11_codereview_comparison():
    fig, ax = plt.subplots(figsize=(10, 7))

    dimensions = ['发现数量', '关键漏洞命中', '误报数', '业务理解']
    student_scores = [3, 2, 0, 4]
    ai_scores = [5, 3, 1, 2]

    x = np.arange(len(dimensions))
    w = 0.35

    b1 = ax.bar(x - w / 2, student_scores, w, color=BLUE, label='学生团队',
                edgecolor='white', linewidth=0.5)
    b2 = ax.bar(x + w / 2, ai_scores, w, color=PURPLE, label='AI审查',
                edgecolor='white', linewidth=0.5)

    # Value labels
    for bar, val in zip(b1, student_scores):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
                f'{val}', ha='center', va='bottom', fontsize=12,
                fontweight='bold', color=BLUE)
    for bar, val in zip(b2, ai_scores):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
                f'{val}', ha='center', va='bottom', fontsize=12,
                fontweight='bold', color=PURPLE)

    # "Winner" markers
    for i in range(len(dimensions)):
        s, a = student_scores[i], ai_scores[i]
        top_y = max(s, a) + 0.55
        if i == 2:
            # Lower is better for false positives
            if s < a:
                winner_x = b1[i].get_x() + b1[i].get_width() / 2
                winner_color = BLUE
                winner_label = '胜出(少)'
            else:
                winner_x = b2[i].get_x() + b2[i].get_width() / 2
                winner_color = PURPLE
                winner_label = '胜出(少)'
        else:
            if s > a:
                winner_x = b1[i].get_x() + b1[i].get_width() / 2
                winner_color = BLUE
                winner_label = '胜出'
            elif a > s:
                winner_x = b2[i].get_x() + b2[i].get_width() / 2
                winner_color = PURPLE
                winner_label = '胜出'
            else:
                continue  # tie
        ax.text(winner_x, top_y, winner_label, ha='center', fontsize=8,
                fontweight='bold', color='white',
                bbox=dict(boxstyle='round,pad=0.2', facecolor=winner_color,
                          edgecolor='none'))

    # Annotation
    ax.text(0.5, 0.93, '人机协同 > 单独任何一方',
            transform=ax.transAxes, ha='center', fontsize=12,
            fontweight='bold', color=RED,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF0F0',
                      edgecolor=RED, alpha=0.9))

    # Score scale note
    ax.text(0.98, 0.02, '评分范围: 0-5分', transform=ax.transAxes,
            ha='right', va='bottom', fontsize=9, color='#888888')

    ax.set_ylabel('评分 (0-5)', fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(dimensions, fontsize=12)
    ax.set_ylim(0, 6.5)
    ax.legend(fontsize=11, loc='upper left')
    ax.set_title('图5  Code Review Battle人机审查发现对比（N=10组）', fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)

    fig.savefig(os.path.join(OUT, '图5_CodeReviewBattle人机审查发现对比.png'))
    plt.close(fig)
    print('[OK] Fig5 done')


# ════════════════════════════════════════════════════════════════
# Fig 12  TeamCoach Contribution Distribution
# ════════════════════════════════════════════════════════════════
def fig12_teamcoach_contribution():
    fig, ax = plt.subplots(figsize=(12, 8))

    teams = ['第1组', '第2组', '第3组', '第4组', '第5组']
    # Each team has 4 members
    member_labels = ['成员A', '成员B', '成员C', '成员D']
    data = [
        [28, 26, 24, 22],  # Team 1 - balanced
        [35, 22, 23, 20],  # Team 2 - one star
        [38, 26, 30, 6],   # Team 3 - one slacker
        [27, 25, 28, 20],  # Team 4 - balanced
        [55, 25, 12, 8],   # Team 5 - one doing everything
    ]

    n_teams = len(teams)
    n_members = len(member_labels)
    bar_height = 0.18
    y_positions = np.arange(n_teams)

    # Color function
    def get_color(val):
        if val >= 25:
            return '#4CAF50'  # green
        elif val >= 15:
            return '#FFC107'  # yellow/amber
        else:
            return '#F44336'  # red

    for i, team_data in enumerate(data):
        for j, val in enumerate(team_data):
            y = y_positions[i] + (j - 1.5) * bar_height
            color = get_color(val)
            bar = ax.barh(y, val, height=bar_height * 0.85, color=color,
                          edgecolor='white', linewidth=0.5, zorder=3)
            # Value label
            ax.text(val + 0.8, y, f'{val}%', ha='left', va='center',
                    fontsize=9, fontweight='bold', color='#333333', zorder=4)
            # Member label inside bar (if wide enough)
            if val > 12:
                ax.text(val / 2, y, member_labels[j], ha='center', va='center',
                        fontsize=8, color='white', fontweight='bold', zorder=4)
            else:
                ax.text(val + 4.5, y, member_labels[j], ha='left', va='center',
                        fontsize=7, color='#888888', zorder=4)

    # Warning line at 15%
    ax.axvline(x=15, color=RED, linestyle='--', linewidth=2, alpha=0.7, zorder=2)
    ax.text(15.5, n_teams - 0.15, '警戒线 15%', fontsize=10, color=RED,
            fontweight='bold', va='bottom')

    # Fair share line at 25%
    ax.axvline(x=25, color=GREEN, linestyle=':', linewidth=1.5, alpha=0.5, zorder=2)
    ax.text(25.5, n_teams - 0.15, '公平线 25%', fontsize=9, color=GREEN,
            fontweight='bold', va='bottom')

    # Annotations for problematic teams
    # Team 3 member D (6%)
    ax.annotate('搭便车预警!\nTeamCoach自动提醒教师',
                xy=(6, 2 - 1.5 * bar_height),
                xytext=(25, 2 - 2.5 * bar_height),
                fontsize=9, color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF0F0',
                          edgecolor=RED, alpha=0.9))

    # Team 5 annotation
    ax.annotate('一人独揽型\n需重新分工',
                xy=(55, 4 + 1.5 * bar_height),
                xytext=(55, 4 + 3.0 * bar_height),
                fontsize=9, color=ORANGE, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.5),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF8E1',
                          edgecolor=ORANGE, alpha=0.9))

    # Legend for colors
    legend_elements = [
        mpatches.Patch(facecolor='#4CAF50', label='贡献度>=25% (均衡)'),
        mpatches.Patch(facecolor='#FFC107', label='贡献度15-25% (偏低)'),
        mpatches.Patch(facecolor='#F44336', label='贡献度<15% (警戒)'),
    ]
    ax.legend(handles=legend_elements, fontsize=10, loc='lower right')

    ax.set_yticks(y_positions)
    ax.set_yticklabels(teams, fontsize=12)
    ax.set_xlabel('贡献度 (%)', fontsize=12)
    ax.set_xlim(0, 70)
    ax.set_ylim(-0.8, n_teams - 0.2 + 0.8)
    ax.invert_yaxis()
    ax.set_title('图4  TeamCoach团队贡献度均衡化趋势', fontsize=14, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)

    fig.savefig(os.path.join(OUT, '图4_TeamCoach团队贡献度均衡化趋势.png'))
    plt.close(fig)
    print('[OK] Fig4 done')


# ── Run all ────────────────────────────────────────────────────
if __name__ == '__main__':
    fig2_architecture()
    fig10_websec_passrate()
    fig11_codereview_comparison()
    fig12_teamcoach_contribution()
    print('\nAll 4 tool figures (9-12) generated successfully.')
