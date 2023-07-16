<template>
  <v-container>
    <v-row justify-center >
      <v-col cols="12" sm="8" style="width: auto; margin: 0 auto;">
        <v-carousel v-model="activeIndex" hide-delimiters>
      <v-carousel-item v-for="(item, index) in images" :key="index" :src="item.src" :alt="item.alt" cover>
      </v-carousel-item>
    </v-carousel>
    <v-row class="small-images">
      <v-col v-for="(item, index) in images" :key="index" cols="auto">
        <v-btn icon :class="{'active': index === activeIndex}" @click="activeIndex = index">
          <v-img :src="item.src" :alt="item.alt" width="50" height="50"></v-img>
        </v-btn>
      </v-col>
    </v-row>
            <h1><b>About Us</b></h1>
            <br>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium tellus ac dolor posuere, id semper arcu vestibulum.</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: 0,
      images: [
        { src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', alt: 'Image 1' },
        { src: 'https://cdn.vuetifyjs.com/images/cards/hotel.jpg', alt: 'Image 2' },
        { src: 'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg', alt: 'Image 3' },
      ],
    };
  },
};
</script>

<style scoped>
.small-images {
  display: flex;
  justify-content: center;
  margin-top: 16px;
}

.small-images .v-btn {
  margin-right: 8px;
}

.active .v-btn {
  background-color: blue !important;
}

.about-card {
  margin-top: 24px;
  box-shadow: none;
  border: none
}

@media only screen and (max-width: 600px) {
  .v-carousel {
    max-width: 80%;
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
