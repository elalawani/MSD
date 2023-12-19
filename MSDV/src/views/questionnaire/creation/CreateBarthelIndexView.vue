<template>
    <div class="p-3 flex relative flex-col text-slate-900 dark:text-slate-50">
        <div class="absolute top-0">
            <router-link
                class="font-extralight hover:text-sky-600"
                :to="`/details/${id}/questionnaire`"
            >
                &lsaquo; back
            </router-link>
        </div>
        <div class="flex flex-row justify-between items-center">
            <div class="py-4">
                patient name :
                <span>
                    {{ patient_name.last_name }}, {{ patient_name.first_name }}
                </span>
            </div>
        </div>
        <div class="h-full w-full shadow dark:bg-slate-600 rounded">
            <div class="flex flex-row justify-between items-center mb-6">
                <div class="font-bold text-2xl p-4 ml-2">barthel Index</div>
                <div class="mr-4">gesamte Zahl: {{ sum }}</div>
            </div>
            <div>
                <form>
                    <div class="flex flex-col">
                        <div
                            class="flex flex-row items-center justify-between py-4 mx-4"
                        >
                            <label for="eat" class="w-40"> Essen </label>
                            <select
                                v-model="selectedFoodOption"
                                class="bg-slate-300 text-slate-700 py-3 rounded md:w-96"
                            >
                                <option
                                    v-for="(option, index) in foodOptions"
                                    :value="option.value"
                                    :key="index"
                                >
                                    {{ option.label }}: &emsp;{{ option.value }}
                                </option>
                            </select>
                            <div class="w-4">
                                {{ selectedFoodOption }}
                            </div>
                        </div>
                        <div
                            class="flex flex-row items-center justify-between py-4 mx-4"
                        >
                            <label for="eat" class="w-40"> Waschen </label>
                            <select
                                v-model="selectedWash"
                                class="bg-slate-300 text-slate-700 py-3 rounded md:w-96"
                            >
                                <option
                                    v-for="(option, index) in wash"
                                    :value="option.value"
                                    :key="index"
                                >
                                    {{ option.label }}: &emsp;{{ option.value }}
                                </option>
                            </select>
                            <div class="w-4">
                                {{ selectedWash }}
                            </div>
                        </div>
                        <div
                            class="flex flex-row items-center justify-between py-4 mx-4"
                        >
                            <label for="eat" class="w-40"> Duschen </label>
                            <select
                                v-model="selectedShower"
                                class="bg-slate-300 text-slate-700 py-3 rounded md:w-96"
                            >
                                <option
                                    v-for="(option, index) in shower"
                                    :value="option.value"
                                    :key="index"
                                >
                                    {{ option.label }}: &emsp;{{ option.value }}
                                </option>
                            </select>
                            <div class="w-4">
                                {{ selectedShower }}
                            </div>
                        </div>
                        <div
                            class="flex flex-row items-center justify-between py-4 mx-4"
                        >
                            <label for="eat" class="w-40">
                                an- ausziehen
                            </label>
                            <select
                                v-model="selectDress"
                                class="bg-slate-300 text-slate-700 py-3 rounded md:w-96"
                            >
                                <option
                                    v-for="(option, index) in dress"
                                    :value="option.value"
                                    :key="index"
                                >
                                    {{ option.label }}: &emsp;{{ option.value }}
                                </option>
                            </select>
                            <div class="w-4">
                                {{ selectDress }}
                            </div>
                        </div>
                        <div
                            class="flex flex-row items-center justify-between py-4 mx-4"
                        >
                            <label for="eat" class="w-40">
                                Stuhlkontrolle
                            </label>
                            <select
                                v-model="selectedStool"
                                class="bg-slate-300 text-slate-700 py-3 rounded md:w-96"
                            >
                                <option
                                    v-for="(option, index) in stool"
                                    :value="option.value"
                                    :key="index"
                                >
                                    {{ option.label }}: &emsp;{{ option.value }}
                                </option>
                            </select>
                            <div class="w-4">
                                {{ selectedStool }}
                            </div>
                        </div>
                        <div
                            class="flex flex-row items-center justify-between py-4 mx-4"
                        >
                            <label for="eat" class="w-40">
                                Harnkontrolle
                            </label>
                            <select
                                v-model="selectedUrin"
                                class="bg-slate-300 text-slate-700 py-3 rounded md:w-96"
                            >
                                <option
                                    v-for="(option, index) in urin"
                                    :value="option.value"
                                    :key="index"
                                >
                                    {{ option.label }}: &emsp;{{ option.value }}
                                </option>
                            </select>
                            <div class="w-4">
                                {{ selectedUrin }}
                            </div>
                        </div>
                        <div
                            class="flex flex-row items-center justify-between py-4 mx-4"
                        >
                            <label for="eat" class="w-40">
                                Toilettenbenutzung
                            </label>
                            <select
                                v-model="selectedWC"
                                class="bg-slate-300 text-slate-700 py-3 rounded md:w-96"
                            >
                                <option
                                    v-for="(option, index) in wc"
                                    :value="option.value"
                                    :key="index"
                                >
                                    {{ option.label }}: &emsp;{{ option.value }}
                                </option>
                            </select>
                            <div class="w-4">
                                {{ selectedWC }}
                            </div>
                        </div>
                        <div
                            class="flex flex-row items-center justify-between py-4 mx-4"
                        >
                            <label for="eat" class="w-40">
                                Aufsetzen & Umsetzen
                            </label>
                            <select
                                v-model="selectedTransf"
                                class="bg-slate-300 text-slate-700 py-3 rounded md:w-96"
                            >
                                <option
                                    v-for="(option, index) in transf"
                                    :value="option.value"
                                    :key="index"
                                >
                                    {{ option.label }}: &emsp;{{ option.value }}
                                </option>
                            </select>
                            <div class="w-4">
                                {{ selectedTransf }}
                            </div>
                        </div>
                        <div
                            class="flex flex-row items-center justify-between py-4 mx-4"
                        >
                            <label for="eat" class="w-40">
                                Aufstehen & Gehen
                            </label>
                            <select
                                v-model="selectedWalk"
                                class="bg-slate-300 text-slate-700 py-3 rounded md:w-96"
                            >
                                <option
                                    v-for="(option, index) in walk"
                                    :value="option.value"
                                    :key="index"
                                >
                                    {{ option.label }}: &emsp;{{ option.value }}
                                </option>
                            </select>
                            <div class="w-4">
                                {{ selectedWalk }}
                            </div>
                        </div>
                        <div
                            class="flex flex-row items-center justify-between py-4 mx-4"
                        >
                            <label for="eat" class="w-40">
                                Treppensteigen
                            </label>
                            <select
                                v-model="selectedStaris"
                                class="bg-slate-300 text-slate-700 py-3 rounded md:w-96"
                            >
                                <option
                                    v-for="(option, index) in staris"
                                    :value="option.value"
                                    :key="index"
                                >
                                    {{ option.label }}: &emsp;{{ option.value }}
                                </option>
                            </select>
                            <div class="w-4">
                                {{ selectedStaris }}
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
        <div class="flex flex-row justify-end mr-5">
            <button
                class="px-3 py-1 rounded bg-sky-700 m-2 text-slate-100"
                @click="createBarthelIndex"
            >
                absenden
            </button>
        </div>
    </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { usePatientStore } from '@/stores/patient/patient';
