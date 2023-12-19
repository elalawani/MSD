<template>
    <div class="flex flex-row justify-between text-slate-900">
        <select class="px-14 py-3 rounded ml-3" v-model="exportValue">
            <option value="">exportieren</option>
            <option value="pdf">pdf</option>
            <option value="excel">excel</option>
        </select>
        <div v-if="exportValue === 'pdf'">
            <download-button
                v-if="barthelIndex.length"
                class="p-2 bg-sky-700 text-slate-50 rounded"
                dom="#invoice"
                :tag-name="exportValue"
                :name="file_name"
            />
        </div>
        <div
            class="py-3 px-10 bg-sky-700 rounded-xl text-slate-100 mr-4 hover:bg-sky-600"
        >
            <router-link :to="`/details/${patient_id}/questionnaire/barthel`"
                >neue Fragebögen</router-link
            >
        </div>
    </div>
    <div
        v-if="barthelIndex.length"
        class="text-slate-900"
        id="invoice"
        v-for="(barthel, index) in barthelIndex"
    >
        <div class="flex flex-col bg-slate-100 p-2 rounded m-2 shadow-lg">
            <div class="flex flex-row justify-between">
                <div class="font-extrabold underline p-5">
                    Aktivitäten des täglichen lebens (ADL), Barthel-index
                </div>
                <div class="flex flex-col py-2 px-4 mt-5">
                    <div>
                        <span class="font-bold">Patient:</span>
                        {{ barthel.patient.last_name }},
                        {{ barthel.patient.first_name }}
                    </div>
                    <div>
                        <span class="font-bold">Versorger:</span>
                        {{ barthel.created_by.username }}
                    </div>
                    <div>
                        <span class="font-bold">Datum:</span>
                        {{ dateTime(barthel.created_at) }}
                    </div>
                </div>
            </div>
            <div>
                <table class="w-full">
                    <tr class="bg-slate-300">
                        <td class="font-extrabold pl-3">Tätigkeiten</td>
                        <th>Punkte</th>
                        <th>ausgewählt</th>
                    </tr>
                    <tr class="bg-slate-300">
                        <td class="font-bold pl-2">Essen:</td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr v-for="(food, index) in foodOptions">
                        <td>{{ food.label }}</td>
                        <td class="text-center align-middle">
                            {{ food.value }}
                        </td>
                        <td
                            v-if="index === foodOptions.length - 1"
                            class="text-center align-middle"
                        >
                            {{ barthel.barthel_food }}
                        </td>
                        <td v-else class="text-center align-middle"></td>
                    </tr>
                    <tr class="bg-slate-300">
                        <td class="font-bold pl-2">Waschen:</td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr v-for="(washs, index) in wash">
                        <td>{{ washs.label }}</td>
                        <td class="text-center align-middle">
                            {{ washs.value }}
                        </td>
                        <td
                            v-if="index === wash.length - 1"
                            class="text-center align-middle"
                        >
                            {{ barthel.barthel_wash }}
                        </td>
                        <td v-else class="text-center align-middle"></td>
                    </tr>
                    <tr class="bg-slate-300">
                        <td class="font-bold pl-2">Duschen:</td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr v-for="(option, index) in shower">
                        <td>{{ option.label }}</td>
                        <td class="text-center align-middle">
                            {{ option.value }}
                        </td>
                        <td
                            v-if="index === shower.length - 1"
                            class="text-center align-middle"
                        >
                            {{ barthel.barthel_shower }}
                        </td>
                        <td v-else class="text-center align-middle"></td>
                    </tr>
                    <tr class="bg-slate-300">
                        <td class="font-bold pl-2">an- ausziehen:</td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr v-for="(option, index) in dress">
                        <td>{{ option.label }}</td>
                        <td class="text-center align-middle">
                            {{ option.value }}
                        </td>
                        <td
                            v-if="index === dress.length - 1"
                            class="text-center align-middle"
                        >
                            {{ barthel.barthel_dress }}
                        </td>
                        <td v-else class="text-center align-middle"></td>
                    </tr>
                    <tr class="bg-slate-300">
                        <td class="font-bold pl-2">Stuhlkontrolle:</td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr v-for="(option, index) in stool">
                        <td>{{ option.label }}</td>
                        <td class="text-center align-middle">
                            {{ option.value }}
                        </td>
                        <td
                            v-if="index === stool.length - 1"
                            class="text-center align-middle"
                        >
                            {{ barthel.barthel_stool }}
                        </td>
                        <td v-else class="text-center align-middle"></td>
                    </tr>
                    <tr class="bg-slate-300">
                        <td class="font-bold pl-2">Harnkontrolle:</td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr v-for="(option, index) in urin">
                        <td>{{ option.label }}</td>
                        <td class="text-center align-middle">
                            {{ option.value }}
                        </td>
                        <td
                            v-if="index === urin.length - 1"
                            class="text-center align-middle"
                        >
                            {{ barthel.barthel_urin }}
                        </td>
                        <td v-else class="text-center align-middle"></td>
                    </tr>
                    <tr class="bg-slate-300">
                        <td class="font-bold pl-2">Toilettenbenutzung:</td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr v-for="(option, index) in wc">
                        <td>{{ option.label }}</td>
                        <td class="text-center align-middle">
                            {{ option.value }}
                        </td>
                        <td
                            v-if="index === wc.length - 1"
                            class="text-center align-middle"
                        >
                            {{ barthel.barthel_wc }}
                        </td>
                        <td v-else class="text-center align-middle"></td>
                    </tr>
                    <tr class="bg-slate-300">
                        <td class="font-bold pl-2">Aufsetzen & Umsetzen:</td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr v-for="(option, index) in transf">
                        <td>{{ option.label }}</td>
                        <td class="text-center align-middle">
                            {{ option.value }}
                        </td>
                        <td
                            v-if="index === transf.length - 1"
                            class="text-center align-middle"
                        >
                            {{ barthel.barthel_transf }}
                        </td>
                        <td v-else class="text-center align-middle"></td>
                    </tr>
                    <tr class="bg-slate-300">
                        <td class="font-bold pl-2">Aufstehen & Gehen:</td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr v-for="(option, index) in walk">
                        <td>{{ option.label }}</td>
                        <td class="text-center align-middle">
                            {{ option.value }}
                        </td>
                        <td
                            v-if="index === walk.length - 1"
                            class="text-center align-middle"
                        >
                            {{ barthel.barthel_walk }}
                        </td>
                        <td v-else class="text-center align-middle"></td>
                    </tr>
                    <tr class="bg-slate-300">
                        <td class="font-bold pl-2">Treppensteigen:</td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr v-for="(option, index) in staris">
                        <td>{{ option.label }}</td>
                        <td class="text-center align-middle">
                            {{ option.value }}
                        </td>
                        <td
                            v-if="index === staris.length - 1"
                            class="text-center align-middle"
                        >
                            {{ barthel.barthel_staris }}
                        </td>
                        <td v-else class="text-center align-middle"></td>
                    </tr>
                </table>
                <div
                    class="bg-slate-300 text-xs font-bold py-2 flex justify-center"
                >
                    {{ barthel.total }} punkte / max Zahl 100 punkte
                </div>
            </div>
        </div>
    </div>
    <div v-else>Keine barthel Index</div>
</template>
<script setup>
import { useQuestionnaireStore } from '@/stores/questionnaires/questionnaire';
import { useRoute } from 'vue-router';
import { computed, onMounted, ref } from 'vue';
import dateTime from '../../../../setUp/global/date-filter';
import axios from 'axios';
import downloadButton from '@/components/helper/downloadButton.vue';
import { usePatientStore } from '@/stores/patient/patient';

let patient = usePatientStore().patient;
let questionnaire = useQuestionnaireStore();
let patient_id = useRoute().params.id;
let exportValue = ref();

let file_name = patient.first_name + '-' + patient.last_name + '.pdf';
const fetchData = async () => {
    await questionnaire.getBarthelIndex(patient_id);
};

onMounted(fetchData);

const barthelIndex = computed(() => questionnaire.barthelIndex);

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
</script>
