"""Generate figures 1, 6-12 for the Innovation Report (创新成果报告)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# ── Global config ──────────────────────────────────────────────
plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'

BLUE = '#4472C4'   # 对照组 2024
GREEN = '#70AD47'  # 实验组 2025
RED = '#C0504D'
ORANGE = '#ED7D31'
GOLD = '#FFC000'
PURPLE = '#7030A0'
TEAL = '#00B0F0'

OUT = os.path.join(os.path.dirname(__file__), 'figures')
os.makedirs(OUT, exist_ok=True)


# ════════════════════════════════════════════════════════════════
# 图1  AI赋能教学全流程闭环架构
# ════════════════════════════════════════════════════════════════
def fig1_flowchart():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    ax.axis('off')
    ax.set_title('图1  AI赋能教学全流程闭环架构', fontsize=16, fontweight='bold', pad=20)

    # Main flow boxes
    phases = [
        (1.0, 3.5, '课前\nAI学情分层', '#D6E4F0', '学情数据采集\n与分析'),
        (3.8, 3.5, '课前\n个性化出题', '#E2EFDA', '个性化\n学习支持'),
        (6.6, 3.5, '课中\n人机协同审查', '#FFF2CC', '师生机\n协同教学'),
        (9.4, 3.5, '课后\nAI智能评价', '#FCE4D6', '多维智能\n评价反馈'),
        (12.2, 3.5, '精准干预\n迭代优化', '#E2D0F0', '数据驱动\n教学决策'),
    ]

    box_w, box_h = 2.2, 1.6
    for x, y, label, color, scenario in phases:
        rect = mpatches.FancyBboxPatch((x - box_w/2, y - box_h/2), box_w, box_h,
                                        boxstyle="round,pad=0.15", facecolor=color,
                                        edgecolor='#333333', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x, y + 0.05, label, ha='center', va='center', fontsize=11, fontweight='bold')
        # Scenario label below
        ax.text(x, y - box_h/2 - 0.35, scenario, ha='center', va='top',
                fontsize=8, color='#555555', style='italic')

    # Arrows between boxes
    for i in range(len(phases) - 1):
        x1 = phases[i][0] + box_w/2 + 0.05
        x2 = phases[i+1][0] - box_w/2 - 0.05
        y = phases[i][1]
        ax.annotate('', xy=(x2, y), xytext=(x1, y),
                    arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Feedback loop arrow (from right back to left)
    ax.annotate('', xy=(1.0, 3.5 + box_h/2 + 0.5), xytext=(12.2, 3.5 + box_h/2 + 0.5),
                arrowprops=dict(arrowstyle='->', color=RED, lw=2,
                                connectionstyle='arc3,rad=0.25'))
    ax.text(6.6, 5.4, '数据闭环反馈', ha='center', va='center',
            fontsize=10, color=RED, fontweight='bold')

    # Tool chain at bottom
    tools = ['Claude/GPT-4', 'Claude/GPT-4', 'Cursor IDE', 'Cursor + LLM', 'Gitea + MOSS']
    for i, (x, y, _, _, _) in enumerate(phases):
        ax.text(x, y - box_h/2 - 0.9, tools[i], ha='center', va='top',
                fontsize=8, color='#666666',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Role labels
    ax.text(0.2, 0.8, '教师角色：审核决策者    学生角色：理解判断者    AI角色：辅助执行者',
            fontsize=9, color='#444444', style='italic')

    fig.savefig(os.path.join(OUT, '图1_AI赋能教学全流程闭环架构.png'))
    plt.close(fig)
    print('[OK] Fig1 done')


# ════════════════════════════════════════════════════════════════
# 图6  MOSS代码相似度逐批次下降趋势
# ════════════════════════════════════════════════════════════════
def fig6_similarity():
    fig, ax1 = plt.subplots(figsize=(10, 6))

    batches = ['HW03\nJSP页面', 'HW06\nJDBC', 'HW10\nMVC综合', 'HW14\n权限控制']
    x = np.arange(len(batches))
    sim_2024 = [45.2, 42.8, 38.6, 35.1]
    sim_2025 = [32.1, 18.5,  8.3,  4.7]
    pairs_2024 = [47, 39, 28, 22]
    pairs_2025 = [12,  3,  0,  0]

    w = 0.35
    bars1 = ax1.bar(x - w/2, sim_2024, w, color=BLUE, label='2024秋（对照组）', alpha=0.85)
    bars2 = ax1.bar(x + w/2, sim_2025, w, color=GREEN, label='2025秋（实验组）', alpha=0.85)

    # Value labels on bars
    for bar, val in zip(bars1, sim_2024):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
                f'{val}%', ha='center', va='bottom', fontsize=10, fontweight='bold', color=BLUE)
    for bar, val in zip(bars2, sim_2025):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
                f'{val}%', ha='center', va='bottom', fontsize=10, fontweight='bold', color=GREEN)

    ax1.set_ylabel('平均代码相似度 (%)', fontsize=12)
    ax1.set_xlabel('作业批次', fontsize=12)
    ax1.set_xticks(x)
    ax1.set_xticklabels(batches, fontsize=10)
    ax1.set_ylim(0, 55)

    # Secondary axis for pair count
    ax2 = ax1.twinx()
    ax2.plot(x, pairs_2024, 'o--', color='#2F5496', linewidth=2, markersize=8, label='高相似度对数(2024)')
    ax2.plot(x, pairs_2025, 's--', color='#375623', linewidth=2, markersize=8, label='高相似度对数(2025)')
    for i, (p1, p2) in enumerate(zip(pairs_2024, pairs_2025)):
        ax2.annotate(f'{p1}对', (x[i], p1), textcoords="offset points", xytext=(8, 5),
                     fontsize=9, color='#2F5496')
        ax2.annotate(f'{p2}对', (x[i], p2), textcoords="offset points", xytext=(8, -12),
                     fontsize=9, color='#375623')
    ax2.set_ylabel('相似度>60%的配对数', fontsize=12)
    ax2.set_ylim(-2, 55)

    # Annotation: AI introduced
    ax1.axvline(x=0.5, color=RED, linestyle=':', linewidth=1.5, alpha=0.7)
    ax1.text(0.55, 52, '← AI个性化出题引入', fontsize=9, color=RED, fontstyle='italic')

    # Combined legend
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1 + h2, l1 + l2, loc='upper right', fontsize=9, framealpha=0.9)

    ax1.set_title('图6  MOSS代码相似度逐批次下降趋势（2024 vs 2025）', fontsize=14, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    fig.savefig(os.path.join(OUT, '图6_MOSS代码相似度逐批次下降趋势.png'))
    plt.close(fig)
    print('[OK] Fig6 done')


# ════════════════════════════════════════════════════════════════
# 图7  AI辅助前后教师单份作业审查时间对比
# ════════════════════════════════════════════════════════════════
def fig7_review_time():
    fig, ax = plt.subplots(figsize=(10, 6))

    phases = ['代码规范检查', '功能正确性测试', '安全漏洞审查', '反馈意见撰写']
    t_2024 = [8.2, 12.5, 6.8, 5.3]
    t_2025 = [1.5, 6.3, 2.1, 2.0]
    savings = ['-81.7%', '-49.6%', '-69.1%', '-62.3%']

    x = np.arange(len(phases))
    w = 0.35
    bars1 = ax.bar(x - w/2, t_2024, w, color=BLUE, label='2024秋（传统审查）', alpha=0.85)
    bars2 = ax.bar(x + w/2, t_2025, w, color=GREEN, label='2025秋（AI辅助审查）', alpha=0.85)

    for bar, val in zip(bars1, t_2024):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                f'{val}min', ha='center', va='bottom', fontsize=10, color=BLUE, fontweight='bold')
    for i, (bar, val) in enumerate(zip(bars2, t_2025)):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                f'{val}min', ha='center', va='bottom', fontsize=10, color=GREEN, fontweight='bold')
        # Savings annotation
        mid_x = (bars1[i].get_x() + bars1[i].get_width()/2 + bar.get_x() + bar.get_width()/2) / 2
        ax.text(mid_x, max(t_2024[i], t_2025[i]) + 1.2, savings[i],
                ha='center', fontsize=9, color=RED, fontweight='bold')

    # Total annotation
    ax.annotate(f'合计: 32.8min → 11.9min\n节约 63.7%',
                xy=(3.5, 6), fontsize=11, fontweight='bold', color=RED,
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF0F0', edgecolor=RED, alpha=0.9))

    ax.set_ylabel('审查时间（分钟/份）', fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(phases, fontsize=11)
    ax.set_ylim(0, 16)
    ax.legend(fontsize=10, loc='upper left')
    ax.set_title('图7  AI辅助前后教师单份作业审查时间对比', fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)

    fig.savefig(os.path.join(OUT, '图7_AI辅助前后教师单份作业审查时间对比.png'))
    plt.close(fig)
    print('[OK] Fig7 done')


# ════════════════════════════════════════════════════════════════
# 图8  SQL注入安全意识四时间点纵向追踪
# ════════════════════════════════════════════════════════════════
def fig8_sql_injection():
    fig, ax = plt.subplots(figsize=(10, 6))

    weeks = ['第1周\n学期初摸底', '第6周\nJDBC讲授后', '第11周\nAI辅助审查后', '第16周\n期末考核']
    x = np.arange(len(weeks))
    recognition = [12.1, 45.2, 79.3, 89.7]
    application  = [5.2, 38.0, 74.1, 86.2]

    line1, = ax.plot(x, recognition, 'o-', color=BLUE, linewidth=2.5, markersize=10, label='识别率（能发现SQL注入风险）')
    line2, = ax.plot(x, application, 's-', color=GREEN, linewidth=2.5, markersize=10, label='应用率（正确使用PreparedStatement）')

    for i, (r, a) in enumerate(zip(recognition, application)):
        ax.annotate(f'{r}%', (x[i], r), textcoords="offset points", xytext=(0, 12),
                    ha='center', fontsize=11, fontweight='bold', color=BLUE)
        ax.annotate(f'{a}%', (x[i], a), textcoords="offset points", xytext=(0, -18),
                    ha='center', fontsize=11, fontweight='bold', color=GREEN)

    # Highlight key jump
    ax.annotate('关键跳升 +34.1pp\nAI审查中展示攻击示例',
                xy=(2, 79.3), xytext=(2.5, 55),
                fontsize=9, color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF0F0', edgecolor=RED))

    # Shade area between curves
    ax.fill_between(x, application, recognition, alpha=0.1, color=ORANGE)

    ax.set_ylabel('比例 (%)', fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(weeks, fontsize=10)
    ax.set_ylim(0, 105)
    ax.legend(fontsize=10, loc='upper left')
    ax.set_title('图8  SQL注入安全意识四时间点纵向追踪（N=58）', fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)

    fig.savefig(os.path.join(OUT, '图8_SQL注入安全意识四时间点纵向追踪.png'))
    plt.close(fig)
    print('[OK] Fig8 done')


# ════════════════════════════════════════════════════════════════
# 图12  学生问卷满意度多维评价雷达图
# ════════════════════════════════════════════════════════════════
def fig12_radar():
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    categories = ['整体满意度\nQ1', '知识理解帮助\nQ2', '代码审查有效性\nQ3',
                  '个性化出题适配\nQ4', 'AI能力提升\nQ5']
    values = [4.31, 4.19, 4.44, 4.07, 4.37]
    pct_45 = [83.3, 77.8, 87.0, 72.2, 85.2]  # 4-5分占比

    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    values_plot = values + [values[0]]
    angles_plot = angles + [angles[0]]

    ax.plot(angles_plot, values_plot, 'o-', linewidth=2.5, color=BLUE, markersize=10)
    ax.fill(angles_plot, values_plot, alpha=0.2, color=BLUE)

    # Add value labels
    for angle, val, pct in zip(angles, values, pct_45):
        ax.text(angle, val + 0.25, f'{val}\n({pct}%给4-5分)',
                ha='center', va='bottom', fontsize=9, fontweight='bold', color='#333333')

    ax.set_xticks(angles)
    ax.set_xticklabels(categories, fontsize=10)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=8)
    ax.set_rlabel_position(30)

    ax.set_title('图12  学生问卷满意度多维评价雷达图（N=54, α=0.87）',
                 fontsize=14, fontweight='bold', pad=30)

    # Add annotation
    ax.text(0.5, -0.08, '92.6%的学生愿意在未来课程中继续使用AI辅助学习（Q15=4.56/5）',
            transform=ax.transAxes, ha='center', fontsize=10, color=RED, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF0F0', edgecolor=RED))

    fig.savefig(os.path.join(OUT, '图12_学生问卷满意度多维评价雷达图.png'))
    plt.close(fig)
    print('[OK] Fig12 done')


# ════════════════════════════════════════════════════════════════
# 图9  实验组与对照组核心成效指标对比
# ════════════════════════════════════════════════════════════════
def fig9_core_metrics():
    fig, axes = plt.subplots(1, 2, figsize=(16, 7), gridspec_kw={'width_ratios': [3, 2]})

    # Left: percentage-based metrics
    ax1 = axes[0]
    labels = ['编译通过率', '异常处理\n覆盖率', '命名规范\n符合率', '分层架构\n合规率', 'MVC正确\n使用率']
    v_2024 = [67.3, 31.5, 54.2, 38.1, 41.9]
    v_2025 = [88.5, 62.8, 85.7, 79.3, 82.8]

    x = np.arange(len(labels))
    w = 0.35
    b1 = ax1.bar(x - w/2, v_2024, w, color=BLUE, label='2024秋（对照组）', alpha=0.85)
    b2 = ax1.bar(x + w/2, v_2025, w, color=GREEN, label='2025秋（实验组）', alpha=0.85)

    for bar, val in zip(b1, v_2024):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{val}%', ha='center', fontsize=9, fontweight='bold', color=BLUE)
    for i, (bar, val) in enumerate(zip(b2, v_2025)):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{val}%', ha='center', fontsize=9, fontweight='bold', color=GREEN)
        diff = v_2025[i] - v_2024[i]
        ax1.text((b1[i].get_x() + bar.get_x() + bar.get_width()) / 2,
                max(v_2024[i], v_2025[i]) + 6,
                f'+{diff:.1f}pp', ha='center', fontsize=8, color=RED, fontweight='bold')

    significance = ['p<0.001\nd=0.76', 'p<0.001\nd=2.41', '', '', '']
    for i, sig in enumerate(significance):
        if sig:
            ax1.text(x[i], 97, sig, ha='center', fontsize=7, color='#666666')

    ax1.set_ylabel('百分比 (%)', fontsize=12)
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, fontsize=10)
    ax1.set_ylim(0, 105)
    ax1.legend(fontsize=9)
    ax1.set_title('代码质量与规范性指标', fontsize=12, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)

    # Right: score-based metrics
    ax2 = axes[1]
    labels2 = ['功能完整性\n(/10)', '安全漏洞数\n(/份)', '期末均分']
    v2_2024 = [6.2, 3.4, 74.8]
    v2_2025 = [8.1, 1.2, 82.1]

    x2 = np.arange(len(labels2))
    b3 = ax2.bar(x2 - w/2, v2_2024, w, color=BLUE, alpha=0.85)
    b4 = ax2.bar(x2 + w/2, v2_2025, w, color=GREEN, alpha=0.85)

    for bar, val in zip(b3, v2_2024):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{val}', ha='center', fontsize=10, fontweight='bold', color=BLUE)
    for bar, val in zip(b4, v2_2025):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{val}', ha='center', fontsize=10, fontweight='bold', color=GREEN)

    sigs2 = ['p<0.001\nd=1.21', 'p<0.001\nd=1.69', 'p<0.001']
    for i, sig in enumerate(sigs2):
        ax2.text(x2[i], max(v2_2024[i], v2_2025[i]) + 4,
                sig, ha='center', fontsize=8, color=RED, fontweight='bold')

    ax2.set_ylabel('数值', fontsize=12)
    ax2.set_xticks(x2)
    ax2.set_xticklabels(labels2, fontsize=10)
    ax2.set_ylim(0, 95)
    ax2.set_title('功能·安全·成绩指标', fontsize=12, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)

    fig.suptitle('图9  实验组与对照组核心成效指标对比（N=58 vs N=62）',
                 fontsize=14, fontweight='bold', y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, '图9_实验组与对照组核心成效指标对比.png'))
    plt.close(fig)
    print('[OK] Fig9 done')


# ════════════════════════════════════════════════════════════════
# 图10  实验组与对照组学业成绩分布对比
# ════════════════════════════════════════════════════════════════
def fig10_grade_distribution():
    fig, ax = plt.subplots(figsize=(10, 6))

    grades = ['优秀\n(90-100)', '良好\n(80-89)', '中等\n(70-79)', '及格\n(60-69)', '不及格\n(<60)']
    pct_2024 = [9.7, 25.8, 35.5, 22.6, 6.5]
    pct_2025 = [20.7, 37.9, 27.6, 12.1, 1.7]

    x = np.arange(len(grades))
    w = 0.35
    b1 = ax.bar(x - w/2, pct_2024, w, color=BLUE, label='2024秋（N=62，均分74.8）', alpha=0.85)
    b2 = ax.bar(x + w/2, pct_2025, w, color=GREEN, label='2025秋（N=58，均分82.1）', alpha=0.85)

    for bar, val in zip(b1, pct_2024):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{val}%', ha='center', fontsize=10, fontweight='bold', color=BLUE)
    for bar, val in zip(b2, pct_2025):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{val}%', ha='center', fontsize=10, fontweight='bold', color=GREEN)

    # Change arrows
    changes = ['+11.0pp', '+12.1pp', '-7.9pp', '-10.5pp', '-4.8pp']
    colors = [GREEN, GREEN, BLUE, BLUE, BLUE]
    for i, (chg, c) in enumerate(zip(changes, colors)):
        y_max = max(pct_2024[i], pct_2025[i])
        ax.text(x[i], y_max + 3.5, chg, ha='center', fontsize=9, fontweight='bold', color=RED)

    # Stats box
    stats_text = ('优良率(≥80): 35.5% → 58.6% (+23.1pp)\n'
                  '均分: 74.8 → 82.1 (+7.3, p<0.001)')
    ax.text(0.98, 0.95, stats_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF8E1', edgecolor=ORANGE, alpha=0.9))

    ax.set_ylabel('学生占比 (%)', fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(grades, fontsize=11)
    ax.set_ylim(0, 45)
    ax.legend(fontsize=10, loc='upper left')
    ax.set_title('图10  实验组与对照组学业成绩分布对比', fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)

    fig.savefig(os.path.join(OUT, '图10_实验组与对照组学业成绩分布对比.png'))
    plt.close(fig)
    print('[OK] Fig10 done')


# ════════════════════════════════════════════════════════════════
# 图11  第14次作业五类安全漏洞出现率对比
# ════════════════════════════════════════════════════════════════
def fig11_vulnerabilities():
    fig, ax = plt.subplots(figsize=(11, 6))

    vulns = ['SQL注入\n(字符串拼接)', '越权访问\n(Filter缺少角色检查)', 'Session残留\n(退出不彻底)',
             'XSS\n(输出未转义)', '密码明文存储']
    rate_2024 = [56.5, 71.0, 48.4, 41.9, 27.4]
    rate_2025 = [6.9, 12.1, 8.6, 15.5, 3.4]

    x = np.arange(len(vulns))
    w = 0.35
    b1 = ax.barh(x + w/2, rate_2024, w, color=BLUE, label='2024秋（对照组）', alpha=0.85)
    b2 = ax.barh(x - w/2, rate_2025, w, color=GREEN, label='2025秋（实验组）', alpha=0.85)

    for bar, val in zip(b1, rate_2024):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                f'{val}%', ha='left', va='center', fontsize=10, fontweight='bold', color=BLUE)
    for bar, val in zip(b2, rate_2025):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                f'{val}%', ha='left', va='center', fontsize=10, fontweight='bold', color=GREEN)

    # Drop annotations
    drops = ['-49.6pp', '-58.9pp', '-39.8pp', '-26.4pp', '-24.0pp']
    for i, drop in enumerate(drops):
        ax.text(max(rate_2024[i], rate_2025[i]) + 8, x[i],
                drop, ha='center', va='center', fontsize=10, fontweight='bold', color=RED,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF0F0', edgecolor=RED, alpha=0.8))

    ax.set_xlabel('漏洞出现率 (%)', fontsize=12)
    ax.set_yticks(x)
    ax.set_yticklabels(vulns, fontsize=10)
    ax.set_xlim(0, 95)
    ax.legend(fontsize=10, loc='lower right')
    ax.set_title('图11  第14次作业五类安全漏洞出现率对比', fontsize=14, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)

    fig.savefig(os.path.join(OUT, '图11_第14次作业五类安全漏洞出现率对比.png'))
    plt.close(fig)
    print('[OK] Fig11 done')


# ── Run all ────────────────────────────────────────────────────
if __name__ == '__main__':
    fig1_flowchart()
    fig6_similarity()
    fig7_review_time()
    fig8_sql_injection()
    fig12_radar()
    fig9_core_metrics()
    fig10_grade_distribution()
    fig11_vulnerabilities()
    print('\nAll 8 figures generated successfully.')
