<template>
  <theme-provider id="app" :theme="theme">
    <MainPage></MainPage>
  </theme-provider>
</template>

<script>
// import LandingPage from "./views/LandingPage";
import MainPage from "./views/MainPage";

import { ThemeProvider } from "vue-styled-components";
import { THEME } from "./configuration";
export default {
  name: "App",
  data() {
    return {
      theme: THEME,
    };
  },
  mounted() {},
  components: {
    MainPage,
    ThemeProvider,
  },
};
</script>

<style>
body,
html {
  margin: 0;
  height: 100%;
  scroll-behavior: smooth !important;
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
/* The emerging W3C standard
   that is currently Firefox-only */
* {
  scrollbar-width: thin;
  scrollbar-color: #6c757d white;
}

/* Works on Chrome/Edge/Safari */
*::-webkit-scrollbar {
  width: 12px;
}
*::-webkit-scrollbar-track {
  background: white;
}
*::-webkit-scrollbar-thumb {
  background-color: #6c757d;
  border-radius: 5px;
  border: 3px solid white;
}
@media screen and (min-width: 320px) and (max-width: 767px) and (orientation: landscape) {
  html {
    transform: rotate(-90deg);
    transform-origin: left top;
    width: 100vh;
    overflow-x: hidden;
    position: absolute;
    top: 100%;
    left: 0;
  }
}
</style>
