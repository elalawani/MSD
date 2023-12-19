<template>
    <div id="app">
        <nav-bar />

        <router-view />

        <toast />
    </div>
</template>
<script>
import NavBar from './components/bars/navbar.vue';
import toast from '../src/components/toast.vue';
import { useUserStore } from '@/stores/accounts/user';
import axios from 'axios';

export default {
    name: 'app',
    setup() {
        const userStore = useUserStore();

        return {
            userStore
        };
    },
    beforeCreate() {
        this.userStore.initStore();
        const token = this.userStore.user.access;

        if (token) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
        } else {
            axios.defaults.headers.common['Authorization'] = '';
        }
    },
    components: {
        NavBar,
        toast
    }
};
</script>
