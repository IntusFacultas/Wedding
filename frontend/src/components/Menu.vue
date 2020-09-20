<template>
  <div class="menusection">
    <section-title id="menu" class="detailssection__title">Menu</section-title>
    <flex-row>
      <div :md="6" :sm="12" class="menusection__column">
        <section-title>Passed Hors D'Oeuvres</section-title>
        <div class="menusection__item">
          <div>
            <category-title>Edamame Pot Sticker</category-title>
            <paragraph :size="14" class="menusection__subtext">with Spicy Soy</paragraph>
          </div>
          <img :src="`${STATIC_URL}${potsticker}`" alt class="menusection__item__img" />
        </div>
        <div class="menusection__item">
          <img
            :src="`${STATIC_URL}${chickensatay}`"
            alt="image of chicken satay"
            class="menusection__item__img"
          />
          <div>
            <category-title>Chicken Satay</category-title>
            <paragraph :size="14" class="menusection__subtext">with Peanut Sauce</paragraph>
          </div>
        </div>
        <div class="menusection__item">
          <category-title class>Teque&ntilde;os</category-title>
          <img
            :src="`${STATIC_URL}${tequeno}`"
            alt="image of a tequeno"
            class="menusection__item__img"
          />
        </div>
        <div class="menusection__item">
          <img
            :src="`${STATIC_URL}${toast}`"
            alt="image of spicy tuna tartar on guacamole toast"
            class="menusection__item__img"
          />
          <div>
            <category-title>Spicy Tuna Tartar on Guacamole Toast</category-title>
            <paragraph class="menusection__subtext" :size="14">with Guasacaca</paragraph>
          </div>
        </div>
      </div>
      <div :md="6" :sm="12" class="menusection__column">
        <div class="menusection__station">
          <section-title>Station I - Indonesian</section-title>
          <div class="menusection__item menusection__itemsection">
            <img
              :src="`${STATIC_URL}${rijsttafel}`"
              alt="image of indonesian rijsttafel"
              class="menusection__item__img"
            />
            <div class="menusection__item__content--block">
              <category-title>Indonesian Rijsttafel</category-title>
              <list class="menusection__subtext">
                <list-item>Steamed Rice</list-item>
                <list-item>Chili Paste</list-item>
                <list-item>Cucumber, Green Bean and Tomato Salad</list-item>
                <list-item>Sweet Indonesian Soy Sauce</list-item>
                <list-item>Cabbage in Peanut Sauce</list-item>
                <list-item>Curried Lentils</list-item>
                <list-item>Chicken Curry</list-item>
                <list-item>Toasted Coconut &amp; Ground Peanuts</list-item>
                <list-item>Warm Nan Bread</list-item>
              </list>
            </div>
          </div>
        </div>
        <div class="menusection__station">
          <section-title>Station II - Chinese</section-title>
          <div class="menusection__item menusection__itemsection">
            <img
              :src="`${STATIC_URL}${seafood}`"
              alt="image of indonesian rijsttafel"
              class="menusection__item__img firefox-fix"
            />
            <div class="menusection__item__content--block">
              <category-title>
                Chinese Seafood Dish served with towers of Cantonese Spinach
                Salad
              </category-title>
              <list class="menusection__subtext">
                <list-item>with Sprouts,</list-item>
                <list-item>Water Chestnuts,</list-item>
                <list-item>Hard Boiled Egg,</list-item>
                <list-item>and Bacon*</list-item>
              </list>
              <paragraph class="menusection__subtext">* some without bacon for vegetarians</paragraph>
            </div>
          </div>
        </div>
        <div class="menusection__station">
          <section-title>Station III - Latino</section-title>
          <div class="menusection__item menusection__itemsection">
            <img
              :src="`${STATIC_URL}${empanadas}`"
              alt="image of indonesian rijsttafel"
              class="menusection__item__img"
            />
            <div class="menusection__item__content--block">
              <category-title>Carved Chimichurri Skirt Steak</category-title>
              <list class="menusection__subtext">
                <list-item>with Ripe Plantains,</list-item>
                <list-item>Cheese Empanadas,</list-item>
                <list-item>and Cilantro Mojo Grilled Assorted Vegetables</list-item>
              </list>
            </div>
          </div>
        </div>
      </div>
    </flex-row>
  </div>
</template>

<script>
import {
  Paragraph,
  SectionTitle,
  SubSectionTitle,
  CategoryTitle,
} from "@IntusFacultas/typography";
import { FlexRow, FlexColumn } from "@IntusFacultas/layout";
import { List, ListItem } from "@IntusFacultas/list";
// Images
import chickensatay from "../assets/chicken-satay.jpg";
import tequeno from "../assets/tequenos.png";
import potsticker from "../assets/edamame_potstickers.jpg";
import toast from "../assets/spicy-tuna-tartare-avocado-toast.jpg";
import rijsttafel from "../assets/rijsttafel.jpeg";
import seafood from "../assets/seafood-birds.jpg";
import empanadas from "../assets/steak and empanadas.png";
export const Menu = {
  data() {
    return {
      chickensatay,
      tequeno,
      toast,
      empanadas,
      seafood,
      potsticker,
      rijsttafel,
      STATIC_URL: process.env.VUE_APP_STATIC_URL,
    };
  },
  components: {
    Paragraph,
    SectionTitle,
    SubSectionTitle,
    CategoryTitle,
    FlexRow,
    FlexColumn,
    List,
    ListItem,
  },
};
export default Menu;
</script>

<style>
.menusection {
  text-align: center;
  max-width: 1600px;
  margin-left: auto;
  margin-right: auto;
}
.menusection__column {
  display: flex;
  flex: 1;
  align-items: center;
  justify-content: flex-start;
  flex-direction: column;
  width: 50%;
}
.menusection__station {
  margin-top: 1em;
}
.menusection__station:first-of-type {
  margin-top: 0;
}
.menusection__item__img {
  height: 200px;
  width: 151px;
  /* margin: 0 0.5em; */
  clip-path: circle(42%);
}
.menusection__title {
  font-size: 1.8em;
  /* margin: 1.5em 0em 0.5em 0; */
}
.menusection__subtext {
  font-style: italic;
  font-weight: 400;
  font-size: 14px;
}
ul.menusection__subtext {
  text-align: left;
}
ul.menusection__subtext li {
  padding-left: 0.5em;
}
.menusection__item {
  /* margin: 0 auto;
  margin-top: 1em; */
  display: flex;
  justify-content: space-around;
  width: 500px;
  align-items: center;
}

@media screen and (max-width: 1066px) {
  .menusection__column {
    width: 100%;
  }
}
.menusection__item__content--block {
  text-align: left;
}
@media screen and (min-width: 451px) {
  .menusection__column:nth-of-type(2) {
    border-left: 2px solid #dedede;
  }
}
@media screen and (max-width: 450px) {
  .menusection__item__content--block {
    width: 100%;
    text-align: center;
  }
  .menusection__itemsection {
    flex-direction: column;
  }
  .menusection__itemsection li {
    text-align: left;
  }
  .menusection__column {
    max-width: 300px;
    margin-left: auto;
    margin-right: auto;
  }
  .menusection__item {
    width: 300px;
  }
}
.menusection__station h2 {
  margin-bottom: 0.5em !important;
}
@-moz-document url-prefix() {
  .firefox-fix {
    height: 220px;
    clip-path: circle();
  }
}
</style>
