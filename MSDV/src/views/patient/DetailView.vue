<template>
    <div class="mt-8 mx-2 flex flex-col-reverse sm:flex-row">
        <div>
            <side-bar />
        </div>
        <div
            class="sm:ml-36 border shadow-xl dark:border-none dark:bg-slate-800 text-slate-100 rounded sm:mr-5 2xl:w-[90%] sm:w-[85%] w-full h-5/6 overflow-auto mb-16 sm:mb-0 chatScroll"
        >
            <router-view></router-view>
        </div>
    </div>
</template>
<script>
import { usePatientStore } from '@/stores/patient/patient';
import { useRoute } from 'vue-router';
import sideBar from '@/components/bars/sideBar.vue';
import { computed } from 'vue';

export default {
    components: {
        sideBar
    },
    setup() {
        const route = useRoute();
        const id = computed(() => route.params.id);

        const patientStore = usePatientStore();
        patientStore.getPatient(id.value);
    }
};
</script>
