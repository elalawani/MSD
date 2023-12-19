<template>
    <div
        class="w-full h-screen fixed backdrop-blur z-10"
        v-if="showList"
        @click="toggleList"
    ></div>
    <div
        class="w-full h-screen fixed backdrop-blur z-10"
        v-if="showProfileList"
        @click="toggleProfileList"
    ></div>
    <nav
        class="sticky top-0 z-40 w-full backdrop-blur flex-none transition-colors duration-500 lg:z-50 lg:border-b lg:border-slate-300 dark:border-slate-300 bg-gray-50 dark:bg-transparent"
    >
        <div class="max-w-8xl mx-auto">
            <div
                class="py-4 border-b border-slate-300 lg:px-8 lg:border-0 dark:border-slate-300 mx-4 lg:mx-0"
            >
                <div class="flex items-center relative">
                    <router-link to="/" class="mr-3 flex-none w-2">
                        <span
                            class="text-slate-900 font-bold text-2xl dark:text-slate-100 w-auto h-5"
                        >
                            MSD
                        </span>
                    </router-link>
                    <div class="relative hidden lg:flex items-center ml-auto">
                        <div
                            v-if="userStore.user.isAuthenticated"
                            class="leading-6 text-slate-700 dark:text-slate-100"
                        >
                            <ul class="flex space-x-8">
                                <li>
                                    <router-link
                                        to="/"
                                        class="hover:text-sky-500 dark:hover:text-sky-400"
                                    >
                                        Home
                                    </router-link>
                                </li>
                                <li>
                                    <router-link
                                        to="/"
                                        class="hover:text-sky-500 dark:hover:text-sky-400"
                                    >
                                        notifications
                                    </router-link>
                                </li>
                                <li>
                                    <router-link
                                        to="/view"
                                        class="hover:text-sky-500 dark:hover:text-sky-400"
                                    >
                                        patients
                                    </router-link>
                                </li>
                            </ul>
                        </div>
                        <div v-else>
                            <div
                                class="flex flex-row items-center justify-center space-x-5"
                            >
                                <div
                                    class="py-1 px-6 dark:bg-sky-900 rounded-lg dark:hover:bg-sky-700 hover:bg-sky-700 dark:border-0 border border-sky-700 text-sky-700 hover:text-slate-100 dark:text-slate-100"
                                >
                                    <router-link to="/login">
                                        Sign in
                                    </router-link>
                                </div>
                                <div
                                    class="py-1 px-6 dark:bg-slate-700 rounded-lg dark:hover:bg-slate-500 hover:bg-slate-500 dark:border-0 border border-slate-700 text-slate-700 hover:text-slate-100 dark:text-slate-100"
                                >
                                    <router-link to="/signup">
                                        Sign up
                                    </router-link>
                                </div>
                            </div>
                        </div>
                        <div
                            class="flex items-center border-l border-slate-300 ml-6 pl-6 dark:border-slate-700"
                        >
                            <button type="button" @click="toggleTheme">
                                <span v-if="isDark">
                                    <light />
                                </span>
                                <span v-else>
                                    <dark />
                                </span>
                            </button>
                            <div
                                v-if="userStore.user.isAuthenticated"
                                class="ml-6 block text-slate-400 hover:text-slate-500 dark:hover:text-slate-300 relative p-3 rounded-full border border-slate-400 hover:border-slate-500 dark:hover:border-slate-300"
                            >
                                <button
                                    @click="toggleProfileList"
                                    class="items-center flex justify-center"
                                >
                                    <i class="absolute">
                                        <font-awesome-icon
                                            icon="fa-solid fa-user"
                                        />
                                    </i>
                                </button>
                            </div>
                        </div>
                    </div>
                    <button
                        type="button"
                        class="ml-auto text-slate-500 w-8 h-8 -my-1 flex items-center justify-center hover:text-slate-600 lg:hidden dark:text-slate-400 dark:hover:text-slate-300"
                    >
                        <span class="sr-only">Search</span>
                        <search />
                    </button>
                    <div class="ml-2 -my-1 lg:hidden">
                        <button
                            type="button"
                            @click="toggleList"
                            class="text-slate-500 w-8 h-8 flex items-center justify-center hover:text-slate-600 dark:text-slate-400 dark:hover:text-slate-300"
                        >
                            <span class="sr-only">Navigation</span>
                            <menu-list />
                        </button>
                    </div>
                    <div
                        v-if="showList && userStore.user.isAuthenticated"
                        class="fixed top-4 right-4 w-full max-w-xs bg-slate-50 rounded-lg shadow-lg p-6 text-slate-900 dark:bg-slate-700 dark:text-slate-300"
                    >
                        <button
                            type="button"
                            class="absolute top-5 right-5 w-8 h-8 flex items-center justify-center text-slate-500 hover:text-slate-600 dark:text-slate-400 dark:hover:text-slate-300"
                            tabindex="0"
                            @click="toggleList"
                        >
                            <span class="sr-only">Close navigation</span>
                            <cross />
                        </button>
                        <ul class="space-y-6">
                            <li>
                                <router-link
                                    to="/"
                                    @click="toggleList"
                                    class="hover:text-sky-500 dark:hover:text-sky-400"
                                >
                                    Home
                                </router-link>
                            </li>
                            <li>
                                <router-link
                                    to="/"
                                    @click="toggleList"
                                    class="hover:text-sky-500 dark:hover:text-sky-400"
                                >
                                    notifications
                                </router-link>
                            </li>
                            <li>
                                <router-link
                                    to="/view"
                                    @click="toggleList"
                                    class="hover:text-sky-500 dark:hover:text-sky-400"
                                >
                                    Patients
                                </router-link>
                            </li>
                            <li>
                                <router-link
                                    to="/profile"
                                    @click="toggleList"
                                    class="hover:text-sky-500 dark:hover:text-sky-400"
                                >
                                    Profile
                                </router-link>
                            </li>
                        </ul>
                        <div
                            class="mt-6 pt-6 border-t border-slate-200 dark:border-slate-200/10"
                        >
                            <button @click="reloadPage">logout</button>
                        </div>
                        <div
                            class="mt-6 pt-6 border-t border-slate-200 dark:border-slate-200/10"
                        >
                            <div
                                type="button"
                                @click="toggleTheme"
                                class="flex items-center justify-between"
                            >
                                switch Theme
                                <div>
                                    <span v-if="isDark">
                                        <light />
                                    </span>
                                    <span v-else>
                                        <dark />
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div
                        v-if="showList && !userStore.user.isAuthenticated"
                        class="fixed top-4 right-4 w-full max-w-xs bg-slate-50 rounded-lg shadow-lg p-6 text-slate-900 dark:bg-slate-700 dark:text-slate-300"
                    >
                        <button
                            type="button"
                            class="absolute top-5 right-5 w-8 h-8 flex items-center justify-center text-slate-500 hover:text-slate-600 dark:text-slate-400 dark:hover:text-slate-300"
                            tabindex="0"
                            @click="toggleList"
                        >
                            <span class="sr-only">Close navigation</span>
                            <cross />
                        </button>
                        <ul class="space-y-6">
                            <li>
                                <button
                                    @click="toggleList"
                                    class="py-1 px-6 w-fit rounded-lg dark:hover:bg-sky-700 hover:bg-sky-700 dark:border-0 border border-sky-700 text-sky-700 hover:text-slate-100 dark:text-slate-100"
                                >
                                    <router-link to="/login">
                                        Einloggen
                                    </router-link>
                                </button>
                            </li>
                            <li>
                                <button
                                    @click="toggleList"
                                    class="py-1 px-6 w-fit dark:bg-slate-700 rounded-lg dark:hover:bg-slate-500 hover:bg-slate-500 dark:border-0 border border-slate-700 text-slate-700 hover:text-slate-100 dark:text-slate-100"
                                >
                                    <router-link to="/signup">
                                        Registrieren
                                    </router-link>
                                </button>
                            </li>
                        </ul>
                        <div
                            class="mt-6 pt-6 border-t border-slate-200 dark:border-slate-200/10"
                        >
                            <div
                                type="button"
                                @click="toggleTheme"
                                class="flex items-center justify-between"
                            >
                                switch Theme
                                <div>
                                    <span v-if="isDark">
                                        <light />
                                    </span>
                                    <span v-else>
                                        <dark />
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="relative" v-if="userStore.user.isAuthenticated">
            <div
                v-if="showProfileList"
                class="fixed top-4 right-4 w-full max-w-xs bg-slate-50 rounded-lg shadow-lg p-6 text-slate-900 dark:bg-slate-700 dark:text-slate-300"
            >
                <button
                    type="button"
                    class="absolute top-5 right-5 w-8 h-8 flex items-center justify-center text-slate-500 hover:text-slate-600 dark:text-slate-400 dark:hover:text-slate-300"
                    tabindex="0"
                    @click="toggleProfileList"
                >
                    <span class="sr-only">Close navigation</span>
                    <cross />
                </button>
                <ul v-if="userStore.user.role === 'ST'" class="space-y-6">
                    <li>
                        <router-link
                            @click="toggleProfileList"
                            to="/"
                            class="hover:text-sky-500 dark:hover:text-sky-400"
                            >Einstellungen</router-link
                        >
                    </li>
                    <li>
                        <router-link
                            @click="toggleProfileList"
                            to="/profile"
                            class="hover:text-sky-500 dark:hover:text-sky-400"
                            >Profile</router-link
                        >
                    </li>
                    <li>
                        <router-link
                            @click="toggleProfileList"
                            to="/todolist"
                            class="hover:text-sky-500 dark:hover:text-sky-400"
                            >Todos</router-link
                        >
                    </li>
                </ul>
                <div
                    class="mt-6 pt-6 border-t border-slate-200 dark:border-slate-200/10"
                >
                    <button @click="reloadPage">logout</button>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
