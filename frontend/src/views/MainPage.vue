<template>
  <main class="mainpage">
    <Navbar></Navbar>
    <background-image :img="picture2" height="80vh" :positioning="picture2Formatting">
      <page-title class="backgroundimage__title" flavor="White">
        April
        <span class="backgroundimage__ampersand">&amp;</span> Pedro
      </page-title>
      <paragraph
        class="backgroundimage__subtext"
        flavor="White"
      >June 12th, 2021 &bull; Cincinnati, Ohio</paragraph>
      <ScrollIndicator
        class="backgroundimage__scrollindicator"
        flavor="White"
        textFlavor="White"
        :theme="theme"
      ></ScrollIndicator>
    </background-image>
    <content-section>
      <OurStory></OurStory>
    </content-section>
    <background-image id="details" :img="picture1" height="80vh" :positioning="picture1Formatting">
      <page-title class="backgroundimage__title" flavor="White">Details</page-title>
    </background-image>
    <content-section>
      <ul class="detailsnavigation">
        <li>
          <a href="#travel">Travel</a>
        </li>
        <li>
          <a href="#accomodation">Accomodation</a>
        </li>
        <li>
          <a href="#schedule">Schedule</a>
        </li>
        <li>
          <a href="#menu">Menu</a>
        </li>
        <li>
          <a href="#dresscode">Dress Code</a>
        </li>
        <li>Wedding Party</li>
      </ul>
      <Travel></Travel>
      <Accomodation></Accomodation>
    </content-section>
    <background-image id="details" :img="picture4" height="80vh" :positioning="picture4Formatting"></background-image>
    <content-section>
      <Schedule></Schedule>
      <Menu></Menu>
    </content-section>
    <background-image id="details" :img="picture5" height="80vh" :positioning="picture5Formatting"></background-image>
    <content-section>
      <DressCode></DressCode>
    </content-section>
    <CopyrightFooter></CopyrightFooter>
  </main>
</template>

<script>
import Navbar from "../components/Navbar";
import CopyrightFooter from "../components/CopyrightFooter";
import ScrollIndicator from "../components/ScrollIndicator";
import styled from "vue-styled-components";
import picture1 from "../assets/picture1.png";
import picture2 from "../assets/picture2.png";
import picture4 from "../assets/picture4.jpg";
import picture5 from "../assets/picture5.jpg";
import OurStory from "../components/OurStory";
import Travel from "../components/Travel";
import Schedule from "../components/Schedule";
import DressCode from "../components/DressCode";
import Menu from "../components/Menu";
import Accomodation from "../components/Accomodation";
import { PageTitle, Paragraph } from "@IntusFacultas/typography";
import VSWoff from "../assets/VladimirScript.woff";
import VSWoff2 from "../assets/VladimirScript.woff2";
import { THEME } from "../configuration";
import Background from "../assets/Wedding Background Optimized.svg";
const props = {
  img: String,
  height: String,
  positioning: String,
};
const BackgroundImage = styled("div", props)`
  background-image: url("${process.env.VUE_APP_STATIC_URL}${(props) =>
    props.img}");
  height: ${(props) => props.height};
  background-attachment: fixed;
  background-size: cover;
  background-repeat: no-repeat;
  ${(props) => props.positioning}
  position:relative;
  background-color: #444;
  display: flex;
  padding: 0 1em;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  @font-face {
    font-family: "Vladimir Script";
    src: url("${process.env.VUE_APP_STATIC_URL}${VSWoff}") format("woff2"),
      url("${process.env.VUE_APP_STATIC_URL}${VSWoff2}") format("woff");
    font-weight: normal;
    font-style: normal;
    font-display: swap;
  }
`;
const ContentSection = styled.div`
  &::before {
    background: linear-gradient(
        to top,
        rgba(255, 255, 255, 0) -65%,
        rgba(255, 255, 255, 1)
      ),
      url("${process.env.VUE_APP_STATIC_URL}${Background}");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
    content: "";
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -2;
    opacity: 0.1;
  }
  position: relative;
  padding: 1em 2em;
  @media screen and (max-width: 450px) {
    text-align: center;
    & * {
      text-align: center;
    }
  }
`;
export const MainPage = {
  components: {
    PageTitle,
    Paragraph,
    BackgroundImage,
    CopyrightFooter,
    ScrollIndicator,
    ContentSection,
    Travel,
    Menu,
    Accomodation,
    OurStory,
    Navbar,
    Schedule,
    DressCode,
  },
  data() {
    return {
      theme: THEME,
      picture1,
      picture1Formatting: `
        background-position: center center;
        @media screen and (min-width: 1700px) {
          background-position: center -200px;
        }
        @media screen and (min-width: 1820px) {
          background-position: center -250px;
        }
        @media screen and (min-width: 1900px) {
          background-position: center -280px;
        }
        @media screen and (min-width: 2100px) {
          background-position: center -310px;
        }
        @media screen and (max-width: 450px) {
            background-position: 40% center;
            background-attachment: scroll;
        }
      `,
      picture2,
      picture2Formatting: `
        background-position:center -165px;
        @media screen and (min-width: 2030px) {
            background-position:center -380px;
        }
        @media screen and (max-width: 800px ) {
          background-position: 40% -165px;
        }
        @media screen and (max-width: 670px ) {
          background-position: 30% -165px;
        }
        @media screen and (max-width: 450px) {
            background-position: 40% center;
            background-attachment: scroll;
        }
      `,
      picture4,
      picture4Formatting: ``,
      picture5,
      picture5Formatting: `
        background-position: center -628px;
      `,
      STATIC_URL: process.env.VUE_APP_STATIC_URL,
    };
  },
};
export default MainPage;
</script>

<style>
.backgroundimage__title {
  font-size: 50px;
  text-shadow: 2px 2px #000;
  text-align: center;
}
.mainpage {
  display: block;
  height: 200vh;
}

.backgroundimage__ampersand {
  font-family: "Vladimir Script" !important;
  font-size: 90px;
}
.backgroundimage__subtext {
  font-size: 19px;
  text-shadow: 2px 2px #000;
}
.backgroundimage__scrollindicator {
  position: absolute;
  bottom: 15px;
  text-align: center;
  margin-left: auto;
  margin-right: auto;
}

.detailsnavigation {
  display: flex;
  justify-content: center;
  list-style: none;
  padding-left: 0px;
  flex-wrap: wrap;
  border-bottom: 2px solid #444;
}
@media screen and (max-width: 450px) {
  .detailsnavigation {
    flex-direction: column;
    align-items: center;
  }
}
.detailsnavigation li {
  cursor: pointer;

  font-size: 18px;
  padding: 0.5em 2em;
}
.detailsnavigation li > a {
  text-decoration: none;
  color: #444;
}
.detailsnavigation li > a:visited {
  color: #444;
}
.detailsnavigation li > a:hover {
  color: #444;
}
.detailsnavigation li:after {
  transition: all 0.25s;
  content: "";
  display: block;
  margin: 0 auto;
  width: 0%;
  padding-top: 2.5px;
  border-bottom: 2px solid #444;
}

.detailsnavigation li:hover::after {
  transition: all 0.25s;
  content: "";
  display: block;
  margin: 0 auto;
  width: 100%;
  padding-top: 2.5px;
  border-bottom: 2px solid #444;
}

@media screen and (max-width: 990px) {
  .ourstory__paragraphs {
    border-left: 0px solid white;
  }
}
</style>
