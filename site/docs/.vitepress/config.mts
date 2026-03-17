import { defineConfig } from "vitepress";

export default defineConfig({
  title: "Java Web AI教学创新实践",
  description: "人工智能赛道参赛网站（Phase 1）",
  lang: "zh-CN",
  base: "/coursecompetation/",
  cleanUrls: true,
  lastUpdated: true,
  themeConfig: {
    nav: [
      { text: "首页", link: "/" },
      { text: "AI教学创新设计", link: "/innovation/" },
      { text: "核心案例", link: "/cases/lesson-15/" },
      { text: "成效与数据", link: "/results/" },
      { text: "教学资源", link: "/resources/" }
    ],
    sidebar: {
      "/": [
        {
          text: "快速导航",
          items: [
            { text: "首页", link: "/" },
            { text: "AI教学创新设计", link: "/innovation/" },
            { text: "核心案例：第15讲", link: "/cases/lesson-15/" },
            { text: "成效与数据", link: "/results/" },
            { text: "教学资源", link: "/resources/" },
            { text: "课程概览（占位）", link: "/course/" },
            { text: "推广与复用（占位）", link: "/promotion/" },
            { text: "关于（占位）", link: "/about/" }
          ]
        }
      ]
    },
    socialLinks: [
      { icon: "github", link: "https://github.com/" }
    ],
    footer: {
      message: "人工智能赛道网站（匿名评审可切换资源）",
      copyright: "Copyright © 2026"
    },
    search: {
      provider: "local"
    }
  }
});