import { useUserStore } from '@/stores/accounts/user';
import Light from '@/components/svgs/light.vue';
import Dark from '@/components/svgs/dark.vue';
import Search from '@/components/svgs/search.vue';
import MenuList from '@/components/svgs/menuList.vue';
import Cross from '@/components/svgs/cross.vue';
import { ref, onMounted, watchEffect } from 'vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

export default {
    name: 'NavBar',
    components: { FontAwesomeIcon, Cross, MenuList, Search, Dark, Light },
    setup() {
        const userStore = useUserStore();
        const isDark = ref(localStorage.getItem('theme') === 'dark');
        const toggleTheme = () => {
            isDark.value = !isDark.value;
        };

        onMounted(() => {
            document.documentElement.classList.toggle('dark', isDark.value);
        });

        watchEffect(() => {
            document.documentElement.classList.toggle('dark', isDark.value);
            localStorage.setItem('theme', isDark.value ? 'dark' : 'light');
        });

        return {
            userStore,
            isDark,
            toggleTheme
        };
    },
    data() {
        return {
            showList: false,
            showProfileList: false,
            formState: ''
        };
    },
    methods: {
        toggleList() {
            this.showList = !this.showList;
        },

        toggleProfileList() {
            this.showProfileList = !this.showProfileList;
        },

        reloadPage() {
            this.userStore.logout();
            window.location.reload();
        }
    }
};
</script>
