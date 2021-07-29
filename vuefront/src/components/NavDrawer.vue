<template>
    <v-navigation-drawer 
    v-model="$store.state.showNav"
    app 
    >
        <v-card-title dark>
            homepage
        </v-card-title>
        <v-list-item  v-for="category, key in categories" :key="key">
            
            <v-list-item-content>
                <v-list-item-title>{{ key }}</v-list-item-title>
                <v-list-item-subtitle  class="mt-4" v-for="subcategory, subkey in category" :key="subkey">{{ subkey }}
                    <v-divider />
                    <div v-for="cat, subsubkey in subcategory" :key="subsubkey">
                        <v-btn class="ma-3" outlined x-small  @click="getItems(cat)">
                            {{ cat }}
                        </v-btn>
                    </div>
                </v-list-item-subtitle>
                
            </v-list-item-content>
            
        </v-list-item>
    </v-navigation-drawer>
</template>
<script>
import axios from 'axios'
import categories from '@/assets/category_dummy.json'
export default {
    data() {
        return {
            items: null,
            categories: categories
        }
    },
    computed:{
        controlDrawer(){
            return this.$store.state.showNav;
        }
    },
    methods:{
        async getItems(category){
            console.log(category)
            var res = await axios.get(`/api/v1/items/${category}/0/40`)
            var data = res.data
            this.$store.state.items = data

        }
    }
}
</script>