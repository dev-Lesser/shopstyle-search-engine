<template>
  <v-container fluid>
    <v-layout wrap>
      <v-flex xs12 sm6 md2 v-for="n in this.resultItems" :key="n">
        <item-card :item="n"/>
      </v-flex>
    </v-layout>
 
  </v-container>
</template>

<script>
import ItemCard from '@/components/ItemCard'
  export default {
    name: 'Main',
    components:{
      ItemCard
    },
    data: () => ({
      
      
    }),
    computed:{
      resultItems(){
        return this.$store.state.items
      }
    }
  }
</script>
