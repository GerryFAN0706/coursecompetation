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
# Fig 9  Four-in-one AI Teaching Tool Architecture
# ════════════════════════════════════════════════════════════════
def fig9_architecture():
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('图9  四位一体AI教学工具架构', fontsize=16, fontweight='bold', pad=20)

    # Center circle
    center_x, center_y = 6, 5
    center_r = 1.3
    circle = plt.Circle((center_x, center_y), center_r, facecolor='#FFF8E1',
                         edgecolor=ORANGE, linewidth=2.5, zorder=5)
    ax.add_patch(circle)
    ax.text(center_x, center_y + 0.15, 'AI赋能', ha='center', va='center',
            fontsize=14, fontweight='bold', color=ORANGE, zorder=6)
    ax.text(center_x, center_y - 0.35, '教学闭环', ha='center', va='center',
            fontsize=14, fontweight='bold', color=ORANGE, zorder=6)

    # Tool definitions: (cx, cy, name, subtitle, color, bg_color, scenarios, phase_label)
    tools = [
        (6, 8.5, 'WebDev助教', '教学智能体', BLUE, '#D6E4F0',
         '场景1 学情分层\n场景2 个性化出题', '课前'),
        (10, 5, 'WebSec挑战', '攻防闯关', CYAN, '#E0F7FA',
         '场景3 安全实训\n场景4 闯关驱动', '课中'),
        (6, 1.5, 'TeamCoach', '项目教练', GREEN, '#E8F5E9',
         '场景5 团队协作\n场景6 贡献分析', '课后'),
        (2, 5, 'Code Review Battle', '评审对战', PURPLE, '#EDE7F6',
         '场景7 人机对比\n场景8 批判思维', '数据反馈'),
    ]

    box_w, box_h = 3.0, 1.6

    for cx, cy, name, subtitle, color, bg_color, scenarios, phase in tools:
        # Main box
        rect = mpatches.FancyBboxPatch(
            (cx - box_w / 2, cy - box_h / 2), box_w, box_h,
            boxstyle="round,pad=0.2", facecolor=bg_color,
            edgecolor=color, linewidth=2.5, zorder=4)
        ax.add_patch(rect)
        ax.text(cx, cy + 0.3, name, ha='center', va='center',
                fontsize=13, fontweight='bold', color=color, zorder=5)
        ax.text(cx, cy - 0.3, subtitle, ha='center', va='center',
                fontsize=10, color='#555555', zorder=5)

        # Phase badge above/below/side
        badge_offsets = {
            (6, 8.5): (cx, cy + box_h / 2 + 0.35),
            (10, 5): (cx + box_w / 2 + 0.05, cy + box_h / 2 + 0.35),
            (6, 1.5): (cx, cy - box_h / 2 - 0.35),
            (2, 5): (cx - box_w / 2 - 0.05, cy + box_h / 2 + 0.35),
        }
        bx, by = badge_offsets[(cx, cy)]
        ax.text(bx, by, phase, ha='center', va='center', fontsize=9,
                fontweight='bold', color='white',
                bbox=dict(boxstyle='round,pad=0.25', facecolor=color, edgecolor='none'),
                zorder=6)

        # Scenario labels below box
        scenario_offsets = {
            (6, 8.5): (cx, cy - box_h / 2 - 0.35),
            (10, 5): (cx, cy - box_h / 2 - 0.35),
            (6, 1.5): (cx, cy + box_h / 2 + 0.35),
            (2, 5): (cx, cy - box_h / 2 - 0.35),
        }
        sx, sy = scenario_offsets[(cx, cy)]
        ax.text(sx, sy, scenarios, ha='center', va='center',
                fontsize=8, color='#666666', linespacing=1.5, zorder=5)

    # Arrows connecting tools in a cycle: top->right->bottom->left->top
    arrow_style = dict(arrowstyle='->', color='#555555', lw=2.0,
                       connectionstyle='arc3,rad=0.3')

    # Top (WebDev) -> Right (WebSec)
    ax.annotate('', xy=(10 - box_w / 2, 5 + box_h / 2),
                xytext=(6 + box_w / 2, 8.5 - box_h / 2),
                arrowprops=dict(arrowstyle='->', color=BLUE, lw=2.0,
                                connectionstyle='arc3,rad=0.2'), zorder=3)
    ax.text(9.0, 7.5, '课前 --> 课中', fontsize=8, color='#666666',
            ha='center', rotation=-40, zorder=3)

    # Right (WebSec) -> Bottom (TeamCoach)
    ax.annotate('', xy=(6 + box_w / 2, 1.5 + box_h / 2),
                xytext=(10 - box_w / 2, 5 - box_h / 2),
                arrowprops=dict(arrowstyle='->', color=CYAN, lw=2.0,
                                connectionstyle='arc3,rad=0.2'), zorder=3)
    ax.text(9.0, 2.5, '课中 --> 课后', fontsize=8, color='#666666',
            ha='center', rotation=40, zorder=3)

    # Bottom (TeamCoach) -> Left (CodeReview)
    ax.annotate('', xy=(2 + box_w / 2, 5 - box_h / 2),
                xytext=(6 - box_w / 2, 1.5 + box_h / 2),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.0,
                                connectionstyle='arc3,rad=0.2'), zorder=3)
    ax.text(3.0, 2.5, '课后 --> 反馈', fontsize=8, color='#666666',
            ha='center', rotation=-40, zorder=3)

    # Left (CodeReview) -> Top (WebDev)
    ax.annotate('', xy=(6 - box_w / 2, 8.5 - box_h / 2),
                xytext=(2 + box_w / 2, 5 + box_h / 2),
                arrowprops=dict(arrowstyle='->', color=PURPLE, lw=2.0,
                                connectionstyle='arc3,rad=0.2'), zorder=3)
    ax.text(3.0, 7.5, '反馈 --> 课前', fontsize=8, color='#666666',
            ha='center', rotation=40, zorder=3)

    # Connecting lines from tools to center
    for cx, cy, _, _, color, _, _, _ in tools:
        ax.plot([cx, center_x], [cy, center_y], '--', color=color,
                linewidth=1.0, alpha=0.4, zorder=2)

    # Footer
    ax.text(6, -0.2, '教师角色: 审核决策者    学生角色: 理解判断者    AI角色: 辅助执行者',
            ha='center', va='center', fontsize=9, color='#888888', style='italic')

    fig.savefig(os.path.join(OUT, '图9_四位一体AI教学工具架构.png'))
    plt.close(fig)
    print('[OK] Fig9 done')


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
    ax.set_title('图10  WebSec挑战通关数据（N=58）', fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)

    fig.savefig(os.path.join(OUT, '图10_WebSec挑战通关数据.png'))
    plt.close(fig)
    print('[OK] Fig10 done')


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
    ax.set_title('图11  Code Review人机对比（N=10组）', fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)

    fig.savefig(os.path.join(OUT, '图11_CodeReview人机对比.png'))
    plt.close(fig)
    print('[OK] Fig11 done')


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
    ax.set_title('图12  团队贡献度分布 (TeamCoach自动分析)', fontsize=14, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)

    fig.savefig(os.path.join(OUT, '图12_TeamCoach团队贡献度分布.png'))
    plt.close(fig)
    print('[OK] Fig12 done')


# ── Run all ────────────────────────────────────────────────────
if __name__ == '__main__':
    fig9_architecture()
    fig10_websec_passrate()
    fig11_codereview_comparison()
    fig12_teamcoach_contribution()
    print('\nAll 4 tool figures (9-12) generated successfully.')
