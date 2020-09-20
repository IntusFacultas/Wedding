<template>
  <timeline-container
    :timeline-flavor="timelineFlavor"
    :timeline-color="timelineColor"
    :width="width"
  >
    <timeline-section
      v-for="(item, index) in items"
      :key="index"
      :item-color="item.color ? item.color : defaultItemColor"
      :item-flavor="item.flavor ? item.flavor : defaultItemFlavor"
      :circle-color="item.circleColor ? item.circleColor : defaultCircleColor"
      :circle-flavor="item.circleFlavor ? item.circleFlavor : defaultCircleFlavor"
      :circle-customization="item.circleCustomization"
      :left="index % 2 == 0"
    >
      <timeline-content
        :item-color="item.color ? item.color : defaultItemColor"
        :item-flavor="item.flavor ? item.flavor : defaultItemFlavor"
      >
        <div v-html="item.content"></div>
      </timeline-content>
    </timeline-section>
  </timeline-container>
</template>

<script>
import styled from "vue-styled-components";
import Theme from "@IntusFacultas/design-system";
const props = {
  width: String,
  timelineColor: String,
  timelineFlavor: String,
  circleColor: String,
  circleFlavor: String,
  itemColor: String,
  itemFlavor: String,
  circleCustomization: String,
  left: Boolean,
  defaultTheme: {
    type: Object,
    default() {
      return Theme;
    },
  },
};
const TimelineContainer = styled("div", props)`
  box-sizing: border-box;
  // margin: 0 auto;
  position: relative;
  max-width: ${(props) => props.width};
  margin-left: auto;
  margin-right: auto;
  &::after {
    content: "";
    position: absolute;
    width: 6px;
    background-color: ${(props) =>
      props.timelineColor
        ? props.timelineColor
        : props.theme && props.theme[props.timelineFlavor]
        ? props.theme[props.timelineFlavor].background.color
        : props.defaultTheme[props.timelineFlavor]
        ? props.defaultTheme[props.timelineFlavor].background.color
        : "#d7d7d7"};
    top: 0;
    bottom: 0;
    left: 50%;
    // margin-left: -3px;
  }
  & * {
    box-sizing: border-box;
  }
  @media screen and (max-width: 600px) {
    &::after {
      left: 31px;
    }
  }
  @media screen and (max-height: 450px) {
    &::after {
      left: 31px;
    }
  }
`;
const TimelineSection = styled("div", props)`
  padding: 10px 40px;
  position: relative;
  background-color: white;
  width: 50%;
  &::after {
    content: "";
    position: absolute;
    width: 25px;
    height: 25px;
    right: -17px;
    background-color: ${(props) =>
      props.circleColor
        ? props.circleColor
        : props.theme && props.theme[props.circleFlavor]
        ? props.theme[props.circleFlavor].background.color
        : props.defaultTheme[props.circleFlavor]
        ? props.defaultTheme[props.circleFlavor].background.color
        : "#d7d7d7"};
    border-width: 4px;
    border-style: solid;
    border-color: ${(props) =>
      props.circleColor
        ? props.circleColor
        : props.theme && props.theme[props.circleFlavor]
        ? props.theme[props.circleFlavor].border.color
        : props.defaultTheme[props.circleFlavor]
        ? props.defaultTheme[props.circleFlavor].border.color
        : "#ff9f55"};
    top: 15px;
    border-radius: 50%;
    z-index: 1;
  }
  ${(props) =>
    props.left
      ? `
        left: 0;
        &::before {
            content: " ";
            height: 0;
            position: absolute;
            top: 22px;
            width: 0;
            z-index: 1;
            right: 30px;
            border: medium solid ${
              props.itemColor
                ? props.itemColor
                : props.theme && props.theme[props.itemFlavor]
                ? props.theme[props.itemFlavor].border.color
                : props.defaultTheme[props.itemFlavor]
                ? props.defaultTheme[props.itemFlavor].border.color
                : "white"
            };
            border-width: 10px 0 10px 10px;
            border-color: transparent transparent transparent ${
              props.itemColor
                ? props.itemColor
                : props.theme && props.theme[props.itemFlavor]
                ? props.theme[props.itemFlavor].border.color
                : props.defaultTheme[props.itemFlavor]
                ? props.defaultTheme[props.itemFlavor].border.color
                : "white"
            };
        }
    `
      : `
        &::after {
            left: -16px;
        }
        left: 50%;
        &::before {
            content: " ";
            height: 0;
            position: absolute;
            top: 22px;
            width: 0;
            z-index: 1;
            left: 30px;
            border: medium solid ${
              props.itemColor
                ? props.itemColor
                : props.theme && props.theme[props.itemFlavor]
                ? props.theme[props.itemFlavor].border.color
                : props.defaultTheme[props.itemFlavor]
                ? props.defaultTheme[props.itemFlavor].border.color
                : "white"
            };
            border-width: 10px 10px 10px 0;
            border-color: transparent ${
              props.itemColor
                ? props.itemColor
                : props.theme && props.theme[props.itemFlavor]
                ? props.theme[props.itemFlavor].border.color
                : props.defaultTheme[props.itemFlavor]
                ? props.defaultTheme[props.itemFlavor].border.color
                : "white"
            } transparent transparent;
        }
  `}

  @media screen and (max-width: 600px) {
    width: 100%;
    padding-left: 70px;
    padding-right: 25px;

    &::before {
      left: 60px;
      border-style: solid;
      border-width: 10px 10px 10px 0;
      border-color: transparent
        ${(props) =>
          props.itemColor
            ? props.itemColor
            : props.theme && props.theme[props.itemFlavor]
            ? props.theme[props.itemFlavor].border.color
            : props.defaultTheme[props.itemFlavor]
            ? props.defaultTheme[props.itemFlavor].border.color
            : "white"}
        transparent transparent;
    }
    &::after {
      left: 15px;
    }
    ${(props) => (props.left ? `` : `left: 0%;`)}
  }
  @media screen and (max-height: 450px) {
    width: 100%;
    padding-left: 70px;
    padding-right: 25px;

    &::before {
      left: 60px;
      border-style: solid;
      border-width: 10px 10px 10px 0;
      border-color: transparent
        ${(props) =>
          props.itemColor
            ? props.itemColor
            : props.theme && props.theme[props.itemFlavor]
            ? props.theme[props.itemFlavor].border.color
            : props.defaultTheme[props.itemFlavor]
            ? props.defaultTheme[props.itemFlavor].border.color
            : "white"}
        transparent transparent;
    }
    &::after {
      left: 15px;
    }
    ${(props) => (props.left ? `` : `left: 0%;`)}
  }
  &::after {
    ${(props) => props.circleCustomization}
  }
`;
const TimelineContent = styled("div", props)`
  padding: 20px 30px;
  background-color: ${(props) =>
    props.itemColor
      ? props.itemColor
      : props.theme && props.theme[props.itemFlavor]
      ? props.theme[props.itemFlavor].background.color
      : props.defaultTheme[props.itemFlavor]
      ? props.defaultTheme[props.itemFlavor].background.color
      : "#d7d7d7"};
  border: 1px solid
    ${(props) =>
      props.itemColor
        ? props.itemColor
        : props.theme && props.theme[props.itemFlavor]
        ? props.theme[props.itemFlavor].border.color
        : props.defaultTheme[props.itemFlavor]
        ? props.defaultTheme[props.itemFlavor].border.color
        : "#d7d7d7"};
  position: relative;
  border-radius: 5px;
`;
export const Timeline = {
  components: {
    TimelineContainer,
    TimelineSection,
    TimelineContent,
  },
  props: {
    defaultItemColor: String,
    defaultItemFlavor: { type: String, default: "Light" },
    defaultCircleFlavor: { type: String, default: "Secondary" },
    defaultCircleColor: String,
    timelineFlavor: { type: String, default: "Secondary" },
    timelineColor: String,
    width: { type: String, default: "1200px" },
    items: Array,
  },
};
export default Timeline;
</script>