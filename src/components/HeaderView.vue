<template>
  <v-app-bar app color="primary" dark class="header">
    <v-container>
      <v-row class="header-row">
        <v-col cols="12" class="header-logo-col">
          <v-toolbar-title class="header-logo">Logo</v-toolbar-title>
        </v-col>
      </v-row>
    </v-container>
    <a href=""><v-icon class="header-icon">mdi-phone</v-icon></a>
  </v-app-bar>
</template>

<style scoped>
.header {
  padding: 0 10%;
}

.header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header-logo-col {
  text-align: center;
}

.header-logo {
  display: flex;
  justify-content: center;
  align-items: center;
}

.header-icon {
  float:right;
  width: 40px;
  height: 40px;
  border-radius: 100%;
  padding: 10px;
  background-color: cornflowerblue;
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
