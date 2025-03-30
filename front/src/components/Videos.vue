<script setup lang="ts">
import { ref, watch } from 'vue';
import { useFetch } from './fetch.ts';

const game = ref("");
let { data, error, loading, fetchData } = useFetch();

function get_videos() {
    fetchData(`http://127.0.0.1:8000/videos/?game_name=${game.value}`);
}
</script>

<template>
    <section>
        <input type="text" v-model="game" placeholder="Enter a game name"/>
        <button @click="get_videos">Search</button>
        <p v-if="loading">Loading...</p>
        <p v-if="error">{{ error }}</p>
        <ol v-if="data">
            <li v-for="video in data" :key="video.id">
                {{ video.title }}
                <img :src="video.thumbnail_url.replace('%{width}', '480').replace('%{height}', '234')" alt="{{ video.title }}" loading="lazy">
                <a :href="video.url"></a>
            </li>
        </ol>
    </section>
</template>
