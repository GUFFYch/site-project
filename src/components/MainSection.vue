<template>
  <v-container>
    <v-row justify-center>
      <v-col cols="12" style="width: auto; margin: 0 auto;">
        <v-carousel v-model="activeIndex" hide-delimiters>
          <v-carousel-item v-for="(item, index) in images" :key="index" :src="item.src" :alt="item.alt" cover></v-carousel-item>
        </v-carousel>

        <!-- Use v-row with dense and scroll properties for horizontal scrolling -->
        <v-row class="small-images">
          <v-btn
            v-for="(item, index) in images"
            :key="index"
            icon
            :class="{'active': index === activeIndex}"
            @click="activeIndex = index"
          >
            <v-img :src="item.src" :alt="item.alt" width="50" height="50"></v-img>
          </v-btn>
        </v-row>

        <!-- start of promotion sector -->
        <v-container fluid>
  <v-row dense style="margin-top: 40px" class="cards-row">
    <v-col v-for="card in cards" :key="card.title" :cols="card.flex" class="card-col">
      <v-card class="card-item">
        <v-img
          :src="card.src"
          class="white-text align-end"
          gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.2)"
          height="200px"
        >
          <v-card-title></v-card-title>
        </v-img>

        <v-card-actions>
          {{ card.title }}
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</v-container>

        <!-- end of promotion sector -->

        <h1><b>About Us</b></h1>
        <br />
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: 0,
      images: [],
      cards: [
                { title: 'Сказочные закаты на дороге', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 3 },
                { title: 'Незабываемые путешествия в дальные страны', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3 },
              ],
    }
  },
  mounted() {
    this.loadImagesFromAssets();
  },
  methods: {
    loadImagesFromAssets() {
      const requireContext = require.context('../assets/corusel_imges', false, /\.(png|jpe?g|svg)$/);
      this.images = requireContext.keys().map((fileName) => ({
        src: requireContext(fileName),
        alt: fileName.split('/').slice(-1)[0],
      }));
    },
  },
};
</script>

<style scoped>
.small-images {
  display: flex;
  margin: 20px auto;
  overflow-x: auto;
  white-space: nowrap;
}

.small-images .v-btn {
  margin: 10px;
}

.about-card {
  margin-top: 24px;
  box-shadow: none;
  border: none;
}

.promotion-block {
  display: flex;
  align-items: center;
  margin-top: 40px;
}

.promo-image {
  max-width: 200px;
  margin-right: 20px;
}

.promo-text {
  flex: 1;
}

.promo-text h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

.promo-text p {
  font-size: 16px;
  margin-bottom: 20px;
}

.promo-link {
  font-size: 14px;
  color: #007bff;
  text-decoration: none;
}

.promo-link:hover {
  text-decoration: underline;
}

.cards-row {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
}

.card-col {
  padding: 5px;
}

.card-item {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}


@media only screen and (max-width: 600px) {
  .v-carousel {
    max-width: 100%;
    margin: 0 auto;
  }

  .small-images {
    margin-top: 8px;
  }

  .about-card {
    margin-top: 16px;
  }
}

</style>
