<template>
    <div class="hidden sm:inline">
        <div
            class="grid grid-cols-2 items-center sm:mt-8 text-slate-700 sm:mr-5 dark:text-slate-100"
        >
            <div
                class="flex col-span-1 border-r border-r-slate-300 items-center text-center flex-col px-2 py-5"
            >
                <i
                    class="px-6 py-5 border-slate-500 text-slate-500 dark:text-slate-100 rounded-full border mb-5"
                >
                    <font-awesome-icon size="4x" icon="fa-solid fa-user" />
                </i>
                <div class="font-bold text-2xl">
                    {{ patientInfo.last_name }}, {{ patientInfo.first_name }}
                </div>
                <div class="text-slate-300 mb-6">test</div>
                <div class="p-3">Termine</div>
                <div class="flex flex-row">
                    <div class="px-3 my-3 border-r border-r-slate-300">
                        <span class="font-bold">4</span><br />
                        <span class="text-slate-500"> Vergangen </span>
                    </div>
                    <div class="px-3 my-3">
                        <span class="font-bold">2</span><br />
                        <span class="text-slate-500"> Aktive </span>
                    </div>
                </div>
                <a
                    :href="`mailto:${patientInfo.email}`"
                    class="py-3 px-8 rounded-xl my-3 dark:text-slate-100 text-sky-700 dark:bg-sky-900 dark:hover:bg-sky-700 dark:border-0 border border-sky-700 hover:bg-sky-700 hover:text-slate-100"
                >
                    Send Email
                </a>
            </div>
            <div class="sm:grid flex-col mt-5 sm:grid-cols-2">
                <div class="col-span-1">
                    <div class="grid grid-rows-4">
                        <div class="grid row-span-1 text-start ml-4 p-5">
                            <span class="text-slate-500 inline-block mb-4"
                                >Geschlecht</span
                            >
                            <span
                                v-if="patientInfo.gender === 'F'"
                                class="border-b border-b-slate-300 pb-2"
                            >
                                Weiblich
                            </span>
                            <span
                                v-if="patientInfo.gender === 'M'"
                                class="border-b border-b-slate-300 pb-2"
                            >
                                Männlich
                            </span>
                        </div>
                        <div class="grid row-span-1 text-start ml-4 p-5">
                            <span class="text-slate-500 inline-block mb-4"
                                >Mobile</span
                            >
                            <span
                                class="border-b border-b-slate-300 pb-2 whitespace-nowrap"
                                >{{ patientInfo.phone }}</span
                            >
                        </div>
                        <div class="grid row-span-1 text-start ml-4 p-5">
                            <span class="text-slate-500 inline-block mb-4"
                                >Stadt</span
                            >
                            <span class="border-b border-b-slate-300 pb-2">{{
                                patientInfo.city
                            }}</span>
                        </div>
                        <div class="grid row-span-1 text-start ml-4 p-5">
                            <span class="text-slate-500 inline-block mb-4"
                                >active seit</span
                            >
                            <span class="pb-2">{{
                                dateTime(patientInfo.created_at)
                            }}</span>
                        </div>
                    </div>
                </div>
                <div class="col-span-1">
                    <div class="grid grid-rows-4">
                        <div class="grid row-span-1 text-start ml-4 p-5">
                            <span class="text-slate-500 inline-block mb-4"
                                >geborn am</span
                            >
                            <span class="border-b border-b-slate-300 pb-2">{{
                                patientInfo.date_of_birth
                            }}</span>
                        </div>

                        <div class="grid row-span-1 text-start ml-4 p-5">
                            <span class="text-slate-500 inline-block mb-4"
                                >Addresse</span
                            >
                            <span class="border-b border-b-slate-300 pb-2">{{
                                patientInfo.street
                            }}</span>
                        </div>
                        <div class="grid row-span-1 text-start ml-4 p-5">
                            <span class="text-slate-500 inline-block mb-4"
                                >PLZ</span
                            >
                            <span class="border-b border-b-slate-300 pb-2">{{
                                patientInfo.postal_code
                            }}</span>
                        </div>
                        <div class="grid row-span-1 text-start ml-4 p-5">
                            <span class="text-slate-500 inline-block mb-4"
                                >Status</span
                            >
                            <span class="pb-2">im Haus</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="inline sm:hidden">
        <patient-info-mobile />
    </div>
</template>
<script>
import { useRoute } from 'vue-router';
import { usePatientStore } from '@/stores/patient/patient';
import { computed, onMounted, ref, watch } from 'vue';
import PatientInfoMobile from '@/components/patient/view/mobileView/patientInfoMobile.vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import dateTime from '../../setUp/global/date-filter';

export default {
    methods: { dateTime },
    components: { FontAwesomeIcon, PatientInfoMobile },
    setup() {
        const route = useRoute();
        const store = usePatientStore();
        const id = ref(route.params.id);

        const fetchData = async () => {
            await store.getPatient(id.value);
        };

        watch(
            () => route.params.id,
            (newId) => {
                id.value = newId;
                fetchData();
            }
        );

        onMounted(fetchData);

        const patientInfo = computed(() => store.patient);

        return { patientInfo };
    }
};
</script>
