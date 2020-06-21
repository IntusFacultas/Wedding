<template>
  <footer-container>
    <footer-line>
      <text-content>Website&nbsp;&nbsp;&copy; Copyright &nbsp;</text-content>
      <text-content>Pedro Del Moral Lopez</text-content>
    </footer-line>
    <footer-line>
      <text-content>Photography &copy; Copyright &nbsp;</text-content>
      <text-content>Larrison Photography</text-content>
    </footer-line>
  </footer-container>
</template>

<script>
import styled from "vue-styled-components";
import { TextContent } from "@IntusFacultas/typography";
const FooterContainer = styled("footer")`
  background-color: white;
  height: 100px;
  position: absolute;
  bottom: 0;
  left: 0;
  border-top: 1px solid #707070;
  right: 0;
  padding: 0 2em;
  display: flex;
  flex-direction: column;
  justify-content: center;
`;
const FooterLine = styled("section")`
  padding: 0.5em 0;
  //   display: flex;
  display: block;
  & > span:first-child {
    margin-right: 5px;
  }
  & > span {
    display: inline-block;
  }
  @media screen and (max-width: 500px) {
    & > span:first-child {
      width: 200px;
    }
  }
`;
const FooterText = styled("div")`
  display: flex;
  flex-direction: column;
  width: 50%;
  min-width: 350px;
  max-width: 840px;
`;
export const CopyrightFooter = {
  components: {
    FooterContainer,
    TextContent,
    FooterLine,
    FooterText
  }
};
export default CopyrightFooter;
</script>