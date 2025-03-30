<script setup lang="ts">
import { useFetch } from './fetch.ts';

const { data, error, loading } = useFetch("http://127.0.0.1:8000/videos/?game_name=league");
</script>

<template>
    <section>
        <p v-if="loading">Loading...</p>
        <ol v-else>
            <li v-for="video in data" :key="video.id">
                {{ video.title }}
                <img :src="video.thumbnail_url.replace('%{width}', '480').replace('%{height}', '234')" alt="{{ video.title }}" loading="lazy">
                <a :href="video.url"></a>
            </li>
        </ol>
    </section>
</template>