import axios from 'axios';
import { computed, onMounted, reactive, ref } from 'vue';
import router from '@/router';
import { useToastStore } from '@/stores/toast';

const id = useRoute().params.id;
const toastStore = useToastStore();
const patient_name = usePatientStore().patient;

const selectedFoodOption = ref(0);
const foodOptions = ref([]);

const selectedWash = ref(0);
const wash = ref([]);

const selectedShower = ref(0);
const shower = ref([]);

const selectDress = ref(0);
const dress = ref([]);

const selectedStool = ref(0);
const stool = ref([]);

const selectedUrin = ref(0);
const urin = ref([]);

const selectedWC = ref(0);
const wc = ref([]);

const selectedTransf = ref(0);
const transf = ref([]);

const selectedWalk = ref(0);
const walk = ref([]);

const selectedStaris = ref(0);
const staris = ref([]);

let sum = computed(
    () =>
        selectedFoodOption.value +
        selectedWash.value +
        selectedShower.value +
        selectDress.value +
        selectedStool.value +
        selectedUrin.value +
        selectedWC.value +
        selectedTransf.value +
        selectedWalk.value +
        selectedStaris.value
);

onMounted(async () => {
    try {
        const response = await axios.get(
            '/api/questionnaires/barthelindex_choices/'
        );
        foodOptions.value = response.data.barthel_food.map(
            ([value, label]) => ({ value, label })
        );
        wash.value = response.data.barthel_wash.map(([value, label]) => ({
            value,
            label
        }));
        shower.value = response.data.barthel_shower.map(([value, label]) => ({
            value,
            label
        }));
        dress.value = response.data.barthel_dress.map(([value, label]) => ({
            value,
            label
        }));
        stool.value = response.data.barthel_stool.map(([value, label]) => ({
            value,
            label
        }));
        urin.value = response.data.barthel_urin.map(([value, label]) => ({
            value,
            label
        }));
        wc.value = response.data.barthel_wc.map(([value, label]) => ({
            value,
            label
        }));
        transf.value = response.data.barthel_transf.map(([value, label]) => ({
            value,
            label
        }));
        walk.value = response.data.barthel_walk.map(([value, label]) => ({
            value,
            label
        }));
        staris.value = response.data.barthel_staris.map(([value, label]) => ({
            value,
            label
        }));
    } catch (error) {
        console.error(error);
    }
});

const createBarthelIndex = async () => {
    try {
        const allData = {
            barthel_food: selectedFoodOption.value,
            barthel_wash: selectedWash.value,
            barthel_shower: selectedShower.value,
            barthel_dress: selectDress.value,
            barthel_stool: selectedStool.value,
            barthel_urin: selectedUrin.value,
            barthel_wc: selectedWC.value,
            barthel_transf: selectedTransf.value,
            barthel_walk: selectedWalk.value,
            barthel_staris: selectedStaris.value,
            total: sum.value
        };
        let response = await axios.post(
            `/api/questionnaires/${id}/create_barthel_index/`,
            allData
        );
        useToastStore().showToast(
            5000,
            'neue Barthel-Index',
            'border border-green-500 bg-green-100 text-green-900'
        );
        await router.push({ path: `/details/${id}/questionnaire` });
    } catch (error) {
        console.log(error);
    }
};
</script>
