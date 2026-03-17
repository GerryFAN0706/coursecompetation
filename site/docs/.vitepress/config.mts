import { defineConfig } from "vitepress";

export default defineConfig({
  title: "Java Web AI教学创新实践",
  description: "Java Web应用开发课程人工智能教学创新实践展示网站",
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
      { text: "教学资源", link: "/resources/" },
      { text: "评审路径", link: "/review-path/" }
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
            { text: "课程概览", link: "/course/" },
            { text: "推广与复用", link: "/promotion/" },
            { text: "关于", link: "/about/" },
            { text: "评审路径", link: "/review-path/" }
          ]
        }
      ]
    },
    socialLinks: [
      { icon: "github", link: "https://github.com/gerryfan0706/coursecompetation" }
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
