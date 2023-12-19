<template>
    <div
        class="flex flex-col bg-slate-100 shadow-lg dark:bg-slate-700 rounded-lg overflow-auto h-96"
    >
        <div class="flex flex-row border-b justify-between mx-4 p-4">
            <div class="text-2xl">Addresse</div>
            <button v-if="!showForm" @click="updateProfile">bearbeiten</button>
            <button v-if="showForm" @click="updateProfile">abbrechen</button>
        </div>
        <div v-if="showForm">
            <profile-address-update />
        </div>
        <div
            v-else
            class="mx-4 flex flex-col space-y-6 divide-y divide-slate-400"
        >
            <div class="pt-3">
                <label class="text-sm"> Straße </label>
                <div>{{ profileInfo.street }}</div>
            </div>
            <div class="pt-3">
                <label class="text-sm"> Huas nummer </label>
                <div>{{ profileInfo.nr }}</div>
            </div>
            <div class="pt-3">
                <label class="text-sm"> PLZ </label>
                <div>{{ profileInfo.PLZ }}</div>
            </div>
            <div class="pt-3">
                <label class="text-sm"> Stadt </label>
                <div>{{ profileInfo.city }}</div>
            </div>
        </div>
    </div>
</template>
<script>
import ProfileAddressUpdate from '@/components/profile/updat/ProfileAddressUpdate.vue';
import { useProfileStore } from '@/stores/accounts/user-details';
import { computed, onMounted } from 'vue';
export default {
    name: 'profileInformation',
    components: {
        ProfileAddressUpdate
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
