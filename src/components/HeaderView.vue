<template>
  <v-app-bar app color="primary" dark class="header">
    <v-container>
      <v-row class="header-row">
        <v-col cols="1"></v-col>
        <v-col cols="10" style="text-align: center;">
          <v-toolbar-title> Logo </v-toolbar-title>
        </v-col>
        <v-col cols="1" style="text-align: right;">
          <a href=""><v-icon class="header-icon">mdi-phone</v-icon></a>
        </v-col>
      </v-row>
    </v-container>
  </v-app-bar>
</template>

<style scoped>
.header {
  padding: 0 10%;
}

/* .header-logo {
  display: flex;
  justify-content: center;
  align-items: center;
} */

.header-icon {
  width: auto;
  border-radius: 100px;
  padding: 10%;
  background-color:cornflowerblue;
  animation: shake 0.5s;
  animation-delay: 1s;

}


@keyframes shake {
  0% { transform: rotate(0deg); }
  15% { transform: rotate(-25deg); }
  25% { transform: rotate(-35deg); }
  45% { transform: rotate(-45deg); }
  55% { transform: rotate(-55deg); }
  65% { transform: rotate(-45deg); }
  75% { transform: rotate(-35deg); }
  85% { transform: rotate(-25deg); }
  100% { transform: rotate(0deg); }
}
</style>
