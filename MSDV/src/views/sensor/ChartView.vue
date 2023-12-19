<template>
    <div class="md:block hidden">
        <div v-if="isLoading && parkinson.parkinsonMeasurements.length">
            loading...
        </div>
        <div v-else class="text-slate-900 dark:text-slate-50">
            <div class="border dark:border-0">
                <ul class="flex flex-row justify-between dark:bg-slate-600">
                    <li class="m-2">
                    <span class="font-bold">patient name : </span
                    >{{ patient.first_name }} {{ patient.last_name }}
                    </li>
                    <li
                            v-if="
                        (dataView === 'chart' || dataView === 'information') &&
                        !isLoading &&
                        parkinson.parkinsonMeasurements.length
                    "
                            class="m-2"
                    >
                        <select
                                v-model="chartIndex"
                                class="mr-5 rounded dark:bg-sky-900 bg-sky-600 text-slate-50 px-1 w-fit"
                        >
                            <option
                                    v-for="(
                                data, index
                            ) in parkinson.parkinsonMeasurements"
                                    :key="index"
                                    :value="index"
                            >
                                added am {{ dateTime(data.uploaded_at) }}
                            </option>
                        </select>
                        <button
                                class="dark:hover:bg-sky-600 bg-sky-600 hover:bg-sky-500 text-slate-50 px-4 rounded-xl dark:bg-sky-700 mr-5"
                                @mousedown="changeDataType('thumb')"
                        >
                            thump
                        </button>
                        <button
                                class="px-4 rounded-xl shadow hover:shadow-xl dark:bg-slate-800 dark:hover:bg-slate-900"
                                @mousedown="changeDataType('digit')"
                        >
                            digit
                        </button>
                    </li>
                </ul>
            </div>
            <div class="border-b border-b-slate-500">
                <ul class="flex flex-row space-x-12 text-xl overflow-auto">
                    <li class="whitespace-nowrap">
                        <button
                                @mousedown="changeDataView('information')"
                                class="py-3 px-2"
                                :class="
                            dataView === 'information'
                                ? 'text-sky-600 dark:bg-slate-800' +
                                  'relative border-t-sky-600 border-t-4 border-b-sky-600'
                                : ''
                        "
                        >
                            übersicht
                        </button>
                    </li>
                    <li class="whitespace-nowrap">
                        <button
                                @mousedown="changeDataView('chart')"
                                class="py-3 px-2"
                                :class="
                            dataView === 'chart'
                                ? 'text-sky-600 dark:bg-slate-800' +
                                  'relative border-t-sky-600 border-t-4 border-b-sky-600'
                                : ''
                        "
                        >
                            Chart
                        </button>
                    </li>
                    <li class="whitespace-nowrap">
                        <button
                                @mousedown="changeDataView('threeD')"
                                class="py-3 px-2"
                                :class="
                            dataView === 'threeD'
                                ? 'text-sky-600 dark:bg-slate-800' +
                                  'relative border-t-sky-600 border-t-4 border-b-sky-600'
                                : ''
                        "
                        >
                            3D Chart
                        </button>
                    </li>
                    <li class="whitespace-nowrap">
                        <button
                                @mousedown="changeDataView('comment')"
                                class="py-3 px-2"
                                :class="
                            dataView === 'comment'
                                ? 'text-sky-600 dark:bg-slate-800 ' +
                                  'relative border-t-sky-600 border-t-4 border-b-sky-600'
                                : ''
                        "
                        >
                            comments
                        </button>
                    </li>
                    <li class="whitespace-nowrap">
                        <button
                                @mousedown="changeDataView('upload')"
                                class="py-3 px-2"
                                :class="
                            dataView === 'upload'
                                ? 'text-sky-600 dark:bg-slate-800 ' +
                                  'relative border-t-sky-600 border-t-4 border-b-sky-600'
                                : ''
                        "
                        >
                            datei hochladen &uparrow;
                        </button>
                    </li>
                    <li class="whitespace-nowrap">
                        <button
                                @mousedown="changeDataView('more')"
                                class="py-3 px-2"
                                :class="
                            dataView === 'more'
                                ? 'text-sky-600 dark:bg-slate-800' +
                                  'relative border-t-sky-600 border-t-4 border-b-sky-600'
                                : ''
                        "
                        >
                            weitere Messungen
                        </button>
                    </li>
                </ul>
            </div>
            <div>
                <div v-if="!isLoading && parkinson.parkinsonMeasurements.length">
                    <div class="p-2" v-if="dataView === 'chart'">
                        <Line :data="chartData" :key="chartKey" />
                    </div>
                    <div v-if="dataView === 'information'">
                        <information-view
                                :allData="dataType"
                                :more-info="information"
                                :out-file-data="outFileData"
                        />
                    </div>
                    <div v-if="dataView === 'comment'">
                        <div>
                            <comments-view :measurement-id="selectedId" />
                        </div>
                    </div>
                    <div v-if="dataView === 'threeD'">
                        <div>
                            <three-d-chart
                                    :digit-points="digitPoints"
                                    :thumb-points="thumbPoints"
                            />
                        </div>
                    </div>
                </div>
                <div v-else>
                    <div
                            v-if="
                        dataView === 'chart' ||
                        dataView === 'information' ||
                        dataView === 'comment' ||
                        dataView === 'threeD'
                    "
                            class="text-2xl m-10 mt-20 flex flex-col justify-center uppercase"
                    >
                        keine Dateien sind Hochgeleden!!!

                        <div class="p-2 space-y-5">
                            es kann kein
                            <span class="text-sky-700">{{ dataView }}</span>
                            angezeigt werden
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="dataView === 'upload'">
                <upload />
            </div>
            <div v-if="dataView === 'more'">
                <sensor-view class="mt-5 mb-5" />
            </div>
        </div>
    </div>
