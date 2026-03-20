import { defineConfig } from "vitepress";

export default defineConfig({
  title: "第六届教学创新大赛成果展示",
  description: "第六届全国高校教师教学创新大赛 · 人工智能赛道 — Java Web应用开发课程AI教学创新成果展示",
  lang: "zh-CN",
  base: "/coursecompetation/",
  cleanUrls: true,
  lastUpdated: true,

  head: [
    ["link", { rel: "preconnect", href: "https://fonts.googleapis.com" }],
    ["link", { rel: "preconnect", href: "https://fonts.gstatic.com", crossorigin: "" }],
    ["link", { href: "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+SC:wght@400;500;700;900&display=swap", rel: "stylesheet" }]
  ],

  markdown: {
    lineNumbers: true
  },

  themeConfig: {
    logo: { light: "/assets/svg/logo.svg", dark: "/assets/svg/logo.svg" },
    siteTitle: "教学创新大赛成果展示",
    nav: [
      { text: "首页", link: "/" },
      {
        text: "教学创新",
        items: [
          { text: "AI教学创新设计", link: "/innovation/" },
          { text: "核心案例：第15讲", link: "/cases/lesson-15/" },
          { text: "课程概览（16讲）", link: "/course/" }
        ]
      },
      { text: "成效数据", link: "/results/" },
      {
        text: "教学资源",
        items: [
          { text: "资源总览", link: "/resources/" },
          { text: "AI提示词库", link: "/resources/prompts/" },
          { text: "学生成果展示", link: "/resources/student-evidence/" }
        ]
      },
      { text: "推广复用", link: "/promotion/" },
      { text: "评审路径", link: "/review-path/" }
    ],

    sidebar: {
      "/": [
        {
          text: "总览",
          items: [
            { text: "首页", link: "/" },
            { text: "评审快速路径", link: "/review-path/" },
            { text: "关于本项目", link: "/about/" }
          ]
        },
        {
          text: "教学创新设计",
          collapsed: false,
          items: [
            { text: "AI教学创新设计", link: "/innovation/" },
            { text: "核心案例：第15讲", link: "/cases/lesson-15/" },
            { text: "课程概览（16讲）", link: "/course/" }
          ]
        },
        {
          text: "成效与成果",
          collapsed: false,
          items: [
            { text: "成效与数据", link: "/results/" },
            { text: "学生成果展示", link: "/resources/student-evidence/" }
          ]
        },
        {
          text: "教学资源",
          collapsed: false,
          items: [
            { text: "资源总览", link: "/resources/" },
            { text: "AI提示词库", link: "/resources/prompts/" }
          ]
        },
        {
          text: "推广与复用",
          items: [
            { text: "推广方案", link: "/promotion/" }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: "github", link: "https://github.com/gerryfan0706/coursecompetation" }
    ],

    footer: {
      message: "第六届全国高校教师教学创新大赛 · 人工智能赛道 · 成果展示",
      copyright: "Copyright © 2026 · AI赋能Java Web应用开发课程教学创新"
    },

    search: {
      provider: "local"
    },

    outline: {
      level: [2, 3],
      label: "页面导航"
    },

    lastUpdated: {
      text: "最后更新",
      formatOptions: { dateStyle: "medium" }
    },

    docFooter: {
      prev: "上一页",
      next: "下一页"
    }
  }
});
