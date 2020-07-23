<template>
  <flex-row>
    <flex-column :md="12" :col="6" class="accomodation__mapcontainer">
      <div v-html="hotel.map"></div>
    </flex-column>
    <flex-column :md="12" :col="6" class="accomodation__details">
      <category-title class="accomodation__hoteltitle">{{hotel.title}}</category-title>
      <paragraph class="accomodation__hotel">
        <text-content :bold="true">Address:</text-content>
        {{hotel.address}}
      </paragraph>
      <paragraph>
        <text-content :bold="true">Distance to Carnegie Center:</text-content>
        {{hotel.distanceToEvent}} miles
      </paragraph>
      <paragraph>
        <text-content :bold="true">Distance to Pedro's Family:</text-content>
        {{hotel.distanceToFamily}} miles
      </paragraph>
      <paragraph class="accomodation__stars">
        <svg
          class="accomodation__stars__star"
          v-for="n in hotel.stars"
          :key="`star-${n}`"
          enable-background="new 0 0 50 50"
          height="50px"
          id="Layer_1"
          version="1.1"
          viewBox="0 0 50 50"
          width="50px"
          xml:space="preserve"
          xmlns="http://www.w3.org/2000/svg"
          xmlns:xlink="http://www.w3.org/1999/xlink"
        >
          <rect fill="none" height="50" width="50" />
          <polygon
            fill="gold"
            points="25,3.553 30.695,18.321 46.5,19.173   34.214,29.152 38.287,44.447 25,35.848 11.712,44.447 15.786,29.152 3.5,19.173 19.305,18.321 "
            stroke="gold"
            stroke-miterlimit="10"
            stroke-width="2"
          />
        </svg>
      </paragraph>
    </flex-column>
  </flex-row>
</template>

<script>
import { FlexColumn, FlexRow } from "@IntusFacultas/layout";

import {
  CategoryTitle,
  Paragraph,
  TextContent,
} from "@IntusFacultas/typography";
export const Hotel = {
  components: { CategoryTitle, Paragraph, TextContent, FlexColumn, FlexRow },
  props: {
    hotel: Object,
  },
};
export default Hotel;
</script>

<style>
.accomodation__hoteltitle {
  font-size: 20px;
  text-align: left;
}

.accomodation__mapcontainer {
  justify-content: center;
  align-items: center;
}
.accomodation__details {
  flex-direction: column;
  align-items: start;
  justify-content: center;
}
@media screen and (max-width: 400px) {
  .accomodation__hoteltitle {
    text-align: center;
  }
  .accomodation__details {
    align-items: center;
  }
}
.accomodation__stars__star {
  height: 30px;
  width: 30px;
}
</style>