</template>

<script setup>
import { useParkinsonMeasurementStore } from '@/stores/sensor/parkinsonMeasurement';
import { computed, onMounted, reactive, ref, watch } from 'vue';
import { Line } from 'vue-chartjs';
import InformationView from '@/views/sensor/InformationView.vue';
import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    CategoryScale,
    LinearScale,
    LineElement,
    PointElement
} from 'chart.js';
import { usePatientStore } from '@/stores/patient/patient';
import Upload from '@/views/sensor/UploadView.vue';
import dateTime from '../../setUp/global/date-filter';
import SensorView from '@/views/sensor/SensorView.vue';
import CommentsView from '@/views/sensor/CommentsView.vue';
import ThreeDChart from '@/views/sensor/ThreeDChart.vue';
ChartJS.register(
    Title,
    Legend,
    Tooltip,
    LineElement,
    PointElement,
    CategoryScale,
    LinearScale
);

const patient = usePatientStore().patient;
const parkinson = useParkinsonMeasurementStore();
const isLoading = ref(true);
const error = ref(null);
let thumb = ref(null);
let digit = ref(null);
let x = ref(null);
let y = ref(null);
let type = ref('thumb');
const objectComponents = ref('');
let dataType = ref({});
let information = ref({});
let outFileData = ref({});
let dataView = ref('chart');
let chartIndex = ref(0);
let thumbPoints = ref({});
let digitPoints = ref({});
const chartData = reactive({
    labels: [],
    datasets: [
        {
            label: 'no data',
            data: [],
            backgroundColor: '#0369a1'
        }
    ]
});
const chartKey = ref(0);
const updateChartData = () => {
    chartData.labels = x.value.map((_, index) => index);
    chartData.datasets = [
        {
            label: 'X Data',
            data: x.value,
            backgroundColor: '#8c03a1',
            borderColor: '#8c03a1',
            borderWidth: 1,
            fill: false
        },
        {
            label: 'Y Data',
            data: y.value,
            backgroundColor: '#0369a1',
            borderColor: '#0369a1',
            borderWidth: 1,
            fill: false
        }
    ];
    chartKey.value++;
};
const fetchData = async () => {
    try {
        await parkinson.getParkinsonMeasurement(patient.id);
        processMeasureData();
        isLoading.value = false;
    } catch (e) {
        error.value = e;
    }
};

