<template>
    <div
        class="bg-opacity-6 text-slate-900 dark:text-slate-50 h-full rounded m-3 flex flex-col"
    >
        <div
            v-if="profileInfo.first_name"
            class="capitalize p-4 ml-4 font-extralight text-2xl"
        >
            {{ profileInfo.first_name }} {{ profileInfo.last_name }}
        </div>
        <div v-else class="capitalize p-4 ml-4 font-extralight text-2xl">
            {{ profileInfo.username }}
        </div>

        <div
            class="flex flex-row justify-around shadow-lg bg-slate-100 dark:bg-slate-700 rounded overflow-scroll scroll-auto"
        >
            <button
                @click="showProfileInformation"
                class="p-4"
                :class="
                    profileInformation
                        ? 'border-b border-b-sky-500 text-sky-500'
                        : 'border-b'
                "
            >
                Algemein
            </button>
            <button
                @click="showAddressInformation"
                class="p-4"
                :class="
                    profileAddressInformation
                        ? 'border-b border-b-sky-500 text-sky-500'
                        : 'border-b'
                "
            >
                Benutzer Info
            </button>
            <button
                @click="showAllPatients"
                class="p-4"
                :class="
                    allPatients
                        ? 'border-b border-b-sky-500 text-sky-500'
                        : 'border-b'
                "
            >
                Alle Patienten
            </button>
            <button
                v-if="profileInfo.role === 'ST'"
                @click="showMoreSettings"
                class="p-4"
                :class="
                    moreSettings
                        ? 'border-b border-b-sky-500 text-sky-500'
                        : 'border-b'
                "
            >
                mehr Einstellungen
            </button>
        </div>
        <div class="flex flex-row w-full mt-2">
            <div class="mr-2 flex flex-col min-w-[30%] max-w-[30%] grow">
                <div
                    class="rounded-lg shadow-lg bg-slate-100 dark:bg-slate-700"
                >
                    <div class="flex flex-col items-center p-2 py-8">
                        <div
                            class="w-24 h-24 flex items-center justify-center mb-3 rounded-full shadow-lg border overflow-hidden"
                        >
                            <div v-if="profileInfo.avatar === null">
                                <font-awesome-icon
                                    size="4x"
                                    icon="fa-solid fa-user"
                                />
                            </div>
                            <div v-else>
                                <img :src="profileInfo.avatar" alt="user" />
                            </div>
                        </div>
                        <div class="mb-1 text-xl font-medium dark:text-white">
                            {{ profileInfo.first_name }}
                            {{ profileInfo.last_name }}
                        </div>
                        <span
                            v-if="profileInfo.role === 'DR'"
                            class="text-sm text-gray-500 dark:text-gray-400"
                            >Arzt
                        </span>
                        <span
                            v-if="profileInfo.role === 'NR'"
                            class="text-sm text-gray-500 dark:text-gray-400"
                            >Pfleger:in</span
                        >
                        <span v-else>-</span>
                        <div class="flex mt-4 space-x-3 md:mt-6">
                            <button
                                class="px-4 py-2 text-sm text-white text-center hover:bg-sky-700 rounded-lg bg-sky-800"
                            >
                                Bearbeiten
                            </button>
                        </div>
                    </div>
                </div>
                <div
                    class="rounded-lg shadow-lg bg-slate-100 dark:bg-slate-700 p-2 flex justify-center mt-2"
                >
                    termine werden hier
                </div>
                <div
                    class="rounded-lg shadow-lg bg-slate-100 dark:bg-slate-700 p-2 flex justify-center mt-2"
                >
                    letzte anmeldung : 12.12.12
                </div>
                <div
                    class="rounded-lg shadow-lg bg-slate-100 dark:bg-slate-700 p-2 flex justify-center mt-2"
                >
                    Nachrichten
                </div>
            </div>
            <div class="grow">
                <div v-if="profileInformation">
                    <profile-information />
                </div>
                <div v-else-if="profileAddressInformation">
                    <address-information />
                </div>
                <div v-else-if="allPatients">
                    <all-patients />
                </div>
                <div v-else-if="moreSettings">
                    <more-to-patients />
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import { useProfileStore } from '@/stores/accounts/user-details';
import { computed, onMounted, ref } from 'vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import ProfileInformation from '@/components/profile/view/ProfileInformation.vue';
import AllPatients from '@/components/profile/view/AllPatients.vue';
import AddressInformation from '@/components/profile/view/AddressInformation.vue';
import MoreToPatients from '@/components/profile/view/MoreToPatients.vue';

const profileStore = useProfileStore();
const profileInformation = ref(true);
const profileAddressInformation = ref(false);
const allPatients = ref(false);
const moreSettings = ref(false);
const getProfile = async () => {
    await profileStore.getProfileInfo();
};
const showProfileInformation = () => {
    profileInformation.value = true;
    profileAddressInformation.value = false;
    allPatients.value = false;
    moreSettings.value = false;
};
const showAddressInformation = () => {
    profileInformation.value = false;
    profileAddressInformation.value = true;
    allPatients.value = false;
    moreSettings.value = false;
};
const showAllPatients = () => {
    profileInformation.value = false;
    profileAddressInformation.value = false;
    allPatients.value = true;
    moreSettings.value = false;
};

const showMoreSettings = () => {
    profileInformation.value = false;
    profileAddressInformation.value = false;
    allPatients.value = false;
    moreSettings.value = true;
};
onMounted(getProfile);
const profileInfo = computed(() => profileStore.infos);
</script>
