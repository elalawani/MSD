<template>
    <div class="p-5 text-slate-900 dark:text-slate-50">
        <div class="flex justify-center p-6 items-center">
            <h1 class="text-4xl">Bitte wählen Sie eine Messung aus</h1>
        </div>

        <div
            class="flex flex-row space-x-4 items-center justify-around overflow-auto w-full"
        >
            <button
                v-for="(myOption, index) in options"
                :key="index"
                :class="
                    option === myOption
                        ? 'border-b border-b-sky-500 text-sky-500 shadow-none'
                        : 'dark:bg-slate-600'
                "
                class="p-4 dark:bg-slate-500 mb-3 rounded shadow-xl h-20"
                @click="option = myOption"
            >
                {{ myOption }}
            </button>
        </div>
    </div>
    <div v-if="option === 'temperature'">
        <add-temperature />
    </div>
    <div v-if="option === 'blood cholesterol'">
        <add-blood-cholesterol />
    </div>
    <div v-if="option === 'blood glucose'">
        <add-blood-glucose />
    </div>
    <div v-if="option === 'blood pressure'">
        <add-blood-pressure />
    </div>
    <div v-if="option === 'heart rate'">
        <add-heart-rate />
    </div>
    <div v-if="option === 'parkinson'">
        <add-parkinson />
    </div>
    <div v-if="option === 'respiration rate'">
        <add-respiration-rate />
    </div>
</template>
<script>
import AddRespirationRate from '@/components/patient/sensor/creation/addRespirationRate.vue';
import AddParkinson from '@/components/patient/sensor/creation/addParkinson.vue';
import AddHeartRate from '@/components/patient/sensor/creation/addHeartRate.vue';
import AddBloodPressure from '@/components/patient/sensor/creation/addBloodPressure.vue';
import AddBloodGlucose from '@/components/patient/sensor/creation/addBloodGlucose.vue';
import AddBloodCholesterol from '@/components/patient/sensor/creation/addBloodCholesterol.vue';
import AddTemperature from '@/components/patient/sensor/creation/addTemperature.vue';

export default {
    name: 'NewDataFormView',
    data() {
        return {
            option: '',
            options: [
                'parkinson',
                'temperature',
                'heart rate',
                'blood pressure',
                'blood glucose',
                'respiration rate',
                'blood cholesterol'
            ]
        };
    },

    components: {
        AddRespirationRate,
        AddParkinson,
        AddHeartRate,
        AddBloodPressure,
        AddBloodGlucose,
        AddBloodCholesterol,
        AddTemperature
    }
};
</script>
