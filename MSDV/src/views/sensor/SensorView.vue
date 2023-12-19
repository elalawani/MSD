<template>
    <div class="flex flex-row h-full">
        <div
            class="left flex flex-col items-center h-full border-r border-r-slate-500 w-full p-2"
        >
            <div class="flex flex-col w-[80%]">
                <div
                    class="flex flex-row border-b items-center border-b-slate-500"
                >
                    <button
                        class="border-r border-r-slate-500 text-slate-500 overflow-hidden flex flex-col items-center justify-center p-2 m-1 hover:font-bold"
                        @click="showChart"
                        :class="
                            dataView === 'chart'
                                ? 'font-extrabold dark:text-white '
                                : ''
                        "
                    >
                        Chart
                    </button>
                    <button
                        class="text-slate-500 overflow-hidden flex flex-col items-center justify-center p-2 m-1 hover:font-bold"
                        @click="showTable"
                        :class="
                            dataView === 'table'
                                ? 'font-extrabold dark:text-white'
                                : ''
                        "
                    >
                        table
                    </button>
                </div>
                <div
                    class="h-full justify-center shadow dark:bg-slate-800 mt-1"
                >
                    <Line
                        v-if="dataView === 'chart'"
                        :data="chartData"
                        :options="chartOptions"
                        :key="chartKey"
                    />
                    <div v-else-if="dataView === 'table'" class="w-full">
                        <div class="overflow-auto h-full">
                            <div
                                v-if="currentTableView === 'temperature'"
                                class="shadow-md rounded-lg"
                            >
                                <table
                                    class="rounded text-sm text-left text-slate-500 dark:text-slate-100 w-full"
                                >
                                    <thead
                                        class="text-slate-100 bg-sky-700 uppercase dark:bg-sky-900 dark:text-slate-300"
                                    >
                                        <tr>
                                            <th class="pl-2 py-3">nr.</th>
                                            <th class="pl-4 py-3">Date</th>
                                            <th class="pl-4 py-3">code</th>
                                            <th class="px-4 py-3">
                                                temperature
                                            </th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr
                                            v-for="(
                                                allTemperature, index
                                            ) in temperature"
                                            :key="index"
                                            class="border-b dark:bg-slate-800 dark:border-slate-700 hover:shadow dark:hover:bg-slate-700"
                                        >
                                            <th class="pl-2 py-4">
                                                {{ index + 1 }}
                                            </th>
                                            <td class="pl-4 py-4">
                                                {{
                                                    dateTime(
                                                        allTemperature.created_at
                                                    )
                                                }}
                                            </td>
                                            <td class="pl-4 py-4">
                                                {{ allTemperature.code }}
                                            </td>
                                            <td class="px-4 py-4">
                                                {{ allTemperature.Temperature }}
                                                {{ allTemperature.unit }}
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div
                                v-if="currentTableView === 'parkinson'"
                                class="shadow-md rounded-lg"
                            >
                                <table
                                    class="rounded text-sm text-left text-slate-500 dark:text-slate-100 w-full"
                                >
                                    <thead
                                        class="text-slate-100 bg-sky-700 uppercase dark:bg-sky-900 dark:text-slate-300"
                                    >
                                        <tr>
                                            <th class="pl-2 py-3">nr.</th>
                                            <th class="pl-4 py-3">Date</th>
                                            <th class="pl-4 py-3">code</th>
                                            <th class="px-4 py-3">
                                                tremor_severity
                                            </th>
                                            <th class="px-4 py-3">
                                                gait_speed
                                            </th>
                                            <th class="px-4 py-3">
                                                daily_assessment
                                            </th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr
                                            v-for="(
                                                allParkinson, index
                                            ) in parkinson"
                                            :key="index"
                                            class="border-b dark:bg-slate-800 dark:border-slate-700 hover:shadow dark:hover:bg-slate-700"
                                        >
                                            <th class="pl-2 py-4">
                                                {{ index + 1 }}
                                            </th>
                                            <td class="pl-4 py-4">
                                                {{
                                                    dateTime(
                                                        allParkinson.created_at
                                                    )
                                                }}
                                            </td>
                                            <td class="pl-4 py-4">
                                                {{ allParkinson.code }}
                                            </td>
                                            <td class="px-4 py-4">
                                                {{
                                                    allParkinson.tremor_severity
                                                }}
                                            </td>
                                            <td class="px-4 py-4">
                                                {{ allParkinson.gait_speed }}
                                            </td>
                                            <td class="px-4 py-4">
                                                {{
                                                    allParkinson.daily_assessment
                                                }}
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div
                                v-if="currentTableView === 'heartRates'"
                                class="shadow-md rounded-lg"
                            >
                                <table
                                    class="rounded text-sm text-left text-slate-500 dark:text-slate-100 w-full"
                                >
                                    <thead
                                        class="text-slate-100 bg-sky-700 uppercase dark:bg-sky-900 dark:text-slate-300"
                                    >
                                        <tr>
                                            <th class="pl-2 py-3">nr.</th>
                                            <th class="pl-4 py-3">Date</th>
                                            <th class="pl-4 py-3">code</th>
                                            <th class="px-4 py-3">
                                                heart rate
                                            </th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr
                                            v-for="(
                                                allHeartRate, index
                                            ) in heartRates"
                                            :key="index"
                                            class="border-b dark:bg-slate-800 dark:border-slate-700 hover:shadow dark:hover:bg-slate-700"
                                        >
                                            <th class="pl-2 py-4">
                                                {{ index + 1 }}
                                            </th>
                                            <td class="pl-4 py-4">
                                                {{
                                                    dateTime(
                                                        allHeartRate.created_at
                                                    )
                                                }}
                                            </td>
                                            <td class="pl-4 py-4">
                                                {{ allHeartRate.code }}
                                            </td>
                                            <td class="px-4 py-4">
                                                {{ allHeartRate.HeartRate }}
                                                {{ allHeartRate.unit }}
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div
                                v-if="currentTableView === 'bloodGlucose'"
                                class="shadow-md rounded-lg"
                            >
                                <table
                                    class="rounded text-sm text-left text-slate-500 dark:text-slate-100 w-full"
                                >
                                    <thead
                                        class="text-slate-100 bg-sky-700 uppercase dark:bg-sky-900 dark:text-slate-300"
                                    >
                                        <tr>
                                            <th class="pl-2 py-3">nr.</th>
                                            <th class="pl-4 py-3">Date</th>
                                            <th class="pl-4 py-3">code</th>
                                            <th class="px-4 py-3">
                                                blood Glucose
                                            </th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr
                                            v-for="(
                                                allBloodGlucose, index
                                            ) in bloodGlucose"
                                            :key="index"
                                            class="border-b dark:bg-slate-800 dark:border-slate-700 hover:shadow dark:hover:bg-slate-700"
                                        >
                                            <th class="pl-2 py-4">
                                                {{ index + 1 }}
                                            </th>
                                            <td class="pl-4 py-4">
                                                {{
                                                    dateTime(
                                                        allBloodGlucose.created_at
                                                    )
                                                }}
                                            </td>
                                            <td class="pl-4 py-4">
                                                {{ allBloodGlucose.code }}
                                            </td>
                                            <td class="px-4 py-4">
                                                {{
                                                    allBloodGlucose.BloodGlucose
                                                }}
                                                {{ allBloodGlucose.unit }}
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div
                                v-if="currentTableView === 'bloodCholesterol'"
                                class="shadow-md rounded-lg"
                            >
                                <table
                                    class="rounded text-sm text-left text-slate-500 dark:text-slate-100 w-full"
                                >
                                    <thead
                                        class="text-slate-100 bg-sky-700 uppercase dark:bg-sky-900 dark:text-slate-300"
                                    >
                                        <tr>
                                            <th class="pl-2 py-3">nr.</th>
                                            <th class="pl-4 py-3">Date</th>
                                            <th class="pl-4 py-3">code</th>
                                            <th class="px-4 py-3">
                                                blood Cholesterol
                                            </th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr
                                            v-for="(
                                                allBloodCholesterol, index
                                            ) in bloodCholesterol"
                                            :key="index"
                                            class="border-b dark:bg-slate-800 dark:border-slate-700 hover:shadow dark:hover:bg-slate-700"
                                        >
                                            <th class="pl-2 py-4">
                                                {{ index + 1 }}
                                            </th>
                                            <td class="pl-4 py-4">
                                                {{
                                                    dateTime(
                                                        allBloodCholesterol.created_at
                                                    )
                                                }}
                                            </td>
                                            <td class="pl-4 py-4">
                                                {{ allBloodCholesterol.code }}
                                            </td>
                                            <td class="px-4 py-4">
                                                {{
                                                    allBloodCholesterol.BloodCholesterol
                                                }}
                                                {{ allBloodCholesterol.unit }}
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div
                                v-if="currentTableView === 'respirationsRates'"
                                class="shadow-md rounded-lg"
                            >
                                <table
                                    class="rounded text-sm text-left text-slate-500 dark:text-slate-100 w-full"
                                >
                                    <thead
                                        class="text-slate-100 bg-sky-700 uppercase dark:bg-sky-900 dark:text-slate-300"
                                    >
                                        <tr>
                                            <th class="pl-2 py-3">nr.</th>
                                            <th class="pl-4 py-3">Date</th>
                                            <th class="pl-4 py-3">code</th>
                                            <th class="px-4 py-3">
                                                Respiration Rate
                                            </th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr
                                            v-for="(
                                                AllRespirationsRates, index
                                            ) in respirationsRates"
                                            :key="index"
                                            class="border-b dark:bg-slate-800 dark:border-slate-700 hover:shadow dark:hover:bg-slate-700"
                                        >
                                            <th class="pl-2 py-4">
                                                {{ index + 1 }}
                                            </th>
                                            <td class="pl-4 py-4">
                                                {{
                                                    dateTime(
                                                        AllRespirationsRates.created_at
                                                    )
                                                }}
                                            </td>
                                            <td class="pl-4 py-4">
                                                {{ AllRespirationsRates.code }}
                                            </td>
                                            <td class="px-4 py-4">
                                                {{
                                                    AllRespirationsRates.RespirationRate
                                                }}
                                                {{ AllRespirationsRates.unit }}
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div
                                v-if="currentTableView === 'bloodPressures'"
                                class="shadow-md rounded-lg"
                            >
                                <table
                                    class="rounded text-sm text-left text-slate-500 dark:text-slate-100 w-full"
                                >
                                    <thead
                                        class="text-slate-100 bg-sky-700 uppercase dark:bg-sky-900 dark:text-slate-300"
                                    >
                                        <tr>
                                            <th class="pl-2 py-3">nr.</th>
                                            <th class="pl-4 py-3">Date</th>
                                            <th class="pl-4 py-3">code</th>
                                            <th class="px-4 py-3">
                                                systolic Pressure
                                            </th>
                                            <th class="px-4 py-3">
                                                diastolic Pressure
                                            </th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr
                                            v-for="(
                                                AllBloodPressures, index
                                            ) in bloodPressures"
                                            :key="index"
                                            class="border-b dark:bg-slate-800 dark:border-slate-700 hover:shadow dark:hover:bg-slate-700"
                                        >
                                            <th class="pl-2 py-4">
                                                {{ index + 1 }}
                                            </th>
                                            <td class="pl-4 py-4">
                                                {{
                                                    dateTime(
                                                        AllBloodPressures.created_at
                                                    )
                                                }}
                                            </td>
                                            <td class="pl-4 py-4">
                                                {{ AllBloodPressures.code }}
                                            </td>
                                            <td class="px-4 py-4">
                                                {{
                                                    AllBloodPressures.systolic_Pressure
                                                }}
                                                {{ AllBloodPressures.unit }}
                                            </td>
                                            <td class="px-4 py-4">
                                                {{
                                                    AllBloodPressures.diastolic_Pressure
                                                }}
                                                {{ AllBloodPressures.unit }}
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="flex flex-col w-[50%] p-2">
            <div class="mb-16 space-y-2 flex flex-col items-center">
                <router-link
                    :to="`/details/${id}/add_data`"
                    class="p-2 bg-sky-700 rounded"
                    >add data +</router-link
                >
            </div>
            <div class="overflow-auto h-1/2 relative">
                <div
                    v-if="parkinson"
                    v-for="(lastParkinson, index) in parkinson"
                    :key="index"
                >
                    <div
                        v-if="index === parkinson.length - 1"
                        class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center justify-center p-1 rounded-xl w-full my-1 dark:bg-slate-500"
                        @click="
                            loadDataset('parkinson');
                            tableView('parkinson');
                        "
                    >
                        <div class="w-full font-extrabold px-2 py-1">
                            <div>
                                tremor severity:
                                {{ lastParkinson.tremor_severity }}
                            </div>
                            <div>
                                gait speed: {{ lastParkinson.gait_speed }}
                            </div>
                            <div>
                                daily assessment:
                                {{ lastParkinson.daily_assessment }}
                            </div>
                        </div>
                        <div class="w-full">
                            {{ lastParkinson.category }}
                        </div>
                        <i
                            class="dark:bg-sky-900 bg-sky-700 absolute px-2 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg"
                        >
                            <font-awesome-icon icon="fa-solid fa-info" />
                        </i>
                    </div>
                </div>
                <div
                    v-if="temperature"
                    v-for="(lastTemperature, index) in temperature"
                    :key="index"
                >
                    <div
                        v-if="index === temperature.length - 1"
                        class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center justify-center p-1 rounded-xl w-full my-1 dark:bg-slate-500 hover:cursor-pointer"
                        @click="
                            loadDataset('Temperature');
                            tableView('temperature');
                        "
                    >
                        <div class="w-full font-extrabold px-2 py-1">
                            <span>
                                {{ lastTemperature.Temperature }}
                                {{ lastTemperature.unit }}
                            </span>
                            <i class="dark:text-sky-900 text-sky-700 px-2">
                                <font-awesome-icon
                                    size="xl"
                                    icon="fa-solid fa-temperature-half"
                                />
                            </i>
                        </div>
                        <div class="w-full">
                            {{ lastTemperature.category }}
                        </div>
                        <i
                            class="dark:bg-sky-900 bg-sky-700 absolute px-2 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg"
                        >
                            <font-awesome-icon icon="fa-solid fa-info" />
                        </i>
                    </div>
                </div>
                <div
                    v-if="respirationsRates"
                    v-for="(respirationsRate, index) in respirationsRates"
                    :key="index"
                >
                    <div
                        v-if="index === respirationsRates.length - 1"
                        class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center justify-center p-1 rounded-xl w-full my-1 dark:bg-slate-500"
                        @click="
                            loadDataset('respirationsRates');
                            tableView('respirationsRates');
                        "
                    >
                        <div class="w-full font-extrabold px-2 py-1">
                            <span>
                                {{ respirationsRate.RespirationRate }}
                                {{ respirationsRate.unit }}
                            </span>
                            <i class="dark:text-sky-900 text-sky-700 px-2">
                                <font-awesome-icon
                                    size="xl"
                                    icon="fa-solid fa-lungs"
                                />
                            </i>
                        </div>
                        <div class="w-full">
                            {{ respirationsRate.category }}
                        </div>
                        <i
                            class="dark:bg-sky-900 bg-sky-700 absolute px-2 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg"
                        >
                            <font-awesome-icon icon="fa-solid fa-info" />
                        </i>
                    </div>
                </div>
                <div
                    v-if="bloodPressures"
                    v-for="(bloodPressure, index) in bloodPressures"
                    :key="index"
                >
                    <div
                        v-if="index === bloodPressures.length - 1"
                        class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center justify-center p-1 rounded-xl w-full my-1 dark:bg-slate-500"
                        @click="
                            loadDataset('bloodPressures');
                            tableView('bloodPressures');
                        "
                    >
                        <div class="w-full font-extrabold px-2 py-1">
                            <span>
                                {{ bloodPressure.systolic_Pressure }} -
                                {{ bloodPressure.diastolic_Pressure }}
                                {{ bloodPressure.unit }}
                            </span>
                            <i class="dark:text-sky-900 text-sky-700 px-2">
                                <font-awesome-icon
                                    size="xl"
                                    icon="fa-solid fa-stethoscope"
                                />
                            </i>
                        </div>
                        <div class="w-full">
                            {{ bloodPressure.category }}
                        </div>
                        <i
                            class="dark:bg-sky-900 bg-sky-700 absolute px-2 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg"
                        >
                            <font-awesome-icon icon="fa-solid fa-info" />
                        </i>
                    </div>
                </div>
                <div
                    v-if="bloodCholesterol"
                    v-for="(lastBloodCholesterol, index) in bloodCholesterol"
                    :key="index"
                >
                    <div
                        v-if="index === bloodCholesterol.length - 1"
                        class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center justify-center p-1 rounded-xl w-full my-1 dark:bg-slate-500"
                        @click="
                            loadDataset('bloodCholesterol');
                            tableView('bloodCholesterol');
                        "
                    >
                        <div class="w-full font-extrabold px-2 py-1">
                            <span>
                                {{ lastBloodCholesterol.BloodCholesterol }}
                                {{ lastBloodCholesterol.unit }}
                            </span>
                            <i class="dark:text-sky-900 text-sky-700 px-2">
                                <font-awesome-icon
                                    size="xl"
                                    icon="fa-solid fa-droplet"
                                />
                            </i>
                        </div>
                        <div class="w-full">
                            {{ lastBloodCholesterol.category }}
                        </div>
                        <i
                            class="dark:bg-sky-900 bg-sky-700 absolute px-2 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg"
                        >
                            <font-awesome-icon icon="fa-solid fa-info" />
                        </i>
                    </div>
                </div>
                <div
                    v-if="bloodGlucose"
                    v-for="(lastBloodGlucose, index) in bloodGlucose"
                    :key="index"
                >
                    <div
                        v-if="index === bloodGlucose.length - 1"
                        class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center justify-center p-1 rounded-xl w-full my-1 dark:bg-slate-500"
                        @click="
                            loadDataset('bloodGlucose');
                            tableView('bloodGlucose');
                        "
                    >
                        <div class="w-full font-extrabold px-2 py-1">
                            <span>
                                {{ lastBloodGlucose.BloodGlucose }}
                                {{ lastBloodGlucose.unit }}
                            </span>
                            <i class="dark:text-sky-900 text-sky-700 px-2">
                                <font-awesome-icon
                                    size="xl"
                                    icon="fa-solid fa-droplet"
                                />
                            </i>
                        </div>
                        <div class="w-full">
                            {{ lastBloodGlucose.category }}
                        </div>
                        <i
                            class="dark:bg-sky-900 bg-sky-700 absolute px-2 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg"
                        >
                            <font-awesome-icon icon="fa-solid fa-info" />
                        </i>
                    </div>
                </div>
                <div
                    v-if="heartRates"
                    v-for="(heartRate, index) in heartRates"
                    :key="index"
                >
                    <div
                        v-if="index === heartRates.length - 1"
                        class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center justify-center p-1 rounded-xl w-full my-1 dark:bg-slate-500"
                        @click="
                            loadDataset('heartRates');
                            tableView('heartRates');
                        "
                    >
                        <div class="w-full font-extrabold px-2 py-1">
                            <span>
                                {{ heartRate.HeartRate }} {{ heartRate.unit }}
                            </span>
                            <i class="dark:text-sky-900 text-sky-700 px-2">
                                <font-awesome-icon
                                    size="xl"
                                    icon="fa-solid fa-heartbeat"
                                />
                            </i>
                        </div>
                        <div class="w-full">
                            {{ heartRate.category }}
                        </div>
                        <i
                            class="dark:bg-sky-900 bg-sky-700 absolute px-2 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg"
                        >
                            <font-awesome-icon icon="fa-solid fa-info" />
                        </i>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { Line } from 'vue-chartjs';
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
import { useRoute } from 'vue-router';
import axios from 'axios';
import { useMeasurementsStore } from '@/stores/sensor/measurements';
import { onMounted, reactive, ref, watchEffect } from 'vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import dateTime from '../../setUp/global/date-filter';

