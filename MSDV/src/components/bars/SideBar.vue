<template>
    <div
        class="border-t sm:border-t-0 sm:border-r border-t-slate-500 border-r-slate-500 sm:top-[21%] flex fixed w-full bottom-0 sm:bottom-1/4 backdrop-blur z-50 sm:flex-col justify-around items-center sm:w-auto"
    >
        <router-link
            :to="`/details/${id}/info`"
            class="relative m-2 sm:m-4 p-3 group"
        >
            <i
                class="p-3 dark:shadow-none text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 border-4 border-slate-500 hover:border-slate-700 dark:hover:border-slate-300 rounded-full hover:cursor-pointer"
            >
                <font-awesome-icon icon="fa-solid fa-user" />
            </i>
            <div class="hidden md:flex justify-center">
                <div
                    class="absolute whitespace-nowrap font-bold top-14 text-xs transition-all scale-0 duration-100 ease-linear group-hover:scale-100"
                >
                    PATIENT INFO
                </div>
            </div>
        </router-link>
        <router-link
            :to="`/details/${id}/questionnaire`"
            class="relative m-2 sm:m-4 p-3 group sm:block hidden"
        >
            <i
                class="py-2.5 px-4 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 border-4 border-slate-500 hover:border-slate-700 dark:hover:border-slate-300 rounded-full hover:cursor-pointer"
            >
                <font-awesome-icon icon="fa-solid fa-info" />
            </i>
            <div class="hidden md:flex justify-center">
                <div
                    class="absolute whitespace-nowrap font-bold top-14 text-xs transition-all scale-0 duration-100 ease-linear group-hover:scale-100"
                >
                    Fragebögen
                </div>
            </div>
        </router-link>
        <router-link
            :to="`/details/${id}/sensor`"
            class="relative m-2 sm:m-4 p-3 group md:block hidden"
        >
            <i
                class="p-3 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 border-4 border-slate-500 hover:border-slate-700 dark:hover:border-slate-300 rounded-full hover:cursor-pointer"
            >
                <font-awesome-icon icon="fa-solid fa-stethoscope" />
            </i>
            <div class="hidden md:flex justify-center">
                <div
                    class="absolute whitespace-nowrap font-bold top-14 text-xs transition-all scale-0 duration-100 ease-linear group-hover:scale-100"
                >
                    Sensors
                </div>
            </div>
        </router-link>
        <router-link
            :to="`/details/${id}/conversation`"
            class="relative m-2 sm:m-4 p-3 group"
        >
            <i
                class="p-3 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 border-4 border-slate-500 hover:border-slate-700 dark:hover:border-slate-300 rounded-full hover:cursor-pointer"
            >
                <font-awesome-icon icon="fa-solid fa-message" />
            </i>
            <div class="hidden md:flex justify-center">
                <div
                    class="absolute whitespace-nowrap font-bold top-14 text-xs transition-all scale-0 duration-100 ease-linear group-hover:scale-100"
                >
                    Nachrichten
                </div>
            </div>
        </router-link>
        <router-link
            :to="`/details/${id}/documentation`"
            class="relative m-2 sm:m-4 p-3 group"
        >
            <i
                class="p-3 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 border-4 border-slate-500 hover:border-slate-700 dark:hover:border-slate-300 rounded-full hover:cursor-pointer"
            >
                <font-awesome-icon icon="fa-solid fa-book-medical" />
            </i>
            <div class="hidden md:flex justify-center">
                <div
                    class="absolute whitespace-nowrap font-bold top-14 text-xs transition-all scale-0 duration-100 ease-linear group-hover:scale-100"
                >
                    Dokumentation
                </div>
            </div>
        </router-link>
    </div>
</template>
<script setup>
import { useRoute } from 'vue-router';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

let id = useRoute().params.id;
</script>
<style scoped>
.router-link-active i {
    color: rgb(203 213 225);
    border-radius: 50%;
    border: 4px solid rgb(203 213 225);
    width: 50%;
    height: 50%;
    box-shadow: 0 10px 20px rgb(100 116 139);
}
</style>
