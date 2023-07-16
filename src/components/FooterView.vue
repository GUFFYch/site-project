<template>
  <v-footer app>
    <v-container fluid>
      <v-row justify="center">
        <v-col cols="12" sm="4">
          <v-row justify="center" align="center">
            <v-col cols="auto">
              <v-icon color="blue" size="24">mdi-phone</v-icon>
            </v-col>
            <v-col cols="auto">
              <span class="footer-info">123-456-7890</span>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="12" sm="4">
          <v-row justify="center" align="center">
            <v-col cols="auto">
              <v-icon color="blue" size="24">mdi-map-marker</v-icon>
            </v-col>
            <v-col cols="auto">
              <span class="footer-info">123 Main Street, City, Country</span>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="12" sm="4">
          <v-row justify="center" align="center">
            <v-col cols="auto">
              <v-img src="path/to/logo.png" width="24" height="24" alt="Logo"></v-img>
            </v-col>
            <v-col cols="auto">
              <span class="footer-info">Your Logo</span>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<style scoped>
footer {
  position: relative;
  padding: 10px 20%;
  text-align: center;
  bottom: 0;
  left: 0;
  width: 100%;
}
</style>