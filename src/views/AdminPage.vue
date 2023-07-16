<template>
    <v-container>
      <h2>Admin Page</h2>
      <v-file-input v-model="selectedFile" label="Choose Image" accept="image/*"></v-file-input>
      <v-btn @click="uploadImage">Upload</v-btn>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        selectedFile: null,
      };
    },
    methods: {
      uploadImage() {
        // Here, you can write the logic to upload the selected file to your server
        console.log('Selected file:', this.selectedFile);
        // Reset the selected file after upload
        this.selectedFile = null;
      },
    },
  };
  </script>
  