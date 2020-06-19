<template>
  <!-- <img :src="svg" alt="" /> -->
  <landing-page-container>
    <LandingPageBackground :svg="svg">
      <span>HI</span>
    </LandingPageBackground>
  </landing-page-container>
</template>

<script>
import styled from "vue-styled-components";
const props = {
  svg: String,
};
const LandingPageContainer = styled("div", props)`
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
`;
const LandingPageBackground = styled("div", props)`
  background-image: url("data:image/svg+xml, ${(props) => props.svg}");
  background-position: center;
  background-repeat: repeat;
  height: 100%;
  width: 100%;
`;
export const LandingPage = {
  components: {
    LandingPageBackground,
    LandingPageContainer,
  },
  data() {
    return {
      svg: () => import("../components/background-svg.js"),
    };
  },
  mounted() {
    let self = this;
    this.svg().then((response) => {
      self.svg = response.default;
      console.log(self.svg);
    });
  },
};
export default LandingPage;
</script>
