<template>
    <div
        class="flex flex-col bg-slate-100 shadow-lg dark:bg-slate-700 rounded-lg overflow-auto h-96"
    >
        <div class="flex flex-row border-b justify-between mx-4 p-4">
            <div class="text-2xl">Kontakt Information</div>
            <button v-if="!showForm" @click="updateProfile">bearbeiten</button>
            <button v-if="showForm" @click="updateProfile">abbrechen</button>
        </div>
        <div v-if="showForm">
            <profile-update />
        </div>
        <div
            v-else
            class="mx-4 flex flex-col space-y-6 divide-y divide-slate-400"
        >
            <div class="pt-3">
                <label class="text-sm"> Vorname </label>
                <div>{{ profileInfo.first_name }}</div>
            </div>
            <div class="pt-3">
                <label class="text-sm"> Nachname </label>
                <div>{{ profileInfo.last_name }}</div>
            </div>
            <div class="pt-3">
                <label class="text-sm"> Kontakt Email </label>
                <div>{{ profileInfo.email }}</div>
            </div>
            <div class="pt-3">
                <label class="text-sm"> Username </label>
                <div>{{ profileInfo.username }}</div>
            </div>
            <div class="pt-3">
                <label class="text-sm"> geschlecht </label>
                <div v-if="profileInfo.gender === 'M'">Männlich</div>
                <div v-else-if="profileInfo.gender === 'F'">Weiblich</div>
                <div v-else>-</div>
            </div>
            <div class="pt-3">
                <label class="text-sm"> Mobile </label>
                <div>leer</div>
            </div>
        </div>
    </div>
</template>
<script>
import ProfileUpdate from '@/components/profile/updat/ProfileUpdate.vue';
import { useProfileStore } from '@/stores/accounts/user-details';
import { computed, onMounted } from 'vue';
export default {
    name: 'profileInformation',
    components: {
        ProfileUpdate
    },
    setup() {
        const profileStore = useProfileStore();

        const getProfile = async () => {
            await profileStore.getProfileInfo();
        };
        onMounted(getProfile);
        const profileInfo = computed(() => profileStore.infos);

        return {
            profileInfo
        };
    },
    data() {
        return {
            showForm: false
        };
    },
    methods: {
        updateProfile() {
            this.showForm = !this.showForm;
        }
    }
};
</script>
