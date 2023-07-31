<template>
  <v-container>
    <v-row justify-center>
      <v-col cols="12" style="width: auto; margin: 0 auto;">
        <v-carousel v-model="activeIndex" hide-delimiters cycle :show-arrows="false">
          <v-carousel-item v-for="(item, index) in images" :key="index" :src="item.src" :alt="item.alt" fill></v-carousel-item>
        </v-carousel>

        <v-scroll-x v-if="images.length > 1" class="small-images">
          <v-btn
            v-for="(item, index) in images"
            :key="index"
            icon
            :class="{'active': index === activeIndex}"
            @click="activeIndex = index"
          >
            <v-img :src="item.src" :alt="item.alt" width="50" height="50"></v-img>
          </v-btn>
        </v-scroll-x>

        <div class="small-images" v-else>
          <v-btn v-for="(item, index) in images" :key="index" icon>
            <v-img :src="item.src" :alt="item.alt" width="50" height="50"></v-img>
          </v-btn>
        </div>

        <!-- start of promotion sector -->

        <v-container>
          <v-row justify-center>
            <v-col v-for="card in cards" :key="card.title" cols="12" sm="6" md="4" lg="3">
              <v-card class="card-item">
                <v-img
                  :src="card.src" 
                  height="200px"
                  gradient="to left, rgba(0,0,0,.1), rgba(0,0,0,.6)"
                  style="display: flex; align-items: flex-start;">
                  <v-card-title class="promo-text">{{ card.title }}</v-card-title>
                </v-img>
                <v-card-actions>
                  <v-btn class="promo-link" text>Learn More</v-btn>
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
/* corusel sector */
.small-images {
    display: flex;
    margin: 20px auto;
    overflow-x: auto;
    white-space: nowrap;
}

.small-images .v-btn {
    margin: 10px;
}

/* promo sector */
.card-item {
  color: white
}
.promo-text{
  color: white;
}
.promo-link {
    font-size: 14px;
    color: #007bff;
    text-decoration: none;
}

.promo-link:hover {
    text-decoration: underline;
}

@media only screen and (max-width: 600px) {

    .small-images {
        margin-top: 8px;
    }
}
</style>
