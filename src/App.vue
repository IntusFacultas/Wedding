<template>
  <div id="app">
    <LandingPage></LandingPage>
  </div>
</template>

<script>
import LandingPage from "./views/LandingPage";

export default {
  name: "App",
  components: {
    LandingPage,
  },
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
h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: "Trajan Pro 3";
}
</style>
