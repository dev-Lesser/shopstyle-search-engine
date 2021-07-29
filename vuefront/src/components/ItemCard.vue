<template>
    <v-card class="ma-3">
        <router-link :to="pageURL">
       <v-img
          :src="this.image"
          aspect-ratio="0.6"
          
        ></v-img>
        </router-link>

        <v-card-title>
            {{brand}} 
        </v-card-title>
        <v-divider />
        <v-card-subtitle>{{ name }}</v-card-subtitle>
        <!-- <v-card-subtitle>{{description}}</v-card-subtitle> -->
        <v-divider/>
        <span v-for="color,key in colors"  :key="key">
            <v-chip class="ma-3" small outlined >{{ color.name }} </v-chip>
        </span>

        <span v-for="category,key in categories"  :key="key">
            <v-chip class="ma-3" small outlined >{{ category.id }} </v-chip>
        </span>


        <v-divider/>
        <v-card-actions>
            
            <v-card-subtitle >
            ${{ price }}
            </v-card-subtitle>
        <v-spacer />
            <v-card-subtitle style="color: red;">
            {{ discount }} %
            </v-card-subtitle>
            <v-card-subtitle>
                <v-icon small >mdi-heart</v-icon>
                {{ favoriteCnt }}
            </v-card-subtitle>

        </v-card-actions>
        
    </v-card>
</template>
<script>
export default {
    props:{
        item: Object
    },
    data() {
        return {
            image: null,
            brand: null,
            brandLogo: null,
            colors : null,
            favoriteCnt: null,
            name: null,
            discount: null,
            price: null,
            pageURL: null,
            categories: null,
            

        }
        
    },
    mounted(){
        this.image = this.item.image.sizes.Best.url
        this.brand = this.item.brand.name
        // this.brandLogo = this.item.brand.logo.sizes.default.url
        this.colors = this.item.colors
        this.description = this.item.description
        this.favoriteCnt = this.item.favoriteCount
        this.name = this.item.name
        this.discount = this.item.discount
        this.price = this.item.price
        this.pageURL = this.item.pageUrl
        this.categories = this.item.categories

    }
    
}
</script>