const changeDataView = (types) => {
    dataView.value = types;
};

const changeDataType = (types) => {
    type.value = types;
    processMeasureData();
    updateChartData();
};

const processMeasureData = () => {
    if (
        (chartIndex.value >= parkinson.parkinsonMeasurements.length ||
            chartIndex.value < 0) &&
        parkinson.parkinsonMeasurements.length !== 0
    ) {
        console.error(
            'ausgewählte Index liegt außerhalb des zulässigen Bereichs'
        );
        return;
    }

    const measure = parkinson.parkinsonMeasurements[chartIndex.value];
    outFileData.value = measure;
    information.value = measure.data;
    thumb.value = measure.data.component[1];
    digit.value = measure.data.component[0];
    switch (type.value) {
        case 'thumb':
            objectComponents.value = thumb.value.valueSampledData;
            dataType.value = thumb.value;
            break;
        case 'digit':
            objectComponents.value = digit.value.valueSampledData;
            dataType.value = digit.value;
            break;
        default:
            objectComponents.value = digit.value.valueSampledData;
            dataType.value = digit.value;
            break;
    }

    try {
        // convert the String pair to number and view in a Chart
        // this is to exclude the out of range values
        let rawData = objectComponents.value.data
            .split('), (')
            .map((pair) => pair.replace('(', '').replace(')', ''))
            .map((pair) => {
                let [x, y] = pair.split(', ').map(Number);
                return { x, y };
            });
        x.value = rawData.map((pair) => pair.x);
        y.value = rawData.map((pair) => pair.y);
        // get points to plot in a 3d view
        // first prepare thumb
        let thumbData = thumb.value.valueSampledData.data
            .split('), (')
            .map((pair) => pair.replace('(', '').replace(')', ''))
            .map((pair) => {
                let [x, y] = pair.split(', ').map(Number);
                return { x, y };
            });
        x.value = thumbData.map((pair) => pair.x);
        y.value = thumbData.map((pair) => pair.y);

        if (x.value.length !== y.value.length) {
            console.error('Arrays are of unequal length');
        } else {
            thumbPoints = x.value
                .map((xi, index) => {
                    return { x: xi, y: y.value[index], z: index + 1 };
                })
                .filter(
                    (point) => point.x >= 0 && point.y >= 0 && point.z >= 0
                );
        }

        // get points to plot in a 3d view
        // now prepare for the Digit
        let digitData = digit.value.valueSampledData.data
            .split('), (')
            .map((pair) => pair.replace('(', '').replace(')', ''))
            .map((pair) => {
                let [x, y] = pair.split(', ').map(Number);
                return { x, y };
            });
        x.value = digitData.map((pair) => pair.x);
        y.value = digitData.map((pair) => pair.y);

        if (x.value.length !== y.value.length) {
            console.error('Arrays are of unequal length');
        } else {
            digitPoints = x.value
                .map((xi, index) => {
                    return { x: xi, y: y.value[index], z: index + 1 };
                })
                .filter(
                    (point) => point.x >= 0 && point.y >= 0 && point.z >= 0
                );
        }

        updateChartData();
    } catch (e) {
        error.value = e;
    }
};

watch(chartIndex, () => {
    processMeasureData();
});
const selectedId = computed(() => {
    if (parkinson.parkinsonMeasurements.length > chartIndex.value) {
        return parkinson.parkinsonMeasurements[chartIndex.value].id;
    }
    return null;
});

onMounted(fetchData);
</script>
