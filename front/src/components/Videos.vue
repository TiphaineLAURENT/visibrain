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
    <section class="section">
        <form action="javascript:void(0);">
            <div class="field">
                <label class="label">Game name</label>
                <input type="text" v-model="game" placeholder="Enter a game name" class="input"/>
                <button @click="get_videos" class="button" type="submit">Search</button>
            </div>
        </form>
        <div class="section">
            <p v-if="loading" class="notification is-info">Loading...</p>
            <p v-if="error" class="notification is-danger">{{ error }}</p>
            <div v-if="data" class="grid is-col-min-12">
                <div v-for="video in data" :key="video.id" class="cell">
                    <div class="card">
                        <div class="card-image">
                            <a :href="video.url" target="_blank">
                                <figure class="image is-16by9">
                                    <img :src="video.thumbnail_url.replace('%{width}', '640').replace('%{height}', '360')" alt="{{ video.title }}" loading="lazy" onclick="">
                                </figure>
                            </a>
                        </div>
                        <div class="card-content">
                            <p class="content">{{ video.title }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
