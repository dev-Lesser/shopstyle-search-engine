<template>
  <v-app>
    <v-app-bar
      app
      color="blue-grey darken-3"
      dark
    >
      <v-app-bar-nav-icon 
      @click="$store.state.showNav = !$store.state.showNav">
      </v-app-bar-nav-icon>
    </v-app-bar>
    <nav-drawer />
    <v-main>
      <Main/>
    </v-main>
  </v-app>
</template>

<script>
import Main from '@/components/Main';
import NavDrawer from '@/components/NavDrawer';

export default {
  name: 'App',

  components: {
    Main,NavDrawer
  },

  data: () => ({
    //
  }),
};
</script>
