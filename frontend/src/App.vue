<template>
  <theme-provider id="app" :theme="theme">
    <div class="router-view">
      <LandingPage></LandingPage>
    </div>
    <CopyrightFooter></CopyrightFooter>
  </theme-provider>
</template>

<script>
import LandingPage from "./views/LandingPage";
import CopyrightFooter from "./components/CopyrightFooter";
import { ThemeProvider } from "vue-styled-components";
import Scrollbar from "smooth-scrollbar";
import { THEME } from "./configuration";
export default {
  name: "App",
  data() {
    return {
      theme: THEME
    };
  },
  mounted() {
    Scrollbar.init(document.querySelector("#app"));
  },
  components: {
    LandingPage,
    ThemeProvider,
    CopyrightFooter
  }
};
</script>

<style>
body,
html {
  margin: 0;
  height: 100%;
}
#app {
  height: 100%;
}
#app * {
  font-family: Montserrat;
}
.router-view {
  padding-bottom: 117px;
}
h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: "Trajan Pro 3" !important ;
  margin-block-end: 0;
  margin-bottom: 0 !important;
}
</style>
