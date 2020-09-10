<template>
  <div class="detailssection">
    <section-title id="dresscode" class="detailssection__title">Dress Code</section-title>
    <paragraph>We can’t wait to see you on the dance floor (dancing is mandatory). Keep this in mind when choosing your outfit!</paragraph>
    <paragraph>The venue has air conditioning, but June weather in Cincinnati can be unforgivingly hot and humid.</paragraph>
    <paragraph>
      The general rule of thumb is
      <strong>semi-formal.</strong>
    </paragraph>
    <flex-row>
      <flex-column :md="6" :sm="12" class="dresscodecolumn">
        <img class="dress__img" :src="dress" alt="Women's dress" />
        <section-title>Ladies</section-title>
        <paragraph>Ladies, wear what you feel most comfortable in. If that means a dress, suit or skirt, then great!</paragraph>
        <paragraph>
          <strong>Note:</strong> The bride will be wearing red.
        </paragraph>
      </flex-column>
      <flex-column :md="6" :sm="12" class="dresscodecolumn">
        <img :src="suit" alt="Men's suit" class="dress__img" />
        <section-title>Gentlemen</section-title>
        <paragraph>Gentlemen, two-piece suits, sports jackets, or just a vest and tie are all great options for the event!</paragraph>
        <paragraph>We only ask that you avoid a three-piece suit, as the bridal party will be wearing three-piece suits.</paragraph>
      </flex-column>
    </flex-row>
  </div>
</template>

<script>
import dress from "../assets/dress.svg";
import suit from "../assets/suit.svg";
import {
  SectionTitle,
  SubSectionTitle,
  Paragraph,
} from "@IntusFacultas/typography";
import { FlexRow, FlexColumn } from "@IntusFacultas/layout";
export const DressCode = {
  data() {
    return {
      dress,
      suit,
    };
  },
  components: {
    SectionTitle,
    SubSectionTitle,
    FlexRow,
    FlexColumn,
    Paragraph,
  },
};
export default DressCode;
</script>

<style>
.dress__img {
  height: 130px;
}
.dresscodecolumn {
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}
</style>