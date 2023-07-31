<template>
  <div>
    <Header />
    <router-view></router-view>
    <v-container class="my-container text-center" center fluid>
      <Main />
    </v-container>
    
    <Footer />
  </div>
</template>

<style scoped>
.my-container {
  margin-top: 10%;
  width: 80%;

}
@media only screen and (max-width: 600px) {
  .my-container {
    width: 100%;
  }
}

</style>

<script>
import Header from '../components/HeaderView.vue';
import Main from '../components/MainSection.vue';
import Footer from '../components/FooterView.vue';

export default {
  components: {
    Header,
    Main,
    Footer,
  },
};
</script>