import DefaultTheme from "vitepress/theme";
import "./custom.css";
import DataDashboard from "./components/DataDashboard.vue";
import SamplePlaceholderBoard from "./components/SamplePlaceholderBoard.vue";
import StudentEvidenceShowcase from "./components/StudentEvidenceShowcase.vue";

export default {
  ...DefaultTheme,
  enhanceApp({ app }) {
    app.component("DataDashboard", DataDashboard);
    app.component("SamplePlaceholderBoard", SamplePlaceholderBoard);
    app.component("StudentEvidenceShowcase", StudentEvidenceShowcase);
  }
};
