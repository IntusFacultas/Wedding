<template>
  <div class="detailssection">
    <section-title id="weddingparty" class="detailssection__title">Wedding Party</section-title>
    <flex-row>
      <flex-column class="weddingparty__container" :sm="12">
        <section-title class="weddingparty__container__title">Officiant</section-title>
        <div class="weddingparty__container__item">
          <img
            class="weddingparty__container__item__image"
            :src="`${STATIC_URL}${dpg}`"
            alt="Picture of Adithya, the man of honor"
          />
          <div class="weddingparty__container__item__text">
            <paragraph bold>Patrick Giblin</paragraph>
            <paragraph>Patrick Giblin is a close friend of Pedro's. He was Pedro's DARE officer in Junior High School, and shared a special relationship both with Pedro, and Pedro's Sensei.</paragraph>
          </div>
        </div>
      </flex-column>
    </flex-row>
    <flex-row>
      <flex-column :md="6" :sm="12" class="weddingparty__container">
        <section-title class="weddingparty__container__title">
          Bridesmaids
          <span class="fancyampersand fancyampersand--big">&amp;</span>
          Bridesguards
        </section-title>
        <div class="weddingparty__container__item">
          <img
            class="weddingparty__container__item__image"
            :src="`${STATIC_URL}${adithya}`"
            alt="Picture of Adithya, the man of honor"
          />
          <div class="weddingparty__container__item__text">
            <sub-section-title>Man of Honor</sub-section-title>
            <paragraph bold>Adithya Batachar</paragraph>
            <paragraph>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Impedit, est minus natus exercitationem corrupti voluptas molestias velit eligendi officia veritatis beatae expedita temporibus dolores, provident iste facere ipsam, voluptate culpa?</paragraph>
          </div>
        </div>
        <div class="weddingparty__container__item">
          <img
            class="weddingparty__container__item__image"
            :src="`${STATIC_URL}${katie}`"
            alt="Picture of Katie, the bridesmaid"
          />
          <div class="weddingparty__container__item__text">
            <sub-section-title>Bridesmaid</sub-section-title>
            <paragraph bold>Katie Thompson</paragraph>
            <paragraph>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ad, deleniti eaque? Cumque, eius saepe. Beatae nesciunt quis autem ad numquam totam dolores, tenetur placeat molestias est voluptas quas cumque sint.</paragraph>
          </div>
        </div>
      </flex-column>
      <flex-column :md="6" :sm="12" class="weddingparty__container">
        <section-title class="weddingparty__container__title">
          Groomsmen
          <span class="fancyampersand fancyampersand--big">&amp;</span>
          Groomsmaids
        </section-title>
        <div class="weddingparty__container__item">
          <img
            class="weddingparty__container__item__image"
            :src="`${STATIC_URL}${nathan}`"
            alt="Picture of Nathan, the best man"
          />
          <div class="weddingparty__container__item__text">
            <sub-section-title>Best Man</sub-section-title>
            <paragraph bold>Nathan Whitney</paragraph>
            <paragraph>Pedro and Nathan have been best friends since the 5th grade, and find common ground in throwing each other violently left, right and center.</paragraph>
          </div>
        </div>
        <div class="weddingparty__container__item">
          <img
            class="weddingparty__container__item__image"
            :src="`${STATIC_URL}${luis}`"
            alt="Picture of Luis, the best man"
          />
          <div class="weddingparty__container__item__text">
            <sub-section-title>Best Man</sub-section-title>
            <paragraph bold>Luis Del Moral Lopez</paragraph>
            <paragraph>Luis is Pedro's brother. Nuff said.</paragraph>
          </div>
        </div>
        <div class="weddingparty__container__item">
          <img
            class="weddingparty__container__item__image"
            :src="`${STATIC_URL}${dasha}`"
            alt="Picture of Dasha, the groomsmaid"
          />
          <div class="weddingparty__container__item__text">
            <sub-section-title>Groomsmaid</sub-section-title>
            <paragraph bold>Dasha Beniash</paragraph>
            <paragraph>Dasha and Pedro have been fast friends ever since Dasha's first day at Karate, where he rather rudely beat her up in front of her dad (much to his approval). Since then, they have been each other's trusted confidants.</paragraph>
          </div>
        </div>
      </flex-column>
    </flex-row>
  </div>
</template>

<script>
import {
  SectionTitle,
  SubSectionTitle,
  Paragraph,
} from "@IntusFacultas/typography";
import { FlexRow, FlexColumn } from "@IntusFacultas/layout";
import adithya from "../assets/adithya.jpg";
import katie from "../assets/katie.png";
import nathan from "../assets/nathan.jpg";
import dasha from "../assets/dasha.jpg";
import luis from "../assets/luis.jpg";
import dpg from "../assets/luis.jpg";
export const WeddingParty = {
  data() {
    return {
      STATIC_URL: process.env.VUE_APP_STATIC_URL,
      adithya,
      katie,
      nathan,
      dasha,
      luis,
      dpg,
    };
  },
  components: {
    SectionTitle,
    SubSectionTitle,
    Paragraph,
    FlexRow,
    FlexColumn,
  },
};
export default WeddingParty;
</script>

<style>
.fancyampersand--big {
  font-size: 40px;
}
.weddingparty__container {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}
.weddingparty__container__item {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin: 0.5em 0;
}
.weddingparty__container__item__image {
  height: 300px;
}
.weddingparty__container__item__text {
  display: flex;
  flex-direction: column;
  padding: 1em;
  text-align: left;
  width: 300px;
}
@media screen and (max-width: 400px) {
  .weddingparty__container__item__text {
    text-align: center;
    width: initial;
  }
  .weddingparty__container__item__image {
    /* height: initial; */
    /* max-height: 100%; */
    max-width: 300px;
    max-height: 300px;
    height: auto;
    width: auto;
    margin-left: auto;
    margin-right: auto;
    /* height: 300px; */
  }
}
</style>