ChartJS.register(
    Title,
    Legend,
    Tooltip,
    LineElement,
    PointElement,
    CategoryScale,
    LinearScale
);

export default {
    components: {
        FontAwesomeIcon,
        Line
    },
    setup() {
        const store = useMeasurementsStore();
        const heartRates = ref([]);
        const parkinson = ref([]);
        const bloodPressures = ref([]);
        const bloodCholesterol = ref([]);
        const bloodGlucose = ref([]);
        const respirationsRates = ref([]);
        const temperature = ref([]);
        let patient_id = useRoute().params.id;
        const chartData = reactive({
            labels: [1, 2, 3],
            datasets: [
                {
                    label: 'no data',
                    data: [2, 2, 2],
                    backgroundColor: '#0369a1'
                }
            ]
        });
        const chartKey = ref(0);
        const updateChartData = (dataset, labelName, measure) => {
            const newChartData = {
                labels: dataset.map((item, index) => index),
                datasets: [
                    {
                        data: dataset.map((item) => item[measure]),
                        label: labelName,
                        backgroundColor: '#0369a1'
                    }
                ]
            };

            chartData.labels = newChartData.labels;
            chartData.datasets = newChartData.datasets;
        };

        const updatePressureChartData = (dataset) => {
            const newChartData = {
                labels: dataset.map((item, index) => index),
                datasets: [
                    {
                        data: dataset.map((item) => item.systolic_Pressure),
                        label: 'systolic Pressure',
                        backgroundColor: '#0369a1'
                    },
                    {
                        data: dataset.map((item) => item.diastolic_Pressure),
                        label: 'diastolic Pressure',
                        backgroundColor: '#8c03a1'
                    }
                ]
            };

            chartData.labels = newChartData.labels;
            chartData.datasets = newChartData.datasets;
        };

        const updateParkinsonChartData = (dataset) => {
            const newChartData = {
                labels: dataset.map((item, index) => index),
                datasets: [
                    {
                        data: dataset.map((item) => item.tremor_severity),
                        label: 'tremor severity',
                        backgroundColor: '#0369a1'
                    },
                    {
                        data: dataset.map((item) => item.gait_speed),
                        label: 'gait speed',
                        backgroundColor: '#8c03a1'
                    },
                    {
                        data: dataset.map((item) => item.daily_assessment),
                        label: 'daily assessment',
                        backgroundColor: '#03a110'
                    }
                ]
            };

            chartData.labels = newChartData.labels;
            chartData.datasets = newChartData.datasets;
        };
        watchEffect(() => {
            if (temperature.value.length) {
                updateChartData(
                    temperature.value,
                    'Temperature',
                    'Temperature'
                );
            }
            if (respirationsRates.value.length > 0) {
                updateChartData(
                    respirationsRates.value,
                    'Respirations Rates',
                    'RespirationRate'
                );
            }
            if (parkinson.value.length > 0) {
                updateParkinsonChartData(parkinson.value);
            }
            if (bloodCholesterol.value.length > 0) {
                updateChartData(
                    bloodCholesterol.value,
                    'Blood Cholesterol',
                    'BloodCholesterol'
                );
            }
            if (bloodGlucose.value.length > 0) {
                updateChartData(
                    bloodGlucose.value,
                    'Blood Glucose',
                    'BloodGlucose'
                );
            }
            if (bloodPressures.value.length > 0) {
                updatePressureChartData(bloodPressures.value);
            }
            if (heartRates.value.length > 0) {
                updateChartData(heartRates.value, 'Heart Rates', 'HeartRate');
            }
        });
        const loadDataset = (datasetName) => {
            chartData.datasets = [];
            switch (datasetName) {
                case 'Temperature':
                    updateChartData(
                        temperature.value,
                        'Temperature',
                        'Temperature'
                    );
                    break;
                case 'parkinson':
                    updateParkinsonChartData(parkinson.value);
                    break;
                case 'heartRates':
                    updateChartData(
                        heartRates.value,
                        'Heart Rates',
                        'HeartRate'
                    );
                    break;
                case 'bloodGlucose':
                    updateChartData(
                        bloodGlucose.value,
                        'Blood Glucose',
                        'BloodGlucose'
                    );
                    break;
                case 'bloodPressures':
                    updatePressureChartData(bloodPressures.value);
                    break;
                case 'bloodCholesterol':
                    updateChartData(
                        bloodCholesterol.value,
                        'Blood Cholesterol',
                        'BloodCholesterol'
                    );
                    break;
                case 'respirationsRates':
                    updateChartData(
                        respirationsRates.value,
                        'Respirations Rates',
                        'RespirationRate'
                    );
                    break;
            }
            chartKey.value++;
        };

        onMounted(async () => {
            await store.getHeartRateMeasurements(patient_id);
            heartRates.value = store.heartRateMeasurements;

            await store.getParkinson(patient_id);
            parkinson.value = store.parkinsonMeasurements;

            await store.getRespirationRateMeasurement(patient_id);
            respirationsRates.value = store.respirationRateMeasurement;

            await store.getBloodCholesterolMeasurement(patient_id);
            bloodCholesterol.value = store.bloodCholesterolMeasurement;

            await store.getBloodPressureMeasurement(patient_id);
            bloodPressures.value = store.bloodPressureMeasurement;

            await store.getBloodGlucoseMeasurement(patient_id);
            bloodGlucose.value = store.bloodGlucoseMeasurement;

            await store.getTemperatureMeasurement(patient_id);
            temperature.value = store.temperatureMeasurement;
        });

        return {
            heartRates,
            parkinson,
            temperature,
            bloodGlucose,
            bloodCholesterol,
            bloodPressures,
            respirationsRates,
            chartData,
            loadDataset,
            chartKey
        };
    },
    data() {
        return {
            dataView: 'chart',
            currentTableView: '',
            id: useRoute().params.id,
            chartOptions: {
                responsive: true
            },
            selectedFile: null
        };
    },
    methods: {
        dateTime,
        async uploadFile() {
            const formData = new FormData();
            formData.append('file', this.selectedFile);
            formData.append('patient', this.id);

            await axios
                .post('/api/measure_fhir/upload_measurement/', formData)
                .then(() => {})
                .catch((error) => {
                    console.log(error);
                });
        },

        handleFileUpload() {
            this.selectedFile = this.$refs.fileInput.files[0];
        },
        showTable() {
            this.dataView = 'table';
        },
        showChart() {
            this.dataView = 'chart';
        },
        tableView(selectedData) {
            switch (selectedData) {
                case 'parkinson':
                    this.currentTableView = 'parkinson';
                    break;
                case 'temperature':
                    this.currentTableView = 'temperature';
                    break;
                case 'respirationsRates':
                    this.currentTableView = 'respirationsRates';
                    break;
                case 'bloodPressures':
                    this.currentTableView = 'bloodPressures';
                    break;
                case 'bloodCholesterol':
                    this.currentTableView = 'bloodCholesterol';
                    break;
                case 'bloodGlucose':
                    this.currentTableView = 'bloodGlucose';
                    break;
                case 'heartRates':
                    this.currentTableView = 'heartRates';
                    break;
            }
        }
    }
};
</script>
