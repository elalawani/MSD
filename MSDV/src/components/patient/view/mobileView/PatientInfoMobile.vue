<template>
    <div class="flex flex-col items-center justify-center">
        <swiper
            :slides-per-view="1"
            :space-between="10"
            :loop="true"
            :pagination="{ clickable: true }"
            :navigation="{
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev'
            }"
            class="w-full"
        >
            <swiper-slide>
                <div class="rounded-xl">
                    <div class="p-4">
                        <div
                            class="flex items-center text-center flex-col px-2 py-5"
                        >
                            <i
                                class="px-6 py-5 border-slate-500 text-slate-500 dark:text-slate-100 rounded-full border mb-5"
                            >
                                <font-awesome-icon
                                    size="4x"
                                    icon="fa-solid fa-user"
                                />
                            </i>
                            <div class="font-bold text-2xl">
                                {{ patientInfo.last_name }},
                                {{ patientInfo.first_name }}
                            </div>
                            <div class="text-slate-300 mb-6">test</div>
                            <div class="p-3">Termine</div>
                            <div class="flex flex-row">
                                <div
                                    class="px-3 my-3 border-r border-r-slate-300"
                                >
                                    <span class="font-bold">4</span><br />
                                    <span class="text-slate-500">
                                        vergangen
                                    </span>
                                </div>
                                <div class="px-3 my-3">
                                    <span class="font-bold">2</span><br />
                                    <span class="text-slate-500"> active </span>
                                </div>
                            </div>
                            <button
                                class="py-3 px-8 rounded-xl my-3 dark:text-slate-100 text-sky-700 dark:bg-sky-900 dark:hover:bg-sky-700 dark:border-0 border border-sky-700 hover:bg-sky-700 hover:text-slate-100"
                            >
                                Send Email
                            </button>
                            swipe to see more >>
                        </div>
                    </div>
                </div>
            </swiper-slide>
            <swiper-slide>
                <div class="rounded-xl overflow-auto p-4">
                    <div class="flex-col">
                        <div class="grid text-start ml-4 p-5">
                            <span class="text-slate-500 inline-block mb-4"
                                >Gender</span
                            >
                            <span class="border-b border-b-slate-300 pb-2">{{
                                patientInfo.gender
                            }}</span>
                        </div>
                        <div class="grid text-start ml-4 p-5">
                            <span class="text-slate-500 inline-block mb-4"
                                >Phone</span
                            >
                            <span
                                class="border-b border-b-slate-300 pb-2 whitespace-nowrap"
                                >{{ patientInfo.phone }}</span
                            >
                        </div>
                        <div class="grid text-start ml-4 p-5">
                            <span class="text-slate-500 inline-block mb-4"
                                >birthdate</span
                            >
                            <span class="border-b border-b-slate-300 pb-2">{{
                                patientInfo.date_of_birth
                            }}</span>
                        </div>

                        <div class="grid text-start ml-4 p-5">
                            <span class="text-slate-500 inline-block mb-4"
                                >active seit</span
                            >
                            <span class="pb-2">12.05.2020</span>
                        </div>
                    </div>
                </div>
            </swiper-slide>
            <swiper-slide>
                <div class="rounded-xl p-4">
                    <div class="flex-col">
                        <div class="grid text-start ml-4 p-5">
                            <span class="text-slate-500 inline-block mb-4"
                                >City</span
                            >
                            <span class="border-b border-b-slate-300 pb-2">{{
                                patientInfo.city
                            }}</span>
                        </div>

                        <div class="grid text-start ml-4 p-5">
                            <span class="text-slate-500 inline-block mb-4"
                                >Address</span
                            >
                            <span class="border-b border-b-slate-300 pb-2">{{
                                patientInfo.street
                            }}</span>
                        </div>
                        <div class="grid text-start ml-4 p-5">
                            <span class="text-slate-500 inline-block mb-4"
                                >PLZ</span
                            >
                            <span class="border-b border-b-slate-300 pb-2">{{
                                patientInfo.postal_code
                            }}</span>
                        </div>
                        <div class="grid text-start ml-4 p-5">
                            <span class="text-slate-500 inline-block mb-4"
                                >Status</span
                            >
                            <span class="pb-2">im Haus</span>
                        </div>
                    </div>
                </div>
            </swiper-slide>
        </swiper>
    </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
import { usePatientStore } from '@/stores/patient/patient';
import 'swiper/swiper.min.css';
import { useRoute } from 'vue-router';
import { computed, onMounted, ref, watch } from 'vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

export default {
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
    },
    components: {
        FontAwesomeIcon,
        Swiper,
        SwiperSlide
    },
    data() {
        return {
            customer: {
                id: 1,
                name: 'John Doe',
                photo: 'path_to_photo',
                address: '123 Main St, Anywhere, USA',
                lastLogin: '2023-06-21'
            }
        };
    }
};
</script>
