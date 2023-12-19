<script setup>
import { useToastStore } from '@/stores/toast';

const store = useToastStore();
</script>
<template>
    <div
        v-if="store.isVisible"
        class="transition ease-in-out delay-[5000ms] duration-[5000ms] px-6 py-6 fixed top-3/4 right-8 rounded-xl shadow-xl"
        :class="store.classes"
    >
        {{ store.message }}
    </div>
</template>
